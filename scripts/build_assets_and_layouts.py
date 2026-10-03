# -*- coding: utf-8 -*-
import os

os.makedirs('static/css', exist_ok=True)
os.makedirs('static/js', exist_ok=True)
os.makedirs('static/images', exist_ok=True)
os.makedirs('layouts/_default', exist_ok=True)
os.makedirs('layouts/partials', exist_ok=True)

# 1. CSS
css_content = """/* Anatole Inspired Clean Minimalist CSS for JichangNow */
:root {
  --bg-primary: #f8fafc;
  --bg-surface: #ffffff;
  --bg-sidebar: #1e293b;
  --text-sidebar: #e2e8f0;
  --text-sidebar-muted: #94a3b8;
  --text-primary: #0f172a;
  --text-secondary: #475569;
  --text-muted: #64748b;
  --accent-primary: #2563eb;
  --accent-hover: #1d4ed8;
  --accent-light: #eff6ff;
  --accent-gold: #f59e0b;
  --border-color: #e2e8f0;
  --border-sidebar: #334155;
  --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 14px;
  --sidebar-width: 320px;
  --content-max-width: 860px;
  --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: var(--font-family);
  background-color: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.75;
  font-size: 16px;
  min-height: 100vh;
  display: flex;
}

a {
  color: var(--accent-primary);
  text-decoration: none;
  transition: color 0.2s ease;
}

a:hover {
  color: var(--accent-hover);
  text-decoration: underline;
}

/* Layout Architecture */
.app-container {
  display: flex;
  width: 100%;
  min-height: 100vh;
}

/* Left Sidebar */
.sidebar {
  width: var(--sidebar-width);
  background-color: var(--bg-sidebar);
  color: var(--text-sidebar);
  padding: 2.5rem 1.75rem;
  display: flex;
  flex-direction: column;
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
  flex-shrink: 0;
  border-right: 1px solid var(--border-sidebar);
}

.sidebar-brand {
  text-align: center;
  margin-bottom: 2rem;
}

.sidebar-avatar {
  width: 76px;
  height: 76px;
  border-radius: 50%;
  margin-bottom: 1rem;
  border: 3px solid #38bdf8;
  background: #0f172a;
  padding: 8px;
}

.sidebar-title {
  font-size: 1.4rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 0.4rem;
  letter-spacing: -0.5px;
}

.sidebar-tagline {
  font-size: 0.88rem;
  color: var(--text-sidebar-muted);
  line-height: 1.4;
}

.sidebar-nav {
  margin-bottom: 2rem;
}

.nav-heading {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: #64748b;
  margin-bottom: 0.75rem;
  padding-left: 0.5rem;
  font-weight: 600;
}

.nav-list {
  list-style: none;
}

.nav-item {
  margin-bottom: 0.35rem;
}

.nav-link {
  display: flex;
  align-items: center;
  padding: 0.55rem 0.85rem;
  color: var(--text-sidebar);
  border-radius: var(--radius-sm);
  font-size: 0.95rem;
  transition: all 0.2s ease;
  text-decoration: none;
}

.nav-link:hover, .nav-link.active {
  background-color: rgba(255, 255, 255, 0.1);
  color: #ffffff;
  text-decoration: none;
  font-weight: 600;
}

.sidebar-promo {
  background: linear-gradient(135deg, #1e3a8a 0%, #1e1b4b 100%);
  border: 1px solid #3b82f6;
  border-radius: var(--radius-md);
  padding: 1.25rem 1rem;
  text-align: center;
  margin-top: auto;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
}

.sidebar-promo-badge {
  display: inline-block;
  background: #f59e0b;
  color: #000000;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 999px;
  margin-bottom: 0.5rem;
  text-transform: uppercase;
}

.sidebar-promo h4 {
  font-size: 1rem;
  color: #ffffff;
  margin-bottom: 0.3rem;
}

.sidebar-promo p {
  font-size: 0.8rem;
  color: #bfdbfe;
  margin-bottom: 0.85rem;
  line-height: 1.35;
}

.sidebar-promo .btn-cta {
  display: block;
  background: #2563eb;
  color: #ffffff;
  font-size: 0.85rem;
  font-weight: 600;
  padding: 0.5rem 1rem;
  border-radius: var(--radius-sm);
  text-decoration: none;
  transition: background 0.2s;
}

.sidebar-promo .btn-cta:hover {
  background: #1d4ed8;
  color: #ffffff;
  text-decoration: none;
}

/* Main Content Area */
.main-wrapper {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.content-container {
  max-width: var(--content-max-width);
  margin: 0 auto;
  padding: 3rem 2rem;
  width: 100%;
}

/* Breadcrumbs */
.breadcrumbs {
  font-size: 0.88rem;
  color: var(--text-muted);
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.breadcrumbs a {
  color: var(--text-secondary);
}

.breadcrumbs span.current {
  color: var(--text-primary);
  font-weight: 500;
}

/* Typography & Content */
h1.page-title {
  font-size: 2.2rem;
  line-height: 1.3;
  color: var(--text-primary);
  margin-bottom: 1.25rem;
  font-weight: 800;
  letter-spacing: -0.5px;
}

.hero-box {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 2rem;
  margin-bottom: 2.5rem;
  box-shadow: var(--card-shadow);
}

.hero-tag {
  display: inline-block;
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--accent-primary);
  background: var(--accent-light);
  padding: 4px 12px;
  border-radius: 999px;
  margin-bottom: 0.85rem;
}

.hero-text {
  font-size: 1.05rem;
  color: var(--text-secondary);
  line-height: 1.8;
  margin-bottom: 1.5rem;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  align-items: center;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.65rem 1.35rem;
  font-size: 0.95rem;
  font-weight: 600;
  border-radius: var(--radius-sm);
  cursor: pointer;
  text-decoration: none;
  transition: all 0.2s ease;
  border: none;
}

.btn-primary {
  background: var(--accent-primary);
  color: #ffffff;
}

.btn-primary:hover {
  background: var(--accent-hover);
  color: #ffffff;
  text-decoration: none;
}

.btn-secondary {
  background: #f1f5f9;
  color: var(--text-primary);
  border: 1px solid var(--border-color);
}

.btn-secondary:hover {
  background: #e2e8f0;
  text-decoration: none;
}

/* Post and Article */
.article-header {
  margin-bottom: 2rem;
}

.article-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem;
  font-size: 0.88rem;
  color: var(--text-muted);
  margin-top: 0.75rem;
}

.article-body {
  font-size: 1.05rem;
  line-height: 1.85;
  color: #1e293b;
}

.article-body h2 {
  font-size: 1.55rem;
  margin: 2.25rem 0 1rem;
  color: var(--text-primary);
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 0.4rem;
}

.article-body h3 {
  font-size: 1.25rem;
  margin: 1.75rem 0 0.75rem;
  color: var(--text-primary);
}

.article-body p {
  margin-bottom: 1.25rem;
}

.article-body ul, .article-body ol {
  margin-bottom: 1.25rem;
  padding-left: 1.5rem;
}

.article-body li {
  margin-bottom: 0.5rem;
}

.article-body table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.75rem 0;
  background: var(--bg-surface);
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--card-shadow);
}

.article-body th, .article-body td {
  padding: 0.85rem 1rem;
  text-align: left;
  border-bottom: 1px solid var(--border-color);
  font-size: 0.95rem;
}

.article-body th {
  background: #f1f5f9;
  font-weight: 600;
  color: var(--text-primary);
}

/* Transparent Recommendation Card */
.promo-card {
  background: #f0fdf4;
  border: 1px solid #86efac;
  border-radius: var(--radius-md);
  padding: 1.25rem 1.5rem;
  margin: 2rem 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.promo-card-content h4 {
  font-size: 1.05rem;
  color: #166534;
  margin-bottom: 0.25rem;
}

.promo-card-content p {
  font-size: 0.88rem;
  color: #15803d;
  margin-bottom: 0;
  line-height: 1.4;
}

.promo-card .btn {
  white-space: nowrap;
}

/* Provider Ranking Cards */
.provider-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 1.75rem;
  margin-bottom: 1.75rem;
  box-shadow: var(--card-shadow);
  transition: transform 0.2s, box-shadow 0.2s;
  position: relative;
}

.provider-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
}

.provider-card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
}

.provider-title-group {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.rank-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--accent-primary);
  color: #ffffff;
  font-weight: 700;
  font-size: 0.95rem;
}

.rank-1 { background: #f59e0b; }
.rank-2 { background: #0284c7; }
.rank-3 { background: #7c3aed; }
.rank-4 { background: #059669; }

.provider-name {
  font-size: 1.35rem;
  font-weight: 700;
  color: var(--text-primary);
}

.provider-price {
  font-size: 1.25rem;
  font-weight: 700;
  color: #e11d48;
}

.provider-features {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.feature-tag {
  background: #f1f5f9;
  color: var(--text-secondary);
  font-size: 0.8rem;
  padding: 3px 10px;
  border-radius: var(--radius-sm);
}

.provider-summary {
  font-size: 0.95rem;
  color: var(--text-secondary);
  margin-bottom: 1.25rem;
  line-height: 1.6;
}

.provider-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.75rem;
  border-top: 1px solid var(--border-color);
  padding-top: 1rem;
}

.coupon-box {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: #fffbeb;
  border: 1px dashed #fcd34d;
  padding: 0.35rem 0.75rem;
  border-radius: var(--radius-sm);
  font-size: 0.85rem;
}

.coupon-code {
  font-weight: 700;
  color: #b45309;
  font-family: monospace;
}

.btn-copy {
  background: #fef3c7;
  border: 1px solid #fde68a;
  color: #92400e;
  padding: 2px 8px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.78rem;
}

.btn-copy:hover {
  background: #fde68a;
}

/* Post Cards in Lists */
.post-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  margin-bottom: 1.25rem;
  box-shadow: var(--card-shadow);
  transition: transform 0.2s;
}

.post-card:hover {
  transform: translateY(-2px);
}

.post-card h3 {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}

.post-card h3 a {
  color: var(--text-primary);
}

.post-card h3 a:hover {
  color: var(--accent-primary);
}

.post-card-summary {
  color: var(--text-secondary);
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 0.75rem;
}

/* FAQ Accordion */
.faq-item {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  margin-bottom: 0.85rem;
  overflow: hidden;
}

.faq-question {
  padding: 1rem 1.25rem;
  font-weight: 600;
  cursor: pointer;
  user-select: none;
  background: #f8fafc;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.faq-answer {
  padding: 1.25rem;
  font-size: 0.95rem;
  color: var(--text-secondary);
  line-height: 1.7;
  border-top: 1px solid var(--border-color);
}

/* Footer */
.site-footer {
  background: var(--bg-surface);
  border-top: 1px solid var(--border-color);
  padding: 3rem 2rem 2rem;
  color: var(--text-muted);
  font-size: 0.88rem;
}

.footer-content {
  max-width: var(--content-max-width);
  margin: 0 auto;
}

.footer-narrative {
  margin-bottom: 1.5rem;
  line-height: 1.7;
  color: var(--text-secondary);
}

.footer-links {
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem;
  margin-bottom: 1.5rem;
}

.footer-links a {
  color: var(--text-secondary);
}

.footer-copy {
  text-align: center;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border-color);
  font-size: 0.8rem;
}

/* Mobile Toggle and Responsive */
.mobile-header {
  display: none;
  background: var(--bg-sidebar);
  color: #ffffff;
  padding: 1rem 1.25rem;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 100;
}

.mobile-brand {
  font-size: 1.15rem;
  font-weight: 700;
  color: #ffffff;
}

.mobile-menu-btn {
  background: none;
  border: 1px solid #475569;
  color: #ffffff;
  padding: 0.35rem 0.65rem;
  border-radius: 4px;
  cursor: pointer;
}

@media (max-width: 960px) {
  body {
    flex-direction: column;
  }
  .app-container {
    flex-direction: column;
  }
  .sidebar {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 280px;
    height: 100vh;
    z-index: 200;
    box-shadow: 4px 0 20px rgba(0, 0, 0, 0.4);
  }
  .sidebar.open {
    display: flex;
  }
  .mobile-header {
    display: flex;
  }
  .content-container {
    padding: 1.75rem 1.25rem;
  }
  h1.page-title {
    font-size: 1.75rem;
  }
}
"""

