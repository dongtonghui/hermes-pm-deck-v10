# AI 工具在硬件产品工作中的深度应用 · V9

一份面向硬件产品经理的 60 分钟内部分享课件，共 37 页，采用纯 HTML 幻灯片形式。

**在线演示**：https://dongtonghui.github.io/hermes-pm-deck-v9/

## 目录结构

- `index.html` — 幻灯片聚合器（网格概览 + 单页演示）
- `slides/` — 35 页独立 HTML 幻灯片
- `shared/` — 共享样式 `tokens.css`
- `scripts/` — 缩略图 / PDF 导出脚本
- `thumbs/` — 无限画廊概览用的缩略图
- `hermes-pm-deck.pdf` — 离线 PDF 版

## 本地预览

```bash
# 直接打开
open index.html

# 或者用任意静态服务器
python3 -m http.server 8080
```

## 导出资源

```bash
npm install
npm run thumbs   # 生成 gallery 缩略图
npm run pdf      # 导出 PDF
```

## 发布到 GitHub Pages

仓库已配置 GitHub Actions，push 到 `main` 分支后会自动部署到 Pages。

```bash
git add .
git commit -m "v9 slides"
git push -u origin main
```
