# TAGLINE

轻量级终端会话管理器

# TLDR

用一条命令**创建**新会话

```abduco -c [session_name] [command]```

**接入**已有会话

```abduco -a [session_name]```

**列出**所有活动会话

```abduco```

创建会话并立即**脱离**

```abduco -n [session_name] [command]```

# SYNOPSIS

**abduco** [_-e detach-key_] [_-r_] [_-f_] [_-l_] _-c|-A|-a_ _session_ [_command_ [_args_]]

# DESCRIPTION

**abduco**（拉丁语"带走、移走"之意）是一个轻量级的会话管理工具，提供终端会话的脱离与重新接入。它让进程在你断开终端后继续运行，稍后还能重新接上。

与 **screen** 或 **tmux** 不同，abduco 只专注会话管理，没有窗口复用或分屏面板。这种极简设计造就了一个小巧、快速且可靠的工具。若需要多路复用功能，它与 **dvtm** 是很好的搭配。

# PARAMETERS

**-c** _session_
> 以给定名称创建新会话

**-a** _session_
> 接入已有会话（若已被他人接入则为只读）

**-A** _session_
> 接入已有会话，不存在则创建

**-n** _session_
> 创建一个新的已脱离会话

**-e** _key_
> 设置脱离键（默认：Ctrl+\\）

**-r**
> 接入时启用只读模式

**-f**
> 即使会话已存在也强制创建

**-l**
> 低带宽模式（减少屏幕刷新）

# CAVEATS

**abduco** 只负责会话管理，不提供窗口分割或复用功能。需要这些功能时请与 **dvtm** 组合使用。会话保存在 /tmp 或 $ABDUCO_SOCKET_DIR 中，除非另行配置，否则系统重启后会丢失。

# HISTORY

**abduco** 由 Marc Andre Tanner 编写，于 **2014 年**首次发布。它的设计定位是 GNU Screen 和 tmux 的极简替代品，遵循"做好一件事"的 Unix 哲学。该工具常与同一作者的 **dvtm**（dynamic virtual terminal manager）搭配使用。

# INSTALL

```dnf: sudo dnf install abduco```

```pacman: sudo pacman -S abduco```

```apk: sudo apk add abduco```

```brew: brew install abduco```

```nix: nix profile install nixpkgs#abduco```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [screen](/man/screen)(1), [dvtm](/man/dvtm)(1), [dtach](/man/dtach)(1)
