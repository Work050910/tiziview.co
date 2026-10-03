# -*- coding: utf-8 -*-
import os
import re
import json

def replace_in_file(file_path, replacements):
    if not os.path.exists(file_path):
        return
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    modified = content
    for old, new in replacements:
        modified = modified.replace(old, new)
        
    if modified != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(modified)
        print(f"Updated: {file_path}")

# 1. Update site-seo-profile.json and docs/site-seo-profile.json
profile_replacements = [
    ('"brandName": "机场看"', '"brandName": "梯子view"'),
    ('"brandName": "JichangNow"', '"brandName": "梯子view"'),
    ('机场看 - 2026新手机场推荐', '梯子view - 2026新手机场推荐'),
    ('JichangNow - 2026新手机场推荐', '梯子view - 2026新手机场推荐'),
    ('机场看 (tiziview.co)', '梯子view (tiziview.co)'),
    ('JichangNow (tiziview.co)', '梯子view (tiziview.co)'),
    ('JichangNow 官方博客', '梯子view 官方博客'),
    ('JichangNow 机场即刻导航', '梯子view 机场即刻导航'),
    ('JichangNow机场即刻导航', '梯子view机场即刻导航'),
    ('JichangNow 专为新手', '梯子view 专为新手'),
    ('{categoryName} - JichangNow', '{categoryName} - 梯子view'),
    ('{title} | JichangNow', '{title} | 梯子view'),
    ('{name}测评：2026价格套餐与新手购买须知 | JichangNow', '{name}测评：2026价格套餐与新手购买须知 | 梯子view'),
    ('{name}机场测评与节点测速：2026价格套餐与新手购买须知 | JichangNow', '{name}测评：2026最新价格套餐与新手购买指南 | 梯子view'),
    ('JichangNow {categoryName}栏目', '梯子view {categoryName}栏目'),
    ('"JichangNow",', '"梯子view",'),
    ('"JichangNow"', '"梯子view"')
]

replace_in_file("site-seo-profile.json", profile_replacements)
replace_in_file("docs/site-seo-profile.json", profile_replacements)

# 2. Update hugo.toml
replace_in_file("hugo.toml", [
    ('title = "JichangNow - 2026新手机场推荐与科学上网梯子配置导航指南 | 即刻连通全球高速网络"', 'title = "梯子view - 2026新手机场推荐与科学上网梯子配置导航指南 | 即刻连通全球高速网络"'),
    ('title = "机场看 - 2026新手机场推荐与科学上网梯子配置导航指南 | 即刻连通全球高速网络"', 'title = "梯子view - 2026新手机场推荐与科学上网梯子配置导航指南 | 即刻连通全球高速网络"'),
    ('brandName = "JichangNow"', 'brandName = "梯子view"'),
    ('brandName = "机场看"', 'brandName = "梯子view"')
])

# 3. Update layouts
layout_files = [
    "layouts/partials/sidebar.html",
    "layouts/partials/footer.html",
    "layouts/partials/schema-jsonld.html",
    "layouts/partials/head.html",
    "layouts/_default/single.html",
    "layouts/_default/list.html",
    "layouts/_default/baseof.html"
]

layout_replacements = [
    ("JichangNow", "梯子view"),
    ("机场看", "梯子view")
]

for lf in layout_files:
    replace_in_file(lf, layout_replacements)

# 4. Update data/faq100.json and docs/faq-keywords-100.csv
replace_in_file("data/faq100.json", [("JichangNow", "梯子view"), ("jichangnow", "梯子view")])
replace_in_file("docs/faq-keywords-100.csv", [("JichangNow", "梯子view"), ("jichangnow", "梯子view")])

