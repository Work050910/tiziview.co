# -*- coding: utf-8 -*-
import os
import re

def count_chinese_chars(text):
    clean_text = re.sub(r'<[^>]+>', '', text)
    clean_text = re.sub(r'---.*?---', '', clean_text, flags=re.S)
    clean_text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', clean_text)
    clean_text = re.sub(r'http[s]?://\S+', '', clean_text)
    zh_chars = re.findall(r'[\u4e00-\u9fa5]', clean_text)
    return len(zh_chars)

# 1. Fine-tune 2026-airport-recommendation-rankings.md to be under 2500
f_rankings = "content/categories/airport-reviews/2026-airport-recommendation-rankings.md"
with open(f_rankings, "r", encoding="utf-8") as f:
    rc = f.read()

# Trim slightly from each card
card_compact = [
    ("· 晚高峰抗封锁", "· 晚高峰稳定"),
    ("· 跨境出海与翻墙梯子", "· 跨境办公翻墙梯子"),
    ("· 原生纯净IP · 4K秒开 · 秒解ChatGPT", "· 原生纯净IP · 秒解ChatGPT"),
    ("· 便宜机场推荐 · 学生党平价翻墙梯子", "· 便宜好用学生党翻墙梯子"),
    ("· 原生IP支持4K视频秒开 · 解锁AI", "· 原生IP解锁4K视频与AI"),
    ("· 好用翻墙梯子 · 8K流媒体大流量冲浪", "· 好用梯子大流量冲浪"),
    ("· 原生纯净IP · 秒解Netflix · 支持AI", "· 原生IP解锁Netflix与AI"),
    ("· 稳定梯子推荐 · 轻度年付科学上网", "· 稳定梯子轻度年付"),
    ("· 稳定解锁ChatGPT与主流流媒体", "· 解锁ChatGPT与流媒体"),
    ("· 高性价比稳定梯子 · 多地区快速切换", "· 高性价比稳定梯子"),
    ("· 节点专线优化 · 三网均衡极速秒开", "· 专线优化三网均衡"),
    ("· 节点网络极速优化 · 大带宽突发秒开", "· 专线优化大带宽秒开"),
    ("· 优质中转高速网络 · 大带宽极速冲浪", "· 高速网络大带宽冲浪"),
    ("· 优质专线全面升级 · 超大流量极速下载", "· 专线升级大流量下载"),
    ("· 专线网络全面覆盖 · 全球多地区节点", "· 专线覆盖全球节点"),
    ("· 全专线架构升级 · 三网智能容灾调度", "· 专线三网智能调度"),
    ("· 外贸出海专用 · 全网调度稳定好用梯子", "· 外贸出海稳定好用梯子"),
    ("· 原生IP支持ChatGPT与海外流媒体超清", "· 原生IP解锁流媒体与AI")
]

for old, new in card_compact:
    rc = rc.replace(old, new)

# Also tighten intro
rc = rc.replace("本榜单由编辑团队历时数月，对国内电信、联通、移动三大运营商进行晚高峰千兆测速压测，全方位采集了 27 家主流机场的起步价格、线路架构、专属优惠码、AI 与流媒体解锁能力，为您提供客观透明的一站式选购参考。",
                "编辑团队对国内三大运营商晚高峰进行实测，采集27家主流机场的起步价格、线路架构、优惠码与AI流媒体解锁能力，提供客观选购参考。")

cnt = count_chinese_chars(rc)
print(f"Rankings after fine-tune: {cnt} zh chars (Target: 800 - 2500)")
with open(f_rankings, "w", encoding="utf-8") as f:
    f.write(rc)

# 2. Fine-tune android-tv-box-clash-installation.md
f_tv = "content/categories/android/android-tv-box-clash-installation.md"
with open(f_tv, "r", encoding="utf-8") as f:
    tc = f.read()

# Replace redundant phrasing
tc = tc.replace("对于广大家庭中拥有小米电视、索尼电视、外贸 Android TV 盒子（如外贸机顶盒、Google Chromecast、Nvidia Shield TV）的用户而言，直接在电视大屏幕上畅享 YouTube 4K 超清画质、Netflix 原生杜比片库以及 Disney+ 动画，是提升家庭娱乐生活品质的最强生产力。",
                "对于在智能电视或电视盒子上畅享 YouTube 4K、Netflix 与 Disney+ 的用户，大屏娱乐需要流畅稳定的代理工具支持。")
cnt = count_chinese_chars(tc)
print(f"TV Box after fine-tune: {cnt} zh chars (Target: 800 - 1350)")
with open(f_tv, "w", encoding="utf-8") as f:
    f.write(tc)

# 3. Fine-tune airport-running-away-defense-strategy.md
f_run = "content/categories/faq/airport-running-away-defense-strategy.md"
with open(f_run, "r", encoding="utf-8") as f:
    runc = f.read()

runc = runc.replace("只要你在科学上网圈子里待过一年以上，你就一定会见证过大大小小的“服务商失联跑路惨剧”：昨天还在高调做活动打广告的某家知名大机场，今天突然官网打不开、节点全飘红超时、官方社群直接全员禁言，随后技术管理团队退群失联，留下成千上万刚刚缴了几年年费的用户在维权群里欲哭无泪。",
                    "在科学上网圈子里，服务商失联跑路屡见不鲜：前一天还在打折宣传，隔天官网关闭、节点全红超时、官方群禁言失联，给冲动购买长期套餐的用户造成直接财产损失。")
cnt = count_chinese_chars(runc)
print(f"Running away after fine-tune: {cnt} zh chars (Target: 800 - 1350)")
with open(f_run, "w", encoding="utf-8") as f:
    f.write(runc)

# 4. Check all 14 airport reviews to ensure each is <= 1350
airport_files = [
    "value-cheap-airport-comparison.md",
    "backup-emergency-cheap-airport.md",
    "cross-border-remote-work-airport.md",
    "monthly-pay-cheap-airport.md",
    "multi-device-family-office-airport.md",
    "novice-airport-buying-guide.md",
    "iepl-专线-airport-selection.md"
]

for af in airport_files:
    p = os.path.join("content/categories/airport-reviews", af)
    with open(p, "r", encoding="utf-8") as f:
        ac = f.read()
    cnt = count_chinese_chars(ac)
    if cnt > 1320:
        # shorten sec3 intro or a sentence
        ac = ac.replace("在选购与实际配置本类服务时，广大用户最关注的高频热搜意图包括：", "选购与配置此类服务时高频搜索热词：")
        ac = ac.replace("为方便您全设备无缝配置科学上网，推荐延伸阅读以下深度实操指南：", "推荐延伸阅读以下实操指南：")
        cnt = count_chinese_chars(ac)
        with open(p, "w", encoding="utf-8") as f:
            f.write(ac)
    print(f"{af} count: {cnt}")

print("Fine-tuning completed successfully!")
