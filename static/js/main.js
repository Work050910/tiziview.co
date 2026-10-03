// 梯子view Minimal Script
document.addEventListener('DOMContentLoaded', () => {
  // Mobile drawer toggle and overlay
  const menuBtn = document.getElementById('mobileMenuBtn');
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('mobileOverlay');
  const closeBtn = document.getElementById('sidebarCloseBtn');

  function openSidebar() {
    if (sidebar) sidebar.classList.add('open');
    if (overlay) overlay.classList.add('active');
    document.body.classList.add('sidebar-open');
  }

  function closeSidebar() {
    if (sidebar) sidebar.classList.remove('open');
    if (overlay) overlay.classList.remove('active');
    document.body.classList.remove('sidebar-open');
  }

  if (menuBtn) {
    menuBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (sidebar && sidebar.classList.contains('open')) {
        closeSidebar();
      } else {
        openSidebar();
      }
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      closeSidebar();
    });
  }

  if (overlay) {
    overlay.addEventListener('click', closeSidebar);
  }

  // Close drawer when clicking any link inside sidebar on mobile
  if (sidebar) {
    sidebar.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 960) {
          closeSidebar();
        }
      });
    });
  }

  // Close drawer on ESC key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeSidebar();
    }
  });

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

  // FAQ Expand All / Collapse All & individual toggle
  const btnExpandAll = document.getElementById('btnExpandAll');
  const btnCollapseAll = document.getElementById('btnCollapseAll');
  const faqItems = document.querySelectorAll('.faq-item');

  function expandAllFAQs() {
    faqItems.forEach(item => {
      item.classList.remove('collapsed');
      const badge = item.querySelector('.faq-badge-expanded');
      if (badge) badge.textContent = '▼ 已展开';
    });
    if (btnExpandAll) btnExpandAll.classList.add('active');
    if (btnCollapseAll) btnCollapseAll.classList.remove('active');
  }

  function collapseAllFAQs() {
    faqItems.forEach(item => {
      item.classList.add('collapsed');
      const badge = item.querySelector('.faq-badge-expanded');
      if (badge) badge.textContent = '▶ 点击展开';
    });
    if (btnExpandAll) btnExpandAll.classList.remove('active');
    if (btnCollapseAll) btnCollapseAll.classList.add('active');
  }

  if (btnExpandAll) btnExpandAll.addEventListener('click', expandAllFAQs);
  if (btnCollapseAll) btnCollapseAll.addEventListener('click', collapseAllFAQs);

  faqItems.forEach(item => {
    const q = item.querySelector('.faq-question');
    if (q) {
      q.addEventListener('click', () => {
        item.classList.toggle('collapsed');
        const isCollapsed = item.classList.contains('collapsed');
        const badge = item.querySelector('.faq-badge-expanded');
        if (badge) {
          badge.textContent = isCollapsed ? '▶ 点击展开' : '▼ 已展开';
        }
      });
    }
  });

  // Ensure on initial load, all FAQs are 100% expanded
  if (faqItems.length > 0) {
    expandAllFAQs();
  }
});
