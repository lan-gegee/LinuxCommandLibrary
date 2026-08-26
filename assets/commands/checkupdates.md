# TAGLINE

安全地检查 Arch Linux 软件包更新

# TLDR

同步数据库并**列出待更新项**

```checkupdates```

**不同步**数据库而列出待更新项

```checkupdates -n```

仅在结果与上次检查**不同**时显示更新

```checkupdates -c```

列出更新并**下载软件包**到缓存

```checkupdates -d```

使用**指定的 pacman 数据库**

```CHECKUPDATES_DB=[path/to/directory] checkupdates```

# SYNOPSIS

**checkupdates** [_options_]

# DESCRIPTION

**checkupdates** 无需 root 权限即可安全地检查 Arch Linux 的待更新项。它会创建同步数据库的临时副本用于检查更新，避免对系统做任何修改。

它是 pacman-contrib 软件包的一部分，提供了一种可安全用于脚本和状态栏的更新检查方式。

# PARAMETERS

**-n, --nosync**
> 不同步数据库，使用缓存数据

**-c, --change**
> 仅当更新与上次检查不同才显示

**-d, --download**
> 检查的同时下载软件包到 pacman 缓存

**-h, --help**
> 显示帮助信息

# ENVIRONMENT

**CHECKUPDATES_DB**
> 用于临时数据库的路径

# CAVEATS

仅限 Arch Linux。除非使用 --nosync，否则需要网络访问来同步数据库。临时数据库存储在用户可写的位置。

# SEE ALSO

[pacman](/man/pacman)(8), [paru](/man/paru)(1), [yay](/man/yay)(1)

# RESOURCES

```[Source code](https://gitlab.archlinux.org/pacman/pacman-contrib)```

<!-- verified: 2026-06-22 -->
