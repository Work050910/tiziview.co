# -*- coding: utf-8 -*-
import re

def count_chinese_chars(text):
    clean_text = re.sub(r'<[^>]+>', '', text)
    clean_text = re.sub(r'---.*?---', '', clean_text, flags=re.S)
    clean_text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', clean_text)
    clean_text = re.sub(r'http[s]?://\S+', '', clean_text)
    zh_chars = re.findall(r'[\u4e00-\u9fa5]', clean_text)
    return len(zh_chars)

f_rankings = "content/categories/airport-reviews/2026-airport-recommendation-rankings.md"
with open(f_rankings, "r", encoding="utf-8") as f:
    c = f.read()

# Let's shorten repetitive phrases in cards
replacements = [
    ("稳定机场推荐·", "优质梯子·"),
    ("好用翻墙梯子·", "好用梯子·"),
    ("便宜机场推荐·", "平价梯子·"),
    ("稳定梯子推荐·", "稳定梯子·"),
    ("IEPL专线稳定推荐·", "专线稳定·"),
    ("原生纯净IP·", "原生IP·"),
    ("原生住宅IP·", "原生IP·"),
    ("秒解ChatGPT·", "解ChatGPT·"),
    ("秒解Netflix·", "解奈飞·"),
    ("支持主流流媒体", "支持流媒体"),
    ("海外流媒体超清", "海外流媒体"),
    ("4K视频秒开·", "4K秒开·"),
    ("大流量大带宽", "大流量带宽"),
    ("三网智能容灾调度", "三网容灾调度"),
    ("全网调度稳定好用梯子", "全网调度稳定梯子")
]

for old, new in replacements:
    c = c.replace(old, new)

# Shorten FAQ slightly
c = c.replace("新手选购机场切忌盲目跟风购买长期套餐。首先明确核心场景（网页浏览、4K超清影音、海外大模型AI或跨境办公）；其次重点关注骨干线路，优先选用搭载真实IEPL/IPLC专线的服务商；最后坚持“先月付实测，满意再升级季付”的避坑铁律。",
              "新手选购切忌盲目年付。首先明确使用场景（网页、4K影音、AI大模型或跨境办公）；其次关注线路，优先选用IEPL/IPLC专线；最后坚持“先月付实测，满意再升级季付”原则。")

c = c.replace("普通公网中转在敏感时期极易遭遇骨干网拥堵、丢包和QoS限速，导致频繁掉线。而IEPL专线具备物理点对点光纤直连，数据不过公网审查网关，晚高峰全天候零丢包、低抖动，能够实现秒开4K和稳定不卡顿。",
              "普通公网中转在敏感期易受拥堵和QoS限速导致掉线。而IEPL专线端到端物理直连，不过公网审查网关，晚高峰全天零丢包、低抖动，能稳定秒开4K。")

c = c.replace("防跑路核心是规避“超低价永久套餐”和“买三年送两年”的高危营销盘；优先选择运营两至三年以上的老牌服务商；充值时尽量选用微信或支付宝快捷通道，遇到突发断联首先检查本地客户端时间同步与订阅更新。",
              "防跑路核心是规避“超低价永久套餐”和“买三年送两年”套路盘；优选运营两年以上老牌服务商，尽量选用快捷支付通道，断联先自查时间同步与订阅更新。")

cnt = count_chinese_chars(c)
print(f"Rankings count after replacements: {cnt} zh chars (Target: 800 - 2500)")

with open(f_rankings, "w", encoding="utf-8") as f:
    f.write(c)
