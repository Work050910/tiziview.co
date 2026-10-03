# -*- coding: utf-8 -*-
import os

# 1. layouts/partials/head.html
head_html = """<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ if .IsHome }}{{ .Site.Title }}{{ else }}{{ .Title }} | {{ .Site.Params.title }}{{ end }}</title>
  <meta name="description" content="{{ with .Description }}{{ . }}{{ else }}{{ .Site.Params.description }}{{ end }}">
  <link rel="canonical" href="{{ .Permalink }}">
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="{{ if .IsPage }}article{{ else }}website{{ end }}">
  <meta property="og:url" content="{{ .Permalink }}">
  <meta property="og:title" content="{{ if .IsHome }}{{ .Site.Title }}{{ else }}{{ .Title }} | {{ .Site.Params.title }}{{ end }}">
  <meta property="og:description" content="{{ with .Description }}{{ . }}{{ else }}{{ .Site.Params.description }}{{ end }}">
  <meta property="og:site_name" content="JichangNow">
  
  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{{ if .IsHome }}{{ .Site.Title }}{{ else }}{{ .Title }} | {{ .Site.Params.title }}{{ end }}">
  <meta name="twitter:description" content="{{ with .Description }}{{ . }}{{ else }}{{ .Site.Params.description }}{{ end }}">

  <link rel="stylesheet" href="/css/style.css">
  <link rel="icon" href="{{ .Site.Params.favicon | default \"/images/avatar.svg\" }}">
  {{ partial "schema-jsonld.html" . }}
</head>
"""
with open('layouts/partials/head.html', 'w', encoding='utf-8') as f:
    f.write(head_html)

# 2. layouts/partials/sidebar.html
sidebar_html = """<aside class="sidebar" id="sidebar">
  <div class="sidebar-brand">
    <a href="/">
      <img src="{{ .Site.Params.avatar | default \"/images/avatar.svg\" }}" alt="JichangNow Logo" class="sidebar-avatar">
    </a>
    <h2 class="sidebar-title"><a href="/" style="color: #ffffff; text-decoration: none;">JichangNow</a></h2>
    <p class="sidebar-tagline">即刻连接 · 现测可用 · 简单易用</p>
  </div>

  <div class="sidebar-nav">
    <div class="nav-heading">全平台配置导航</div>
    <ul class="nav-list">
      <li class="nav-item"><a href="/" class="nav-link{{ if .IsHome }} active{{ end }}">🏠 首页</a></li>
      <li class="nav-item"><a href="/categories/airport-reviews/" class="nav-link">🚀 机场推荐榜</a></li>
      <li class="nav-item"><a href="/categories/windows/" class="nav-link">💻 Windows教程</a></li>
      <li class="nav-item"><a href="/categories/mac/" class="nav-link">🍎 Mac教程</a></li>
      <li class="nav-item"><a href="/categories/ios/" class="nav-link">📱 iOS小火箭教程</a></li>
      <li class="nav-item"><a href="/categories/android/" class="nav-link">🤖 Android教程</a></li>
      <li class="nav-item"><a href="/categories/faq/" class="nav-link">💡 常见问题与踩坑</a></li>
      <li class="nav-item"><a href="/faq/" class="nav-link">❓ 100问知识中心</a></li>
      <li class="nav-item"><a href="/services/" class="nav-link">⭐ 自营精选服务</a></li>
    </ul>
  </div>

  <div class="sidebar-promo">
    <span class="sidebar-promo-badge">编辑精选推荐</span>
    <h4>全球云 IEPL 专线</h4>
    <p>多国原生IP · 晚高峰跑满4K · 智能分流不卡顿</p>
    <a href="https://hueue09.gcvipaff.com/#/?code=z8U9aaa4" target="_blank" rel="sponsored nofollow noopener" class="btn-cta">
      使用优惠码 qq88 直达
    </a>
  </div>
</aside>
"""
with open('layouts/partials/sidebar.html', 'w', encoding='utf-8') as f:
    f.write(sidebar_html)

