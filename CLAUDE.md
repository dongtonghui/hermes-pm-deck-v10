# 项目上下文 · hermes-pm-deck-publish-v8

这份文档是给后续继续处理这个项目的 session 看的。它记录了这个项目的背景、已经做出的关键决策、文件组织方式、设计规范和常见坑。

## 1. 项目是什么

这是 **《AI 工具在硬件产品工作中的深度应用 · V8》** 培训课件的 HTML 幻灯片版本，面向硬件产品经理，60 分钟内部分享 + 实战。

- 共 35 页独立 HTML 幻灯片
- 尺寸固定 1920×1080
- 用 `index.html` 作为聚合器，支持网格概览和单页演示
- 附带 PDF 导出脚本和缩略图生成脚本

核心案例是「带氛围灯功能的植物生长照射仪」，用多 Agent 交叉校验论证氛围灯不是刚需。

## 2. 目录结构

```
hermes-pm-deck-publish-v8/
├── index.html                  # 聚合器：概览墙 + 单页演示
├── slides/                     # 35 页独立 HTML
├── shared/
│   ├── tokens.css             # 全局样式变量和工具类
│   └── tech-batch.css         # 已删除；历史残留不要在后续使用
├── scripts/
│   ├── gen_deck_thumbs.mjs    # 生成 gallery 缩略图
│   └── export_deck_pdf.mjs    # 导出 PDF（项目根目录也有同名文件）
├── thumbs/                    # 35 张预渲染缩略图
├── hermes-pm-deck.pdf         # 离线 PDF
├── README.md                  # 对外 README
├── PUBLISH.md                 # GitHub Pages 发布步骤
├── package.json               # 依赖：playwright, sharp, pdf-lib
└── .github/workflows/
    └── deploy.yml             # GitHub Actions 自动部署
```

## 3. 当前状态（重要）

### 3.1 设计风格：混合状态

项目经历过一次风格摇摆：

- **原始风格**：暖色纸质感，浅底深字，橙色 accent
- 用户要求把第 30 页改成 **n8n 式深色科技感**
- 后续又把 01、05、12、35 四页改成同样的深色科技风格
- 然后尝试批量把所有 35 页改成深色科技风
- **最后回滚了批量改动**，只保留 5 个关键页的深色科技风

所以当前状态是：

| 页码 | 页面 | 风格 |
|------|------|------|
| 01 | 封面 | 深色科技感 |
| 05 | 新范式 | 深色科技感 |
| 12 | 植物灯案例 | 深色科技感 |
| 30 | 完整自动化闭环 | 深色科技感 |
| 35 | 资源与 Q&A | 深色科技感 |
| 其余 30 页 | — | 原始暖色纸质感 |
| index.html 概览 | — | 原始暖色风格 |

`shared/tokens.css` 里同时保留了两套变量：原始暖色变量 + 新增的 tech-dark 变量。`body.tech-dark` 才会触发深色样式，所以不会影响原始页面。

### 3.2 GitHub Pages 未部署完成

- 已在 GitHub 创建仓库：`dongtonghui/hermes-pm-deck-v8`
- 本地 git 已初始化，remote 已配置
- **但 push 失败**：Token 缺少 `workflow` scope，无法提交 `.github/workflows/deploy.yml`
- 解决方式见 [PUBLISH.md](PUBLISH.md)：给 Token 加上 `workflow` scope 后重新 push，或者删掉 deploy.yml 改用 branch 部署

### 3.3 缩略图 / PDF 未重新生成

这个 Linux 容器里的 Chromium 运行 Playwright 会 segfault，所以无法在这里重新生成缩略图和 PDF。本机如果 Playwright 正常，可以运行：

```bash
npm install
npm run thumbs
npm run pdf
```

## 4. 设计规范

### 4.1 幻灯片基本结构

每页 HTML 必须包含：

