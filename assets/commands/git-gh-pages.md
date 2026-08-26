# TAGLINE

创建用于 GitHub Pages 的孤儿分支

# TLDR

**创建 gh-pages 分支**

```git gh-pages```

# SYNOPSIS

**git** **gh-pages**

# DESCRIPTION

**git gh-pages** 创建并配置用于 GitHub Pages 托管的 **gh-pages** 分支。这是一条 **git-extras** 命令，自动创建具有空历史的孤儿分支，适合承载与主项目历史相互独立的静态网站。

该命令创建孤儿分支，移除所有被跟踪的文件，并做一个初始空提交。创建之后，即可向 gh-pages 分支填充 HTML、CSS 和 JavaScript 文件。推送到 GitHub 后，仓库内容就能以 **https://username.github.io/repository** 的形式作为网站访问。

# CAVEATS

需要安装 **git-extras** 软件包。该命令会将工作目录切换到新的 gh-pages 分支。现代 GitHub Pages 也可以从主分支的子目录（如 /docs）部署，或通过 GitHub Actions 部署，这使得孤儿分支方案已不如从前常见。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-fresh-branch](/man/git-fresh-branch)(1), [git-extras](/man/git-extras)(1), [git-checkout](/man/git-checkout)(1), [git-branch](/man/git-branch)(1)