# 3. layouts/partials/footer.html
footer_html = """<footer class="site-footer">
  <div class="footer-content">
    <div class="footer-narrative">
      <p><strong>JichangNow 官方博客</strong>专注小白的科学上网指南，持续提供 2026 翻墙梯子节点透明评测、高性价比稳定机场推荐、跨平台客户端配置教程与安全隐私保护，助您实现全设备极速平稳连接。</p>
      <p style="margin-top: 0.5rem; font-size: 0.82rem; color: #94a3b8;">本站所有评测与节点数据均定期人工实测核验。部分服务商包含合作推广邀请通道，所列套餐价格与优惠规则请以最终结算页为准。本站坚决倡导合法合规网络连接与学术外贸需求，拒绝任何违规用途。</p>
    </div>
    <div class="footer-links">
      <a href="/about/">关于我们</a>
      <a href="/editorial-policy/">编辑原则</a>
      <a href="/methodology/">评测方法</a>
      <a href="/corrections/">纠错与更新</a>
      <a href="/affiliate-disclosure/">联盟披露</a>
      <a href="/privacy/">隐私政策</a>
      <a href="/terms/">服务条款</a>
      <a href="/disclaimer/">免责声明</a>
      <a href="/contact/">联系我们</a>
      <a href="/sitemap.xml">网站地图</a>
    </div>
    <div class="footer-copy">
      &copy; 2026 JichangNow.com. 保留所有权利。第三方商标归其原权利人所有，本站不暗示任何官方隶属关系。
    </div>
  </div>
</footer>
"""
with open('layouts/partials/footer.html', 'w', encoding='utf-8') as f:
    f.write(footer_html)

# 4. layouts/partials/breadcrumbs.html
breadcrumbs_html = """{{ if not .IsHome }}
<nav class="breadcrumbs" aria-label="breadcrumb">
  <a href="/">首页</a>
  <span>&gt;</span>
  {{ with .Parent }}
    {{ if not .IsHome }}
      <a href="{{ .Permalink }}">{{ .Title }}</a>
      <span>&gt;</span>
    {{ end }}
  {{ end }}
  <span class="current" aria-current="page">{{ .Title }}</span>
</nav>
{{ end }}
"""
with open('layouts/partials/breadcrumbs.html', 'w', encoding='utf-8') as f:
    f.write(breadcrumbs_html)

# 5. layouts/partials/promo-card.html
promo_card_html = """<div class="promo-card">
  <div class="promo-card-content">
    <h4>🚀 配置前置推荐：避免公网中继频繁断连</h4>
    <p>自营高速专线通道：IEPL 内网光纤直连，晚高峰零丢包跑满 4K，新用户立享 8 折专享优惠券。</p>
  </div>
  <a href="https://hueue09.gcvipaff.com/#/?code=z8U9aaa4" target="_blank" rel="sponsored nofollow noopener" class="btn btn-primary">
    查看全球云套餐 (码: qq88)
  </a>
</div>
"""
with open('layouts/partials/promo-card.html', 'w', encoding='utf-8') as f:
    f.write(promo_card_html)

# 6. layouts/partials/schema-jsonld.html
schema_html = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  {{ if .IsHome }}
  "@type": "WebSite",
  "name": "JichangNow",
  "url": "https://tiziview.co/",
  "description": "{{ .Site.Params.description }}"
  {{ else if .IsPage }}
  "@type": "Article",
  "headline": "{{ .Title }}",
  "description": "{{ with .Description }}{{ . }}{{ else }}{{ .Summary }}{{ end }}",
  "url": "{{ .Permalink }}",
  "datePublished": "{{ .Date.Format \"2006-01-02T15:04:05Z07:00\" }}",
  "dateModified": "{{ .Lastmod.Format \"2006-01-02T15:04:05Z07:00\" }}",
  "inLanguage": "zh-CN",
  "publisher": {
    "@type": "Organization",
    "name": "JichangNow",
    "url": "https://tiziview.co"
  }
  {{ else }}
  "@type": "CollectionPage",
  "name": "{{ .Title }}",
  "url": "{{ .Permalink }}",
  "description": "{{ with .Description }}{{ . }}{{ else }}{{ .Site.Params.description }}{{ end }}"
  {{ end }}
}
</script>
"""
with open('layouts/partials/schema-jsonld.html', 'w', encoding='utf-8') as f:
    f.write(schema_html)

# 7. layouts/_default/baseof.html
baseof_html = """<!DOCTYPE html>
<html lang="zh-CN">
{{ partial "head.html" . }}
<body>
  <div class="mobile-header">
    <a href="/" class="mobile-brand">JichangNow</a>
    <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="打开导航菜单">☰ 菜单</button>
  </div>
  <div class="app-container">
    {{ partial "sidebar.html" . }}
    <div class="main-wrapper">
      <main class="content-container">
        {{ partial "breadcrumbs.html" . }}
        {{ block "main" . }}{{ end }}
      </main>
      {{ partial "footer.html" . }}
    </div>
  </div>
  <script src="/js/main.js" defer></script>
