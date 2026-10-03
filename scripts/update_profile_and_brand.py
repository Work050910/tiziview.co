# -*- coding: utf-8 -*-
import json

files_to_update = ['site-seo-profile.json', 'docs/site-seo-profile.json']

for path in files_to_update:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    data['brandName'] = '机场看'
    data['siteTitle'] = '机场看 - 2026新手机场推荐与科学上网梯子配置导航指南 | 即刻连通全球高速网络'
    data['telegramChannel'] = 'https://t.me/+7Kvx9bNqRFhlM2Q1'
    data['siteDescription'] = '机场看 (tiziview.co) 专为新手小白打造的实时机场推荐与翻墙科学上网导航指南，主打即刻连接、现测可用与简单易用。提供高性价比稳定机场测速评测、主流客户端保姆级配置教程及自营专线透明入口。'
    data['footerSummaryParagraph1'] = '机场看 (tiziview.co) 官方博客专注小白的科学上网指南，持续提供 2026 翻墙梯子节点透明评测、高性价比稳定机场推荐、跨平台客户端配置教程与安全隐私保护，助您实现全设备极速平稳连接。'

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated site-seo-profile.json with brand name '机场看' and TG channel.")
