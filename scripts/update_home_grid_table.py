# -*- coding: utf-8 -*-
import json

with open('data/providers.json', 'r', encoding='utf-8') as f:
    providers = json.load(f)

table_rows_html = """
<div class="mobile-table-hint">
  <span>👉 左右滑动查看完整 27 家服务商横向参数 👈</span>
</div>
<div class="comparison-table-wrapper">
<table class="comparison-grid-table">
  <thead>
    <tr>
      <th class="col-center col-nowrap" style="width: 50px;">排名</th>
      <th class="col-nowrap" style="width: 110px;">服务商名称</th>
      <th class="col-nowrap" style="width: 110px;">起步价格</th>
      <th class="col-nowrap" style="width: 100px;">起步流量</th>
      <th class="col-nowrap">专属优惠码</th>
      <th class="col-center col-nowrap" style="width: 95px;">独立测评</th>
      <th class="col-center col-nowrap" style="width: 95px;">官方通道</th>
    </tr>
  </thead>
  <tbody>
"""

for p in providers:
    rank = p['rank']
    name = p['name']
    slug = p['slug']
    price = p['priceFrom']
    traffic = p['trafficFrom']
    coupon = p['coupon']
    coupon_str = f"<code>{coupon}</code>" if coupon and coupon != "暂无优惠码" else '<span style="color: #94a3b8; font-size: 0.8rem;">暂无</span>'
    invite_url = p['inviteURL']
    
    table_rows_html += f"""    <tr>
      <td class="col-center col-nowrap" style="font-weight: 700;">{rank}</td>
      <td class="col-nowrap" style="font-weight: 700; color: #0f172a;">{name}</td>
      <td class="col-nowrap" style="color: #e11d48; font-weight: 600;">{price}</td>
      <td class="col-nowrap">{traffic}</td>
      <td class="col-nowrap">{coupon_str}</td>
      <td class="col-center col-nowrap"><a href="/providers/{slug}/" class="btn-detail">查看测评</a></td>
      <td class="col-center col-nowrap"><a href="{invite_url}" target="_blank" rel="sponsored nofollow noopener" class="btn-register">官方选购</a></td>
    </tr>
"""

table_rows_html += """  </tbody>
</table>
</div>
"""

with open('content/_index.md', 'r', encoding='utf-8') as f:
    home_content = f.read()

# Replace the table section
if "## 📊 快速横向对比总表" in home_content:
    parts = home_content.split("## 📊 快速横向对比总表")
    after_table = parts[1].split("## 💻 跨平台新手客户端保姆级配置入口")
    
    new_home = parts[0] + "## 📊 快速横向对比总表（全网27家服务商参数对照表）\n\n" + table_rows_html + "\n## 💻 跨平台新手客户端保姆级配置入口" + after_table[1]
    
    with open('content/_index.md', 'w', encoding='utf-8') as f:
        f.write(new_home)
    print("Updated content/_index.md with 27-provider grid table.")
else:
    print("Pattern '## 📊 快速横向对比总表' not found in content/_index.md")
