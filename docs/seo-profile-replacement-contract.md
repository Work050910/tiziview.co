# 万能 SEO 配置整体替换协议 (SEO Profile Replacement Contract)

## 概述
本协议定义了如何使用一套全新的 SEO 关键词、导航结构和品牌定位，通过修改单一数据源 `site-seo-profile.json` 自动更新全站所有元数据、Hero、Footer、导航、文章推荐和内链，而无需手动修改各个 HTML 模板。

## 单一数据源路径
- 生产配置文件：`site-seo-profile.json`
- 规范副本：`docs/site-seo-profile.json`

## 替换接口字段定义
| 字段名 | 类型 | 说明 | 必须性 |
| :--- | :--- | :--- | :--- |
| `domain` | String | 统一 HTTPS 绝对域名 | 必填 |
| `siteTitle` | String | 全局首页 Title 及标题模式前缀 | 必填 |
| `siteDescription` | String | 首页及全站默认 meta description | 必填 |
| `primaryKeywords` | Array | 核心关键词列表（首页、核心H1、重点内链） | 必填 |
| `secondaryKeywords` | Array | 辅助关键词列表（栏目页、副标题、次要内链） | 必填 |
| `longTailKeywords` | Array | 长尾搜索词列表（教程、FAQ、长尾落地页） | 必填 |
| `heroKeywords` | Array | 首屏大标题下方 90-160 字说明内自然覆盖的词簇 | 必填 |
| `footerKeywords` | Array | 页脚品牌介绍 70-130 字说明内自然覆盖的词簇 | 必填 |
| `navigationItems` | Array | 导航条目（标签、URL、关键词、落地页文章数） | 必填 |
| `faqClusters` | Array | 100 问长尾 FAQ 主题集群与配额分配 | 必填 |

## 整体替换实施顺序
1. **读取与备份**：读取现有 `site-seo-profile.json`，导出当前 URL 清单。
2. **规范化新词表**：消除大小写及意图重复，建立新搜索意图集群。
3. **写入新配置**：更新 `site-seo-profile.json`。
4. **URL 重定向维护**：若导航路径有变更，在 `_redirects` 中建立 301 映射，坚决杜绝 404。
5. **保护核心商业资产**：保持前四名主推服务（全球云、飞猫云、暮光加速、微风网络）的专属邀请链接、优惠码与转化位不变。
6. **自动化重新构建**：运行 `python3 scripts/build.py` 与 `python3 scripts/verify.py`，确保无残留旧词，全站页面结构完备。
