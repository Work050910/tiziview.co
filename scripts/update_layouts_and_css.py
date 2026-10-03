# -*- coding: utf-8 -*-

# 1. layouts/partials/sidebar.html
sidebar_html = """<aside class="sidebar" id="sidebar">
  <div class="sidebar-brand">
    <a href="/" style="display: inline-block;">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="76" height="76" class="sidebar-avatar" style="border: 3px solid #38bdf8; border-radius: 50%; background: #0f172a; padding: 4px; display: block; margin: 0 auto 1rem;">
        <defs>
          <linearGradient id="avatarGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#38bdf8;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#2563eb;stop-opacity:1" />
          </linearGradient>
        </defs>
        <circle cx="50" cy="50" r="48" fill="url(#avatarGrad)" />
        <path d="M 22 50 L 78 26 L 48 78 L 44 56 Z" fill="#ffffff" />
        <path d="M 44 56 L 78 26 L 54 56 Z" fill="#cbd5e1" opacity="0.8" />
        <circle cx="78" cy="26" r="4" fill="#facc15" />
      </svg>
    </a>
    <h2 class="sidebar-title"><a href="/" style="color: #ffffff; text-decoration: none; font-size: 1.5rem; font-weight: 800;">机场看</a></h2>
    <p class="sidebar-tagline" style="color: #94a3b8; font-size: 0.88rem;">即刻连接 · 现测可用 · 简单易用</p>
  </div>

  <div class="sidebar-nav">
    <div class="nav-heading" style="color: #94a3b8; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.75rem; padding-left: 0.5rem; font-weight: 700;">全平台配置导航</div>
    <ul class="nav-list" style="list-style: none; padding: 0; margin: 0;">
      <li class="nav-item" style="margin-bottom: 0.35rem;">
        <a href="/" class="nav-link nav-link-home">
          <span class="nav-icon">🏠</span>
          <span class="nav-text">首页</span>
        </a>
      </li>
      <li class="nav-item" style="margin-bottom: 0.35rem;">
        <a href="/categories/airport-reviews/" class="nav-link">
          <span class="nav-icon">🚀</span>
          <span class="nav-text">机场推荐榜</span>
        </a>
      </li>
      <li class="nav-item" style="margin-bottom: 0.35rem;">
        <a href="/categories/windows/" class="nav-link">
          <span class="nav-icon">💻</span>
          <span class="nav-text">Windows教程</span>
        </a>
      </li>
      <li class="nav-item" style="margin-bottom: 0.35rem;">
        <a href="/categories/mac/" class="nav-link">
          <span class="nav-icon">🍎</span>
          <span class="nav-text">Mac教程</span>
        </a>
      </li>
      <li class="nav-item" style="margin-bottom: 0.35rem;">
        <a href="/categories/ios/" class="nav-link">
          <span class="nav-icon">📱</span>
          <span class="nav-text">iOS小火箭教程</span>
        </a>
      </li>
      <li class="nav-item" style="margin-bottom: 0.35rem;">
        <a href="/categories/android/" class="nav-link">
          <span class="nav-icon">🤖</span>
          <span class="nav-text">Android教程</span>
        </a>
      </li>
      <li class="nav-item" style="margin-bottom: 0.35rem;">
        <a href="/categories/faq/" class="nav-link">
          <span class="nav-icon">💡</span>
          <span class="nav-text">常见问题与踩坑</span>
        </a>
      </li>
      <li class="nav-item" style="margin-bottom: 0.35rem;">
        <a href="/faq/" class="nav-link">
          <span class="nav-icon">❓</span>
          <span class="nav-text">100问知识中心</span>
        </a>
      </li>
      <li class="nav-item" style="margin-bottom: 0.35rem;">
        <a href="/services/" class="nav-link">
          <span class="nav-icon">⭐</span>
          <span class="nav-text">自营精选服务</span>
        </a>
      </li>
    </ul>
  </div>

  <div style="margin-bottom: 1.5rem;">
    <a href="https://t.me/+7Kvx9bNqRFhlM2Q1" target="_blank" rel="noopener noreferrer" style="display: flex; align-items: center; justify-content: center; gap: 8px; background: #0088cc; color: #ffffff; padding: 0.6rem 1rem; border-radius: 8px; font-weight: 700; font-size: 0.9rem; text-decoration: none; box-shadow: 0 4px 10px rgba(0,136,204,0.3);">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="#ffffff"><path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.894 8.221l-1.97 9.28c-.145.658-.537.818-1.084.508l-3-2.21-1.446 1.394c-.16.16-.295.295-.605.295l.213-3.053 5.56-5.023c.242-.213-.054-.333-.373-.121l-6.871 4.326-2.962-.924c-.643-.204-.657-.643.136-.953l11.57-4.461c.535-.194 1.006.131.832.946z"/></svg>
      加入 Telegram 频道
    </a>
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

# 2. layouts/partials/footer.html
footer_html = """<footer class="site-footer">
  <div class="footer-content">
    <div class="footer-narrative">
      <p><strong>机场看 (tiziview.co) 官方博客</strong>专注小白的科学上网指南，持续提供 2026 翻墙梯子节点透明评测、高性价比稳定机场推荐、跨平台客户端配置教程与安全隐私保护，助您实现全设备极速平稳连接。</p>
      <p style="margin-top: 0.5rem; font-size: 0.85rem; color: #64748b;">
        📢 <strong>官方 Telegram 频道：</strong><a href="https://t.me/+7Kvx9bNqRFhlM2Q1" target="_blank" rel="noopener noreferrer" style="color: #0284c7; font-weight: 600;">https://t.me/+7Kvx9bNqRFhlM2Q1</a> （实时节点测速更新与紧急通知）
      </p>
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
      <a href="https://t.me/+7Kvx9bNqRFhlM2Q1" target="_blank" rel="noopener noreferrer">TG频道</a>
      <a href="/sitemap.xml">网站地图</a>
    </div>
    <div class="footer-copy">
      &copy; 2026 机场看 (tiziview.co). 保留所有权利。第三方商标归其原权利人所有，本站不暗示任何官方隶属关系。
    </div>
  </div>
