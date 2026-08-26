# TAGLINE

基于终端的俄罗斯方块游戏

# TLDR

**开始一局** tetris 游戏

```tetris```

**从指定等级开始**

```tetris -l [level]```

**在本地以双人模式开始**

```tetris 2p```

**在某端口上监听网络对战**

```tetris listen [port]```

**连接到网络对战**

```tetris connect [hostname]:[port]```

**设置终端宽度**

```tetris -w [80]```

**显示游戏选项的帮助**

```tetris -help game```

# SYNOPSIS

**tetris** [_options_] [_mode_]

# PARAMETERS

**-l** _level_
> 设置起始等级（影响下落速度）。

**-h** _height_
> 设置垃圾方块的初始高度。

**-w** _width_
> 设置终端宽度。

**2p**
> 开始本地双人游戏。

**listen** _port_
> 在指定端口监听传入的网络连接。

**connect** _host:port_
> 连接到远程玩家进行网络对战。

**-help**
> 打印帮助并退出。

**-help game**
> 列出游戏选项并退出。

**-help term**
> 列出终端选项并退出。

# DESCRIPTION

**vitetris**（通常安装为 **tetris**）是一款基于终端的俄罗斯方块克隆，玩法类似早期的任天堂俄罗斯方块。它支持单人、本地双人和网络多人模式。

游戏特色包括可自定义的控制键、可配置的外观，以及网络对战——双方玩家可以各自独立选择难度设置。它只需要 libc，没有额外的库依赖。

控制和外观可通过游戏内菜单或命令行选项自定义。高分记录保存在 **~/.vitetris** 中。

# CAVEATS

网络对战需要一名玩家在连接方可访问的端口上监听。防火墙和 NAT 可能需要配置端口转发。游戏不包含声音。

# HISTORY

vitetris 由 **Victor Geraldsson** 创建，于 **2007** 年首次发布。它的设计目标是成为一款轻量、可移植的终端俄罗斯方块实现。该游戏已被移植到多个平台，包括 Linux、BSD、Windows 和 DOS。加入网络对战支持是为了实现跨互联网的竞技多人游戏。

# INSTALL

```apk: sudo apk add micro-tetris```

```nix: nix profile install nixpkgs#tetris```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tetris-bsd](/man/tetris-bsd)(6), [bastet](/man/bastet)(6), [nudoku](/man/nudoku)(6)
