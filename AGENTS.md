# AGENTS.md

## 梯子view 项目开发与维护约定

- **技术栈**：纯静态双栏博客，遵循 Hugo Extended + Anatole 设计理念。
- **构建输出目录**：`public/`。
- **SEO 配置文件**：`site-seo-profile.json` 为全站单一数据源，修改关键词或导航必须优先修改该文件。
- **商业与推广铁律**：
  - 前四名服务商顺序（1. 全球云、2. 飞猫云、3. 暮光加速、4. 微风网络）固定不变。
  - 所有推广链接必须保留原始 inviteURL 与 code 参数，不可替换或简写。
  - 外部商业推广链接必须附带 `rel="sponsored nofollow noopener"`。
- **合规隔离铁律**：
  - 严禁将 `docs/reference-publisher-blocklist.md` 中的任何竞品或参考博客名称暴露在任何公开 HTML、JS、JSON 或 RSS 中。
- **字数控制**：
  - 导航文章与服务商测评正文净中文字符数严格维持在 800 至 1200 字之间（2026全网27家机场总榜综合大文放宽至2500字内）。
- **构建与测试**：
  - 提交任何变更前，必须运行 `python3 scripts/build.py` 与 `python3 scripts/verify.py`，确保错误数与预警数均为 0。
