# TAGLINE

支持联网对战的俄罗斯方块游戏

# TLDR

**单人玩俄罗斯方块**

```netris```

**主持网络游戏**

```netris -w```

**连接到主机**

```netris -c [host]```

**设置难度**

```netris -l [5]```

**本地双人对战**

```netris -2```

# SYNOPSIS

**netris** [_options_]

# PARAMETERS

**-w**
> 等待对手（服务器模式）。

**-c** _HOST_
> 连接到位于 _HOST_ 的对手（客户端模式）。

**-p** _PORT_
> 使用给定的 TCP 端口（默认 9284）。

**-l** _LEVEL_
> 起始等级（1–9）。

**-s** _SPEED_
> 初始下落速度（数值越大越快）。

**-k** _KEYS_
> 使用自定义按键字符串。

**-F**
> "公平"模式——双方获得相同的方块序列。

**-D**
> 不显示下一个方块预览。

**-i** _SECS_
> 设置游戏邀请请求的超时时间。

**-r** _PATH_
> 运行机器人对手的可执行文件。

**-S** _FILE_
> 将游戏会话保存到 _FILE_，或从 _FILE_ 重放。

**-2**
> 同一终端上的本地双人模式。

**-h**
> 显示帮助信息。

# DESCRIPTION

**netris** 是一款支持联网对战的俄罗斯方块游戏。可以单人游玩，也可以通过网络与他人对战。

该工具提供经典的俄罗斯方块玩法，支持一对一对抗。

# CAVEATS

终端游戏。联机对战需要额外配置。遵循经典俄罗斯方块规则。

# HISTORY

netris 的诞生是为了通过 TCP/IP 在互联网上提供**联网对战**的俄罗斯方块玩法。

# INSTALL

```brew: brew install netris```

```nix: nix profile install nixpkgs#netris```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bastet](/man/bastet)(1), [tetrinet](/man/tetrinet)(1), [bsdgames](/man/bsdgames)(1)
