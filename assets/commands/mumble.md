# TAGLINE

开源语音聊天应用程序

# TLDR

**启动 Mumble**

```mumble```

**连接到服务器**

```mumble [mumble://server.example.com]```

**以指定用户名连接**

```mumble [mumble://user@server.example.com]```

**连接特定端口**

```mumble [mumble://server.example.com:64738]```

**最小化启动**

```mumble --minimized```

# SYNOPSIS

**mumble** [_options_] [_url_]

# PARAMETERS

_URL_
> Mumble 服务器 URL。

**--minimized**
> 最小化到托盘启动。

**--nooverlay**
> 禁用游戏内叠加层。

**--nospeech**
> 禁用文字转语音。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mumble** 是一款开源语音聊天应用程序。它提供低延迟语音通信。

该工具专为游戏设计，具备位置音频和低延迟特性。

# CAVEATS

需要 Mumble 服务器（murmur）。需要进行音频设置。虽以游戏为主，但也可通用。

# HISTORY

Mumble 创建于 **2005 年**，作为面向玩家的专有语音聊天软件的开源替代品。

# INSTALL

```apt: sudo apt install mumble```

```dnf: sudo dnf install mumble```

```pacman: sudo pacman -S mumble```

```apk: sudo apk add mumble```

```zypper: sudo zypper install mumble```

```nix: nix profile install nixpkgs#mumble```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[discord](/man/discord)(1), [signal-desktop](/man/signal-desktop)(1)