# 5. Update content markdown files
content_replacements = [
    ("JichangNow - 2026", "梯子view - 2026"),
    ("机场看 - 2026", "梯子view - 2026"),
    ("JichangNow 专为新手", "梯子view 专为新手"),
    ("机场看 (tiziview.co)", "梯子view (tiziview.co)"),
    ("JichangNow (tiziview.co)", "梯子view (tiziview.co)"),
    ("JichangNow 机场即刻导航", "梯子view 机场即刻导航"),
    ("JichangNow机场即刻导航", "梯子view机场即刻导航"),
    ("JichangNow 编辑团队", "梯子view 编辑团队"),
    ("JichangNow 评测团队", "梯子view 评测团队"),
    ("JichangNow 评测组", "梯子view 评测组"),
    ("JichangNow 独家整理", "梯子view 独家整理"),
    ("JichangNow 独家评测室", "梯子view 独家评测室"),
    ("JichangNow 独家核验", "梯子view 独家核验"),
    ("JichangNow 官方沟通渠道", "梯子view 官方沟通渠道"),
    ("JichangNow 官方博客", "梯子view 官方博客"),
    ("JichangNow 客观性承诺", "梯子view 客观性承诺"),
    ("JichangNow 编辑原则", "梯子view 编辑原则"),
    ("JichangNow 编辑部准则", "梯子view 编辑部准则"),
    ("JichangNow 隐私保护声明", "梯子view 隐私保护声明"),
    ("JichangNow 服务条款", "梯子view 服务条款"),
    ("JichangNow 法律免责声明", "梯子view 法律免责声明"),
    ("JichangNow 纠错与更新政策", "梯子view 纠错与更新政策"),
    ("JichangNow 联合顶级数据中心", "梯子view 联合顶级数据中心"),
    ("JichangNow 联合主推", "梯子view 联合主推"),
    ("JichangNow 制定了标准化的评测流程", "梯子view 制定了标准化的评测流程"),
    ("JichangNow 建立了周期性内容巡检机制", "梯子view 建立了周期性内容巡检机制"),
    ("JichangNow 极其重视用户隐私", "梯子view 极其重视用户隐私"),
    ("离开 JichangNow", "离开 梯子view"),
    ("JichangNow 成立于 2026 年", "梯子view 成立于 2026 年"),
    ("JichangNow 的创立初衷", "梯子view 的创立初衷"),
    ("使用 JichangNow 的权利与义务", "使用 梯子view 的权利与义务"),
    ("JichangNow 保留随时修改", "梯子view 保留随时修改"),
    ("JichangNow 不承担任何连带责任", "梯子view 不承担任何连带责任"),
    ("JichangNow 推荐广大 Windows 用户", "梯子view 推荐广大 Windows 用户"),
    ("JichangNow 团队惊讶地发现", "梯子view 团队惊讶地发现"),
    ("在 JichangNow 的日常读者咨询中", "在 梯子view 的日常读者咨询中"),
    ("| JichangNow", "| 梯子view"),
    ("JichangNow", "梯子view"),
    ("「机场看」", "「梯子view」"),
    ("“机场看”", "“梯子view”"),
    ("机场看评测实验室", "梯子view评测实验室"),
    ("加入机场看评测池", "加入梯子view评测池"),
    ("机场看 科学上网", "梯子view 科学上网")
]

for root, dirs, files in os.walk("content"):
    for f in files:
        if f.endswith(".md"):
            replace_in_file(os.path.join(root, f), content_replacements)

# 6. Update scripts/build.py
build_replacements = [
    ('"name": "JichangNow"', '"name": "梯子view"'),
    ('content="JichangNow"', 'content="梯子view"'),
    ('| JichangNow', '| 梯子view'),
    ('| 机场看', '| 梯子view'),
    ('JichangNow 独家核验', '梯子view 独家核验'),
    ('JichangNow 独家评测室', '梯子view 独家评测室'),
    ('JichangNow 评测组', '梯子view 评测组'),
    ('JichangNow', '梯子view'),
    ('机场看', '梯子view')
]
replace_in_file("scripts/build.py", build_replacements)

# 7. Update scripts/verify.py
verify_replacements = [
    ('JichangNow 全自动化质量', '梯子view 全自动化质量')
]
replace_in_file("scripts/verify.py", verify_replacements)

# 8. Update static files
replace_in_file("static/css/style.css", [("JichangNow", "梯子view")])
replace_in_file("static/js/main.js", [("JichangNow", "梯子view")])

# 9. Update AGENTS.md and README.md
replace_in_file("AGENTS.md", [("JichangNow", "梯子view")])
replace_in_file("README.md", [("JichangNow", "梯子view")])

# 10. Update generator scripts
gen_scripts = [
    "scripts/build_home_and_services.py",
    "scripts/build_trust_pages.py",
    "scripts/generate_unique_providers.py",
    "scripts/generate_all_articles.py",
    "scripts/batch1_airport.py",
    "scripts/batch6_faq.py"
]
for gs in gen_scripts:
    replace_in_file(gs, [("JichangNow", "梯子view"), ("机场看", "梯子view")])

print("Brand rename to 梯子view completed successfully across all targets.")
