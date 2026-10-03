# -*- coding: utf-8 -*-
import os
import re
import json
import shutil
from datetime import datetime

PUBLIC_DIR = "public"
DOMAIN = "https://tiziview.co"

# Clean and recreate contents of public/ while preserving directory inode
os.makedirs(PUBLIC_DIR, exist_ok=True)
for item in os.listdir(PUBLIC_DIR):
    item_path = os.path.join(PUBLIC_DIR, item)
    if os.path.isdir(item_path):
        shutil.rmtree(item_path)
    else:
        os.remove(item_path)

# Copy static assets
shutil.copytree("static", PUBLIC_DIR, dirs_exist_ok=True)

# Load data
with open("site-seo-profile.json", "r", encoding="utf-8") as f:
    site_profile = json.load(f)

with open("data/providers.json", "r", encoding="utf-8") as f:
    providers = json.load(f)

with open("data/faq100.json", "r", encoding="utf-8") as f:
    faq100 = json.load(f)

# Helper: parse front matter
def parse_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    front_matter = {}
    content = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            content = parts[2]
            for line in fm_text.strip().split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    if val.startswith("[") and val.endswith("]"):
                        val = [item.strip().strip('"').strip("'") for item in val[1:-1].split(",") if item.strip()]
                    front_matter[key] = val
    return front_matter, content.strip()

