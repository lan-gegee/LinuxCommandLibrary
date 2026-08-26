# TAGLINE

语音、视频和文字通信平台

# TLDR

**启动 Discord**

```discord```

**最小化启动**到系统托盘

```discord --start-minimized```

**忽略 GPU 黑名单**

```discord --ignore-gpu-blocklist```

**禁用硬件**加速

```discord --disable-gpu```

**启用详细日志**

```discord --enable-logging```

# SYNOPSIS

**discord** [_options_]

# PARAMETERS

**--start-minimized**
> 最小化启动到系统托盘。

**--ignore-gpu-blocklist**
> 忽略 GPU 硬件黑名单。

**--disable-gpu**
> 禁用硬件加速。

**--enable-logging**
> 启用详细日志。

**--no-sandbox**
> 禁用沙箱（不推荐）。

**--proxy-server** _URL_
> 使用指定的代理服务器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Discord** 是一个语音、视频和文字通信平台，在游戏社区中广受欢迎，并日益被用于一般协作。Linux 客户端提供服务器、私信、语音频道和屏幕共享等功能。

这个基于 Electron 的应用支持所有核心 Discord 功能，包括富状态显示、按键说话、噪声抑制和服务器管理。它集成系统托盘以支持后台运行。

Discord 在 Linux 上可通过官方软件包、Flatpak、Snap 或发行版软件仓库安装。某些功能（如游戏检测）与 Windows 相比可能受限。

# CAVEATS

基于 Electron，资源占用较高。Wayland 下的屏幕共享可能有限制。部分游戏集成在 Linux 上不可用。自定义 Electron 标志可在 **~/.config/discord-flags.conf** 中设置（每行一个标志）。

# HISTORY

Discord 由 **Jason Citron** 创立，于 **2015** 年发布。最初面向玩家，后来扩展到一般社区。Linux 客户端于 **2017** 年推出，与 Windows、macOS、iOS 和 Android 一同构成跨平台支持。

# INSTALL

```pacman: sudo pacman -S discord```

```nix: nix profile install nixpkgs#discord```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[slack](/man/slack)(1), [mumble](/man/mumble)(1)
