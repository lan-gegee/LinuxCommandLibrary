# TAGLINE

安装和更新 Void Linux 软件包

# TLDR

**安装**新软件包

```xbps-install [package]```

**同步并更新**所有软件包

```xbps-install -S -u```

# SYNOPSIS

**xbps-install** [_options_] [_package_...]

# PARAMETERS

**-S, --sync**
> 同步软件仓库索引

**-u, --update**
> 更新已安装的软件包

**-y, --yes**
> 对所有提问自动回答 yes

**-n, --dry-run**
> 显示将要执行的操作

**-f, --force**
> 强制安装

**-R, --repository _url_**
> 添加要搜索的软件仓库

**-D, --download-only**
> 仅下载软件包

**-v, --verbose**
> 详细输出

# DESCRIPTION

**xbps-install** 是 XBPS（Void Linux 所用的包管理器）的软件包安装和更新工具。它负责软件包安装、依赖解析和系统更新。

在安装或更新软件包之前，先用 **-S** 同步软件仓库索引以获取最新的软件包信息。

# CAVEATS

系统级安装需要 root 权限。更新前应先运行仓库同步（**-S**）。属于 Void Linux 的 XBPS 包管理系统的一部分。

# INSTALL

```apk: sudo apk add xbps```

```nix: nix profile install nixpkgs#xbps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xbps-query](/man/xbps-query)(1), [xbps-remove](/man/xbps-remove)(1), [xbps-reconfigure](/man/xbps-reconfigure)(1)
