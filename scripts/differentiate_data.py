# -*- coding: utf-8 -*-
import os
import re
import json

# ==============================================================================
# 1. Unique Interlink Blocks by Category
# ==============================================================================
CATEGORY_INTERLINKS = {
    "windows": """## 🔗 Windows 进阶玩法与系统代理排障索引

为保障 Windows 桌面端长期平稳运行并彻底杜绝系统代理异常，推荐延伸阅读以下针对性配置实操：
- **核心系统接管**：[Clash Verge Rev TUN 虚拟网卡模式配置教程](/categories/windows/clash-verge-rev-tun-mode-setup/)，深度接管各类不支持系统代理的桌面应用与游戏。
- **排障与自救**：[Windows 系统代理死锁与浏览器红叉排查](/categories/windows/windows-system-proxy-troubleshooting/)，手把手解决代理异常关闭后无法上网的常见故障。
- **分流防偷跑**：[Windows 客户端分流规则自定义与国内直连优化](/categories/windows/windows-sub-rule-group-routing/)，智能规避国内流量误走代理节点。
- **现代化替代方案**：[Mihomo Party Windows 客户端安装与配置全流程](/categories/windows/mihomo-party-windows-guide/)，体验现代化高颜值交互界面。
- **优质梯子推荐**：[2026 最新翻墙梯子排行榜与横向参数对照表](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "mac": """## 🔗 macOS 生产力与生态环境进阶索引

为了在 Apple Silicon 芯片与 macOS 现代化桌面环境中获取更出色的网络加速体验，推荐阅读以下专属指南：
- **架构专属调优**：[Mac Apple Silicon M系列芯片专用 ARM64 客户端调优](/categories/mac/mac-m-series-apple-silicon-tuning/)，释放原生架构能耗比优势。
- **开发者必备**：[Mac 终端 Terminal 与增强模式代理配置实操教程](/categories/mac/mac-enhanced-mode-terminal-proxy/)，彻底搞定 Git、Homebrew 及命令行加速。
- **浏览器排障**：[Mac Safari 与 Chrome 浏览器代理防死锁排查指南](/categories/mac/mac-safari-chrome-proxy-bypass/)，告别系统网络设置黄叹号。
- **新兴极简轻量**：[Sing-box Mac 客户端配置教程](/categories/mac/sing-box-mac-tutorial/)，体验无图形库绑架的超低内存开销。
- **核心节点推荐**：[2026 稳定好用翻墙梯子测速排行榜](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "ios": """## 🔗 iOS 移动生态与保活优化进阶索引

针对 iPhone 与 iPad 系统的内存管理机制与后台应用限制，推荐继续查阅以下针对性实操攻略：
- **电量与长效连接**：[iPhone 后台频繁掉线排查与网络长效保活省电优化指南](/categories/ios/ios-battery-saving-background-keepalive/)，彻底避免熄屏断流。
- **必备海外账号**：[苹果美区 Apple ID 注册与海外付费应用充值避坑指南](/categories/ios/ios-apple-id-purchase-guide/)，安全获取正版客户端。
- **高颜值高阶工具**：[Loon iOS 客户端新手配置上手指南](/categories/ios/loon-ios-setup-tutorial/) 与 [Quantumult X 圈X 规则进阶解析](/categories/ios/quantumult-x-ios-novice-guide/)。
- **极简低功耗**：[Sing-box iOS 客户端配置教程](/categories/ios/sing-box-ios-configuration/)，体验极速省电网络接管。
- **优质专线节点**：[2026 最新机场推荐测速排行榜单](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "android": """## 🔗 Android 深度调优与跨设备生态索引

针对国内主流安卓厂商系统的激进省电策略与定制 ROM 特性，推荐延伸参考以下深度实战方案：
- **常驻后台防杀**：[安卓系统电池优化白名单与常驻后台保活配置](/categories/android/android-battery-optimization-whitelist/)，彻底搞定熄屏断开痛点。
- **应用分流隔离**：[安卓分应用代理（Split Tunnel）实操技巧](/categories/android/android-app-proxy-bypass-split-tunnel/)，杜绝国内银行与社交应用误走海外线路。
- **大屏家庭场景**：[电视盒子与智能投影 Android TV 专用安装教程](/categories/android/android-tv-box-clash-installation/)，客厅大屏秒开 4K 超清。
- **极简原生代理**：[v2rayNG 安卓客户端极简轻量配置](/categories/android/v2rayng-android-configuration/) 与 [Sing-box 安卓入门指南](/categories/android/sing-box-android-novice-guide/)。
- **高品质节点索引**：[2026 核心机场推荐榜单与测速对比](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "faq": """## 🔗 常见网络排障与安全防御实操索引

若您在日常连接过程中遭遇其他报错或突发断网，可根据故障现象查阅以下针对性自救指南：
- **超时与连接失败**：[节点全部显示超时（Timeout）自救指南](/categories/faq/airport-node-timeout-troubleshooting/)，快速定位链路故障源头。
- **订阅报错排查**：[机场订阅链接无法更新与 Network Error 深度修复](/categories/faq/subscription-link-update-failed-solution/)，恢复节点同步。
- **数字资产与防盗**：[机场跑路征兆识别与资金避险自救策略](/categories/faq/airport-running-away-defense-strategy/) 及 [订阅链接防泄漏必备常识](/categories/faq/airport-subscription-security-leak-prevention/)。
- **隐私与 DNS 泄漏**：[客户端 TUN 模式防 DNS 泄漏实战](/categories/faq/client-tun-mode-dns-leak-prevention/) 及 [免费公开节点黑客蜜罐风险揭秘](/categories/faq/free-nodes-security-privacy-risks/)。
- **稳定节点推荐**：[2026 最新优质机场推荐榜单](/categories/airport-reviews/2026-airport-recommendation-rankings/)。"""
}

# Unique Interlink Blocks for 14 Airport Reviews
AIRPORT_REVIEW_INTERLINKS = {
    "4k-streaming-netflix-airport.md": """## 🔗 流媒体追剧与超清影音进阶索引

为了让您在全设备畅享超高清影音并规避流媒体地区封锁，建议延伸阅读以下专属评测：
- **高带宽大吞吐**：[大带宽大流量机场推荐](/categories/airport-reviews/high-bandwidth-large-traffic-airport/)，满足 4K/8K 码率与海量剧集缓存。
- **低延迟亚太专线**：[香港日本低延迟节点机场推荐](/categories/airport-reviews/hong-kong-japan-low-latency-nodes/)，实现视频列表秒级响应与拖动零缓冲。
- **流媒体排障指南**：[Netflix与Disney+非自制剧解锁失败彻底排查](/categories/faq/netflix-disney-streaming-unlock-tips/)。
- **大屏观影方案**：[电视盒子与智能投影 Android TV 专用安装教程](/categories/android/android-tv-box-clash-installation/)。
- **全网综合排名**：[2026 最新好用机场测速排行榜与横向参数对照表](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "ai-tools-chatgpt-claude-airport.md": """## 🔗 AI 大模型生态与开发者加速索引

为了协助您全方位构建高效无阻的海外 AI 生产力工作流，推荐延伸阅读以下深度指南：
- **原生住宅IP鉴别**：[ChatGPT原生家庭住宅IP选购指南](/categories/airport-reviews/chatgpt-native-ip-airport/)，深度识别双 ISP 家宽出口。
- **外贸商务协同**：[跨国远程办公与外贸独立站专线梯子推荐](/categories/airport-reviews/cross-border-remote-work-airport/)，保护商业资产安全。
- **访问被拒自救**：[ChatGPT提示Access Denied或IP被封锁的高效换节点解法](/categories/faq/chatgpt-ip-blocked-node-switching/)。
- **桌面终端加速**：[Mac 终端 Terminal 与增强模式代理配置教程](/categories/mac/mac-enhanced-mode-terminal-proxy/)。
- **核心节点排行**：[2026 稳定好用翻墙梯子测速排行榜](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "backup-emergency-cheap-airport.md": """## 🔗 灾备容灾与防失联体系索引

为了防止主力机场突发断网或跑路导致的业务中断，推荐延伸参考以下容灾方案：
- **灵活月付方案**：[2026按月付费便宜机场精选](/categories/airport-reviews/monthly-pay-cheap-airport/)，随时取消、无绑架平价专线。
- **平价横向测评**：[十元内高性价比平价机场横向测速对比](/categories/airport-reviews/value-cheap-airport-comparison/)。
- **机场跑路识别**：[机场跑路征兆识别与资金避险自救策略](/categories/faq/airport-running-away-defense-strategy/)。
- **连接超时排查**：[节点全部显示超时（Timeout）自救指南](/categories/faq/airport-node-timeout-troubleshooting/)。
- **综合总榜参考**：[2026 最新机场推荐测速排行榜单](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "chatgpt-native-ip-airport.md": """## 🔗 原生住宅 IP 与风控规避进阶索引

为了全方位掌握 IP 纯净度鉴别技巧并彻底规避各类平台的风控封禁，推荐阅读以下攻略：
- **多模型生产力**：[2026海外AI大模型与开发者专线机场推荐](/categories/airport-reviews/ai-tools-chatgpt-claude-airport/)，兼顾 Claude 与 Cursor。
- **跨国商务专线**：[跨国远程办公与外贸独立站专线梯子推荐](/categories/airport-reviews/cross-border-remote-work-airport/)，固定商业 IP 防关联。
- **IP封禁高效自救**：[ChatGPT提示Access Denied或IP被封锁的高效换节点解法](/categories/faq/chatgpt-ip-blocked-node-switching/)。
- **虚拟网卡接管**：[Clash Verge Rev TUN 虚拟网卡服务模式配置教程](/categories/windows/clash-verge-rev-tun-mode-setup/)。
- **核心排行榜单**：[2026 最新好用机场测速排行榜与参数表](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "cross-border-remote-work-airport.md": """## 🔗 跨境业务与出海企业加速索引

为了保障跨国协同办公、外贸店铺资产与海外支付通道的高度安全，推荐查阅以下专线方案：
- **原生住宅IP方案**：[ChatGPT原生家庭住宅IP选购指南](/categories/airport-reviews/chatgpt-native-ip-airport/)，保障海外支付与账户合规。
- **多设备并发支持**：[多设备不限并发通用机场推荐](/categories/airport-reviews/multi-device-family-office-airport/)，满足多人团队同时在线。
- **安全防泄漏技巧**：[客户端 TUN 模式防 DNS 泄漏实战指南](/categories/faq/client-tun-mode-dns-leak-prevention/)。
- **系统代理排障**：[Windows 系统代理死锁与浏览器红叉排查](/categories/windows/windows-system-proxy-troubleshooting/)。
- **核心服务总榜**：[2026 稳定好用翻墙梯子测速排行榜](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "high-bandwidth-large-traffic-airport.md": """## 🔗 海量流量与极速下载方案索引

针对大文件多线程并发下载、超高清追剧与家庭多设备共享的带宽挑战，推荐继续查阅：
- **流媒体专线支持**：[4K/8K流媒体非自制剧解锁机场推荐](/categories/airport-reviews/4k-streaming-netflix-airport/)，秒开超清无缓冲。
- **全家多端共享**：[多设备不限并发通用机场推荐](/categories/airport-reviews/multi-device-family-office-airport/)，单套订阅覆盖多端设备。
- **分流防偷跑配置**：[Windows 客户端分流规则自定义与国内直连优化](/categories/windows/windows-sub-rule-group-routing/)。
- **大屏影音配置**：[电视盒子与智能投影 Android TV 专用安装教程](/categories/android/android-tv-box-clash-installation/)。
- **全站测速排行榜**：[2026 最新好用机场测速排行榜与横向参数对照表](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "hong-kong-japan-low-latency-nodes.md": """## 🔗 低延迟与外服对战进阶索引

为了在亚太网络环境中获取极致的端到端低延迟并杜绝游戏联机丢包，推荐延伸阅读：
- **物理光纤专线**：[2026高品质IEPL物理专线机场推荐](/categories/airport-reviews/iepl-专线-airport-selection/)，晚高峰零丢包与低抖动。
- **经典轻量协议**：[Shadowsocks老牌极简协议机场推荐](/categories/airport-reviews/ss-shadowsocks-stable-airport.md -> /categories/airport-reviews/ss-shadowsocks-stable-airport/)，极低系统开销。
- **超时快速排查**：[节点全部显示超时（Timeout）自救指南](/categories/faq/airport-node-timeout-troubleshooting/)。
- **虚拟网卡游戏代理**：[Clash Verge Rev TUN 模式全局网络接管教程](/categories/windows/clash-verge-rev-tun-mode-setup/)。
- **核心机场总榜**：[2026 最新优质机场推荐测速总榜](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "iepl-专线-airport-selection.md": """## 🔗 跨境物理专线与企业级网络索引

针对晚高峰网络拥堵与对网络可用率有苛刻要求的专业用户，推荐延伸参考以下高规格方案：
- **低延迟亚太直连**：[香港日本低延迟直连节点机场推荐](/categories/airport-reviews/hong-kong-japan-low-latency-nodes/)，外服电竞联机首选。
- **高伪装抗封锁**：[Trojan深度伪装协议机场推荐](/categories/airport-reviews/trojan-protocol-stable-nodes/)，标准 HTTPS 443 伪装防御。
- **DNS防泄漏排查**：[客户端 TUN 模式防 DNS 泄漏实战指南](/categories/faq/client-tun-mode-dns-leak-prevention/)。
- **全平台客户端配置**：[Windows Clash Verge Rev 保姆级配置教程](/categories/windows/clash-verge-rev-windows-tutorial/) 与 [Mac Mihomo Party 完整指南](/categories/mac/mihomo-party-mac-complete-guide/)。
- **综合总榜参考**：[2026 最新好用机场测速排行榜单](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "monthly-pay-cheap-airport.md": """## 🔗 平价轻量与灵活周期选购索引

为了在控制试错成本的同时享受高可用网络加速，建议继续参考以下平价测评：
- **单位流量横向对比**：[十元内高性价比平价机场横向测速对比](/categories/airport-reviews/value-cheap-airport-comparison/)，深入解析流量成本。
- **不限时按量灾备**：[2026备用应急机场精选](/categories/airport-reviews/backup-emergency-cheap-airport/)，冷备节点双订阅容灾。
- **新手首购防坑**：[新手小白买梯子防坑五大铁律](/categories/airport-reviews/novice-airport-buying-guide/)，识破倍率陷阱。
- **跑路征兆识别**：[机场跑路征兆识别与资金避险自救策略](/categories/faq/airport-running-away-defense-strategy/)。
- **核心测速排行榜**：[2026 最新好用机场推荐测速总榜](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "multi-device-family-office-airport.md": """## 🔗 多端协同与全屋网络索引

面向多设备同时并发与跨平台协同加速需求，推荐参考以下全场景部署攻略：
- **大流量大吞吐**：[TB级大带宽大流量机场推荐](/categories/airport-reviews/high-bandwidth-large-traffic-airport/)，杜绝多端争抢带宽。
- **外贸商务出海**：[跨国远程办公与外贸独立站专线梯子推荐](/categories/airport-reviews/cross-border-remote-work-airport/)，固定商业 IP 协同。
- **家庭大屏影音**：[电视盒子与智能投影 Android TV 专用安装教程](/categories/android/android-tv-box-clash-installation/)。
- **手机保活配置**：[iPhone 后台频繁掉线排查与省电优化](/categories/ios/ios-battery-saving-background-keepalive/)。
- **全网综合榜单**：[2026 最新好用机场测速排行榜与参数表](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "novice-airport-buying-guide.md": """## 🔗 新手入门与全平台避坑实操索引

初涉科学上网领域，除了掌握选购常识外，建议延伸学习各平台主流客户端极速配置技巧：
- **平价月付试错**：[2026按月付费便宜机场精选](/categories/airport-reviews/monthly-pay-cheap-airport/)，随用随续杜绝年付被坑。
- **桌面入门教程**：[Windows Clash Verge Rev 保姆级配置教程](/categories/windows/clash-verge-rev-windows-tutorial/) 与 [Mac 配置指南](/categories/mac/clash-verge-rev-mac-setup/)。
- **移动入门教程**：[iOS Shadowrocket 小火箭配置保姆级教程](/categories/ios/shadowrocket-us-account-download-config/) 与 [安卓 Clash Meta 入门](/categories/android/clash-meta-for-android-tutorial/)。
- **订阅报错排查**：[机场订阅链接无法更新与 Network Error 深度修复](/categories/faq/subscription-link-update-failed-solution/)。
- **年度权威总榜**：[2026 最新好用机场测速排行榜与参数表](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "ss-shadowsocks-stable-airport.md": """## 🔗 经典轻量协议与固件生态索引

针对追求极简低开销、路由器固件翻墙与老旧设备平稳运行的用户，推荐延伸参考：
- **现代伪装协议**：[Trojan深度伪装协议机场推荐](/categories/airport-reviews/trojan-protocol-stable-nodes/)，对比标准 HTTPS 伪装性能。
- **亚太低延迟节点**：[香港日本低延迟直连节点机场推荐](/categories/airport-reviews/hong-kong-japan-low-latency-nodes/)，体验极速交互。
- **极简原生客户端**：[Sing-box Windows 客户端配置规则解析](/categories/windows/sing-box-windows-client-guide/) 与 [Mac Sing-box 教程](/categories/mac/sing-box-mac-tutorial/)。
- **连接超时排查**：[节点全部显示超时（Timeout）自救指南](/categories/faq/airport-node-timeout-troubleshooting/)。
- **核心机场总榜**：[2026 最新优质机场推荐测速总榜](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "trojan-protocol-stable-nodes.md": """## 🔗 高伪装传输与抗审查体系索引

针对敏感时期网络封锁与深层流量审查环境，推荐继续查阅以下高抗封锁技术方案：
- **经典轻量对比**：[Shadowsocks老牌极简协议机场推荐](/categories/airport-reviews/ss-shadowsocks-stable-airport/)，分析不同加密算法优劣。
- **物理光纤专线**：[2026高品质IEPL物理专线机场推荐](/categories/airport-reviews/iepl-专线-airport-selection/)，内网直连彻底绕过审查。
- **虚拟网卡防漏**：[客户端 TUN 模式防 DNS 泄漏实战指南](/categories/faq/client-tun-mode-dns-leak-prevention/)。
- **客户端原生适配**：[Sing-box iOS 客户端配置教程](/categories/ios/sing-box-ios-configuration/) 与 [Android Sing-box 入门](/categories/android/sing-box-android-novice-guide/)。
- **全网综合排行**：[2026 最新稳定好用翻墙梯子排行榜](/categories/airport-reviews/2026-airport-recommendation-rankings/)。""",

    "value-cheap-airport-comparison.md": """## 🔗 平价预算与单位流量测速索引

为了在有限的预算内榨干每一分性价比并杜绝套路虚标，建议延伸阅读以下专业对比：
- **按月付费无套路**：[2026按月付费便宜机场精选](/categories/airport-reviews/monthly-pay-cheap-airport/)，灵活续费试错成本低。
- **容灾应急方案**：[2026备用应急机场精选](/categories/airport-reviews/backup-emergency-cheap-airport/)，不限时按量小包备用。
- **新手避坑常识**：[新手小白买梯子防坑五大铁律](/categories/airport-reviews/novice-airport-buying-guide/)，识别黑心倍率套路。
- **资金避险技巧**：[机场跑路征兆识别与资金避险自救策略](/categories/faq/airport-running-away-defense-strategy/)。
- **全景测速榜单**：[2026 最新好用机场测速排行榜与参数表](/categories/airport-reviews/2026-airport-recommendation-rankings/)。"""
}

# ==============================================================================
# 2. Unique Top 4 Recommendation Lead-in Paragraph for Airport Reviews
# ==============================================================================
AIRPORT_TOP4_LEADINS = {
    "4k-streaming-netflix-airport.md": "针对 4K/8K 超高清流媒体播放对突发大带宽、原生家庭住宅 IP 落地与非自制剧全解锁的严苛指标，实测以下四家跨境专线表现最为稳健：",
    "ai-tools-chatgpt-claude-airport.md": "针对调用 Claude 3.5 Sonnet、ChatGPT Plus、Cursor 等海外 AI 大模型对 API 稳定长连接与独立纯净出口的严苛风控要求，精选以下四家高信誉专线服务商：",
    "backup-emergency-cheap-airport.md": "在主力线路遭遇突发故障或敏感期网络波动时，构建双客户端灾备冗余尤为关键，以下精选四家支持灵活周期且长期高可用的备选服务商：",
    "chatgpt-native-ip-airport.md": "为了彻底解决 OpenAI 登录时的 Access Denied 1020 报错与防范账号关联风控，经过 IP 纯净度与欺诈值严格审计，推荐以下四家提供真实住宅 ISP 出口的服务商：",
    "cross-border-remote-work-airport.md": "针对外贸独立站运营、亚马逊店铺管理及 PayPal/Stripe 跨境结算对固定纯净商业出口防关联的刚性要求，推荐以下四家企业级高可用专线服务商：",
    "high-bandwidth-large-traffic-airport.md": "面对 TB 级大文件高速传输、PT 下载以及全天候超高清追剧等高吞吐量需求，实测以下四家具备千兆突发带宽与充沛冗余冗余的服务商表现优异：",
    "hong-kong-japan-low-latency-nodes.md": "针对亚太外服游戏联机对战、跨国网页秒开交互对物理端到端延迟（RTT）与极低抖动的极致追求，实测以下四家专线骨干表现最为出色：",
    "iepl-专线-airport-selection.md": "基于内网端到端物理光纤直连技术，彻底规避公网 GFW 审查与晚高峰国际拥堵，为您精选以下四家部署纯正 IEPL 跨境专线的标杆服务商：",
    "monthly-pay-cheap-airport.md": "打破一次性年付的高资金占用与跑路风险，坚持低试错成本与随用随续，为您推荐以下支持灵活月付周期、高性价比的平价优质服务商：",
    "multi-device-family-office-airport.md": "面向全家多端共享、小微工作室多人协同以及软路由全屋代理等并发场景，精选以下不限在线设备数、带宽充沛的高承载专线服务商：",
    "novice-airport-buying-guide.md": "新手初次涉足科学上网，首要任务是避开虚标带宽与高倍率吸费陷阱，结合新手友好度与一键配置体验，优先推荐以下四家老牌高口碑服务商：",
    "ss-shadowsocks-stable-airport.md": "凭借经典 AEAD 算法极低的 CPU 占用与卓越的嵌入式设备兼容性，结合专线网络底层加持，推荐以下四家长期稳定支持 Shadowsocks 协议的服务商：",
    "trojan-protocol-stable-nodes.md": "通过标准 HTTPS 端口伪装与 TLS 1.3 现代加密技术，实现对深度流量检测（DPI）的高维隐匿，推荐以下四家深度部署 Trojan 伪装架构的高抗封锁服务商：",
    "value-cheap-airport-comparison.md": "以单位流量真实成本、百兆带宽跑满率与晚高峰连接可用性为核心评估维度，为您横向实测评选出以下四家兼具平价与稳定品质的高性价比服务商："
}

# ==============================================================================
# 3. Unique Section 3 Hot Search Lead-in Sentence for Airport Reviews
# ==============================================================================
AIRPORT_SECTION3_LEADINS = {
    "4k-streaming-netflix-airport.md": "在挑选流媒体追剧专线与配置各大电视盒子客户端时，主流用户高频检索的意图分布如下：",
    "ai-tools-chatgpt-claude-airport.md": "从事海外大模型开发、API 流式调用及内容创作时，行业用户核心关注的高频搜索热词包括：",
    "backup-emergency-cheap-airport.md": "构建双订阅应急容灾网络与寻找高性价比平价备用节点时，用户最为关切的搜索方向涵盖：",
    "chatgpt-native-ip-airport.md": "排查 OpenAI 网页端风控、解除 1020 报错及采购家庭住宅 IP 节点时，核心检索词如下：",
    "cross-border-remote-work-airport.md": "跨国出海企业、亚马逊跨境电商运营与远程办公技术栈中，高频高点击的搜索词包括：",
    "high-bandwidth-large-traffic-airport.md": "选购 TB 级大流量大带宽专线及下载重度用户日常检索的高点击率核心词涵盖：",
    "hong-kong-japan-low-latency-nodes.md": "追求极致亚太低延迟、外服联机秒级响应与交互提速的用户，重点检索的高频词包括：",
    "iepl-专线-airport-selection.md": "甄别真实物理专线、规避虚假内网套路与保障晚高峰零丢包时，高频关注的核心词如下：",
    "monthly-pay-cheap-airport.md": "拒绝年付捆绑、寻找十余元平价月付与随用随走翻墙梯子时，用户最集中的搜索词涵盖：",
    "multi-device-family-office-airport.md": "配置家庭软路由全屋翻墙、工作室多端并发与不限设备数方案时，主流高点击热词包括：",
    "novice-airport-buying-guide.md": "新手小白第一次接触翻墙梯子、识破倍率套路与自查防跑路时，高频检索的指南关键词包括：",
    "ss-shadowsocks-stable-airport.md": "部署极简低能耗 Shadowsocks 节点、适配老旧终端与嵌入式路由器时，用户高频搜索词如下：",
    "trojan-protocol-stable-nodes.md": "部署高隐匿 Trojan 伪装流量、对抗深度包检测（DPI）与敏感期防断连时，高频搜索词包括：",
    "value-cheap-airport-comparison.md": "对比平价机场单位流量性价比、小年付套餐真实跑满率时，用户重点关注的搜索意图涵盖："
}

print("Loaded all differentiation dictionaries successfully.")
