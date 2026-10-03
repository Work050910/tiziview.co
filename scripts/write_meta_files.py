# -*- coding: utf-8 -*-

readme_content = """# JichangNow (`https://tiziview.co`)

> 面向新手小白的实时机场推荐与翻墙科学上网导航指南，主打“即刻连接、现测可用、简单易用”。

---

## 项目概览与技术架构

- **域名**：`https://tiziview.co`
- **技术框架**：Hugo Extended + Anatole 主题架构（纯静态双栏响应式文章博客与即刻导航体系）
- **左侧栏 (Sidebar)**：展示站点一句话定位、全平台设备快速分类入口、实时推荐自营/精选服务透明通道
- **正文核心区域**：聚焦深度客户端配置保姆级教程、实时测速横向评测、常见排障避坑指南
- **单一数据源**：`site-seo-profile.json` 与 `docs/site-seo-profile.json` 统一管理全站核心关键词、长尾词、Hero/Footer 说明及导航映射
- **商业与合规**：
  - 固定前四名商业服务商（全球云、飞猫云、暮光加速、微风网络）顺序永久锁定，邀请链接与专属优惠码原生绑定
  - 所有商业外链附带 `rel=\"sponsored nofollow noopener\"`
  - 100% 杜绝竞品与参考发布者黑名单泄露
  - 53 篇导航文章 + 27 个服务商独立测评，净中文字符数严格控制在 800 至 1200 字之间
  - 100 问长尾 FAQ 问答中心，严格遵循 9 大主题配额（18, 14, 10, 10, 8, 14, 10, 8, 8），每条问答 120-180 字精炼直接解答

---

## 快速上手与本地运行

### 1. 依赖环境
- Python 3.8+（自带标准库，无需任何额外 pip 安装）
- Hugo Extended（可选，用于直接运行 `hugo server` 或原生构建）

### 2. 本地生产构建
```bash
# 运行生产构建，将所有 Markdown 内容、数据与静态资源编译至 public/
python3 scripts/build.py
```

### 3. 全维度自动化质量与 SEO 验证
```bash
# 执行 H1、Canonical、JSON-LD、死链、字数（800-1200字）与合规审查
python3 scripts/verify.py
```

### 4. 本地静态预览
```bash
# 启动本地轻量 HTTP 服务器预览
python3 -m http.server 1313 -d public
```
浏览器打开 `http://localhost:1313` 即可浏览完整网站。

---

## 目录结构

```
tiziview.co/
├── hugo.toml                            # Hugo Extended 原生站点配置文件
├── site-seo-profile.json                # 全站 SEO 关键词与导航单一数据源
├── data/
│   ├── providers.json                   # 27 个机场服务商数据源（含前四名与扩展池）
│   └── faq100.json                      # 100 问长尾 FAQ 结构化数据集
├── content/
│   ├── _index.md                        # 首页内容（英雄区、榜单、横评对比、教程入口）
│   ├── services/                        # 自营精选专线服务专页
│   ├── categories/                      # 6 大分类目录（共 53 篇核心导航文章）
│   │   ├── airport-reviews/             # 机场推荐榜 (15 篇)
│   │   ├── windows/                     # Windows 教程 (8 篇)
│   │   ├── mac/                         # Mac 教程 (6 篇)
│   │   ├── ios/                         # iOS 教程 (8 篇)
│   │   ├── android/                     # Android 教程 (6 篇)
│   │   └── faq/                         # 常见问题与踩坑 (10 篇)
│   ├── providers/                       # 27 个服务商独立规范评测文章
│   ├── faq/                             # 100 问知识中心大落地页
│   └── (trust pages)                    # 9 个法律与信任页面 (about, terms, privacy...)
├── layouts/                             # Anatole 风格响应式模板
│   ├── _default/                        # baseof.html, single.html, list.html
│   ├── index.html                       # 首页专属模板
│   ├── 404.html                         # 自定义 404 页面
│   └── partials/                        # head, sidebar, footer, promo-card, schema...
├── static/                              # 纯静态资源（CSS, JS, 矢量图标, robots.txt）
├── docs/                                # 内部文档、合规审查与万能替换协议
│   ├── site-seo-profile.json            # SEO 配置文件备份
│   ├── seo-profile-replacement-contract.md # 万能替换操作协议
│   ├── reference-publisher-blocklist.md    # 竞品与参考黑名单（严禁公开）
│   ├── keyword-map.md                   # 关键词聚类与意图映射
│   ├── keyword-coverage.csv             # 关键词全量覆盖表
│   ├── faq-keywords-100.csv             # 100 问 FAQ 矩阵
│   ├── faq-content-matrix.md            # FAQ 内容规划大纲
│   ├── provider-review-matrix.md        # 27 个服务商评测矩阵
│   ├── content-plan.md                  # 60+ 篇后续主题扩展路线图
│   ├── publishing-guide.md              # 内容发布与日常维护指南
│   ├── search-console-setup.md          # 搜索引擎站长工具接入指南
│   └── launch-checklist.md              # 上线前合规检查清单
└── scripts/
    ├── build.py                         # 生产构建编译脚本
    └── verify.py                        # 全自动化验收测试脚本
```

---

## 日常维护与操作指引

### 如何更新价格与优惠码？
1. 编辑 `data/providers.json`，修改对应服务商的 `priceFrom`、`coupon`、`lastChecked` 字段；
2. 运行 `python3 scripts/build.py` 重新生成生产站点；
3. 运行 `python3 scripts/verify.py` 确保各项合规指标 100% 达标。

### 如何整体替换关键词与导航？
参考 `docs/seo-profile-replacement-contract.md` 协议，修改 `site-seo-profile.json` 中的 `primaryKeywords`、`heroKeywords`、`footerKeywords` 与 `navigationItems`，随后重新运行构建脚本即可全站自动化同步生效。
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

agents_content = """# AGENTS.md

## JichangNow 项目开发与维护约定

- **技术栈**：纯静态双栏博客，遵循 Hugo Extended + Anatole 设计理念。
- **构建输出目录**：`public/`。
- **SEO 配置文件**：`site-seo-profile.json` 为全站单一数据源，修改关键词或导航必须优先修改该文件。
- **商业与推广铁律**：
  - 前四名服务商顺序（1. 全球云、2. 飞猫云、3. 暮光加速、4. 微风网络）固定不变。
  - 所有推广链接必须保留原始 inviteURL 与 code 参数，不可替换或简写。
  - 外部商业推广链接必须附带 `rel=\"sponsored nofollow noopener\"`。
- **合规隔离铁律**：
  - 严禁将 `docs/reference-publisher-blocklist.md` 中的任何竞品或参考博客名称暴露在任何公开 HTML、JS、JSON 或 RSS 中。
- **字数控制**：
  - 导航文章与服务商测评正文净中文字符数严格维持在 800 至 1200 字之间。
- **构建与测试**：
  - 提交任何变更前，必须运行 `python3 scripts/build.py` 与 `python3 scripts/verify.py`，确保错误数与预警数均为 0。
"""

with open("AGENTS.md", "w", encoding="utf-8") as f:
    f.write(agents_content)

gitignore_content = """public/
resources/
.DS_Store
*.pyc
__pycache__/
.system_generated/
"""

with open(".gitignore", "w", encoding="utf-8") as f:
    f.write(gitignore_content)

print("README.md, AGENTS.md, and .gitignore written successfully.")
