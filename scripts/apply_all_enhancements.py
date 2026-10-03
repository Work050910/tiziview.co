# -*- coding: utf-8 -*-
import os
import re
import json
import glob

def count_chinese_chars(text):
    clean_text = re.sub(r'<[^>]+>', '', text)
    clean_text = re.sub(r'---.*?---', '', clean_text, flags=re.S)
    clean_text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', clean_text)
    clean_text = re.sub(r'http[s]?://\S+', '', clean_text)
    zh_chars = re.findall(r'[\u4e00-\u9fa5]', clean_text)
    return len(zh_chars)

from data_faqs import ALL_FAQS
from data_airport_rich import AIRPORT_RICH_SECTIONS

with open("data/providers.json", "r", encoding="utf-8") as f:
    providers = json.load(f)

# Helper cards and links
with open("scripts/enrich_all_53_articles.py", "r", encoding="utf-8") as f:
    helper = f.read()

top4_cards_html = helper.split('top4_cards_html = """')[1].split('"""')[0].strip()
links_block = helper.split('links_block = """')[1].split('"""')[0].strip()

# -------------------------------------------------------------
# Part 1: Update 14 airport reviews with rich content & custom FAQ
# -------------------------------------------------------------
print("Updating 14 airport-reviews articles...")
for filename, data in AIRPORT_RICH_SECTIONS.items():
    filepath = os.path.join("content/categories/airport-reviews", filename)
    with open(filepath, "r", encoding="utf-8") as f:
        orig = f.read()
    
    tm = re.search(r"^title:\s*[\"\x27]?(.*?)[\"\x27]?\s*$", orig, re.M)
    title = tm.group(1) if tm else data["h2"]
    dm = re.search(r"^description:\s*[\"\x27]?(.*?)[\"\x27]?\s*$", orig, re.M)
    desc = dm.group(1) if dm else ""

    sec3 = f"""### 三、 本文高点击率与标题核心搜索词速查

在选购与实际配置本类服务时，广大用户最关注的高频热搜意图包括：
- **核心搜索词**：`{data["sec3_core"][0]}`、`{data["sec3_core"][1]}`、`{data["sec3_core"][2]}`
- **高点击长尾词**：`{data["sec3_long"][0]}`、`{data["sec3_long"][1]}`、`{data["sec3_long"][2]}`
- **强意图转化词**：`{data["sec3_trans"][0]}`、`{data["sec3_trans"][1]}`、`{data["sec3_trans"][2]}`"""

    faqs = ALL_FAQS[filepath]
    faq_lines = ["## 常见排障与新手自查 (FAQ)\n"]
    for q, a in faqs:
        faq_lines.append(f"**Q：{q}**  \nA：{a}\n")
    faq_text = "\n".join(faq_lines)

    tags_json = json.dumps(data["sec3_core"] + data["sec3_long"], ensure_ascii=False)

    article_md = f"""---
title: "{title}"
description: "{desc}"
date: 2026-09-22T08:00:00+08:00
lastmod: 2026-09-22T08:00:00+08:00
categories: ["airport-reviews"]
tags: {tags_json}
primaryKeyword: "{data["sec3_core"][0]}"
---

## {data["h2"]}

{data["sec1_title"]}

{data["sec1_text"]}

{data["sec2_title"]}

{data["sec2_text"]}

{sec3}

## 🏆 2026 核心机场推荐榜单（固定精选前四）

本站经多网实测核验，为您精选当前稳定性与售后最卓越的四家核心服务商，支持各大主流客户端一键导入配置：

{top4_cards_html}

{faq_text}
{links_block}
"""
    cnt = count_chinese_chars(article_md)
    print(f"  {filename}: {cnt} zh chars")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(article_md)

# -------------------------------------------------------------
# Part 2: Update 2026 rankings comprehensive article (Rank 1 to 27)
# -------------------------------------------------------------
print("Updating 2026-airport-recommendation-rankings.md...")
rankings_path = "content/categories/airport-reviews/2026-airport-recommendation-rankings.md"
with open(rankings_path, "r", encoding="utf-8") as f:
    rc = f.read()

# Replace generic FAQ with rankings-specific FAQ from ALL_FAQS
r_faqs = ALL_FAQS[rankings_path]
r_faq_text = "## 常见排障与新手自查 (FAQ)\n\n"
for q, a in r_faqs:
    r_faq_text += f"**Q：{q}**  \nA：{a}\n\n"

if "## 常见排障与新手自查 (FAQ)" in rc:
    parts = rc.split("## 常见排障与新手自查 (FAQ)")
    subparts = parts[1].split("## 🔗 推荐互链与全平台科学上网教程索引")
    rc = parts[0] + r_faq_text + "## 🔗 推荐互链与全平台科学上网教程索引" + subparts[1]

# Ensure all 27 cards have clean price and coupon
for p in providers:
    r = p["rank"]
    c = p["coupon"]
    price = p["priceFrom"]
    traffic = p["trafficFrom"]
    card_pat = re.compile(rf'(#### #{r:02d}\s+[^\n]+\n(?:- \*\*[^\n]+\n)+)', re.M)
    m = card_pat.search(rc)
    if m:
        old_card = m.group(1)
        price_line = f"- **价格资费**：{price} · {traffic} · （专属券码: `{c}`）\n"
        new_card = re.sub(r'- \*\*价格资费\*\*：[^\n]+\n', price_line, old_card)
        rc = rc.replace(old_card, new_card)