# Helper: markdown to HTML converter (simple & robust for our structured content)
def markdown_to_html(md_text):
    html = md_text
    
    # Tables
    def convert_table(match):
        lines = match.group(0).strip().split("\n")
        if len(lines) < 2:
            return match.group(0)
        header_cells = [c.strip() for c in lines[0].strip("|").split("|")]
        # skip separator line lines[1]
        body_rows = []
        for line in lines[2:]:
            cells = [c.strip() for c in line.strip("|").split("|")]
            body_rows.append(cells)
        
        table_html = "<table>\n<thead>\n<tr>"
        for c in header_cells:
            table_html += f"<th>{c}</th>"
        table_html += "</tr>\n</thead>\n<tbody>\n"
        for row in body_rows:
            table_html += "<tr>"
            for c in row:
                table_html += f"<td>{c}</td>"
            table_html += "</tr>\n"
        table_html += "</tbody>\n</table>\n"
        return table_html

    # Detect markdown tables
    html = re.sub(r'(\|.+\|\n\|[-:\s|]+\|\n(?:\|.+\|\n?)+)', convert_table, html)

    # Headers
    html = re.sub(r'^#### (.*$)', r'<h4>\1</h4>', html, flags=re.M)
    html = re.sub(r'^### (.*$)', r'<h3>\1</h3>', html, flags=re.M)
    html = re.sub(r'^## (.*$)', r'<h2>\1</h2>', html, flags=re.M)
    html = re.sub(r'^# (.*$)', r'<h1>\1</h1>', html, flags=re.M)

    # Bold and Italic
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)

    # Links: [text](url)
    def link_repl(m):
        txt, url = m.group(1), m.group(2)
        if url.startswith("http") and not url.startswith(DOMAIN):
            return f'<a href="{url}" target="_blank" rel="sponsored nofollow noopener">{txt}</a>'
        return f'<a href="{url}">{txt}</a>'
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link_repl, html)

    # Inline code
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)

    # Code blocks
    html = re.sub(r'```(?:bash|sh)?\n(.*?)```', r'<pre><code>\1</code></pre>', html, flags=re.S)

    # Unordered Lists
    lines = html.split("\n")
    in_ul = False
    new_lines = []
    for line in lines:
        if line.strip().startswith("- "):
            if not in_ul:
                new_lines.append("<ul>")
                in_ul = True
            new_lines.append(f"<li>{line.strip()[2:]}</li>")
        elif re.match(r'^\d+\.\s', line.strip()):
            item_text = re.sub(r'^\d+\.\s', '', line.strip())
            new_lines.append(f"<p style=\"margin-left: 1.25rem;\">• {item_text}</p>")
        else:
            if in_ul:
                new_lines.append("</ul>")
                in_ul = False
            new_lines.append(line)
    if in_ul:
        new_lines.append("</ul>")
    html = "\n".join(new_lines)

    # Transform #### #XX airport lists into responsive .airport-grid cards
    def airport_card_repl(m):
        rank_str = m.group(1).strip()
        name = m.group(2).strip()
        list_content = m.group(3).strip()
        
        items = re.findall(r'<li>(.*?)</li>', list_content, re.DOTALL)
        fields = []
        reg_link = ""
        rev_link = ""
        price_tag = ""
        
        for it in items:
            it_clean = it.strip()
            if "官方通道" in it_clean:
                reg_m = re.search(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(?:👉\s*)?官网选购</a>', it_clean)
                if reg_m:
                    reg_link = reg_m.group(1)
                rev_m = re.search(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(?:📖\s*)?评测</a>', it_clean)
                if rev_m:
                    rev_link = rev_m.group(1)
            else:
                parts = re.split(r'<strong>(.*?)</strong>[：:]\s*', it_clean)
                if len(parts) >= 3:
                    lbl = parts[1].strip()
                    val = parts[2].strip()
                    fields.append((lbl, val))
                    if "价格" in lbl or "资费" in lbl:
                        pm = re.search(r'(\d+(?:\.\d+)?\s*元/(?:月|年))', val)
                        if pm:
                            price_tag = pm.group(1)
                else:
                    fields.append(("", it_clean))
                    
        rank_num = int(re.sub(r'\D', '', rank_str) or 0)
        
        # High contrast color schemes for distinct boxes
        if rank_num == 1:
            accent = "#f59e0b"
            b_bg, b_fg, b_bd = "#fef3c7", "#92400e", "#fde68a"
        elif rank_num == 2:
            accent = "#0284c7"
            b_bg, b_fg, b_bd = "#e0f2fe", "#0369a1", "#bae6fd"
        elif rank_num == 3:
            accent = "#7c3aed"
            b_bg, b_fg, b_bd = "#f3e8ff", "#6b21a8", "#e9d5ff"
        elif rank_num == 4:
            accent = "#059669"
            b_bg, b_fg, b_bd = "#dcfce7", "#15803d", "#bbf7d0"
        else:
            accent = "#2563eb"
            b_bg, b_fg, b_bd = "#f1f5f9", "#334155", "#cbd5e1"

        badge_cls = f"badge-top{rank_num}" if 1 <= rank_num <= 4 else "badge-normal"
        if not price_tag:
            price_tag = "查看资费"
            
        card_html = f'  <div class="airport-card" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-left: 6px solid {accent}; border-radius: 12px; box-shadow: 0 4px 10px rgba(15,23,42,0.06); display: flex; flex-direction: column; justify-content: space-between; overflow: hidden; margin-bottom: 0.5rem;">\n'
        card_html += f'    <div class="airport-card-header" style="background: #f8fafc; padding: 0.85rem 1.25rem; border-bottom: 1.5px solid #e2e8f0; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem;">\n'
        card_html += f'      <div class="airport-card-title" style="display: flex; align-items: center; gap: 0.6rem;"><span class="airport-badge {badge_cls}" style="background: {b_bg}; color: {b_fg}; border: 1px solid {b_bd}; font-weight: 800; font-size: 0.85rem; padding: 0.2rem 0.6rem; border-radius: 6px;">{rank_str}</span><span class="airport-name" style="font-size: 1.15rem; font-weight: 800; color: #0f172a;">{name}</span></div>\n'
        card_html += f'      <span class="airport-price-tag" style="font-size: 0.92rem; font-weight: 700; color: #e11d48; background: #fff1f2; padding: 0.25rem 0.65rem; border-radius: 6px; border: 1px solid #ffe4e6; white-space: nowrap;">{price_tag}</span>\n'
        card_html += f'    </div>\n'
        card_html += f'    <div class="airport-card-body" style="padding: 1.25rem; display: flex; flex-direction: column; gap: 0.65rem; flex-grow: 1;">\n'
        for lbl, val in fields:
            card_html += f'      <div class="airport-field" style="display: flex; align-items: flex-start; font-size: 0.88rem; line-height: 1.55; color: #334155;"><span class="airport-field-label" style="font-weight: 700; color: #475569; white-space: nowrap; flex-shrink: 0; margin-right: 0.4rem;">{lbl}：</span><span class="airport-field-val" style="color: #0f172a; word-break: break-word;">{val}</span></div>\n'
        card_html += f'    </div>\n'
        card_html += f'    <div class="airport-card-footer" style="padding: 0.85rem 1.25rem; background: #f8fafc; border-top: 1.5px dashed #cbd5e1; display: flex; align-items: center; justify-content: space-between; gap: 0.75rem; margin-top: auto;">\n'
        if rev_link:
            card_html += f'      <a href="{rev_link}" class="btn-detail" style="display: inline-flex; align-items: center; justify-content: center; background: #ffffff; color: #334155 !important; border: 1.5px solid #cbd5e1; font-weight: 600; font-size: 0.85rem; padding: 0.45rem 0.95rem; border-radius: 6px; text-decoration: none !important; box-shadow: 0 1px 2px rgba(0,0,0,0.04);">📖 评测详情</a>\n'
        if reg_link:
            card_html += f'      <a href="{reg_link}" target="_blank" rel="sponsored nofollow noopener" class="btn-register" style="display: inline-flex; align-items: center; justify-content: center; background: #2563eb; color: #ffffff !important; font-weight: 700; font-size: 0.88rem; padding: 0.5rem 1.15rem; border-radius: 6px; text-decoration: none !important; box-shadow: 0 2px 5px rgba(37,99,235,0.25);">👉 官网选购</a>\n'
        card_html += f'    </div>\n'
        card_html += f'  </div>'
        return card_html

    airport_pattern = re.compile(r'<h4>(#\d+)\s+([^<]+)</h4>\s*<ul>\s*(.*?)\s*</ul>', re.DOTALL)
    airport_blocks = list(airport_pattern.finditer(html))
    if airport_blocks:
        start_idx = airport_blocks[0].start()
        end_idx = airport_blocks[-1].end()
        cards_html = [airport_card_repl(m) for m in airport_blocks]
        grid_html = '\n\n<div class="airport-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 1.5rem; margin: 2rem 0;">\n' + "\n".join(cards_html) + '\n</div>\n\n'
        html = html[:start_idx] + grid_html + html[end_idx:]

    # Wrap non-block lines in <p>
    paragraphs = []
    for p in html.split("\n\n"):
        p_clean = p.strip()
        if not p_clean:
            continue
        if p_clean.startswith("<h") or p_clean.startswith("<table") or p_clean.startswith("<ul") or p_clean.startswith("<div") or p_clean.startswith("</div") or p_clean.startswith("<!--") or p_clean.startswith("<pre") or p_clean.startswith("<p"):
            paragraphs.append(p_clean)
        else:
            paragraphs.append(f"<p>{p_clean}</p>")
    
    return "\n\n".join(paragraphs)

def sanitize_external_links(html):
    def repl(m):
        full_tag = m.group(0)
        href = m.group(1)
        if href.startswith("http") and not href.startswith(DOMAIN):
            if re.search(r'\brel=[\"\'][^\"\']*[\"\']', full_tag):
                full_tag = re.sub(r'\brel=[\"\'][^\"\']*[\"\']', 'rel="sponsored nofollow noopener"', full_tag)
            else:
                full_tag = full_tag[:-1].rstrip() + ' rel="sponsored nofollow noopener">'
            if not re.search(r'\btarget=[\"\'][^\"\']*[\"\']', full_tag):
                full_tag = full_tag[:-1].rstrip() + ' target="_blank">'
        return full_tag
    return re.sub(r'<a\s+[^>]*href=[\"\']([^\"\']+)[\"\'][^>]*>', repl, html)

# Read partial templates
with open("layouts/partials/sidebar.html", "r", encoding="utf-8") as f:
    sidebar_tpl = f.read()

with open("layouts/partials/footer.html", "r", encoding="utf-8") as f:
    footer_tpl = f.read()

with open("layouts/partials/promo-card.html", "r", encoding="utf-8") as f:
    promo_card_tpl = f.read()

# Base layout assembler
def render_full_page(title, desc, canonical, body_html, is_home=False, breadcrumbs=None, published_time=None, modified_time=None):
    schema_type = "WebSite" if is_home else "Article"
    
    bc_html = ""
    if not is_home and breadcrumbs:
        bc_html = '<nav class="breadcrumbs" aria-label="breadcrumb">\n'
        for idx, (b_title, b_url) in enumerate(breadcrumbs):
            if idx == len(breadcrumbs) - 1:
                bc_html += f'  <span class="current" aria-current="page">{b_title}</span>\n'
            else:
                bc_html += f'  <a href="{b_url}">{b_title}</a> <span>&gt;</span>\n'
        bc_html += '</nav>\n'

    pub_iso = published_time if published_time else "2026-09-22T08:00:00+08:00"
    mod_iso = modified_time if modified_time else pub_iso

    json_ld = {
        "@context": "https://schema.org",
        "@type": schema_type,
        "headline": title,
        "description": desc,
        "url": canonical,
        "inLanguage": "zh-CN",
        "publisher": {
            "@type": "Organization",
            "name": "梯子view",
            "url": DOMAIN
        }
    }
    if not is_home:
        json_ld["datePublished"] = pub_iso
        json_ld["dateModified"] = mod_iso

    page_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  
  <meta property="og:type" content="{"website" if is_home else "article"}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:site_name" content="梯子view">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">

  <link rel="stylesheet" href="/css/style.css?v=20260923h">
  <link rel="icon" href="/images/avatar.svg">
  <script type="application/ld+json">
{json.dumps(json_ld, ensure_ascii=False, indent=2)}
  </script>
</head>
<body>
  <div class="mobile-header">
    <a href="/" class="mobile-brand">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display:inline-block;vertical-align:-3px;margin-right:6px;color:#38bdf8;"><path d="M22 2L11 13"></path><path d="M22 2L15 22L11 13L2 9L22 2Z"></path></svg>
      梯子view
    </a>
    <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="打开导航菜单">☰ 菜单</button>
  </div>
  <div class="mobile-overlay" id="mobileOverlay"></div>
  <div class="app-container">
    {sidebar_tpl}
    <div class="main-wrapper">
      <main class="content-container">
        {bc_html}
        {body_html}
      </main>
      {footer_tpl}
    </div>
  </div>
  <script src="/js/main.js" defer></script>
</body>
</html>
"""
    return sanitize_external_links(page_html)

all_sitemap_urls = []

# 1. Render Homepage
home_fm, home_md = parse_markdown("content/_index.md")
home_body = markdown_to_html(home_md)
home_html = render_full_page(
    site_profile["siteTitle"],
    site_profile["siteDescription"],
    f"{DOMAIN}/",
    f"{home_body}",
    is_home=True
)
with open(f"{PUBLIC_DIR}/index.html", "w", encoding="utf-8") as f:
    f.write(home_html)
all_sitemap_urls.append(f"{DOMAIN}/")

# 2. Render Services Page
services_fm, services_md = parse_markdown("content/services/_index.md")
services_body = f"""<article class="article-post">
  <h1 class="page-title">{services_fm.get('title', '自营精选服务')}</h1>
  {promo_card_tpl}
  <div class="article-body">
    {markdown_to_html(services_md)}
  </div>
</article>"""
services_html = render_full_page(
    f"{services_fm.get('title')} | 梯子view",
    services_fm.get('description'),
    f"{DOMAIN}/services/",
    services_body,
    breadcrumbs=[("首页", "/"), ("自营精选服务", "/services/")]
)
os.makedirs(f"{PUBLIC_DIR}/services", exist_ok=True)
with open(f"{PUBLIC_DIR}/services/index.html", "w", encoding="utf-8") as f:
    f.write(services_html)
all_sitemap_urls.append(f"{DOMAIN}/services/")

# 3. Render FAQ Hub
faq_fm, faq_md = parse_markdown("content/faq/_index.md")
faq_body = f"""<article class="article-post">
  {promo_card_tpl}
  <div class="article-body">
    {markdown_to_html(faq_md)}
  </div>
</article>"""
faq_html = render_full_page(
    f"{faq_fm.get('title')} | 梯子view",
    faq_fm.get('description'),
    f"{DOMAIN}/faq/",
    faq_body,
    breadcrumbs=[("首页", "/"), ("常见问题100问", "/faq/")]
)
os.makedirs(f"{PUBLIC_DIR}/faq", exist_ok=True)
with open(f"{PUBLIC_DIR}/faq/index.html", "w", encoding="utf-8") as f:
    f.write(faq_html)
all_sitemap_urls.append(f"{DOMAIN}/faq/")

# 4. Render Trust Pages
trust_slugs = ["about", "contact", "editorial-policy", "methodology", "corrections", "affiliate-disclosure", "privacy", "terms", "disclaimer"]
for slug in trust_slugs:
    t_fm, t_md = parse_markdown(f"content/{slug}/_index.md")
    t_body = f"""<article class="article-post">
      <h1 class="page-title">{t_fm.get('title')}</h1>
      <div class="article-body">
        {markdown_to_html(t_md)}
      </div>
    </article>"""
    t_html = render_full_page(
        f"{t_fm.get('title')} | 梯子view",
        t_fm.get('description'),
        f"{DOMAIN}/{slug}/",
        t_body,
        breadcrumbs=[("首页", "/"), (t_fm.get('title'), f"/{slug}/")]
    )
    os.makedirs(f"{PUBLIC_DIR}/{slug}", exist_ok=True)
    with open(f"{PUBLIC_DIR}/{slug}/index.html", "w", encoding="utf-8") as f:
        f.write(t_html)
    all_sitemap_urls.append(f"{DOMAIN}/{slug}/")

# 5. Render 27 Provider Pages & All Providers Hub Page
os.makedirs(f"{PUBLIC_DIR}/providers", exist_ok=True)
for p in providers:
    slug = p['slug']
    p_path = f"content/providers/{slug}.md"
    if os.path.exists(p_path):
        p_fm, p_md = parse_markdown(p_path)
        p_body = f"""<article class="article-post">
          <h1 class="page-title">{p_fm.get('title')}</h1>
          <div class="article-meta">
            <span>📅 核验日期：{p['lastChecked']}</span>
            <span>⭐ 推荐排名：第 {p['rank']} 名</span>
            <span>✍️ 评测团队：梯子view 独家核验</span>
          </div>
          {promo_card_tpl}
          <div class="article-body">
            {markdown_to_html(p_md)}
          </div>
          {promo_card_tpl}
        </article>"""
        p_html = render_full_page(
            f"{p_fm.get('title')} | 梯子view",
            p_fm.get('description'),
            f"{DOMAIN}/providers/{slug}/",
            p_body,
            breadcrumbs=[("首页", "/"), ("全部机场测评", "/providers/"), (p['name'], f"/providers/{slug}/")]
        )
        os.makedirs(f"{PUBLIC_DIR}/providers/{slug}", exist_ok=True)
        with open(f"{PUBLIC_DIR}/providers/{slug}/index.html", "w", encoding="utf-8") as f:
            f.write(p_html)
        all_sitemap_urls.append(f"{DOMAIN}/providers/{slug}/")

# Render /providers/ Hub Page (全部机场测评大全)
hub_fm, hub_md = parse_markdown("content/providers/_index.md")
cards_html = ""
for p in providers:
    rank = p['rank']
    is_top4 = rank <= 4
    border_style = "border: 2px solid #0284c7; background: #ffffff;" if is_top4 else "border: 1px solid #e2e8f0; background: #ffffff;"
    badge = f'<span style="background: linear-gradient(135deg, #0284c7, #0369a1); color: #fff; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 700; margin-left: 8px;">👑 编辑部首选</span>' if is_top4 else ""
    
    coupon_html = ""
    if p.get("coupon"):
        coupon_html = f"""<div style="margin-top: 0.6rem; font-size: 0.88rem; color: #0369a1; background: #f0f9ff; padding: 0.4rem 0.75rem; border-radius: 6px; border: 1px dashed #bae6fd; display: inline-block;">
          🎟️ 专属优惠码：<strong>{p['coupon']}</strong> <span style="color: #64748b; font-size: 0.82rem;">({p.get('couponNote', '结算可用')})</span>
        </div>"""
    
    packages_preview = ""
    if p.get("packages"):
        pkg_items = [f"{pkg['name']} ({pkg['price']} / {pkg['traffic']})" for pkg in p["packages"][:3]]
        packages_preview = f"""<div style="margin-top: 0.5rem; font-size: 0.85rem; color: #64748b;">
          <strong>📦 热门套餐：</strong>{ " · ".join(pkg_items) }
        </div>"""

    cards_html += f"""
    <div class="provider-card-hub" style="{border_style} border-radius: 12px; padding: 1.25rem 1.5rem; margin-bottom: 1.25rem; box-shadow: 0 2px 5px rgba(0,0,0,0.03);">
      <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.5rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 0.75rem;">
        <div style="display: flex; align-items: center;">
          <span style="display: inline-block; width: 28px; height: 28px; line-height: 28px; text-align: center; background: {'#0284c7' if is_top4 else '#64748b'}; color: #fff; font-weight: 800; border-radius: 50%; font-size: 0.85rem; margin-right: 0.6rem;">{rank}</span>
          <h3 style="margin: 0; font-size: 1.25rem;"><a href="/providers/{p['slug']}/" style="color: #0f172a; text-decoration: none;">{p['name']}</a></h3>
          {badge}
        </div>
        <div style="font-size: 0.95rem; font-weight: 700; color: #e11d48;">
          起步门槛：{p.get('priceFrom', '详见评测')} · {p.get('trafficFrom', '')}
        </div>
      </div>
      
      <div style="margin-top: 0.75rem;">
        <p style="font-size: 0.95rem; color: #334155; line-height: 1.6; margin: 0;">
          <strong>💡 核心特色：</strong>{p.get('summary', '')}
        </p>
        {coupon_html}
        {packages_preview}
      </div>
      
      <div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1rem; align-items: center; justify-content: flex-end;">
        <a href="/providers/{p['slug']}/" style="padding: 0.5rem 1.1rem; border-radius: 6px; background: #f8fafc; color: #0f172a; border: 1px solid #cbd5e1; font-weight: 600; text-decoration: none; font-size: 0.9rem;">
          📖 查看完整测评报告 &rarr;
        </a>
        <a href="{p['inviteURL']}" target="_blank" rel="sponsored nofollow noopener" style="padding: 0.5rem 1.25rem; border-radius: 6px; background: #0284c7; color: #ffffff; font-weight: 700; text-decoration: none; font-size: 0.9rem; box-shadow: 0 2px 4px rgba(2,132,199,0.25);">
          🛒 前往官网选购
        </a>
      </div>
    </div>
    """

hub_body = f"""<article class="article-post">
  <h1 class="page-title">{hub_fm.get('title', '全部机场测评大全')}</h1>
  <div class="article-meta">
    <span>📅 核验更新：2026-09-22</span>
    <span>📊 测评规模：全网 27 家主流梯子实机核验</span>
    <span>✍️ 评测团队：梯子view 独家评测室</span>
  </div>
  {promo_card_tpl}
  <div class="article-body">
    {markdown_to_html(hub_md)}
  </div>
  <div class="providers-catalog" style="margin-top: 2rem;">
    <h2 style="font-size: 1.35rem; color: #0f172a; border-left: 4px solid #0284c7; padding-left: 0.75rem; margin-bottom: 1.25rem;">2026 全网 27 家翻墙机场深度实测名录</h2>
    {cards_html}
  </div>
</article>"""

hub_canonical = f"{DOMAIN}/providers/"
hub_html = render_full_page(
    f"{hub_fm.get('title', '全部机场测评')} | 梯子view",
    hub_fm.get('description', '2026年全部27家机场测评汇总'),
    hub_canonical,
    hub_body,
    breadcrumbs=[("首页", "/"), ("全部机场测评", hub_canonical)]
)
with open(f"{PUBLIC_DIR}/providers/index.html", "w", encoding="utf-8") as f:
    f.write(hub_html)
all_sitemap_urls.append(hub_canonical)

# 6. Render Categories and 53 Articles
categories_meta = {
    "airport-reviews": {"name": "机场推荐榜", "desc": "精选 2026 高性价比稳定机场测速与深度评测，涵盖 IEPL 专线、便宜年付与 4K 超清解锁梯子推荐。"},
    "windows": {"name": "Windows教程", "desc": "Windows 平台主流科学上网客户端保姆级教程，涵盖 Clash Verge Rev、Mihomo Party、v2rayN 与 Sing-box。"},
    "mac": {"name": "Mac教程", "desc": "苹果 macOS 平台翻墙客户端深度配置，适配 Apple Silicon M 系列芯片与终端命令行代理。"},
    "ios": {"name": "iOS教程", "desc": "苹果 iPhone/iPad 平台 Shadowrocket 小火箭、Loon、Quantumult X 圈X 与 Sing-box 保姆级配置指南。"},
    "android": {"name": "Android教程", "desc": "安卓手机与智能电视 TV 盒子客户端配置教程，涵盖 Clash Meta for Android、v2rayNG 与分应用分流。"},
    "faq": {"name": "常见问题与踩坑", "desc": "节点超时、订阅更新失败、4K 高延迟与 ChatGPT 解锁等高频报错排查与避坑实操。"}
}

for cat_dir, meta in categories_meta.items():
    cat_folder = f"content/categories/{cat_dir}"
    os.makedirs(f"{PUBLIC_DIR}/categories/{cat_dir}", exist_ok=True)
    
    cat_articles = []
    if os.path.exists(cat_folder):
        for f_name in sorted(os.listdir(cat_folder)):
            if f_name.endswith(".md") and not f_name.startswith("_"):
                a_slug = f_name[:-3]
                a_path = os.path.join(cat_folder, f_name)
                a_fm, a_md = parse_markdown(a_path)
                
                # Render single article
                a_title = a_fm.get("title", a_slug)
                a_desc = a_fm.get("description", "")
                cat_name = meta["name"]
                
                a_body = f"""<article class="article-post">
                  <h1 class="page-title">{a_title}</h1>
                  <div class="article-meta">
                    <span>📅 发布日期：{a_fm.get('date', '2026-09-22')[:10]}</span>
                    <span>🔄 最后更新：{a_fm.get('lastmod', '2026-09-22')[:10]}</span>
                    <span>📂 分类：<a href="/categories/{cat_dir}/">{cat_name}</a></span>
                    <span>✍️ 作者：梯子view 评测组</span>
                  </div>
                  {promo_card_tpl}
                  <div class="article-body">
                    {markdown_to_html(a_md)}
                  </div>
                  {promo_card_tpl}
                </article>"""
                
                a_canonical = f"{DOMAIN}/categories/{cat_dir}/{a_slug}/"
                a_html = render_full_page(
                    f"{a_title} | 梯子view",
                    a_desc,
                    a_canonical,
                    a_body,
                    breadcrumbs=[("首页", "/"), (cat_name, f"/categories/{cat_dir}/"), (a_title, a_canonical)],
                    published_time=a_fm.get("date"),
                    modified_time=a_fm.get("lastmod")
                )
                
                os.makedirs(f"{PUBLIC_DIR}/categories/{cat_dir}/{a_slug}", exist_ok=True)
                with open(f"{PUBLIC_DIR}/categories/{cat_dir}/{a_slug}/index.html", "w", encoding="utf-8") as f_out:
                    f_out.write(a_html)
                all_sitemap_urls.append(a_canonical)
                
                cat_articles.append((a_slug, a_title, a_desc, a_fm.get("date", "2026-09-22")[:10]))

    # Render Category List Page
    list_body = f"""<div class="category-header">
      <h1 class="page-title">{meta['name']}</h1>
      <p style="font-size: 1.05rem; color: #475569; line-height: 1.7; margin-bottom: 2rem;">{meta['desc']}</p>
    </div>
    {promo_card_tpl}
    <div class="posts-list">
    """
    for a_slug, a_title, a_desc, a_date in cat_articles:
        list_body += f"""
      <div class="post-card">
        <h3><a href="/categories/{cat_dir}/{a_slug}/">{a_title}</a></h3>
        <p class="post-card-summary">{a_desc}</p>
        <div class="article-meta" style="margin-top: 0.5rem;">
          <span>📅 {a_date}</span>
          <a href="/categories/{cat_dir}/{a_slug}/" style="margin-left: auto; font-weight: 600;">阅读全文 &rarr;</a>
        </div>
      </div>
        """
    list_body += "</div>"
    
    cat_canonical = f"{DOMAIN}/categories/{cat_dir}/"
    cat_html = render_full_page(
        f"{meta['name']} - 2026科学上网指南 | 梯子view",
        meta['desc'],
        cat_canonical,
        list_body,
        breadcrumbs=[("首页", "/"), (meta['name'], cat_canonical)]
    )
    with open(f"{PUBLIC_DIR}/categories/{cat_dir}/index.html", "w", encoding="utf-8") as f_out:
        f_out.write(cat_html)
    all_sitemap_urls.append(cat_canonical)

# 7. Render 404 Page
with open("layouts/404.html", "r", encoding="utf-8") as f:
    notfound_content = f.read()
# extract main block
nf_body = notfound_content.replace('{{ define "main" }}', '').replace('{{ end }}', '')
nf_html = render_full_page(
    "404 - 页面未找到 | 梯子view",
    "抱歉，您访问的页面不存在或已被移除。",
    f"{DOMAIN}/404.html",
    nf_body
)
with open(f"{PUBLIC_DIR}/404.html", "w", encoding="utf-8") as f:
    f.write(nf_html)

# 8. Generate Sitemap.xml
sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url in sorted(all_sitemap_urls):
    sitemap_xml.append("  <url>")
    sitemap_xml.append(f"    <loc>{url}</loc>")
    sitemap_xml.append("    <lastmod>2026-09-22</lastmod>")
    sitemap_xml.append("    <changefreq>weekly</changefreq>")
    sitemap_xml.append("    <priority>0.8</priority>")
    sitemap_xml.append("  </url>")
sitemap_xml.append("</urlset>")

with open(f"{PUBLIC_DIR}/sitemap.xml", "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_xml))

# 9. Generate RSS index.xml
rss_xml = [
    '<?xml version="1.0" encoding="utf-8" standalone="yes"?>',
    '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
    '  <channel>',
    f'    <title>{site_profile["siteTitle"]}</title>',
    f'    <link>{DOMAIN}/</link>',
    f'    <description>{site_profile["siteDescription"]}</description>',
    '    <language>zh-CN</language>',
    f'    <lastBuildDate>{datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0800")}</lastBuildDate>',
    f'    <atom:link href="{DOMAIN}/index.xml" rel="self" type="application/rss+xml" />'
]
for url in sorted(all_sitemap_urls)[:25]:
    rss_xml.append("    <item>")
    rss_xml.append(f"      <title>{url.split('/')[-2] if url.endswith('/') else url.split('/')[-1]}</title>")
    rss_xml.append(f"      <link>{url}</link>")
    rss_xml.append("      <pubDate>Tue, 22 Sep 2026 08:00:00 +0800</pubDate>")
    rss_xml.append("    </item>")
rss_xml.append("  </channel>")
rss_xml.append("</rss>")

with open(f"{PUBLIC_DIR}/index.xml", "w", encoding="utf-8") as f:
    f.write("\n".join(rss_xml))

print(f"Build complete! Generated {len(all_sitemap_urls)} URLs into {PUBLIC_DIR}/ successfully.")
