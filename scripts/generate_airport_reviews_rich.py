# -*- coding: utf-8 -*-
import os
import re
import json

def count_chinese_chars(text):
    clean_text = re.sub(r'<[^>]+>', '', text)
    clean_text = re.sub(r'---.*?---', '', clean_text, flags=re.S)
    clean_text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', clean_text)
    clean_text = re.sub(r'http[s]?://\S+', '', clean_text)
    zh_chars = re.findall(r'[\u4e00-\u9fa5]', clean_text)
    return len(zh_chars)

with open("scripts/enrich_articles_and_faqs.py", "r", encoding="utf-8") as f:
    helper_code = f.read()

# Load top4_cards_html and links_block from helper
top4_cards_html = helper_code.split('top4_cards_html = """')[1].split('"""')[0].strip()
links_block = helper_code.split('links_block = """')[1].split('"""')[0].strip()

# Rich data for 14 articles
articles_rich_data = {
    "4k-streaming-netflix-airport.md": {
        "title": "4K流媒体解锁机场推荐：2026稳定观看Netflix与Disney+超清视频的高速梯子",
        "description": "追剧不卡顿！2026优质4K流媒体解锁机场推荐，深度实测Netflix非自制剧、Disney+、HBO Max与YouTube 4K秒开的高性价比翻墙梯子。",
        "h2": "追剧发烧友专属：2026 4K/8K流媒体解锁高速机场推荐",
        "sec1_title": "### 一、 4K/8K 流媒体对节点带宽与 IP 纯净度的硬性指标",
        "sec1_text": """在日常科学上网中，观看 Netflix、Disney+、YouTube 4K 以及 HBO Max 等海外高清流媒体，对代理节点有着极为苛刻的双重考验。首先是**持续稳定的物理下行带宽**。普通的网页浏览或文字通讯仅需数十 KB 吞吐，而播放码率高达 25Mbps 至 50Mbps 的 4K HDR、杜比视界高规格影片，要求节点在晚高峰网络拥堵期也能拥有充沛的带宽冗余，绝不能出现阶段性跳水限速。

其次是**流媒体原生 IP 的纯净度画像**。Netflix 等跨国流媒体巨头部署了极为先进的机房代理 IP 识别算法。如果服务商使用的是廉价广播 IP 或被上万人共用的机房数据中心 IP，平台会立刻判定该请求来源于代理软件，从而限制用户只能观看其自制剧，甚至直接弹出“检测到代理工具”的阻断报错。

因此，真正优质的流媒体专线机场不仅在骨干网上搭载物理 IEPL 内网专线以确保晚高峰 0% 丢包率，更在香港、日本、新加坡及美西核心落地机房配置了正规 ISP 住宅家宽 IP 或自建动态 DNS 解锁中继，实现点击视频瞬间 4K 秒开、全程拖动进度条零缓冲转圈。""",
        "sec2_title": "### 二、 客户端流媒体智能分流与防风控配置技巧",
        "sec2_text": """为了在多设备上获得极致的追剧体验，建议用户在客户端中科学配置流媒体专用分流规则，而不是盲目开启容易导致全局减速的全局模式：

1. **精准分流规则集配置**：在 Clash Verge Rev、Mihomo Party 或小火箭中，启用专门的 `Media / Streaming` 策略组。将 Netflix、Disney+ 等特定域名规则精准绑定到带有“原生解锁”或“Streaming”标识的专属节点，确保只有流媒体流量走高品质解锁通道。
2. **防范本地 DNS 污染与泄漏**：部分用户即使节点支持解锁，仍会遭遇锁区报错，其根本原因往往是本地运营商 DNS 发生了泄漏。务必在客户端内开启 TUN 虚拟网卡模式，并配置防污染的海外安全 DoH/DoT 加密解析（如 Cloudflare `1.1.1.1` 或 Google `8.8.8.8`）。
3. **节点定期测速与健康检查**：在策略组中开启自动健康检查（URL-Test），每隔 10-15 分钟自动探测一次流媒体节点的真实握手时延，自动剔除偶发性波动的备选节点。""",
        "sec3_core": ["4K流媒体解锁机场推荐", "Netflix超清不卡梯子", "2026Disney+翻墙节点"],
        "sec3_long": ["YouTube4K秒开机场购买", "稳定解锁奈飞非自制剧梯子", "流媒体原生住宅IP专线"],
        "sec3_trans": ["小火箭看奈飞节点一键导入", "杜比视界零缓冲翻墙工具", "晚高峰追剧不掉线梯子"],
        "faqs": [
            ("观看 Netflix 或 Disney+ 4K 视频时提示“检测到代理工具”被拦截该怎么解决？",
             "流媒体平台拦截主要是因为出口 IP 被标记为数据中心机房 IP。解决办法是选用配备原生住宅 IP 或支持流媒体 DNS 智能解锁的节点；同时在客户端（如 Clash Verge 或小火箭）中启用专用的流媒体分流规则，确保流媒体流量精准走解锁通道。"),
            ("观看海外流媒体 4K 甚至 8K 蓝光影视，对机场单节点测速带宽的最低门槛是多少？",
             "流畅播放 Netflix 4K（高规格 HDR/杜比视界）需要稳定持续的下行带宽至少在 25-50Mbps 以上，且网络抖动必须小于 15ms。优质专线机场单节点通常具备百兆乃至千兆冗余带宽，能在晚高峰彻底杜绝缓冲转圈和画质骤降。")
        ]
    }
}

print("Rich generator template initialized.")
