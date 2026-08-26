# TAGLINE

Telegram 即时通讯桌面客户端

# TLDR

**启动 Telegram**

```telegram-desktop```

**通过 URL 打开**

```telegram-desktop -- [tg://resolve?domain=username]```

**以最小化方式启动**

```telegram-desktop -startintray```

**指定工作目录**

```telegram-desktop -workdir [~/.telegram]```

**调试模式**

```telegram-desktop -debug```

# SYNOPSIS

**telegram-desktop** [_-startintray_] [_-workdir dir_] [_options_]

# PARAMETERS

**-startintray**
> 最小化到系统托盘启动。

**-workdir** _DIR_
> 数据目录。

**-debug**
> 调试模式。

**-scale** _N_
> 界面缩放系数。

**--**
> 打开 URL。

# DESCRIPTION

**telegram-desktop** 是 Telegram 即时通讯平台的官方桌面客户端。它以原生桌面应用的形式提供 Telegram 的全部功能，包括文字消息、语音和视频通话、媒体分享以及频道。

该客户端支持最多 20 万成员的群聊、端到端加密的秘密聊天、单个最大 2GB 的文件传输，以及在所有设备间的无缝同步。它基于 Qt 构建，可运行于 Linux、macOS 和 Windows，数据存储在可配置的工作目录中。

# CAVEATS

需要账号。需要联网。基于 Qt 的应用程序。

# HISTORY

**Telegram Desktop** 是 **Telegram** 的官方桌面客户端，由 Durov 兄弟的团队打造。

# INSTALL

```pacman: sudo pacman -S telegram-desktop```

```zypper: sudo zypper install telegram-desktop```

```nix: nix profile install nixpkgs#telegram-desktop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[signal-desktop](/man/signal-desktop)(1), [discord](/man/discord)(1)
