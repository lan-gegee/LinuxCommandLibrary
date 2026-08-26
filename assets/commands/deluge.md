# TAGLINE

采用插件架构的轻量级 BitTorrent 客户端

# TLDR

**启动 Deluge** GTK 客户端

```deluge```

**添加种子文件**

```deluge [file.torrent]```

**通过磁力链接添加种子**

```deluge "[magnet:?xt=urn:btih:...]"```

**启动指定的 UI**（gtk、web 或 console）

```deluge [console]```

**设置默认启动的 UI**

```deluge -s [gtk]```

**使用自定义配置目录**

```deluge -c [path/to/config]```

# SYNOPSIS

**deluge** [_options_] [_torrent_...]

# PARAMETERS

_TORRENT_
> 要添加的种子文件或磁力链接。

_UI_
> 以子命令形式指定要启动的 UI：gtk、web 或 console（如 deluge console）。

**-s**, **--set-default-ui** _UI_
> 设置未指定 UI 时默认运行的 UI。

**-c**, **--config** _DIR_
> 配置目录。

**-l**, **--logfile** _FILE_
> 将日志输出到文件。

**-L**, **--loglevel** _LEVEL_
> 日志级别：none、error、warning、info、debug。

**-q**, **--quiet**
> 减少日志输出（等同于 loglevel none）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**deluge** 是一款轻量级的跨平台 BitTorrent 客户端，以其插件架构和多种界面选项著称。此命令用于启动 GTK 图形界面来管理种子下载。

Deluge 采用守护进程/客户端架构，下载守护进程（deluged）可以独立运行，客户端则在本地或远程连接。GTK 客户端提供功能完整的界面，用于添加种子、管理下载和配置设置。

该客户端支持带宽计划、按种子设置、peer 交换、magnet URI 和加密等特性。其插件系统可通过标签、通知、Web 种子等功能扩展软件。

# CONFIGURATION

**~/.config/deluge/**
> 配置文件所在目录，包括 core.conf、gtk-ui.conf 以及各插件配置。

# CAVEATS

完整功能需要 deluged 守护进程运行中。GTK 界面需要图形环境。部分功能依赖可选插件。远程连接需要正确配置认证。

# HISTORY

Deluge 创建于 **2006 年**，使用 Python 和 GTK 开发。它的定位是其他 BitTorrent 客户端的全能而轻量的替代品，强调插件可扩展性和跨平台支持。

# INSTALL

```dnf: sudo dnf install deluge```

```pacman: sudo pacman -S deluge```

```apk: sudo apk add deluge```

```zypper: sudo zypper install deluge```

```nix: nix profile install nixpkgs#deluge```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[deluged](/man/deluged)(1), [deluge-console](/man/deluge-console)(1), [transmission-cli](/man/transmission-cli)(1)

# RESOURCES

```[Source code](https://github.com/deluge-torrent/deluge)```

```[Homepage](https://deluge-torrent.org)```

```[Documentation](https://dev.deluge-torrent.org/wiki/UserGuide)```

<!-- verified: 2026-07-11 -->
