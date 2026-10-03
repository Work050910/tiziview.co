# -*- coding: utf-8 -*-
import glob
import re

compact_top4 = """
## 🏆 2026 核心机场推荐榜单（固定前四）

本站经多网实测核验，为您整理当前稳定性与售后最卓越的四家服务商：

1. **[全球云](/providers/quanqiu-cloud/) (Rank 1 · 综合旗舰推荐)**：多国原生IP、智能分流、晚高峰流畅4K。参考价20元/月起，优惠码 `qq88` 享8折。[前往全球云选购](https://hueue09.gcvipaff.com/#/?code=z8U9aaa4) *(rel="sponsored nofollow noopener")*。
2. **[飞猫云](/providers/flycat-cloud/) (Rank 2 · 平价轻量首选)**：折合7元/月，IEPL专线中继，极简小白客户端。84元/年起，新用户优惠码 `flycat888`。[前往飞猫云选购](https://quanqiu.flycatvipaff.cc/#/?code=7ZOeVmNS) *(rel="sponsored nofollow noopener")*。
3. **[暮光加速](/providers/twilight/) (Rank 3 · 4K影音大流量)**：晚高峰超清视频与AI解锁，带宽冗余充足。20元/月起，优惠码 `mm88`。[前往暮光加速选购](https://quanqi12.twilightaff.com/#/?code=beAVqNPf) *(rel="sponsored nofollow noopener")*。
4. **[微风网络](/providers/breezenet/) (Rank 4 · 稳定平价备用)**：全平台兼容性好，支持Clash、Sing-box一键导入。价格以结算页为准。[前往微风网络选购](https://edp01.breezenetaff.com/#/?code=vxDUI8kY) *(rel="sponsored nofollow noopener")*。
"""

compact_faq = """
## 常见排障与新手自查 (FAQ)

**Q1：不同客户端在相同网络下测速为何有差异？**  
A：不同客户端底层核心（如Mihomo内核与C/Rust驱动）在并发调度与DNS解析上机制不同。Windows首推Clash Verge Rev，Mac首推Mihomo Party。

**Q2：如何防止订阅被盗刷与泄露？**  
A：切勿将含Token的链接公开发布；公共网络选用TLS1.3加密专线；重要账户开启2FA并固定同地区专线出口。

## 延伸阅读
- 各服务商真实机房测速与丢包率对比：[2026 机场推荐榜与深度测评](/categories/airport-reviews/)。
- 客户端导入报错或DNS污染排查：[常见问题与避坑指南](/categories/faq/)。
"""

files = glob.glob('content/categories/**/*.md', recursive=True)
for f in files:
    if f.endswith('_index.md'): continue
    with open(f, 'r', encoding='utf-8') as fp:
        raw = fp.read()
    
    # Split out the specific body before top4
    if "## 🏆 2026 核心机场推荐榜单" in raw:
        head_and_body = raw.split("## 🏆 2026 核心机场推荐榜单")[0].strip()
        new_content = head_and_body + "\n" + compact_top4 + "\n" + compact_faq
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(new_content)

print("Nav articles standardized.")