</footer>
"""

with open('layouts/partials/footer.html', 'w', encoding='utf-8') as f:
    f.write(footer_html)

# 3. Append CSS enhancements to static/css/style.css
css_append = """
/* Enhancements for Sidebar Navigation and Grid Table */
.nav-link {
  display: flex !important;
  align-items: center !important;
  gap: 0.65rem !important;
  color: #ffffff !important; /* All nav items are bright white */
  text-decoration: none !important;
  padding: 0.55rem 0.85rem !important;
  border-radius: 6px !important;
  font-size: 0.95rem !important;
  transition: all 0.2s ease !important;
}

.nav-link .nav-icon {
  font-size: 1.15rem !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 24px !important;
}

.nav-link .nav-text {
  color: #ffffff !important; /* Pure white text */
  font-weight: 600 !important;
}

.nav-link:hover {
  background-color: rgba(255, 255, 255, 0.15) !important;
  color: #ffffff !important;
  text-decoration: none !important;
}

.nav-link.active, .nav-link-home {
  color: #ffffff !important;
}

.nav-link.active .nav-text, .nav-link-home .nav-text {
  color: #ffffff !important;
}

/* Explicit Grid Table with clear cell borders */
.comparison-grid-table {
  width: 100% !important;
  border-collapse: collapse !important;
  margin: 1.75rem 0 !important;
  background: #ffffff !important;
  border: 2px solid #94a3b8 !important;
  border-radius: 8px !important;
  overflow: hidden !important;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05) !important;
}

.comparison-grid-table th, .comparison-grid-table td {
  border: 1px solid #cbd5e1 !important; /* Clear visible grid line */
  padding: 10px 14px !important;
  text-align: left !important;
  font-size: 0.92rem !important;
  vertical-align: middle !important;
}

.comparison-grid-table th {
  background: #e2e8f0 !important;
  color: #0f172a !important;
  font-weight: 700 !important;
  border-bottom: 2px solid #64748b !important;
  white-space: nowrap !important;
}

.comparison-grid-table tr:nth-child(even) {
  background: #f8fafc !important;
}

.comparison-grid-table tr:hover {
  background: #f1f5f9 !important;
}

/* 4 Distinct Separated Airport Cards in Tutorial Articles */
.top4-cards-container {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  margin: 1.75rem 0 2.25rem;
}

.top4-box {
  background: #ffffff;
  border: 1.5px solid #cbd5e1;
  border-radius: 12px;
  padding: 1.25rem 1.5rem;
  box-shadow: 0 2px 5px rgba(0,0,0,0.04);
  transition: transform 0.2s, box-shadow 0.2s;
}

.top4-box:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0,0,0,0.08);
}

.top4-box-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px dashed #e2e8f0;
}

.top4-box-title {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-size: 1.2rem;
  font-weight: 800;
  color: #0f172a;
}

.top4-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  color: #ffffff;
  font-weight: 700;
  font-size: 0.85rem;
}

.badge-rank-1 { background: #f59e0b; }
.badge-rank-2 { background: #0284c7; }
.badge-rank-3 { background: #7c3aed; }
.badge-rank-4 { background: #059669; }

.top4-price {
  font-size: 1.1rem;
  font-weight: 700;
  color: #e11d48;
}

.top4-desc {
  font-size: 0.95rem;
  color: #334155;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.top4-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.btn-register {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: #2563eb;
  color: #ffffff !important;
  font-weight: 700;
  font-size: 0.92rem;
  padding: 0.55rem 1.25rem;
  border-radius: 6px;
  text-decoration: none !important;
  box-shadow: 0 2px 4px rgba(37,99,235,0.25);
  transition: background 0.2s;
}

.btn-register:hover {
  background: #1d4ed8;
  color: #ffffff !important;
}

.btn-detail {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: #f1f5f9;
  color: #1e293b !important;
  border: 1px solid #cbd5e1;
  font-weight: 600;
  font-size: 0.88rem;
  padding: 0.45rem 0.95rem;
  border-radius: 6px;
  text-decoration: none !important;
}

.btn-detail:hover {
  background: #e2e8f0;
}
"""

with open('static/css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_append)

print("Updated sidebar, footer, and CSS.")