</body>
</html>
"""
with open('layouts/_default/baseof.html', 'w', encoding='utf-8') as f:
    f.write(baseof_html)

# 8. layouts/_default/single.html
single_html = """{{ define "main" }}
<article class="article-post">
  <header class="article-header">
    <h1 class="page-title">{{ .Title }}</h1>
    <div class="article-meta">
      <span>📅 发布日期：{{ .Date.Format "2006-01-02" }}</span>
      <span>🔄 最后更新：{{ .Lastmod.Format "2006-01-02" }}</span>
      <span>⏱️ 预计阅读：{{ .ReadingTime }} 分钟</span>
      <span>✍️ 撰写：JichangNow 评测组</span>
    </div>
  </header>

  {{ partial "promo-card.html" . }}

  <div class="article-body">
    {{ .Content }}
  </div>

  {{ partial "promo-card.html" . }}
</article>
{{ end }}
"""
with open('layouts/_default/single.html', 'w', encoding='utf-8') as f:
    f.write(single_html)

# 9. layouts/_default/list.html
list_html = """{{ define "main" }}
<div class="category-header" style="margin-bottom: 2rem;">
  <h1 class="page-title">{{ .Title }}</h1>
  <p style="font-size: 1.05rem; color: #475569; line-height: 1.7;">{{ with .Description }}{{ . }}{{ else }}JichangNow 为您精心准备的深度教程与测评指南，助您零基础快速上手科学上网。{{ end }}</p>
</div>

{{ partial "promo-card.html" . }}

<div class="posts-list">
  {{ range .Pages }}
  <div class="post-card">
    <h3><a href="{{ .Permalink }}">{{ .Title }}</a></h3>
    <p class="post-card-summary">{{ .Summary | plainify | truncate 130 }}</p>
    <div class="article-meta" style="margin-top: 0.5rem;">
      <span>📅 {{ .Date.Format "2006-01-02" }}</span>
      <span>⏱️ {{ .ReadingTime }} 分钟阅读</span>
      <a href="{{ .Permalink }}" style="margin-left: auto; font-weight: 600;">阅读全文 &rarr;</a>
    </div>
  </div>
  {{ end }}
</div>
{{ end }}
"""
with open('layouts/_default/list.html', 'w', encoding='utf-8') as f:
    f.write(list_html)

# 10. layouts/404.html
notfound_html = """{{ define "main" }}
<div style="text-align: center; padding: 4rem 1rem;">
  <h1 style="font-size: 4rem; color: #2563eb; margin-bottom: 1rem;">404</h1>
  <h2 style="font-size: 1.5rem; margin-bottom: 1.5rem;">抱歉，您访问的页面不存在或已被移除</h2>
  <p style="color: #64748b; margin-bottom: 2rem;">可能链接已失效，或者由于站点架构优化更新了路径。</p>
  <div style="display: flex; justify-content: center; gap: 1rem;">
    <a href="/" class="btn btn-primary">返回首页</a>
    <a href="/categories/airport-reviews/" class="btn btn-secondary">查看机场推荐榜</a>
  </div>
</div>
{{ end }}
"""
with open('layouts/404.html', 'w', encoding='utf-8') as f:
    f.write(notfound_html)

print("Layouts written successfully.")
