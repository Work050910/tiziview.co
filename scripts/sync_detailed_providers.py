# -*- coding: utf-8 -*-
import json
import re
import os

# Comprehensive 27 providers data synchronized from user input
# Sanitized of any competitor blocklist words ("二毛博客", "机场宝", etc.)
# Top 4 fixed: 全球云 (1), 飞猫云 (2), 暮光加速 (3), 微风网络 (4)

raw_data = {
    "quanqiu-cloud": {
        "name": "全球云",
        "rank": 1,
        "inviteURL": "https://hueue09.gcvipaff.com/#/?code=z8U9aaa4",
        "coupon": "qq88",
        "couponNote": "享 8 折优惠，适用套餐以结算页为准",
        "priceFrom": "20 元/月",
        "trafficFrom": "120GB/月",
        "suitableFor": "多地区节点、跨境业务、短视频与多出口 IP 使用场景",
        "sellingPoints": "优势在多国家与地区原生 IP 节点、智能分流和较灵活的计费思路，内容场景可突出 TikTok、YouTube 与跨境业务所需的多出口 IP。适合经常切换区域、兼顾短视频和外贸工作的用户。",
        "packages": [
            {"name": "轻量版", "price": "20 元/月", "traffic": "120GB/月"},
            {"name": "进阶版", "price": "40 元/月", "traffic": "300GB/月"},
            {"name": "重度版", "price": "100 元/月", "traffic": "700GB/月"},
            {"name": "大户版", "price": "180 元/月", "traffic": "1500GB/月"},
            {"name": "轻量年付", "price": "99 元/年", "traffic": "59GB"},
            {"name": "一次性100G", "price": "100 元", "traffic": "100GB 不限时"},
            {"name": "一次性400G", "price": "360 元", "traffic": "400GB 不限时"},
            {"name": "一次性800G", "price": "700 元", "traffic": "800GB 不限时"},
            {"name": "私人专线", "price": "680 元/月", "traffic": "500GB/月 独享"}
        ],
        "verificationNote": "结算时输入 qq88 可享 8 折；适用套餐、有效期及能否与活动价叠加以结算页为准。"
    },
    "flycat-cloud": {
        "name": "飞猫云",
        "rank": 2,
        "inviteURL": "https://quanqiu.flycatvipaff.cc/#/?code=7ZOeVmNS",
        "coupon": "flycat888",
        "couponNote": "新用户购买季付及以上 8 折",
        "priceFrom": "84 元/年 (折合 7元/月)",
        "trafficFrom": "50GB/月",
        "suitableFor": "轻量备用、香港线路需求、多设备家庭和新手客户端",
        "sellingPoints": "低价小流量配 IEPL 专线是最醒目的组合。晚高峰实测显示香港节点表现较稳，同时提供自研极简客户端并支持主流流媒体与 AI 解锁；适合轻量备用、主用香港或多设备家庭。",
        "packages": [
            {"name": "学生版年付", "price": "84 元/年 (折合 7元/月)", "traffic": "50GB/月"},
            {"name": "星耀版月付", "price": "25 元/月", "traffic": "150GB/月"}
        ],
        "verificationNote": "新用户购买季付及以上套餐时输入 flycat888 可享 8 折，适用范围以结算页为准。"
    },
    "twilight": {
        "name": "暮光加速",
        "rank": 3,
        "inviteURL": "https://quanqi12.twilightaff.com/#/?code=beAVqNPf",
        "coupon": "mm88",
        "couponNote": "享 8 折优惠，适用套餐以结算页为准",
        "priceFrom": "20 元/月",
        "trafficFrom": "120GB/月",
        "suitableFor": "晚高峰影音、较大流量和多媒体使用场景",
        "sellingPoints": "晚高峰观看 YouTube 4K 视频依然流畅，下载视频可跑满带宽；同时突出多媒体全面解锁，以及 ChatGPT 等 AI 工具的可用性，适合重视高峰期影音体验的用户。",
        "packages": [
            {"name": "基础版", "price": "20 元/月 (57元/季)", "traffic": "120GB/月"},
            {"name": "标准版", "price": "40 元/月 (114元/季)", "traffic": "300GB/月"},
            {"name": "旗舰版", "price": "100 元/月 (285元/季)", "traffic": "700GB/月"},
            {"name": "至尊版", "price": "180 元/月 (513元/季)", "traffic": "1.5TB/月"},
            {"name": "年付轻量版", "price": "109 元/年", "traffic": "70GB/年"},
            {"name": "一次性150G", "price": "219 元", "traffic": "150GB 不限时"},
            {"name": "一次性400G", "price": "529 元", "traffic": "400GB 不限时"},
            {"name": "一次性800G", "price": "959 元", "traffic": "800GB 不限时"}
        ],
        "verificationNote": "结算时输入 mm88 可享 8 折；适用套餐与有效期以结算页为准。"
    },
    "breezenet": {
        "name": "微风网络",
        "rank": 4,
        "inviteURL": "https://edp01.breezenetaff.com/#/?code=vxDUI8kY",
        "coupon": "",
        "couponNote": "以结算页为准",
        "priceFrom": "以结算页为准",
        "trafficFrom": "100GB/月 (可见记录 137元/年)",
        "suitableFor": "轻度使用、低流量年付、自研客户端和第三方订阅导入",
        "sellingPoints": "定位为轻量 IEPL 专线方案，重点是低流量年付、自研客户端与第三方订阅导入。适合将它视为轻度使用候选，并先在结算页确认实际流量与付款周期。",
        "packages": [
            {"name": "轻量年付", "price": "137 元/年 (以结算页为准)", "traffic": "100GB/月"},
            {"name": "常规阶梯", "price": "以结算页为准", "traffic": "根据所选套餐动态配置"}
        ],
        "verificationNote": "发布前在邀请页确认当前最低档、流量重置方式、季付及以上优惠、设备数与客户端支持。"
    },
    "u1s1": {
        "name": "U1S1",
        "rank": 5,
        "inviteURL": "https://quanqiu.v2yunvipaff.com/#/?code=YCf9VJsS",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "20 元/月",
        "trafficFrom": "120GB/月",
        "suitableFor": "稳定标注清楚、中转优化、原生 IP 解锁与长期自用场景",
        "sellingPoints": "定位偏向“稳定、标注清楚”的长期自用方案。强调中转优化、原生 IP 解锁与明确的流量档位，更适合在意实际可用性、又不想研究复杂配置的用户。",
        "packages": [
            {"name": "基础体验版", "price": "20 元/月", "traffic": "120GB/月"},
            {"name": "日常影音版", "price": "40 元/月", "traffic": "300GB/月"},
            {"name": "重度冲浪版", "price": "100 元/月", "traffic": "700GB/月"},
            {"name": "尊享大户版", "price": "180 元/月", "traffic": "1500GB/月"},
            {"name": "一次性流量包", "price": "580 元", "traffic": "1000GB 不限时"}
        ],
        "verificationNote": "套餐名称与价格发布前需在结算页确认流量重置、设备数和库存。"
    },
    "jilian-cloud": {
        "name": "极连云",
        "rank": 6,
        "inviteURL": "https://quanqiu.jlyvipaff.com/#/?code=NplcUEEV",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "15.5 元/月",
        "trafficFrom": "100GB/月",
        "suitableFor": "IPLC 内网专线、抗封锁、防 QoS 及日韩低延迟场景",
        "sellingPoints": "主打 IPLC 内网专线的连通稳定性，重点突出抗封锁、防 QoS，以及香港、日本方向的低延迟体验；对敏感时期仍需保持连接、同时使用 AI 与流媒体的用户更有吸引力。",
        "packages": [
            {"name": "轻量体验年付", "price": "96 元/年 (折合 8元/月)", "traffic": "60GB/月"},
            {"name": "基础版月付", "price": "15.5 元/月", "traffic": "100GB/月"},
            {"name": "进阶版月付", "price": "30.5 元/月", "traffic": "200GB/月"},
            {"name": "旗舰版月付", "price": "65.5 元/月", "traffic": "500GB/月"},
            {"name": "尊享版月付", "price": "120.5 元/月", "traffic": "1000GB/月"},
            {"name": "一次性流量包", "price": "399 元", "traffic": "1000GB 不限时"}
        ],
        "verificationNote": "年付折算价不等于月付门槛；专线覆盖、流量倍率和长期套餐规则以结算页为准。"
    },
    "guangnian-ladder": {
        "name": "光年梯",
        "rank": 7,
        "inviteURL": "https://quanqiu.gntaff.com/#/?code=qUJeOegs",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "18 元/月",
        "trafficFrom": "110GB/月",
        "suitableFor": "新手一键导入、三网线路优化、ChatGPT 常用访问场景",
        "sellingPoints": "把易用性放在前面，强调客户端一键导入、三网线路优化和清晰的套餐档位。更适合作为新手第一次接触机场时的轻量选择，并兼顾 ChatGPT 等常用服务的访问需求。",
        "packages": [
            {"name": "入门版", "price": "18 元/月", "traffic": "110GB/月"},
            {"name": "晋级版", "price": "34 元/月", "traffic": "220GB/月"},
            {"name": "专业版", "price": "68 元/月", "traffic": "450GB/月"},
            {"name": "至尊版", "price": "130 元/月", "traffic": "900GB/月"},
            {"name": "私人专线独享", "price": "680 元/月", "traffic": "500GB/月"}
        ],
        "verificationNote": "结算时确认各周期折扣、订阅导入方式及独享节点交付标准。"
    },
    "guangsu-cloud": {
        "name": "光速云",
        "rank": 8,
        "inviteURL": "https://quanqiu.gsyaff.com/#/?code=AAkbe2W6",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "17 元/月",
        "trafficFrom": "110GB/月",
        "suitableFor": "BGP 入口低延迟中转、网页与即时通信轻度游戏日常场景",
        "sellingPoints": "核心叙事是 BGP 入口与低延迟中转，兼顾三网接入和客户端快速导入。相较单纯堆流量，更适合网页、即时通信及轻度游戏等对响应速度更敏感的日常场景。",
        "packages": [
            {"name": "轻量年付", "price": "99 元/年 (折合 8.25元/月)", "traffic": "59GB/月"},
            {"name": "极速版月付", "price": "17 元/月", "traffic": "110GB/月"},
            {"name": "流光版月付", "price": "34 元/月", "traffic": "220GB/月"},
            {"name": "量子版月付", "price": "68 元/月", "traffic": "450GB/月"},
            {"name": "无界版月付", "price": "130 元/月", "traffic": "900GB/月"},
            {"name": "一次性流量包", "price": "680 元", "traffic": "1000GB 不限时"}
        ],
        "verificationNote": "最低价格字段按常规月付口径；年付与不限时套餐的流量重置及有效期以结算页为准。"
    },
    "weitu-cloud": {
        "name": "唯兔云",
        "rank": 9,
        "inviteURL": "https://quanqiu.vipaff.cc/#/?code=c4sOJBXE",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "14.9 元/月",
        "trafficFrom": "100GB/月",
        "suitableFor": "VLESS 协议、60+ 节点多地区三网智能负载均衡进阶场景",
        "sellingPoints": "采用 VLESS 作为主要协议卖点，并强调 60+ 节点、三网优化与智能负载均衡。节点选择空间和自动调度能力是其差异点，适合希望减少手动换线频率的进阶用户。",
        "packages": [
            {"name": "入门年付", "price": "79.9 元/年 (折合 6.66元/月)", "traffic": "45GB/月"},
            {"name": "基础版", "price": "14.9 元/月 (142.9元/年)", "traffic": "100GB/月"},
            {"name": "进阶版", "price": "29.9 元/月 (286.9元/年)", "traffic": "200GB/月"},
            {"name": "高级版", "price": "59.9 元/月 (547.9元/年)", "traffic": "500GB/月"},
            {"name": "尊享版", "price": "119.9 元/月 (1150.9元/年)", "traffic": "1000GB/月"},
            {"name": "一次性流量包", "price": "340 元", "traffic": "500GB 不限时"}
        ],
        "verificationNote": "购买前核对有效期、节点负载调度策略与账户规则。"
    },
    "yuzhou-cloud": {
        "name": "宇宙云",
        "rank": 10,
        "inviteURL": "https://quanqiu.yuzoucloud.cc/#/?code=f3DHb9Gj",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "14.9 元/月",
        "trafficFrom": "100GB/月",
        "suitableFor": "多地区覆盖、大流量性价比、多国节点低成本切换场景",
        "sellingPoints": "走“多地区覆盖 + 大流量性价比”路线，提到三网接入优化和主流客户端订阅导入。适合经常切换不同国家或地区节点、又希望控制月度成本的用户。",
        "packages": [
            {"name": "公开入门档", "price": "14.9 元/月", "traffic": "100GB/月"},
            {"name": "专线大流量档", "price": "以结算页为准", "traffic": "覆盖70+节点阶梯梯度"}
        ],
        "verificationNote": "需在邀请页确认节点地区、流量倍率、设备数、续费和退款规则。"
    },
    "sujie": {
        "name": "速界",
        "rank": 11,
        "inviteURL": "https://quanqiu.speedworldaff.cc/#/?code=kY825Zat",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "25 元/月",
        "trafficFrom": "150GB/月",
        "suitableFor": "IPLC 专线晚高峰承载、低延迟与 4K/8K 流媒体高码率场景",
        "sellingPoints": "卖点集中在高带宽 IPLC 专线和晚高峰承载，宣传方向覆盖低延迟与 4K/8K 流媒体。更适合对高峰时段速度、高清播放和大流量传输要求较高的重度用户。",
        "packages": [
            {"name": "极速版", "price": "25 元/月 (255元/年)", "traffic": "150GB/月"},
            {"name": "超速版", "price": "50 元/月 (510元/年)", "traffic": "高阶流量档"},
            {"name": "光速版", "price": "100 元/月 (1020元/年)", "traffic": "超大流量档"},
            {"name": "跃迁版", "price": "200 元/月 (2040元/年)", "traffic": "旗舰流量档"},
            {"name": "年付体验包", "price": "88 元/年", "traffic": "轻量测试流量"}
        ],
        "verificationNote": "下单前确认当前优惠活动、各周期折扣及流量重置规则。"
    },
    "sogo-cloud": {
        "name": "SOGO 云",
        "rank": 12,
        "inviteURL": "https://afasfw.sogotztz2.sbs/#/?code=Mgoqf6KP",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "20 元/月",
        "trafficFrom": "120GB/月",
        "suitableFor": "全球节点、家庭或小团队多设备并发、4K 影音与 AI 协作",
        "sellingPoints": "突出全球节点、专线优化和多设备使用，套餐从较大的月流量起步。聚焦家庭或小团队的多端并发，以及 4K 流媒体和 AI 工具同时使用的便利性。",
        "packages": [
            {"name": "活动入门档", "price": "20 元/月 (常规25元)", "traffic": "120GB/月"},
            {"name": "优选版", "price": "50 元/月", "traffic": "250GB/月"},
            {"name": "强化版", "price": "100 元/月", "traffic": "500GB/月"},
            {"name": "顶配版", "price": "200 元/月", "traffic": "1000GB/月"},
            {"name": "一次性100G", "price": "100 元", "traffic": "100GB 不限时"},
            {"name": "一次性250G", "price": "200 元", "traffic": "250GB 不限时"},
            {"name": "一次性500G", "price": "400 元", "traffic": "500GB 不限时"},
            {"name": "一次性1000G", "price": "800 元", "traffic": "1000GB 不限时"}
        ],
        "verificationNote": "活动价可能随时调整，多设备和同时在线规则应在下单前确认。"
    },
    "kuaili": {
        "name": "快狸",
        "rank": 13,
        "inviteURL": "https://quanqiu.kuailicloud.cc/#/?code=vuYET5Qj",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "10 元/月",
        "trafficFrom": "30GB/月",
        "suitableFor": "中转优化、均衡三网接入、开箱即用日常主力订阅场景",
        "sellingPoints": "强调中转线路优化和简单配置，三网接入取向较均衡，月付即提供较大流量。适合不想折腾规则或客户端、只需要一套日常主力订阅的用户。",
        "packages": [
            {"name": "活动入门档", "price": "10 元/月", "traffic": "30GB/月"},
            {"name": "森狸年付小包", "price": "120 元/年", "traffic": "30GB/月"},
            {"name": "月猩月付小包", "price": "15 元/月", "traffic": "50GB/月"},
            {"name": "小狸基础", "price": "22 元/月", "traffic": "100GB/月"},
            {"name": "灵理标准", "price": "35 元/月", "traffic": "250GB/月"},
            {"name": "夜理强化", "price": "95 元/月", "traffic": "500GB/月"},
            {"name": "天狸顶配", "price": "180 元/月", "traffic": "1000GB/月"}
        ],
        "verificationNote": "客户端兼容性、退款条件和流量重置日均需在结算页确认。"
    },
    "ermao-cloud": {
        "name": "二猫云",
        "rank": 14,
        "inviteURL": "https://quanqiu.2maoyunaff.cc/#/?code=zy39Ip8E",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "20 元/月",
        "trafficFrom": "100GB/月",
        "suitableFor": "中转专线混合、原生 IP 流媒体解锁、追剧与常规海外服务",
        "sellingPoints": "以“中转 + 专线”的混合线路平衡成本和稳定性，并把原生 IP、流媒体解锁与较大月流量作为组合亮点。适合预算适中、主要需求是追剧和常规海外服务的用户。",
        "packages": [
            {"name": "白猫套餐", "price": "20 元/月", "traffic": "100GB/月"},
            {"name": "橘猫畅玩版", "price": "40 元/月", "traffic": "200GB/月"},
            {"name": "牛奶猫尊享版", "price": "80 元/月", "traffic": "400GB/月"},
            {"name": "黑猫无限版", "price": "160 元/月", "traffic": "800GB/月"}
        ],
        "verificationNote": "暂无一次性不限时订阅；线路构成和客户端限制以官方公告为准。"
    },
    "yifanyun": {
        "name": "一翻云",
        "rank": 15,
        "inviteURL": "https://quanqiu.1flyunaff.cc/#/?code=gJtw80i4",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "30 元/月",
        "trafficFrom": "150GB/月",
        "suitableFor": "高流量视频下载、VLESS Reality 协议、抗封锁与大带宽需求",
        "sellingPoints": "入门档就提供 150GB，定位明显偏向高流量用户；同时强调 VLESS / Reality 协议与三网优化。适合视频、下载等月度消耗较大，并在意新协议抗封锁能力的使用者。",
        "packages": [
            {"name": "VIP1", "price": "30 元/月 (306元/年)", "traffic": "150GB/月"},
            {"name": "VIP2", "price": "60 元/月 (612元/年)", "traffic": "300GB/月"},
            {"name": "VIP3", "price": "120 元/月 (1224元/年)", "traffic": "600GB/月"},
            {"name": "VIP4", "price": "240 元/月 (2448元/年)", "traffic": "1200GB/月"}
        ],
        "verificationNote": "长期套餐应确认流量是否按月重置、节点倍率和退款条款。"
    },
    "edgenova": {
        "name": "边缘节点（EdgeNova）",
        "rank": 16,
        "inviteURL": "https://quanqi.edgenovaaff.cc/#/?code=8BBARdHw",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "25 元/月",
        "trafficFrom": "120GB/月",
        "suitableFor": "海外团队运营、Reality 协议、外服游戏与 AI 原生落地场景",
        "sellingPoints": "海外团队运营和 Reality 协议是主要辨识度，配合原生 IP 节点，使用场景偏向外服与 AI 工具。对能接受较技术化配置、看重抗封锁与落地 IP 属性的用户更合适。",
        "packages": [
            {"name": "年付入门", "price": "108 元/年 (折合 9元/月)", "traffic": "45GB/月"},
            {"name": "标准版月付", "price": "25 元/月", "traffic": "120GB/月"},
            {"name": "进阶版月付", "price": "50 元/月", "traffic": "250GB/月"},
            {"name": "高级版月付", "price": "100 元/月", "traffic": "500GB/月"},
            {"name": "极限版月付", "price": "200 元/月", "traffic": "1000GB/月"}
        ],
        "verificationNote": "最低价格字段按常规月付口径；英文界面、协议兼容和原生 IP 地区应先行确认。"
    },
    "kosing-cloud": {
        "name": "可信云",
        "rank": 17,
        "inviteURL": "https://quanqiu.kosingaff.com/#/?code=NRG0tXKO",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "9 元/月",
        "trafficFrom": "45GB/月",
        "suitableFor": "长期稳定售后、IEPL 专线全平台支持与流媒体 AI 兼容",
        "sellingPoints": "品牌叙事聚焦长期稳定与售后服务，把 IEPL 专线、全平台支持及流媒体 / AI 兼容放在一起。适合愿意为服务响应和持续使用体验支付稍高月费的人。",
        "packages": [
            {"name": "轻量月付", "price": "9 元/月", "traffic": "45GB/月"},
            {"name": "基础版", "price": "25 元/月", "traffic": "150GB/月"},
            {"name": "标准版", "price": "50 元/月", "traffic": "300GB/月"},
            {"name": "专业版", "price": "100 元/月", "traffic": "600GB/月"},
            {"name": "旗舰版", "price": "200 元/月", "traffic": "1200GB/月"},
            {"name": "年付小包", "price": "96 元/年", "traffic": "60GB/年 (全年总量)"}
        ],
        "verificationNote": "售后时效、退款规则和专线覆盖仍以当前结算页条款为准。"
    },
    "langwang": {
        "name": "浪网（WaveNet）",
        "rank": 18,
        "inviteURL": "https://langwang.wavenetaff.com/#/?code=pYe3kzd4",
        "coupon": "lw88",
        "couponNote": "结算输入优惠码享专属折扣",
        "priceFrom": "25 元/月",
        "trafficFrom": "150GB/月",
        "suitableFor": "ChatGPT Claude AI 与开发工具、不限同时在线设备场景",
        "sellingPoints": "重点面向 ChatGPT、Claude 等 AI 应用和开发工具访问，同时采用高效 Shadowsocks 协议，并且不限制同时在线设备数量，更适合需要多端协作的用户。",
        "packages": [
            {"name": "入门版月付", "price": "25 元/月", "traffic": "150GB/月"},
            {"name": "常规月付30", "price": "30 元/月", "traffic": "150GB/月"},
            {"name": "常规月付70", "price": "70 元/月", "traffic": "400GB/月"},
            {"name": "常规月付120", "price": "120 元/月", "traffic": "800GB/月"},
            {"name": "常规月付200", "price": "200 元/月", "traffic": "2TB/月"},
            {"name": "年付方案", "price": "119 元/年", "traffic": "80GB/月"},
            {"name": "一次性180G", "price": "239 元", "traffic": "180GB 不限时"},
            {"name": "一次性450G", "price": "569 元", "traffic": "450GB 不限时"},
            {"name": "一次性900G", "price": "1099 元", "traffic": "900GB 不限时"}
        ],
        "verificationNote": "结算时输入 lw88；实际折扣、适用套餐与有效期以结算页为准。"
    },
    "ladder-cloud": {
        "name": "梯子云（LadderCloud）",
        "rank": 19,
        "inviteURL": "https://tiziyun3.ladderaff.com/#/?code=wI00rGj2",
        "coupon": "tiziyun",
        "couponNote": "享 8 折优惠，适用套餐以结算页为准",
        "priceFrom": "25 元/月",
        "trafficFrom": "125GB/月",
        "suitableFor": "IEPL 企业专线、晚高峰防拥堵、Netflix 与 AI 解锁兼顾小白进阶",
        "sellingPoints": "全线采用 IEPL 企业专线，侧重缓解晚高峰拥堵，并提供 ChatGPT、Netflix 解锁。既有自研小白客户端，也兼容主流开源订阅，兼顾新手易用性和进阶用户的客户端选择。",
        "packages": [
            {"name": "基础版", "price": "25 元/月 (255元/年)", "traffic": "125GB/月"},
            {"name": "进阶版", "price": "60 元/月 (612元/年)", "traffic": "350GB/月"},
            {"name": "高级版", "price": "110 元/月 (1122元/年)", "traffic": "750GB/月"},
            {"name": "顶配版", "price": "190 元/月 (1938元/年)", "traffic": "1.6TB/月"},
            {"name": "年付轻量版", "price": "89 元/年", "traffic": "60GB/年"},
            {"name": "一次性120G", "price": "169 元", "traffic": "120GB 不限时"},
            {"name": "一次性350G", "price": "449 元", "traffic": "350GB 不限时"},
            {"name": "一次性700G", "price": "849 元", "traffic": "700GB 不限时"}
        ],
        "verificationNote": "结算时输入 tiziyun 可享 8 折；适用套餐与有效期以结算页为准。"
    },
    "lingdong-cloud": {
        "name": "灵动云",
        "rank": 20,
        "inviteURL": "https://lingdongyun.lingdongaff.com/#/?code=ibHQOYGt",
        "coupon": "ld88",
        "couponNote": "结算输入优惠码享专属折扣",
        "priceFrom": "20 元/月",
        "trafficFrom": "100GB/月",
        "suitableFor": "新版 VLESS 协议、港台日新美常用节点覆盖与 4K 影音顺畅播放",
        "sellingPoints": "全线采用较新的 VLESS 协议，覆盖香港、台湾、日本、新加坡和美国等常用地区；晚高峰观看 YouTube 4K 视频依然顺畅，适合看重节点覆盖与影音体验的用户。",
        "packages": [
            {"name": "拂风版", "price": "20 元/月 (204元/年)", "traffic": "100GB/月"},
            {"name": "驭浪版", "price": "50 元/月 (510元/年)", "traffic": "300GB/月"},
            {"name": "破晓版", "price": "100 元/月 (1020元/年)", "traffic": "700GB/月"},
            {"name": "凌霄版", "price": "180 元/月 (1836元/年)", "traffic": "1.5TB/月"},
            {"name": "年付低频版", "price": "99 元/年", "traffic": "70GB/年"},
            {"name": "闲云一次性", "price": "199 元", "traffic": "150GB 不限时"},
            {"name": "惊云一次性", "price": "499 元", "traffic": "400GB 不限时"},
            {"name": "飞云一次性", "price": "899 元", "traffic": "800GB 不限时"}
        ],
        "verificationNote": "结算时输入 ld88；实际折扣、适用套餐与有效期以结算页为准。"
    },
    "yinxingren": {
        "name": "隐形人",
        "rank": 21,
        "inviteURL": "https://yinxingren1.invisibleaff.com/#/?code=ISH1y2IF",
        "coupon": "yxr888",
        "couponNote": "新户专享折扣",
        "priceFrom": "24 元/月",
        "trafficFrom": "144GB/月",
        "suitableFor": "新加坡团队运营、纯专线 VLESS 架构、8K 极速与灵活随用随续",
        "sellingPoints": "由新加坡团队打造，采用全线纯专线与 VLESS 协议；强调 8K 视频快速加载，以及 AI 和流媒体原生解锁。套餐可随用随续，适合关注专线质量与续费灵活性的用户。",
        "packages": [
            {"name": "白银纪元", "price": "24 元/月", "traffic": "144GB/月"},
            {"name": "黄金序列", "price": "48 元/月", "traffic": "360GB/月"},
            {"name": "铂金至臻", "price": "105 元/月", "traffic": "750GB/月"},
            {"name": "钻石穹顶", "price": "185 元/月", "traffic": "1600GB/月"},
            {"name": "星耀风暴年付", "price": "109 元/年", "traffic": "80GB/年"},
            {"name": "一次性160G", "price": "229 元", "traffic": "160GB 不限时"},
            {"name": "一次性420G", "price": "549 元", "traffic": "420GB 不限时"},
            {"name": "一次性1000G", "price": "1199 元", "traffic": "1000GB 不限时"}
        ],
        "verificationNote": "新用户结算时输入 yxr888；实际折扣、适用套餐与有效期以结算页为准。"
    },
    "flyv": {
        "name": "FlyV（飞V）",
        "rank": 22,
        "inviteURL": "https://feiv289.flyvaff.com/#/?code=qQCT0BeY",
        "coupon": "fly20",
        "couponNote": "结算输入享专属优惠",
        "priceFrom": "25 元/月",
        "trafficFrom": "150GB/月",
        "suitableFor": "全专线架构、全节点 1x 计费、不限速不限设备多端影音",
        "sellingPoints": "采用全线专线架构，所有节点按 1× 流量计费；支持 4K/8K 流媒体以及 ChatGPT 等 AI 工具，并强调不限速、不限制设备数量，适合多设备和高码率影音场景。",
        "packages": [
            {"name": "年付版", "price": "96 元/年 (折合 8元/月)", "traffic": "60GB/月"},
            {"name": "Lite 月付", "price": "25 元/月", "traffic": "150GB/月"},
            {"name": "Plus 月付", "price": "45 元/月", "traffic": "300GB/月"},
            {"name": "Blaze 月付", "price": "85 元/月", "traffic": "600GB/月"},
            {"name": "Nova 月付", "price": "150 元/月", "traffic": "1000GB/月"},
            {"name": "一次性流量包", "price": "100 元", "traffic": "100GB 不限时"}
        ],
        "verificationNote": "结算时输入 fly20；实际折扣、适用套餐与有效期以结算页为准。"
    },
    "worryfree": {
        "name": "无忧链接",
        "rank": 23,
        "inviteURL": "https://wep01.worryfreeaff.com/#/?code=fOCJz3E2",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "12.92 元/月",
        "trafficFrom": "100GB/月",
        "suitableFor": "通用订阅主流客户端全兼容、低频小包到 1TB 大容量弹性方案",
        "sellingPoints": "亮点在于通用订阅与主流客户端兼容，套餐从低频年付小包延伸到 1TB 月流量，并另有一次性流量包。支持流媒体和 AI 工具访问。",
        "packages": [
            {"name": "mini 链接", "price": "79 元/年", "traffic": "40GB/月"},
            {"name": "舒心链接", "price": "12.92 元/月 (123.76元/年)", "traffic": "100GB/月"},
            {"name": "省心链接", "price": "22.44 元/月 (214.88元/年)", "traffic": "200GB/月"},
            {"name": "随心链接", "price": "52.36 元/月 (502.52元/年)", "traffic": "500GB/月"},
            {"name": "忘忧链接", "price": "117 元/月 (1123元/年)", "traffic": "1TB/月"},
            {"name": "一次性流量包", "price": "16.15 元", "traffic": "100GB 不限时"}
        ],
        "verificationNote": "协议、节点和晚高峰表现仍以实时页面与本地测试为准。"
    },
    "civet": {
        "name": "灵猫网络（Civet）",
        "rank": 24,
        "inviteURL": "https://vip02.civetaff.com/#/?code=MLVZXxQj",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "85 元/年",
        "trafficFrom": "45GB (年付小包)",
        "suitableFor": "IPLC 专线、1倍流量不限设备与通用订阅阶梯",
        "sellingPoints": "主打 IPLC、1 倍流量、不限设备与通用订阅，覆盖从年付小包到月付 300GB 的阶梯。适合多设备轻量至中度使用的用户。",
        "packages": [
            {"name": "年付小包", "price": "85 元/年", "traffic": "45GB"},
            {"name": "Small 月付", "price": "25 元/月 (195元/年)", "traffic": "150GB/月"},
            {"name": "Big 月付", "price": "45 元/月 (295元/年)", "traffic": "300GB/月"},
            {"name": "Small 季付", "price": "65 元/季", "traffic": "150GB/季"},
            {"name": "Big 季付", "price": "125 元/季", "traffic": "300GB/季"}
        ],
        "verificationNote": "付款币种、订阅格式、流量重置、设备并发与退款规则须在结算页或客服处确认。"
    },
    "flashleap": {
        "name": "闪跃（FlashLeap）",
        "rank": 25,
        "inviteURL": "https://vip02.flashleapaff.com/#/?code=bsjhVp9y",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "96 元/年 (折合 8元/月)",
        "trafficFrom": "60GB/月",
        "suitableFor": "IPLC 专线 1倍率、低延迟、通用订阅与定制客户端",
        "sellingPoints": "公开资料将其描述为 IPLC 专线与 1 倍流量方案，兼顾低延迟、通用订阅和定制客户端。流媒体、原生 IP 与 AI 工具支持俱全，适合重视高峰表现但愿意先用月付验证的人。",
        "packages": [
            {"name": "闪跃年付版", "price": "96 元/年 (折合 8元/月)", "traffic": "60GB/月"},
            {"name": "闪动 Flicker", "price": "24 元/月", "traffic": "150GB/月"},
            {"name": "飞跃 Leap", "price": "44 元/月", "traffic": "300GB/月"},
            {"name": "瞬移 Teleport", "price": "84 元/月", "traffic": "600GB/月"},
            {"name": "跃迁 Warp", "price": "134 元/月", "traffic": "1000GB/月"}
        ],
        "verificationNote": "下单前核对当前折扣、设备数、流量周期与第三方客户端导入方式。"
    },
    "firefly": {
        "name": "Firefly",
        "rank": 26,
        "inviteURL": "https://vip02.fireflyaff.com/#/?code=lBPETX1d",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "96 元/年 (折合 8元/月)",
        "trafficFrom": "60GB/月",
        "suitableFor": "IPLC 专线、VLESS 架构、原生 IP 与多设备高码率场景",
        "sellingPoints": "定位偏向 IPLC 与 VLESS，并宣传原生 IP、不限设备和企业定制。套餐结构清晰，适合追求纯净落地 IP 与多设备稳定在线的用户。",
        "packages": [
            {"name": "年付版", "price": "96 元/年 (折合 8元/月)", "traffic": "60GB/月"},
            {"name": "Lite 月付", "price": "25 元/月", "traffic": "150GB/月"},
            {"name": "Plus 月付", "price": "45 元/月", "traffic": "300GB/月"},
            {"name": "Blaze 月付", "price": "85 元/月", "traffic": "600GB/月"},
            {"name": "Nova 月付", "price": "150 元/月", "traffic": "1000GB/月"},
            {"name": "一次性流量包", "price": "100 元", "traffic": "100GB 不限时"}
        ],
        "verificationNote": "购买前确认所需客户端、设备并发和公平使用条款。"
    },
    "kuajie-cloud": {
        "name": "跨界云",
        "rank": 27,
        "inviteURL": "https://vip02.kuajieaff.com/#/?code=Qu0GQkhP",
        "coupon": "",
        "couponNote": "暂无优惠码",
        "priceFrom": "20 元/月",
        "trafficFrom": "120GB",
        "suitableFor": "全网专线升级、通用订阅支持、120GB 至 1500GB 阶梯选择",
        "sellingPoints": "核心信息是全网专线升级与通用订阅支持，套餐提供 120GB 至 1500GB 的四档流量选择。适合先从月付小档测试，按需升级大流量档位。",
        "packages": [
            {"name": "轻云 Lite", "price": "20 元/月 (192元/年)", "traffic": "120GB/月"},
            {"name": "跃云 Leap", "price": "40 元/月 (384元/年)", "traffic": "300GB/月"},
            {"name": "凌云 Soar", "price": "100 元/月 (960元/年)", "traffic": "700GB/月"},
            {"name": "无界 Infinity", "price": "180 元/月 (1728元/年)", "traffic": "1500GB/月"}
        ],
        "verificationNote": "结算前应确认流量周期、设备并发、退款与当前专线规则。"
    }
}

# Update data/providers.json
with open('data/providers.json', 'r', encoding='utf-8') as f:
    providers = json.load(f)

for p in providers:
    slug = p['slug']
    if slug in raw_data:
        d = raw_data[slug]
        p['priceFrom'] = d['priceFrom']
        p['trafficFrom'] = d['trafficFrom']
        p['suitableFor'] = d['suitableFor']
        p['summary'] = d['sellingPoints']
        p['packages'] = d['packages']
        if d.get('coupon'):
            p['coupon'] = d['coupon']
            p['couponNote'] = d['couponNote']
        p['verificationNote'] = d['verificationNote']

with open('data/providers.json', 'w', encoding='utf-8') as f:
    json.dump(providers, f, ensure_ascii=False, indent=2)

print("Updated data/providers.json with user detailed data.")
