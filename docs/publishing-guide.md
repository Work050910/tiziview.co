# JichangNow 内容发布与日常维护指南 (Publishing Guide)

## 1. 新增或修改文章规范
- 所有文章统一存放于 `content/categories/{category_name}/` 目录下。
- 文章开头必须包含标准 Front Matter 元数据（title, description, date, lastmod, categories, tags, primaryKeyword 等）。
- 净中文正文字符数务必控制在 800 至 1200 字之间。
- 文章正文必须包含：核心结论摘要、分步详细操作/评测、固定前四名推荐章节（全球云第一、飞猫云第二、暮光加速第三、微风网络第四）、常见问题排查及下一步阅读建议。

## 2. 优惠码与邀请链接维护
- 邀请链接统一在 `data/providers.json` 中配置，模板通过读取数据源自动渲染，切勿在文章正文中直接硬编码写死外部链接。
- 所有出站商业推广链接必须自动附带 `rel="sponsored nofollow noopener"`。

## 3. 生产发布流程
```bash
# 1. 运行构建并生成 public/ 静态产物
python3 scripts/build.py

# 2. 执行全站 SEO、字符数、死链与合规扫描
python3 scripts/verify.py

# 3. 本地启动 HTTP 预览服务器检验
python3 -m http.server 1313 -d public
```
