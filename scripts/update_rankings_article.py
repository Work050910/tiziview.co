# -*- coding: utf-8 -*-
import re
import json

def count_chinese_chars(text):
    clean_text = re.sub(r'<[^>]+>', '', text)
    clean_text = re.sub(r'---.*?---', '', clean_text, flags=re.S)
    clean_text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', clean_text)
    clean_text = re.sub(r'http[s]?://\S+', '', clean_text)
    zh_chars = re.findall(r'[\u4e00-\u9fa5]', clean_text)
    return len(zh_chars)

with open("data/providers.json", "r", encoding="utf-8") as f:
    provs = json.load(f)

with open("content/categories/airport-reviews/2026-airport-recommendation-rankings.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace generic FAQ with rankings-specific FAQ
rankings_faq = """## 常见排障与新手自查 (FAQ)

**Q：2026年面对全网几十家翻墙机场，新手应该如何挑选最适合自己的梯子？**  
A：新手选购机场切忌盲目跟风购买长期套餐。首先明确核心场景（网页浏览、4K超清影音、海外大模型AI或跨境办公）；其次重点关注骨干线路，优先选用搭载真实IEPL/IPLC专线的服务商；最后坚持“先月付实测，满意再升级季付”的避坑铁律。

**Q：为什么大榜单前列推荐的优质服务商普遍采用专线而非普通公网中转？**  
A：普通公网中转在敏感时期极易遭遇骨干网拥堵、丢包和QoS限速，导致频繁掉线。而IEPL专线具备物理点对点光纤直连，数据不过公网审查网关，晚高峰全天候零丢包、低抖动，能够实现秒开4K和稳定不卡顿。

**Q：购买大榜单上的机场时，新手如何避免遭遇跑路或充值陷阱？**  
A：防跑路核心是规避“超低价永久套餐”和“买三年送两年”的高危营销盘；优先选择运营两至三年以上的老牌服务商；充值时尽量选用微信或支付宝快捷通道，遇到突发断联首先检查本地客户端时间同步与订阅更新。"""

if "## 常见排障与新手自查 (FAQ)" in content:
    parts = content.split("## 常见排障与新手自查 (FAQ)")
    subparts = parts[1].split("## 🔗 推荐互链与全平台科学上网教程索引")
    content = parts[0] + rankings_faq + "\n\n## 🔗 推荐互链与全平台科学上网教程索引" + subparts[1]

# Now let's update card prices and coupons
# For each provider in provs, make sure price and coupon are formatted cleanly
coupon_replacements = {
    4: ("以结算页为准 · 100GB/月 (记录 137元/年)", "16 元/月 · 100GB/月 · （专属券码: `wfwl88`）"),
    5: ("20 元/月 · 120GB/月 · 基础版20元/月", "20 元/月 · 120GB/月 · （专属券码: `u1s188`）"),
    6: ("15.5 元/月 · 100GB/月 · 基础版15.5元/月", "15.5 元/月 · 100GB/月 · （专属券码: `jly88`）"),
    7: ("18 元/月 · 110GB/月 · 基础版18元/月", "18 元/月 · 110GB/月 · （专属券码: `gnt88`）"),
    8: ("17 元/月 · 110GB/月 · 基础版17元/月", "17 元/月 · 110GB/月 · （专属券码: `gsy88`）"),
    9: ("14.9 元/月 · 100GB/月 · 基础版14.9元/月", "14.9 元/月 · 100GB/月 · （专属券码: `wty88`）"),
    10: ("14.9 元/月 · 100GB/月 · 基础版14.9元/月", "14.9 元/月 · 100GB/月 · （专属券码: `yzy88`）"),
    11: ("25 元/月 · 150GB/月 · 基础版25元/月", "25 元/月 · 150GB/月 · （专属券码: `sj88`）"),
    12: ("20 元/月 · 120GB/月 · 多种不限时大流量包", "20 元/月 · 120GB/月 · （专属券码: `sgy88`）"),
    13: ("10 元/月 · 30GB/月 · 基础版22元100GB/月", "18.5 元/月 · 100GB/月 · （专属券码: `kl88`）"),
    14: ("20 元/月 · 100GB/月 · 多档大容量套餐丰富", "20 元/月 · 100GB/月 · （专属券码: `emy88`）"),
    15: ("30 元/月 · 150GB/月 · 大流量梯度专属套餐", "16.8 元/月 · 120GB/月 · （专属券码: `yfy88`）"),
    16: ("25 元/月 · 120GB/月 · 年付入门108元", "25 元/月 · 120GB/月 · （专属券码: `byjd88`）"),
    17: ("9 元/月 · 45GB/月 · 常规标准版25元150G", "19.9 元/月 · 150GB/月 · （专属券码: `kxy88`）"),
    19: ("25 元/月 · 125GB/月 · （专属券码: `tiziyun` 8折）", "17.5 元/月 · 110GB/月 · （专属券码: `tzy88`）"),
    23: ("10 元/月 · 30GB/月 · 灵活小包按需选购", "18.8 元/月 · 120GB/月 · （专属券码: `wylj88`）"),
    24: ("85 元/年 (折合7元/月) · 45GB/年 · 平价备用", "85 元/年 · 45GB/年 · （专属券码: `lmwl88`）"),
    25: ("96 元/年 (折合8元/月) · 60GB/月 · 轻量专线", "96 元/年 (折合8元/月) · 60GB/月 · （专属券码: `sy88`）"),
    26: ("96 元/年 (折合8元/月) · 60GB/月 · 轻量稳定", "96 元/年 (折合8元/月) · 60GB/月 · （专属券码: `ff88`）"),
    27: ("20 元/月 · 120GB/月 · 阶梯流量覆盖全面", "20 元/月 · 120GB/月 · （专属券码: `kjy88`）")
}

for r, (old_p, new_p) in coupon_replacements.items():
    if old_p in content:
        content = content.replace(old_p, new_p)
        print(f"Updated card #{r} price & coupon.")
    else:
        print(f"Pattern for card #{r} not found!")

cnt = count_chinese_chars(content)
print("Updated rankings article Chinese count:", cnt)

with open("content/categories/airport-reviews/2026-airport-recommendation-rankings.md", "w", encoding="utf-8") as f:
    f.write(content)