```html
<div class="slide-content">
  <div class="page-masthead">
    <div class="brand">AI 工具深度应用</div>
    <div>XX / 35 · 章节名</div>
  </div>

  <div class="main">
    <!-- 页面主体内容 -->
  </div>

  <div class="page-footer">
    <div class="section-tag">章节 · 子标题</div>
    <div>AI 工具在产品工作中的深度应用</div>
  </div>
</div>
```

页码由 deck 外壳统一承载，**单页内容不要自带页码 / 进度条**。

### 4.2 样式系统

`shared/tokens.css` 定义了：

- 颜色变量：`--paper`, `--paper-warm`, `--ink`, `--accent`, `--dark-block`, `--tech-bg` 等
- 字体变量：`--font-display`（衬线）、`--font-body`（无衬线）、`--font-en`
- 字号变量：`--h1` ~ `--tiny`
- 工具类：`.card`, `.kicker`, `.subtitle`, `.body-large`, `.check-list` 等
- 动画类：`.anim-fade-up`, `.anim-scale-in`, `.anim-fade-in` 和 `.delay-1` ~ `.delay-8`

深色页面需要在 `<body>` 上加 `class="tech-dark"`，并设置 `style="background: var(--tech-bg);"`。

### 4.3 添加新页或修改页面的原则

- 保持 1920×1080 固定尺寸
- 尽量复用 `tokens.css` 里的变量和工具类
- 如果要和现有某页风格一致，直接 copy 那页的 HTML 结构再改内容
- 不要给单页加页码、不要加底部进度条
- 卡片/面板优先用半透明暗色（深色页）或白色（暖色页），保持一致

## 5. 常见操作

### 本地预览

```bash
# 在项目根目录
python3 -m http.server 8080
# 浏览器打开 http://localhost:8080
```

或者直接用浏览器打开 `index.html`。

### 修改后验证

修改任何 slide 后，建议做两件事：

1. HTML 语法校验（可用 Python 简单解析）
2. 在浏览器里翻到对应页看效果

这个环境没法用 Playwright 截图，视觉验证必须在本机浏览器做。

### 生成缩略图和 PDF

```bash
npm install
npm run thumbs
npm run pdf
```

### 发布到 GitHub Pages

见 [PUBLISH.md](PUBLISH.md)。当前主要阻塞是 Token 权限。

## 6. 已知问题和注意点

1. **Playwright 在容器里不可用**：不要在这里尝试跑 `gen_deck_thumbs.mjs` 或 `export_deck_pdf.mjs`，会 segfault。
2. **文件编码**：所有 HTML/CSS 都是 UTF-8，保持这个编码。
3. **Google Fonts**：每页都引用了 Google Fonts，离线环境可能加载慢，但这是当前设计的一部分。
4. **混合风格**：如果后续要把所有页面统一成深色或统一成暖色，需要批量处理。当前 5 页深色 + 30 页暖色是用户明确的决策，不要轻易再改，除非用户重新要求。
5. **deploy.yml 提交问题**：push 到 GitHub 时如果 Token 没有 workflow scope，会报 `refusing to allow a Personal Access Token to create or update workflow`。
6. **旧版本备份**：`hermes-pm-deck-publish-v8-clean/` 是一个干净的回滚备份，必要时可以从那里恢复文件。

## 7. 用户偏好

- 用户喜欢直接、高效的风格
- 对第 30 页的 n8n 式工作流编排图比较满意
- 对「连接线不要重叠」「节点不要穿帮」这类视觉细节比较敏感
- 倾向于用深色科技感做关键页的强调，但不一定要全 deck 深色
- 用户会把 Token 等敏感信息通过聊天提供，不会持久保存在环境变量里

## 8. 如果从头继续这个项目

建议先做以下检查：

1. 打开 `index.html` 翻一遍 35 页，确认当前视觉状态
2. 检查 git 状态：`git status`、`git log --oneline`
3. 确认 GitHub Pages 是否已经部署成功
4. 如果需要改风格，先问用户要「统一深色」「统一暖色」还是「保持当前混合」
5. 任何批量修改前，先 copy 一份到 `hermes-pm-deck-publish-v8-backup/` 作为保险

---

最后更新：2026-07-06