with open('static/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. JavaScript
js_content = """// JichangNow Minimal Script
document.addEventListener('DOMContentLoaded', () => {
  // Mobile drawer toggle
  const menuBtn = document.getElementById('mobileMenuBtn');
  const sidebar = document.getElementById('sidebar');
  if (menuBtn && sidebar) {
    menuBtn.addEventListener('click', () => {
      sidebar.classList.toggle('open');
    });
    // Close sidebar on outside click
    document.addEventListener('click', (e) => {
      if (sidebar.classList.contains('open') && !sidebar.contains(e.target) && !menuBtn.contains(e.target)) {
        sidebar.classList.remove('open');
      }
    });
  }

  // Coupon copy button with instant visual feedback
  document.querySelectorAll('.btn-copy').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const code = btn.getAttribute('data-coupon');
      if (!code || code === '暂无优惠码') return;
      navigator.clipboard.writeText(code).then(() => {
        const origText = btn.textContent;
        btn.textContent = '已复制！';
        btn.style.backgroundColor = '#86efac';
        btn.style.color = '#14532d';
        setTimeout(() => {
          btn.textContent = origText;
          btn.style.backgroundColor = '';
          btn.style.color = '';
        }, 2000);
      }).catch(() => {
        alert('复制失败，请手动长按复制：' + code);
      });
    });
  });
});
"""

with open('static/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# 3. Robots.txt
robots_content = """User-agent: *
Allow: /
Disallow: /admin/
Disallow: /private/

Sitemap: https://tiziview.co/sitemap.xml
"""

with open('static/robots.txt', 'w', encoding='utf-8') as f:
    f.write(robots_content)

# 4. Avatar SVG
avatar_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#38bdf8;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#2563eb;stop-opacity:1" />
    </linearGradient>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#grad1)" />
  <!-- Paper airplane / Rocket speed icon -->
  <path d="M 22 50 L 78 26 L 48 78 L 44 56 Z" fill="#ffffff" />
  <path d="M 44 56 L 78 26 L 54 56 Z" fill="#cbd5e1" opacity="0.8" />
  <circle cx="78" cy="26" r="4" fill="#facc15" />
</svg>"""

with open('static/images/avatar.svg', 'w', encoding='utf-8') as f:
    f.write(avatar_svg)

print("Static assets written successfully.")
