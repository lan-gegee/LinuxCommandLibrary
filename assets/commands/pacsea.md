# TAGLINE

用于 Arch Linux 官方仓库与 AUR 的 TUI 软件包搜索工具

# TLDR

**启动软件包搜索 TUI**

```pacsea```

**从命令行搜索软件包**

```pacsea -s [query]```

**直接安装软件包**

```pacsea -i [package1] [package2]```

**安装文件中列出的软件包**

```pacsea -I [packages.txt]```

**更新官方仓库与 AUR 软件包**

```pacsea -u```

**列出显式安装的软件包**

```pacsea -l --exp```

**预览操作而不实际更改**

```pacsea --dry-run```

**启动前刷新软件包数据库**

```pacsea -y```

# SYNOPSIS

**pacsea** [_options_] [_query_ | _package_...]

# PARAMETERS

**-s**, **--search** _query_
> 在官方仓库和 AUR 中搜索软件包。

**-i**, **--install** _package_...
> 安装一个或多个软件包。

**-I** _file_
> 安装文件中列出的软件包（支持 `#` 注释）。

**-r**, **--remove** _package_...
> 移除软件包前会弹出确认提示。

**-u**, **--update**
> 更新官方仓库与 AUR 软件包。

**-l** [**--exp** | **--imp** | **--all**]
> 列出已安装的软件包（显式、隐式或全部）。

**-n** [**--read** | **--unread** | **--all**]
> 显示 Arch Linux 新闻源。

**-y**, **--refresh**
> 启动 TUI 前先刷新软件包数据库。

**--clear-cache**
> 删除所有缓存的文件。

**--dry-run**
> 预览操作而不实际更改。

**-v**, **--verbose**
> 启用详细输出。

**--log-level** _level_
> 设置日志级别（trace、debug、info、warn、error）。

**--no-color**
> 禁用彩色输出。

**--version**
> 显示版本信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**pacsea** 是一个基于 Rust 的快速终端用户界面，可用于搜索、查看来自 Arch Linux 官方仓库和 AUR 的软件包并将其加入队列。它提供键盘优先、对 Vim 友好的导航方式，可在多个可重新排序的面板中查看搜索结果、软件包详情、PKGBUILD 预览和 AUR 评论。

除了交互式 TUI 之外，pacsea 还提供了 CLI，可直接执行搜索、安装、移除和升级操作。它集成了结合 Arch 新闻、安全公告和更新通知的新闻源，并支持使用 ClamAV、Trivy、Semgrep、ShellCheck 和 VirusTotal 等工具进行可选的 AUR 安全扫描。

# CAVEATS

仅适用于 Arch Linux 及基于 Arch 的发行版。安装 AUR 软件包需要 **paru** 或 **yay** 等 AUR 助手。安全扫描工具是可选项，需要单独安装。

# HISTORY

**pacsea** 由 **Firstp1ck** 开发，使用 **Rust** 编写。可通过 `cargo install pacsea` 和 AUR 分发获取。

# SEE ALSO

[pacman](/man/pacman)(8), [pacseek](/man/pacseek)(1), [paru](/man/paru)(1), [yay](/man/yay)(1)
