# -*- coding: utf-8 -*-
import glob
import re

top4_cards_html = """
## 🏆 2026 核心机场推荐榜单（固定前四精选）

本站经多网实测核验，为您精选当前稳定性与售后最卓越的四家核心服务商：

<div class="top4-cards-container">
  <!-- Card 1: 全球云 -->
  <div class="top4-box" style="border-left: 5px solid #f59e0b;">
    <div class="top4-box-header">
      <div class="top4-box-title">
        <span class="top4-badge badge-rank-1">1</span>
        <span>全球云 (综合旗舰推荐)</span>
      </div>
      <div class="top4-price">20 元/月 起</div>
    </div>
    <p class="top4-desc">
      主打多国家和地区原生 IP 节点、智能 BGP 调度，晚高峰实测流畅跑满 4K 视频，完美解锁 ChatGPT 与海外主流流媒体。
    </p>
    <div class="top4-footer">
      <div class="coupon-box">
        <span>专属优惠码：</span>
        <span class="coupon-code">qq88</span>
        <button class="btn-copy" data-coupon="qq88">复制</button>
        <small style="color: #64748b; margin-left: 4px;">(享 8 折优惠)</small>
      </div>
      <div style="display: flex; gap: 8px;">
        <a href="/providers/quanqiu-cloud/" class="btn-detail">查看评测</a>
        <a href="https://hueue09.gcvipaff.com/#/?code=z8U9aaa4" target="_blank" rel="sponsored nofollow noopener" class="btn-register">👉 官方选购注册</a>
      </div>
    </div>
  </div>

  <!-- Card 2: 飞猫云 -->
  <div class="top4-box" style="border-left: 5px solid #0284c7;">
    <div class="top4-box-header">
      <div class="top4-box-title">
        <span class="top4-badge badge-rank-2">2</span>
        <span>飞猫云 (平价轻量首选)</span>
      </div>
      <div class="top4-price">84 元/年 (折合 7元/月)</div>
    </div>
    <p class="top4-desc">
      平价小年付代表方案，采用 IEPL 专线中继，附带小白一键极简客户端，超低入门门槛，非常适合轻度浏览与备用网络。
    </p>
    <div class="top4-footer">
      <div class="coupon-box">
        <span>专属优惠码：</span>
        <span class="coupon-code">flycat888</span>
        <button class="btn-copy" data-coupon="flycat888">复制</button>
        <small style="color: #64748b; margin-left: 4px;">(新用户 8 折)</small>
      </div>
      <div style="display: flex; gap: 8px;">
        <a href="/providers/flycat-cloud/" class="btn-detail">查看评测</a>
        <a href="https://quanqiu.flycatvipaff.cc/#/?code=7ZOeVmNS" target="_blank" rel="sponsored nofollow noopener" class="btn-register">👉 官方选购注册</a>
      </div>
    </div>
  </div>

  <!-- Card 3: 暮光加速 -->
  <div class="top4-box" style="border-left: 5px solid #7c3aed;">
    <div class="top4-box-header">
      <div class="top4-box-title">
        <span class="top4-badge badge-rank-3">3</span>
        <span>暮光加速 (4K影音大流量)</span>
      </div>
      <div class="top4-price">20 元/月 起</div>
    </div>
    <p class="top4-desc">
      专注晚高峰超清影视与大带宽突发下载，专线冗余带宽充沛，全节点解锁主流海外流媒体与主流大语言模型。
    </p>
    <div class="top4-footer">
      <div class="coupon-box">
        <span>专属优惠码：</span>
        <span class="coupon-code">mm88</span>
        <button class="btn-copy" data-coupon="mm88">复制</button>
        <small style="color: #64748b; margin-left: 4px;">(专享 8 折优惠)</small>
      </div>
      <div style="display: flex; gap: 8px;">
        <a href="/providers/twilight/" class="btn-detail">查看评测</a>
        <a href="https://quanqi12.twilightaff.com/#/?code=beAVqNPf" target="_blank" rel="sponsored nofollow noopener" class="btn-register">👉 官方选购注册</a>
      </div>
    </div>
  </div>

  <!-- Card 4: 微风网络 -->
  <div class="top4-box" style="border-left: 5px solid #059669;">
    <div class="top4-box-header">
      <div class="top4-box-title">
        <span class="top4-badge badge-rank-4">4</span>
        <span>微风网络 (稳定平价备用)</span>
      </div>
      <div class="top4-price">以结算页为准</div>
    </div>
    <p class="top4-desc">
      全平台协议兼容性好，支持标准 Clash Verge Rev、Mihomo Party、Sing-box 一键导入，适合作为主力与备用双节点池。
    </p>
    <div class="top4-footer">
      <div class="coupon-box">
        <span>专属优惠：</span>
        <span class="coupon-code">暂无优惠码</span>
        <small style="color: #64748b; margin-left: 4px;">(以结算页为准)</small>
      </div>
      <div style="display: flex; gap: 8px;">
        <a href="/providers/breezenet/" class="btn-detail">查看评测</a>
        <a href="https://edp01.breezenetaff.com/#/?code=vxDUI8kY" target="_blank" rel="sponsored nofollow noopener" class="btn-register">👉 官方选购注册</a>
      </div>
    </div>
  </div>
</div>
"""

