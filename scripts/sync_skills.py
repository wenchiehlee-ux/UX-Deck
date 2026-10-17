#!/usr/bin/env python3
"""
UX-Deck Skills Synchronizer
Synchronizes UX skills from this repository to target directories (default: ../skills/common)
and the local workspace .agents/skills directory.

Features:
- Fast MD5 hash-based delta synchronization (only copies modified or new files)
- SKILL.md frontmatter validation (ensures valid YAML name and description)
- Legacy folder cleanup
- Rich CLI with dry-run, target overriding, verbose logging, and force modes
"""

import argparse
import hashlib
import os
import re
import shutil
import sys
from pathlib import Path

LEGACY_SKILL_NAMES = [
    "ux-design-system",
    "ux-mkdocs-life",
    "ux-google-alert-manager",
    "ux-youtube-audio-fetch",
    "ux-mkdocs-investment",
    "ux-homeassistant-tv",
]


def compute_md5(file_path: Path) -> str:
    """Compute MD5 checksum of a file in binary mode."""
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def validate_skill(skill_dir: Path) -> tuple[bool, str]:
    """Validate that skill_dir contains a valid SKILL.md with frontmatter."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return False, "Missing SKILL.md"

    try:
        content = skill_md.read_text(encoding="utf-8")
        if not content.startswith("---"):
            return False, "SKILL.md missing frontmatter starting with '---'"

        parts = content.split("---", 2)
        if len(parts) < 3:
            return False, "SKILL.md incomplete frontmatter"

        frontmatter = parts[1]
        if not re.search(r"^name:\s*([^\s]+)", frontmatter, re.MULTILINE):
            return False, "SKILL.md missing 'name:' field in frontmatter"
        if not re.search(r"^description:", frontmatter, re.MULTILINE):
            return False, "SKILL.md missing 'description:' field in frontmatter"

        return True, "Valid"
    except Exception as e:
        return False, f"Failed to read SKILL.md: {e}"


def clean_legacy_folders(parent_skills_dir: Path, dry_run: bool = False, verbose: bool = False) -> int:
    """Remove legacy unprefixed skill folders from target directory."""
    removed = 0
    for legacy_name in LEGACY_SKILL_NAMES:
        target = parent_skills_dir / legacy_name
        if target.exists() and target.is_dir():
            if dry_run:
                print(f"  [DryRun Clean] Would remove legacy: {target}")
            else:
                shutil.rmtree(target)
                print(f"  [Cleaned Legacy] Removed: {target}")
            removed += 1
    return removed


def sync_directory(
    source_dir: Path,
    dest_dir: Path,
    dry_run: bool = False,
    force: bool = False,
    verbose: bool = False,
) -> tuple[int, int]:
    """
    Recursively copy files from source_dir to dest_dir based on MD5 checksum.
    Returns (copied_count, unchanged_count).
    """
    copied = 0
    unchanged = 0

    if not dest_dir.exists() and not dry_run:
        dest_dir.mkdir(parents=True, exist_ok=True)

    for root, _, files in os.walk(source_dir):
        root_path = Path(root)
        rel_root = root_path.relative_to(source_dir)
        target_root = dest_dir / rel_root

        for filename in files:
            src_file = root_path / filename
            dst_file = target_root / filename

            needs_copy = force or not dst_file.exists()
            if not needs_copy:
                try:
                    if compute_md5(src_file) != compute_md5(dst_file):
                        needs_copy = True
                except Exception:
                    needs_copy = True

            rel_display = (rel_root / filename).as_posix()

            if needs_copy:
                if dry_run:
                    print(f"     [DryRun Copy] {rel_display}")
                else:
                    target_root.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src_file, dst_file)
                    print(f"     [Copied] {rel_display}")
                copied += 1
            else:
                if verbose:
                    print(f"     [Up-to-date] {rel_display}")
                unchanged += 1

    return copied, unchanged


def main():
    parser = argparse.ArgumentParser(
        description="Synchronize UX-Deck skills to external repository and local workspace."
    )
    parser.add_argument(
        "--target",
        "-t",
        default="../skills/common",
        help="Destination directory for skills (default: ../skills/common)",
    )
    parser.add_argument(
        "--dry-run",
        "-n",
        action="store_true",
        help="Simulate operations without making changes to disk",
    )
    parser.add_argument(
        "--no-local-agents",
        action="store_true",
        help="Skip syncing to local workspace .agents/skills directory",
    )
    parser.add_argument(
        "--skip-clean",
        action="store_true",
        help="Skip cleaning legacy unprefixed folders",
    )
    parser.add_argument(
        "--prefix",
        default="skill-*",
        help="Glob pattern to match skill folders (default: skill-*)",
    )
    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Force overwrite all files regardless of MD5 hash match",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show detailed unchanged file statuses",
    )

    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    skills_source = repo_root / "skills"

    print("=" * 60)
    print(" UX-Deck Skills Synchronizer (Python Engine)")
    print(f" Source: {skills_source}")
    print(f" Target: {args.target}")
    if args.dry_run:
        print(" Mode  : DRY-RUN (No files will be modified)")
    print("=" * 60)

    if not skills_source.exists():
        print(f"ERROR: Skills source directory not found: {skills_source}", file=sys.stderr)
        sys.exit(1)

    # 1. Resolve destination path
    resolved_target = (repo_root / args.target).resolve()
    print(f"\n[1/4] Destination directory: {resolved_target}")
    if not resolved_target.exists():
        if args.dry_run:
            print(f"  [DryRun] Would create directory: {resolved_target}")
        else:
            resolved_target.mkdir(parents=True, exist_ok=True)
            print(f"  Created destination directory: {resolved_target}")

    # 2. Clean legacy unprefixed folders if requested
    if not args.skip_clean:
        print("\n[2/4] Checking & cleaning legacy unprefixed skills...")
        parent_skills = (repo_root / "../skills").resolve()
        removed = clean_legacy_folders(parent_skills, dry_run=args.dry_run, verbose=args.verbose)
        if removed == 0:
            print("  No legacy folders found in target.")

    # 3. Discover and validate skills
    matched_skills = [d for d in skills_source.glob(args.prefix) if d.is_dir()]
    print(f"\n[3/4] Syncing {len(matched_skills)} skills to {resolved_target}...")

    total_copied = 0
    total_unchanged = 0

    for skill in sorted(matched_skills):
        skill_name = skill.name
        is_valid, reason = validate_skill(skill)
        if not is_valid:
            print(f"  WARNING: Skipping invalid skill '{skill_name}': {reason}", file=sys.stderr)
            continue

        dest_skill_dir = resolved_target / skill_name
        print(f"  -> Skill: [{skill_name}]")
        copied, unchanged = sync_directory(
            skill,
            dest_skill_dir,
            dry_run=args.dry_run,
            force=args.force,
            verbose=args.verbose,
        )
        total_copied += copied
        total_unchanged += unchanged

    # 4. Sync to local .agents/skills
    if not args.no_local_agents:
        local_agents = repo_root / ".agents" / "skills"
        print(f"\n[4/4] Syncing to local workspace {local_agents}...")
        if not args.skip_clean:
            clean_legacy_folders(local_agents, dry_run=args.dry_run, verbose=args.verbose)

        for skill in sorted(matched_skills):
            dest_local_dir = local_agents / skill.name
            sync_directory(
                skill,
                dest_local_dir,
                dry_run=args.dry_run,
                force=args.force,
                verbose=args.verbose,
            )
            print(f"  [Local .agents] {skill.name} verified")

    print("\n" + "=" * 60)
    print(
        f"[OK] Sync completed! Copied/Updated: {total_copied} file(s), Unchanged: {total_unchanged} file(s)."
    )
    print("=" * 60)


if __name__ == "__main__":
    main()
