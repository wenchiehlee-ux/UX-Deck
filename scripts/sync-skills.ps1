[CmdletBinding()]
param (
    [string]$TargetPath = "../skills/common",
    [switch]$DryRun,
    [switch]$SyncLocalAgents = $true
)

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$repoRoot = Split-Path -Parent $scriptDir
$skillsSource = Join-Path $repoRoot "skills"

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host " UX-Deck Skills Synchronizer" -ForegroundColor Cyan
Write-Host " Source: $skillsSource" -ForegroundColor Gray
Write-Host " Target: $TargetPath" -ForegroundColor Gray
if ($DryRun) {
    Write-Host " Mode  : DRY-RUN (No files will be modified)" -ForegroundColor Yellow
}
Write-Host "==================================================" -ForegroundColor Cyan

if (-not (Test-Path $skillsSource)) {
    Write-Error "Source skills directory not found: $skillsSource"
    exit 1
}

# Resolve target path relative to repo root
$resolvedTarget = [System.IO.Path]::GetFullPath((Join-Path $repoRoot $TargetPath))
Write-Host "`n[1/4] Destination directory: $resolvedTarget" -ForegroundColor Green

if (-not (Test-Path $resolvedTarget)) {
    if ($DryRun) {
        Write-Host "  [DryRun] Would create directory: $resolvedTarget" -ForegroundColor Yellow
    } else {
        Write-Host "  Creating destination directory: $resolvedTarget" -ForegroundColor Gray
        New-Item -ItemType Directory -Path $resolvedTarget -Force | Out-Null
    }
}

# Clean legacy unprefixed folders from previous run if present
$legacyNames = @(
    "ux-design-system",
    "ux-mkdocs-life",
    "ux-google-alert-manager",
    "ux-youtube-audio-fetch",
    "ux-mkdocs-investment",
    "ux-homeassistant-tv"
)

Write-Host "`n[2/4] Cleaning legacy unprefixed skills if present..." -ForegroundColor Green
$parentSkillsDir = [System.IO.Path]::GetFullPath((Join-Path $repoRoot "../skills"))
foreach ($legacy in $legacyNames) {
    $legacyTarget = Join-Path $parentSkillsDir $legacy
    if (Test-Path $legacyTarget) {
        if ($DryRun) {
            Write-Host "  [DryRun] Would remove legacy: $legacyTarget" -ForegroundColor Yellow
        } else {
            Remove-Item -Path $legacyTarget -Recurse -Force
            Write-Host "  [Removed legacy] $legacyTarget" -ForegroundColor DarkYellow
        }
    }
}

# Enumerate skills matching naming convention skill-*
$skills = Get-ChildItem -Path $skillsSource -Directory | Where-Object { $_.Name -like "skill-*" }

Write-Host "`n[3/4] Syncing $($skills.Count) skills to $resolvedTarget..." -ForegroundColor Green

foreach ($skill in $skills) {
    $skillName = $skill.Name
    $destSkillDir = Join-Path $resolvedTarget $skillName

    Write-Host "  -> Syncing skill: [$skillName]" -ForegroundColor Cyan

    if (-not (Test-Path $destSkillDir)) {
        if (-not $DryRun) {
            New-Item -ItemType Directory -Path $destSkillDir -Force | Out-Null
        }
    }

    $allFiles = Get-ChildItem -Path $skill.FullName -Recurse -File

    foreach ($file in $allFiles) {
        $relativePath = $file.FullName.Substring($skill.FullName.Length + 1)
        $destFile = Join-Path $destSkillDir $relativePath
        $destDir = Split-Path -Parent $destFile

        if (-not (Test-Path $destDir) -and -not $DryRun) {
            New-Item -ItemType Directory -Path $destDir -Force | Out-Null
        }

        $needsCopy = $true
        if (Test-Path $destFile) {
            $srcHash = (Get-FileHash -Path $file.FullName -Algorithm MD5).Hash
            $destHash = (Get-FileHash -Path $destFile -Algorithm MD5).Hash
            if ($srcHash -eq $destHash) {
                $needsCopy = $false
            }
        }

        if ($needsCopy) {
            if ($DryRun) {
                Write-Host "     [DryRun Copy] $relativePath" -ForegroundColor Yellow
            } else {
                Copy-Item -Path $file.FullName -Destination $destFile -Force
                Write-Host "     [Copied] $relativePath" -ForegroundColor Gray
            }
        } else {
            Write-Host "     [Up-to-date] $relativePath" -ForegroundColor DarkGray
        }
    }
}

# Sync to local .agents/skills
$localAgentsSkills = Join-Path $repoRoot ".agents\skills"
if ($SyncLocalAgents) {
    Write-Host "`n[4/4] Syncing to local workspace .agents/skills..." -ForegroundColor Green
    if (-not (Test-Path $localAgentsSkills) -and -not $DryRun) {
        New-Item -ItemType Directory -Path $localAgentsSkills -Force | Out-Null
    }

    # Clean legacy unprefixed folders from local .agents
    foreach ($legacy in $legacyNames) {
        $locLegacy = Join-Path $localAgentsSkills $legacy
        if (Test-Path $locLegacy) {
            if (-not $DryRun) {
                Remove-Item -Path $locLegacy -Recurse -Force
            }
            Write-Host "  [Removed legacy local] $legacy" -ForegroundColor DarkYellow
        }
    }

    foreach ($skill in $skills) {
        $dest = Join-Path $localAgentsSkills $skill.Name
        if (-not $DryRun) {
            Copy-Item -Path $skill.FullName -Destination $localAgentsSkills -Recurse -Force
        }
        Write-Host "  [Local .agents] $($skill.Name) synced" -ForegroundColor Gray
    }
}

Write-Host "`n[OK] Synchronization completed successfully!" -ForegroundColor Green