cross_links_html = """
## 🔗 推荐互链与全平台教程索引

为方便您全设备无缝配置科学上网，推荐延伸阅读以下深度实操指南：
- **桌面端推荐**：[Windows Clash Verge Rev 保姆级配置教程](/categories/windows/clash-verge-rev-windows-tutorial/) 与 [Mac Mihomo Party 客户端完整指南](/categories/mac/mihomo-party-mac-complete-guide/)。
- **移动端推荐**：[iOS Shadowrocket 小火箭免外币账号下载与导入](/categories/ios/shadowrocket-us-account-download-config/) 与 [Android Clash Meta 极速上手](/categories/android/clash-meta-for-android-tutorial/)。
- **故障排障避坑**：[节点全红全部显示 Timeout 超时解决办法](/categories/faq/airport-node-timeout-fix/) 及 [订阅链接无法更新报错修复技巧](/categories/faq/subscription-link-update-failed-solution/)。
- **核心机场排行榜**：[2026 最新好用机场测速排行榜与横向参数对照表](/categories/airport-reviews/)。
- **官方社群通道**：欢迎加入 [Telegram 官方订阅频道](https://t.me/+7Kvx9bNqRFhlM2Q1) 获取实时节点状态。
"""

files = glob.glob('content/categories/**/*.md', recursive=True)
count = 0
for f in files:
    if f.endswith('_index.md'): continue
    with open(f, 'r', encoding='utf-8') as fp:
        raw = fp.read()
    
    # Clean any old visible rel=... text
    raw = raw.replace('(rel="sponsored nofollow noopener")', '')
    raw = raw.replace('(rel=\\"sponsored nofollow noopener\\")', '')
    
    # Split body
    if "## 🏆 2026 核心机场推荐榜单" in raw:
        head_and_body = raw.split("## 🏆 2026 核心机场推荐榜单")[0].strip()
        
        # Check if FAQ is present
        faq_part = ""
        if "## 常见排障与新手自查" in raw:
            faq_part = "## 常见排障与新手自查" + raw.split("## 常见排障与新手自查")[1]
            if "## 延伸阅读" in faq_part:
                faq_part = faq_part.split("## 延伸阅读")[0].strip()
            if "## 下一步阅读" in faq_part:
                faq_part = faq_part.split("## 下一步阅读")[0].strip()
        elif "## 常见问题解答" in raw:
            faq_part = "## 常见问题解答" + raw.split("## 常见问题解答")[1]
            if "## 延伸阅读" in faq_part:
                faq_part = faq_part.split("## 延伸阅读")[0].strip()
            if "## 下一步阅读" in faq_part:
                faq_part = faq_part.split("## 下一步阅读")[0].strip()
        
        new_content = head_and_body + "\n\n" + top4_cards_html + "\n\n" + (faq_part if faq_part else "") + "\n\n" + cross_links_html
        
        # Clean any double newlines
        new_content = re.sub(r'\n{3,}', '\n\n', new_content)
        
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(new_content)
        count += 1

print(f"Updated {count} navigation articles with 4 separated cards, clean nofollow buttons, and rich cross-links.")
