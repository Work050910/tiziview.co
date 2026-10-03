# Google Search Console 与 Bing Webmaster 设置指南

## 1. 站点所有权验证
在 `hugo.toml` 或 `site-seo-profile.json` 中配置验证码：
- Google 验证：添加 HTML meta 标签或 DNS TXT 记录。
- Bing 验证：添加 BingSiteAuth.xml 或 meta 验证标签。

## 2. Sitemap 提交
- 站点主 Sitemap URL：`https://tiziview.co/sitemap.xml`
- 在 Google Search Console 的“Sitemaps”模块输入 `sitemap.xml` 并点击提交。
- 在 Bing Webmaster 的“站点地图”模块提交相同地址。

## 3. IndexNow 自动索引推送
针对 Bing 等支持 IndexNow 的现代搜索引擎：
- 在根目录放置包含 API Key 的文本文件（如 `{api_key}.txt`）。
- 每次新文章发布后，运行 IndexNow 提交脚本，自动向 API 端点推送最新变更 URL。
