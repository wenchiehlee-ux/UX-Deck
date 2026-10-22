import os

lucide_dir = 'tokens/icons/lucide'
emblem_dir = 'tokens/icons/modern-emblem'
chibi_dir = 'tokens/icons/kawaii-chibi'

def read_svg(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            return content.replace('<?xml version="1.0" encoding="utf-8"?>', '')
    return None

# Section 1: Active Endpoints (12 animals)
master_animals = [
    {
        'id': 'deer',
        'name_zh': '幾何林鹿',
        'name_en': 'Scandinavian Deer',
        'status': '✅ 已上線：mkdocs-life',
        'category': 'active',
        'color': '#10b981',
        'desc': '象徵北歐簡約森林生活、生活美學反思與優雅自然沉靜韻律。',
        'lucide_file': 'lucide-deer.svg',
        'emblem_file': 'emblem-deer.svg'
    },
    {
        'id': 'falcon',
        'name_zh': '破曉警報鳥',
        'name_en': 'Alert Falcon / Bird',
        'status': '✅ 已上線：GoogleAlertManager',
        'category': 'active',
        'color': '#f97316',
        'desc': '象徵清晨破曉鳴叫報訊、雷達俯瞰與晨光過濾降噪通知。',
        'lucide_file': 'lucide-bird.svg',
        'emblem_file': 'emblem-falcon.svg'
    },
    {
        'id': 'whale',
        'name_zh': '聲波座頭鯨',
        'name_en': 'Sonic Whale',
        'status': '✅ 已上線：YoutubeAudio.Fetch',
        'category': 'active',
        'color': '#0284c7',
        'desc': '象徵深海聲納悠揚共鳴、沉浸式水下聲學與多模態音頻串流。',
        'lucide_file': 'lucide-whale.svg',
        'emblem_file': 'emblem-whale.svg'
    },
    {
        'id': 'bull',
        'name_zh': '幾何狂牛',
        'name_en': 'Fintech Alpha Bull',
        'status': '✅ 已上線：mkdocs-investment (多頭)',
        'category': 'active',
        'color': '#ef4444',
        'desc': '象徵華爾街牛市多頭動能、資產成長動能與宏觀主動 Alpha。',
        'lucide_file': 'lucide-bull.svg',
        'emblem_file': 'emblem-bull.svg'
    },
    {
        'id': 'owl',
        'name_zh': '拍拍翅萌萌鴞',
        'name_en': 'Research Owlet',
        'status': '✅ 已上線：My-TW-Coverage',
        'category': 'active',
        'color': '#8b5cf6',
        'desc': '象徵個股深度研究智慧、夜間透視研報先機與萌態啟發。',
        'lucide_file': 'lucide-owl.svg',
        'emblem_file': 'emblem-owl.svg'
    },
    {
        'id': 'cat',
        'name_zh': '敏捷守護貓',
        'name_en': 'Private Cloud Cat',
        'status': '✅ 已上線：wenchiehlee.quickconnect.to',
        'category': 'active',
        'color': '#0284c7',
        'desc': '象徵 24/7 私有雲默默巡視守護、輕靈敏捷與 DevOps 容器管理。',
        'lucide_file': 'lucide-cat.svg',
        'emblem_file': 'emblem-cat.svg'
    },
    {
        'id': 'dog_sentinel',
        'name_zh': '客廳小管家 柴柴',
        'name_en': 'Sentinel Dog / Shiba',
        'status': '✅ 已上線：HomeAssistant on TV',
        'category': 'active',
        'color': '#d97706',
        'desc': '象徵客廳忠誠守候、Android TV 大螢幕通知小管家與安全衛士。',
        'lucide_file': 'lucide-dog.svg',
        'emblem_file': 'emblem-dog.svg'
    },
    {
        'id': 'eagle',
        'name_zh': '破曉雄鷹 / 領航鷹',
        'name_en': 'Sovereign Eagle',
        'status': '⚡ 整合評選中：InvestorConference',
        'category': 'active',
        'color': '#22a553',
        'desc': '象徵資本市場破曉領航、宏觀全景高空俯瞰與法人第一手訊息。',
        'lucide_file': 'lucide-eagle.svg',
        'emblem_file': 'emblem-eagle.svg'
    },
    {
        'id': 'rhino',
        'name_zh': '重甲灰犀牛',
        'name_en': 'Grey Rhino',
        'status': '⚡ 整合評選中：VIX 波動率雷達',
        'category': 'active',
        'color': '#64748b',
        'desc': '象徵宏觀不可阻擋的巨大衝擊（Grey Rhino）、系統性轉折動能。',
        'lucide_file': 'lucide-rhino.svg',
        'emblem_file': 'emblem-rhino.svg'
    },
    {
        'id': 'swan',
        'name_zh': '幾何黑天鵝 / 天鵝',
        'name_en': 'Black Swan / Swan',
        'status': '⚡ 整合評選中：VIX 波動率雷達',
        'category': 'active',
        'color': '#ef4444',
        'desc': '象徵極端市場尾端風險（Black Swan）、優雅冷酷與深水突襲。',
        'lucide_file': 'lucide-swan.svg',
        'emblem_file': 'emblem-swan.svg'
    },
    {
        'id': 'squirrel',
        'name_zh': '採集松鼠 🐿️',
        'name_en': 'Organizing Squirrel',
        'status': '✅ 已上線：Synology-Photo-Tagger',
        'category': 'active',
        'color': '#8b5cf6',
        'desc': '象徵勤奮分類與珍藏記憶果實，負責 AI 視覺照片辨識、物件場景分類與 EXIF/XMP 智慧標籤入庫。',
        'lucide_file': 'lucide-squirrel.svg',
        'emblem_file': 'emblem-squirrel.svg'
    },

    # Section 2: 3034 Reserves (7 animals)
    {
        'id': 'dolphin',
        'name_zh': '飛躍海豚',
        'name_en': 'Fluid Dolphin',
        'status': '📦 備選動物庫存',
        'category': 'reserve',
        'color': '#06b6d4',
        'desc': '破浪躍起，象徵資本市場流動性之王、高敏捷交易節奏與活力。',
        'lucide_file': 'lucide-dolphin.svg',
        'emblem_file': 'emblem-dolphin.svg'
    },
    {
        'id': 'lion',
        'name_zh': '王者雄獅',
        'name_en': 'Imperial Lion',
        'status': '📦 備選動物庫存',
        'category': 'reserve',
        'color': '#eab308',
        'desc': '王者鬃毛與沉穩步態，象徵權威龍頭指標、藍籌企業霸主實力。',
        'lucide_file': 'lucide-lion.svg',
        'emblem_file': 'emblem-lion.svg'
    },
    {
        'id': 'elephant',
        'name_zh': '穩健巨象',
        'name_en': 'Steadfast Elephant',
        'status': '📦 備選動物庫存',
        'category': 'reserve',
        'color': '#64748b',
        'desc': '頂天立地、戲水長鼻，象徵萬億主權基金規模與堅如磐石穩健底盤。',
        'lucide_file': 'lucide-elephant.svg',
        'emblem_file': 'emblem-elephant.svg'
    },
    {
        'id': 'camel',
        'name_zh': '耐力駱駝',
        'name_en': 'Endurance Camel',
        'status': '📦 備選動物庫存',
        'category': 'reserve',
        'color': '#b45309',
        'desc': '日落沙漠中長途跋涉，象徵穿越多空牛熊景氣週期與極強抗壓韌性。',
        'lucide_file': 'lucide-camel.svg',
        'emblem_file': 'emblem-camel.svg'
    },
    {
        'id': 'bear',
        'name_zh': '防禦巨熊',
        'name_en': 'Defensive Bear',
        'status': '📦 備選動物庫存 (mkdocs-investment 空頭盾牌)',
        'category': 'reserve',
        'color': '#78350f',
        'desc': '冬眠防禦步態，象徵在極端空頭市場下保全資產價值的堅強護盾。',
        'lucide_file': 'lucide-bear.svg',
        'emblem_file': 'emblem-bear.svg'
    },
    {
        'id': 'rabbit',
        'name_zh': '敏捷白兔',
        'name_en': 'Agile Rabbit',
        'status': '✅ 已上線：Skills Registry',
        'category': 'active',
        'color': '#059669',
        'desc': '流暢的實心剪影、後掠長耳與舒展步伐，象徵快速探索技能、分類知識與跨專案重用。',
        'lucide_file': 'lucide-rabbit.svg',
        'emblem_file': 'emblem-rabbit.svg'
    },
    {
        'id': 'turtle',
        'name_zh': '裝甲玄龜',
        'name_en': 'Armored Turtle',
        'status': '📦 備選動物庫存',
        'category': 'reserve',
        'color': '#14b8a6',
        'desc': '極簡幾何切面甲冑，象徵硬體極致安全性、堅不可摧與千年長青。',
        'lucide_file': 'lucide-turtle.svg',
        'emblem_file': 'emblem-turtle.svg'
    }
]

# Section 3: Kawaii Chibi Animals paired with their dedicated Lucide linear icons!
chibi_animals = [
    {
        'id': 'chibi-lion',
        'name_zh': 'Q版小獅王',
        'name_en': 'Chibi Lion',
        'color': '#f97316',
        'desc': '波浪暖橙圓形鬃毛、奶黃大臉與圓球尾巴，象徵龍頭總覽與核心總督。',
        'chibi_file': 'chibi-lion.svg',
        'lucide_file': 'lucide-lion.svg'
    },
    {
        'id': 'chibi-giraffe',
        'name_zh': 'Q版長頸鹿',
        'name_en': 'Chibi Giraffe',
        'color': '#f59e0b',
        'desc': '斑點圓耳、小觸角與敦實坐姿，象徵高瞻遠矚、長期投資與視野規劃。',
        'chibi_file': 'chibi-giraffe.svg',
        'lucide_file': 'lucide-giraffe.svg'
    },
    {
        'id': 'chibi-elephant',
        'name_zh': 'Q版小象',
        'name_en': 'Chibi Elephant',
        'color': '#64748b',
        'desc': '粉嫩大象耳、捲捲象鼻與雙頰腮紅，象徵龐大資產規模與安全沉穩備份。',
        'chibi_file': 'chibi-elephant.svg',
        'lucide_file': 'lucide-elephant.svg'
    },
    {
        'id': 'chibi-monkey',
        'name_zh': 'Q版小猴',
        'name_en': 'Chibi Monkey',
        'color': '#b45309',
        'desc': '大圓耳朵、兩側幸運星星與俏皮微笑，象徵敏捷自動化爬蟲與靈巧交易。',
        'chibi_file': 'chibi-monkey.svg',
        'lucide_file': 'lucide-monkey.svg'
    },
    {
        'id': 'chibi-zebra',
        'name_zh': 'Q版小斑馬',
        'name_en': 'Chibi Zebra',
        'color': '#475569',
        'desc': '黑白幾何相間條紋、粉嫩腮紅，象徵財務對帳黑白分明與結構化表格。',
        'chibi_file': 'chibi-zebra.svg',
        'lucide_file': 'lucide-zebra.svg'
    },
    {
        'id': 'chibi-tiger',
        'name_zh': 'Q版小跳虎',
        'name_en': 'Chibi Tiger',
        'color': '#ea580c',
        'desc': '暖橘底色帶黑色虎紋斑、萌萌小肉掌，象徵成長爆發力與主動出擊衝刺。',
        'chibi_file': 'chibi-tiger.svg',
        'lucide_file': 'lucide-tiger.svg'
    },
    {
        'id': 'chibi-hippo',
        'name_zh': 'Q版深灰河馬',
        'name_en': 'Chibi Hippo',
        'color': '#0284c7',
        'desc': '圓弧下巴、深色鼻孔與明亮腮紅，象徵堅守陣地、沉浸式閱讀與深海抗壓。',
        'chibi_file': 'chibi-hippo.svg',
        'lucide_file': 'lucide-hippo.svg'
    },
    {
        'id': 'chibi-hippo_lite',
        'name_zh': 'Q版淡藍河馬',
        'name_en': 'Chibi Hippo Lite',
        'color': '#06b6d4',
        'desc': '淺藍灰色清爽配色版，象徵簡潔介面、無干擾沉浸式輕量化模式。',
        'chibi_file': 'chibi-hippo_lite.svg',
        'lucide_file': 'lucide-hippo.svg'
    }
]

def render_section1_2_card(item):
    lucide_svg = read_svg(os.path.join(lucide_dir, item['lucide_file'])) if item['lucide_file'] else None
    emblem_svg = read_svg(os.path.join(emblem_dir, item['emblem_file'])) if item['emblem_file'] else None
    color = item['color']
    
    emblem_box = f'''
      <div class="col-box">
        <div class="col-label">Modern Emblem 徽章</div>
        <div class="preview-white">
          {emblem_svg}
        </div>
        <div class="col-meta">{item['emblem_file']}</div>
      </div>
    ''' if emblem_svg else f'''
      <div class="col-box">
        <div class="col-label">Modern Emblem 徽章</div>
        <div class="preview-empty">
          <span>（純極簡線條型）</span>
        </div>
        <div class="col-meta">無彩塊版本</div>
      </div>
    '''

    lucide_box = f'''
      <div class="col-box">
        <div class="col-label">Lucide 極簡線性</div>
        <div class="preview-dark" style="color: {color};">
          {lucide_svg}
        </div>
        <div class="col-meta">{item['lucide_file']}</div>
      </div>
    ''' if lucide_svg else '''
      <div class="col-box">
        <div class="col-label">Lucide 極簡線性</div>
        <div class="preview-empty">無</div>
      </div>
    '''

    status_badge_class = 'badge-active' if item['category'] == 'active' else ('badge-eval' if '評選' in item['status'] else 'badge-reserve')

    return f'''
    <div class="card" data-category="{item['category']}">
      <div class="card-header">
        <div>
          <div class="animal-title">{item['name_zh']} <span class="en-title">({item['name_en']})</span></div>
          <span class="status-tag {status_badge_class}">{item['status']}</span>
        </div>
        <span class="id-tag" style="background: {color}15; color: {color}; border-color: {color}40;">
          {item['id']}
        </span>
      </div>

      <div class="compare-row">
        {emblem_box}
        {lucide_box}
      </div>

      <div class="card-desc">{item['desc']}</div>
    </div>
    '''

def render_chibi_card(item):
    chibi_svg = read_svg(os.path.join(chibi_dir, item['chibi_file']))
    lucide_svg = read_svg(os.path.join(lucide_dir, item['lucide_file']))
    color = item['color']
    
    return f'''
    <div class="card" style="border-top: 3px solid {color};">
      <div class="card-header">
        <div>
          <div class="animal-title">{item['name_zh']} <span class="en-title">({item['name_en']})</span></div>
          <span class="status-tag" style="background: rgba(244, 114, 182, 0.15); color: #f472b6; border: 1px solid rgba(244, 114, 182, 0.3);">
            💖 Kawaii Chibi 萌寵體系
          </span>
        </div>
        <span class="id-tag" style="background: {color}15; color: {color}; border-color: {color}40;">
          {item['id']}
        </span>
      </div>

      <!-- Side-by-side comparison: Left = Kawaii Chibi, Right = Lucide Style -->
      <div class="compare-row">
        <div class="col-box">
          <div class="col-label">Kawaii Chibi 萌寵</div>
          <div class="preview-white" style="height: 110px; padding: 6px;">
            {chibi_svg}
          </div>
          <div class="col-meta">{item['chibi_file']}</div>
        </div>

        <div class="col-box">
          <div class="col-label">Lucide 極簡線性對照</div>
          <div class="preview-dark" style="color: {color}; height: 110px;">
            {lucide_svg}
          </div>
          <div class="col-meta">{item['lucide_file']}</div>
        </div>
      </div>

      <div class="card-desc">{item['desc']}</div>
    </div>
    '''

cards_active = ''.join(render_section1_2_card(it) for it in master_animals if it['category'] == 'active')
cards_reserve = ''.join(render_section1_2_card(it) for it in master_animals if it['category'] == 'reserve')
cards_chibi = ''.join(render_chibi_card(it) for it in chibi_animals)
active_count = sum(1 for it in master_animals if it['category'] == 'active')
reserve_count = sum(1 for it in master_animals if it['category'] == 'reserve')
total_animal_count = active_count + reserve_count + len(chibi_animals)

html_content = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="utf-8">
<title>UX-Deck 全端點吉祥物與三大風格動物圖庫全圖鑑</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{
    background: #090d16;
    color: #f1f5f9;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans TC", sans-serif;
    padding: 40px 30px;
    margin: 0;
  }}
  .container {{
    max-width: 1400px;
    margin: 0 auto;
  }}
  .header {{
    margin-bottom: 32px;
  }}
  h1 {{
    font-size: 28px;
    font-weight: 800;
    color: #38bdf8;
    margin: 0 0 10px 0;
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  p.subtitle {{
    font-size: 14px;
    color: #94a3b8;
    margin: 0 0 24px 0;
    line-height: 1.6;
  }}
  .meta-stats {{
    background: #111827;
    border: 1px solid #1f2937;
    border-radius: 14px;
    padding: 16px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    flex-wrap: wrap;
    margin-bottom: 36px;
  }}
  .stat-group {{
    display: flex;
    gap: 24px;
  }}
  .stat-item {{
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
  }}
  .stat-num {{
    font-size: 18px;
    font-weight: 800;
    color: #f8fafc;
  }}
  .section-divider {{
    display: flex;
    align-items: center;
    gap: 16px;
    margin: 44px 0 20px 0;
    padding-bottom: 12px;
    border-bottom: 2px solid #1f2937;
  }}
  .section-title {{
    font-size: 20px;
    font-weight: 800;
    color: #f1f5f9;
    margin: 0;
    display: flex;
    align-items: center;
    gap: 10px;
  }}
  .section-badge {{
    font-size: 12px;
    font-weight: 700;
    padding: 3px 12px;
    border-radius: 9999px;
  }}
  .grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
  }}
  @media (max-width: 1200px) {{
    .grid {{ grid-template-columns: repeat(2, 1fr); }}
  }}
  @media (max-width: 768px) {{
    .grid {{ grid-template-columns: 1fr; }}
  }}
  .card {{
    background: #111827;
    border: 1px solid #1f2937;
    border-radius: 18px;
    padding: 22px;
    transition: all 0.25s ease;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .card:hover {{
    border-color: #38bdf8;
    transform: translateY(-4px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.5), 0 0 24px rgba(56, 189, 248, 0.12);
  }}
  .card-header {{
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 1px solid #1f2937;
  }}
  .animal-title {{
    font-size: 17px;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 4px;
  }}
  .en-title {{
    font-size: 13px;
    color: #94a3b8;
    font-weight: 600;
  }}
  .status-tag {{
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 6px;
    margin-top: 4px;
  }}
  .badge-active {{ background: rgba(34, 165, 83, 0.15); color: #4ade80; border: 1px solid rgba(74, 222, 128, 0.3); }}
  .badge-eval {{ background: rgba(234, 88, 12, 0.15); color: #fb923c; border: 1px solid rgba(251, 146, 60, 0.3); }}
  .badge-reserve {{ background: rgba(100, 116, 139, 0.15); color: #94a3b8; border: 1px solid rgba(148, 163, 184, 0.2); }}
  .id-tag {{
    font-size: 11px;
    font-weight: 700;
    padding: 2px 10px;
    border-radius: 9999px;
    border: 1px solid;
    font-family: monospace;
  }}
  .compare-row {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 16px;
  }}
  .col-box {{
    display: flex;
    flex-direction: column;
    align-items: center;
  }}
  .col-label {{
    font-size: 11px;
    font-weight: 700;
    color: #94a3b8;
    margin-bottom: 8px;
  }}
  .preview-white {{
    width: 100%;
    height: 110px;
    background: #ffffff;
    border-radius: 10px;
    padding: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .preview-white svg {{
    max-width: 100%;
    max-height: 100%;
  }}
  .preview-dark {{
    width: 100%;
    height: 110px;
    background: #090d16;
    border: 1px solid #1f2937;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .preview-dark svg {{
    width: 48px;
    height: 48px;
  }}
  .preview-empty {{
    width: 100%;
    height: 110px;
    background: #0d131f;
    border: 1px dashed #1f2937;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
    color: #475569;
  }}
  .col-meta {{
    font-size: 10px;
    color: #64748b;
    margin-top: 6px;
    font-family: monospace;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 130px;
  }}
  .card-desc {{
    font-size: 12px;
    color: #94a3b8;
    line-height: 1.5;
    background: #090d16;
    padding: 10px 12px;
    border-radius: 8px;
    border: 1px solid #1f2937;
    margin-top: auto;
  }}
</style>
</head>
<body>

<div class="container">
  <div class="header">
    <h1>🏛️ UX-Deck 全端點吉祥物與三大風格動物圖庫全圖鑑</h1>
    <p class="subtitle">
      完整收錄 <strong>UX-Deck 生態系已上線之各端點吉祥物</strong>、<strong>3034.eps 提取之 Modern Emblem 徽章動物</strong>、<strong>Kawaii Chibi 日系 Q 版萌寵</strong>，以及 <strong>Lucide 原生與備選動物儲備庫</strong>。<br>
      全方位呈現「<strong>3034.eps 現代商標徽章</strong>」、「<strong>Lucide 極簡單色線性</strong>」與「<strong>Kawaii Chibi 萌系腮紅</strong>」三大風格體系！
    </p>

    <div class="meta-stats">
      <div class="stat-group">
        <div class="stat-item">
          <span>現役與評選中端點：</span>
          <span class="stat-num" style="color: #4ade80;">{active_count} 隻</span>
        </div>
        <div class="stat-item">
          <span>3034 / Lucide 備選：</span>
          <span class="stat-num" style="color: #38bdf8;">{reserve_count} 隻</span>
        </div>
        <div class="stat-item">
          <span>Kawaii Chibi 萌寵：</span>
          <span class="stat-num" style="color: #f472b6;">8 隻 (均含 Lucide 對照)</span>
        </div>
        <div class="stat-item">
          <span>總收錄動物種類：</span>
          <span class="stat-num" style="color: #fbbf24;">{total_animal_count} 隻</span>
        </div>
      </div>
      <div style="font-size: 12px; color: #64748b;">
        資源目錄：<code>tokens/icons/lucide/</code> · <code>modern-emblem/</code> · <code>kawaii-chibi/</code>
      </div>
    </div>
  </div>

  <!-- Section 1: Active Endpoints -->
  <div class="section-divider">
    <h2 class="section-title">
      <span>🚀 第一部分：現役端點與進行中評選動物 ({active_count} 隻)</span>
    </h2>
    <span class="section-badge" style="background: rgba(74, 222, 128, 0.15); color: #4ade80;">
      已部署至 9 大 Sibling Repositories & 進行中
    </span>
  </div>
  <div class="grid">
    {cards_active}
  </div>

  <!-- Section 2: Reserve Animals -->
  <div class="section-divider">
    <h2 class="section-title">
      <span>📦 第二部分：Modern Emblem & Lucide 備選儲備庫存 ({reserve_count} 隻)</span>
    </h2>
    <span class="section-badge" style="background: rgba(56, 189, 248, 0.15); color: #38bdf8;">
      3034.eps 現代徽章風格 & Lucide 極簡線性對照 ({reserve_count} 隻全備齊)
    </span>
  </div>
  <div class="grid">
    {cards_reserve}
  </div>

  <!-- Section 3: Kawaii Chibi Animals paired with Lucide -->
  <div class="section-divider">
    <h2 class="section-title">
      <span>💖 第三部分：Kawaii Chibi 日系 Q 版萌寵動物庫 (8 隻 · 左右並列 Lucide 極簡線性對照)</span>
    </h2>
    <span class="section-badge" style="background: rgba(244, 114, 182, 0.15); color: #f472b6;">
      大頭身比 · 治癒腮紅 ⇄ 24×24 2px 極簡線性雙軌並列
    </span>
  </div>
  <div class="grid">
    {cards_chibi}
  </div>

</div>

</body>
</html>
'''

# Write to both filenames so that both work seamlessly
with open('preview_animal_styles.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('preview_3034_and_lucide.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Updated both preview_animal_styles.html and preview_3034_and_lucide.html with complete Chibi Lucide pairings!')
