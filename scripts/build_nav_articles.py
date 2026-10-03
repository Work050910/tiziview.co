# -*- coding: utf-8 -*-
import os

def write_article(category_dir, slug, title, desc, category_name, primary_kw, specific_body):
    path = f"content/categories/{category_dir}/{slug}.md"
    
    # Standard Fixed Top 4 section required for all articles
    top4_section = """
## 🏆 2026 核心机场推荐榜单（固定精选前四）

在深入探讨具体实操前，JichangNow 评测团队根据 2026 年最新人工多网交叉测速结果，为您整理出当前稳定性、口碑与售后保障最为卓越的四家核心服务商，按综合体验严格排序：

1. **[全球云](/providers/quanqiu-cloud/) (Rank 1 · 综合旗舰推荐)**
   - **核心优势**：多国家和地区原生 IP 节点、智能分流调度、晚高峰实测跑满 4K。
   - **参考价格**：20 元/月 起（提供 120GB/月 至 1500GB/月 多梯度套餐）。
   - **专属优惠**：专属优惠码 `qq88` 享 8 折优惠。
   - **官方通道**：[前往全球云官方选购套餐](https://hueue09.gcvipaff.com/#/?code=z8U9aaa4) *(rel="sponsored nofollow noopener")*

2. **[飞猫云](/providers/flycat-cloud/) (Rank 2 · 平价轻量首选)**
   - **核心优势**：折合仅 7 元/月（84元/年），内网 IEPL 专线中继，提供极简小白一键客户端。
   - **参考价格**：84 元/年 起（学生版 50GB/月）。
   - **专属优惠**：新用户专享 8 折优惠码 `flycat888`。
   - **官方通道**：[前往飞猫云官方选购套餐](https://quanqiu.flycatvipaff.cc/#/?code=7ZOeVmNS) *(rel="sponsored nofollow noopener")*

3. **[暮光加速](/providers/twilight/) (Rank 3 · 4K影音与大流量)**
   - **核心优势**：专注晚高峰超清视频流畅加载与主流 AI 工具解锁，大带宽冗余充足。
   - **参考价格**：20 元/月 起（另有年付轻量版 109 元及不限时流量包）。
   - **专属优惠**：专享 8 折优惠码 `mm88`。
   - **官方通道**：[前往暮光加速官方选购套餐](https://quanqi12.twilightaff.com/#/?code=beAVqNPf) *(rel="sponsored nofollow noopener")*

4. **[微风网络](/providers/breezenet/) (Rank 4 · 稳定平价备用)**
   - **核心优势**：全平台兼容性好，支持 Clash Verge Rev、Mihomo Party、v2rayN 一键无缝导入。
   - **参考价格**：以当前官方结算页实时公示为准。
   - **专属优惠**：暂无优惠码。
   - **官方通道**：[前往微风网络官方选购套餐](https://edp01.breezenetaff.com/#/?code=vxDUI8kY) *(rel="sponsored nofollow noopener")*
"""

    full_content = f"""---
title: "{title}"
description: "{desc}"
date: 2026-09-22T08:00:00+08:00
lastmod: 2026-09-22T08:00:00+08:00
categories: ["{category_name}"]
tags: ["科学上网", "梯子推荐", "{primary_kw}", "新手教程"]
primaryKeyword: "{primary_kw}"
---

{specific_body}

{top4_section}

## 常见问题解答 (FAQ)

**Q1：为什么在相同网络环境下，不同客户端的测速与连接表现会有差异？**  
A：不同客户端所采用的网络核心（如 Golang Mihomo 内核、C/Rust 编写的底层驱动）在多线程调度、DNS 本地缓存解析以及虚拟网卡 TUN 接管机制上存在架构差异。建议 Windows 平台首推 Clash Verge Rev，Mac 首推 Mihomo Party，以获得最平稳的系统级代理体验。

**Q2：新手使用机场订阅时，如何最大限度防止个人账号与数据泄露？**  
A：切勿将包含 Token 秘钥的订阅链接公开发布至任何论坛或社交群组；在公共网络环境下优先选用具备 TLS1.3 加密传输的 Trojan 或 Shadowsocks 节点；对于企业级关键账户，务必开启两步验证（2FA）并固定使用同一地区的纯净专线出口。

## 下一步阅读与延伸建议
- 想要了解各服务商的真实机房测速与丢包率对比？欢迎查阅 [2026 机场推荐榜与深度测评](/categories/airport-reviews/)。
- 客户端导入出现报错或 DNS 污染？请直接进入 [常见问题与避坑指南](/categories/faq/) 获取直观解答。
"""

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(full_content)

print("Article generator helper defined.")
