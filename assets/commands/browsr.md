# TAGLINE

支持云存储的文件浏览器 TUI

# TLDR

在当前目录**启动**

```browsr```

浏览指定目录

```browsr [path/to/directory]```

浏览 GitHub 仓库

```browsr [github://owner/repo]```

浏览 S3 存储桶

```browsr [s3://bucket-name]```

# SYNOPSIS

**browsr** [_options_] [_path_]

# PARAMETERS

**--theme** _THEME_
> 设置配色主题。

**--debug**
> 启用调试模式。

# DESCRIPTION

**browsr** 是基于 **Textual**（Python）构建的终端文件浏览器。它提供丰富的 TUI，可浏览文件和目录并显示带语法高亮的文件预览。除本地文件系统外，它还支持浏览远程源，包括 **GitHub 仓库**、**AWS S3** 存储桶以及其他云存储后端。

界面包含目录树面板和文件预览面板，后者对源码文件提供语法高亮。同时支持键盘和鼠标导航。

# CAVEATS

访问云存储需要配置适当的凭证和身份验证（如 S3 需要 AWS 凭证，私有仓库需要 GitHub 令牌）。远程源的性能取决于网速。大文件的预览可能较慢。

# HISTORY

**browsr** 由 **Juftin** 创建，是一款集成云存储的 Textual 文件浏览器，旨在把带语法高亮的丰富文件浏览体验带入终端。

# INSTALL

```nix: nix profile install nixpkgs#browsr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ranger](/man/ranger)(1), [nnn](/man/nnn)(1), [lf](/man/lf)(1), [mc](/man/mc)(1)
