# 发布到 GitHub Pages 步骤

## 方案

新建仓库：`hermes-pm-deck-v9`

## 1. 在 GitHub 创建仓库

访问：https://github.com/new

- Repository name：`hermes-pm-deck-v9`
- 保持 Public（GitHub Pages 免费部署需要 Public，或 Pro/Team 才能私有部署）
- 不要勾选 README / .gitignore / license（本地已有）
- 点击 **Create repository**

## 2. 推送代码

在 `hermes-pm-deck-publish-v9/` 目录下执行：

```bash
# HTTPS 方式（会提示输入 GitHub 用户名和 Personal Access Token）
git push -u origin main
```

如果你用 SSH：

```bash
git remote set-url origin git@github.com:dongtonghui/hermes-pm-deck-v9.git
git push -u origin main
```

> 从 2023 年起 GitHub 不再支持密码直接推送，需要用 **Personal Access Token (classic)** 作为密码。可以在 https://github.com/settings/tokens 生成。
>
> **安全提示**：不要把 token 直接写入 `.git/config` 的 URL 中。推荐使用 git credential helper 或 GitHub CLI 管理凭据。

## 3. 开启 GitHub Pages

推送完成后：

1. 打开仓库页面：https://github.com/dongtonghui/hermes-pm-deck-v9
2. 进入 **Settings → Pages**
3. 在 **Build and deployment → Source** 中选择 **GitHub Actions**
4. 回到 **Actions** 标签，等待 `Deploy to GitHub Pages` workflow 跑完

## 4. 访问在线演示

部署成功后即可访问：

```
https://dongtonghui.github.io/hermes-pm-deck-v9/
```

## 后续更新

每次修改后只需要：

```bash
git add .
git commit -m "update slides"
git push
```

GitHub Actions 会自动重新部署。