# Check character count and tune to be safely under 2500
cnt = count_chinese_chars(rc)
print(f"  Rankings count before trim: {cnt} zh chars")
if cnt > 2480:
    intro_start = rc.find("## 2026年最新机场推荐与翻墙梯子深度实测榜单")
    intro_end = rc.find("## 🏆 2026 全网 27 家翻墙机场深度测评与官方注册通道库")
    if intro_start != -1 and intro_end != -1:
        new_intro = """## 2026年最新机场推荐与翻墙梯子深度实测榜单

### 一、 2026 稳定机场推荐选购指标
挑选好用机场核心在于骨干专线与带宽冗余：采用 IEPL/IPLC 内网专线避开公网丢包，晚高峰不卡顿；提供原生住宅 IP，解锁 Netflix 与 ChatGPT；支持主流客户端一键导入。

### 二、 便宜机场推荐与避坑策略
小白与学生党挑选便宜机场应坚持低试错成本：首选月付或平价小年付梯子，实测晚高峰 4K 播放流畅再考虑长期订阅。

### 三、 核心高频热搜速查
- **核心搜索词**：`2026最新机场推荐`、`稳定好用翻墙梯子`、`机场测速排行榜`、`便宜机场节点购买`、`4K秒开不卡顿`、`机场专属优惠码`

"""
        rc = rc[:intro_start] + new_intro + rc[intro_end:]
        cnt = count_chinese_chars(rc)
        print(f"  After intro trim, Rankings count: {cnt} zh chars")

with open(rankings_path, "w", encoding="utf-8") as f:
    f.write(rc)

# -------------------------------------------------------------
# Part 3: Update 38 tutorial and FAQ articles
# -------------------------------------------------------------
print("Updating 38 tutorial and FAQ articles...")
other_articles = sorted(glob.glob("content/categories/**/*.md", recursive=True))
for fpath in other_articles:
    if "airport-reviews" in fpath or fpath.endswith("_index.md"):
        continue
    with open(fpath, "r", encoding="utf-8") as fp:
        c = fp.read()
    
    # 1. Update Card 4 in top 4 cards if present
    if "以结算页为准" in c or "暂无优惠码" in c:
        c = c.replace('<div class="top4-price">以结算页为准</div>', '<div class="top4-price">16 元/月 起</div>')
        c = c.replace('<span class="coupon-code">暂无优惠码</span>', '<span class="coupon-code">wfwl88</span>')
        c = c.replace('data-coupon="暂无优惠码"', 'data-coupon="wfwl88"')
        c = c.replace('<small style="color: #64748b; margin-left: 4px;">(以结算页为准)</small>', '<small style="color: #64748b; margin-left: 4px;">(专属优惠)</small>')
    
    # 2. Update FAQ section
    if fpath in ALL_FAQS:
        faqs = ALL_FAQS[fpath]
        faq_text = "## 常见排障与新手自查 (FAQ)\n\n"
        for q, a in faqs:
            faq_text += f"**Q：{q}**  \nA：{a}\n\n"
        
        if "## 常见排障与新手自查 (FAQ)" in c:
            parts = c.split("## 常见排障与新手自查 (FAQ)")
            # Heading after FAQ can be "## 🔗 推荐互链与全平台科学上网教程索引" or "## 🔗 推荐互链与全平台教程索引"
            next_heading = "## 🔗 推荐互链与全平台科学上网教程索引" if "## 🔗 推荐互链与全平台科学上网教程索引" in parts[1] else "## 🔗 推荐互链与全平台教程索引"
            if next_heading in parts[1]:
                subparts = parts[1].split(next_heading)
                c = parts[0] + faq_text + next_heading + subparts[1]
    
    cnt = count_chinese_chars(c)
    if cnt < 800 or cnt > 1350:
        print(f"  WARNING: {fpath} count = {cnt}")
    else:
        print(f"  {os.path.basename(fpath)}: {cnt} zh chars")
    
    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(c)

# -------------------------------------------------------------
# Part 4: Update 27 provider reviews in content/providers/*.md
# -------------------------------------------------------------
print("Updating 27 provider reviews in content/providers/*.md...")
for p in providers:
    slug = p["slug"]
    name = p["name"]
    price = p["priceFrom"]
    traffic = p["trafficFrom"]
    coupon = p["coupon"]
    p_file = f"content/providers/{slug}.md"
    if not os.path.exists(p_file):
        continue
    with open(p_file, "r", encoding="utf-8") as fp:
        c = fp.read()
    
    # Replace priceFrom & trafficFrom if was 以结算页为准
    c = re.sub(r'参考起步门槛约为 \*\*以结算页为准\*\*', f'参考起步门槛约为 **{price}**', c)
    c = re.sub(r'基础流量约为 \*\*以官网套餐为准\*\*', f'基础流量约为 **{traffic}**', c)
    c = re.sub(r'基础流量约为 \*\*100GB/月 \(可见记录 137元/年\)\*\*', f'基础流量约为 **{traffic}**', c)
    
    # Replace coupon if was 暂无专属优惠码
    c = re.sub(r'- \*\*专属优惠码\*\*：暂无专属优惠码[^\n]*', f'- **专属优惠码**：`{coupon}` (享专属折扣优惠)', c)
    
    # Also update table rows if "以结算页为准"
    if "以结算页为准" in c:
        c = c.replace("以结算页为准", price)
    if "以官网套餐为准" in c:
        c = c.replace("以官网套餐为准", traffic)
    if "暂无优惠码" in c:
        c = c.replace("暂无优惠码", coupon)
        
    cnt = count_chinese_chars(c)
    with open(p_file, "w", encoding="utf-8") as fp:
        fp.write(c)

print("All article enhancements applied successfully!")
