# TAGLINE

玩家在迷宫中互相追杀的多人终端游戏

# TLDR

**启动 hunt 游戏**

```hunt```

**连接到服务器**

```hunt -h [hostname]```

**使用指定的名字**

```hunt -n [playername]```

**连接到指定端口**

```hunt -p [port]```

# SYNOPSIS

**hunt** [_options_]

# PARAMETERS

**-h** _HOST_
> 服务器主机名。

**-n** _NAME_
> 玩家名字。

**-p** _PORT_
> 服务器端口。

**-t** _TEAM_
> 队伍编号。

**-c**
> 自动连接。

**--help**
> 显示帮助信息。

# PREVIEW

```
 ######  ######
 #    #  # @  #
 # #  ####    #
 #        # X #
 ##############
```

# DESCRIPTION

**hunt** 是一款多人终端游戏，玩家在迷宫中互相追杀。玩家在基于文本的战斗中射击和闪避。

游戏会连接到 huntd 服务器，多名玩家在其中竞技。游戏包含墙壁、炸弹和迷宫导航等元素。

# CAVEATS

需要 huntd 服务器。属于 BSD games 的一部分。采用基于终端的图形。

# HISTORY

hunt 是上世纪 80 年代的经典 **BSD** 网络游戏，在终端中提供多人对战体验。

# INSTALL

```apt: sudo apt install hunt```

```dnf: sudo dnf install hunt```

```nix: nix profile install nixpkgs#hunt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[huntd](/man/huntd)(6), [nethack](/man/nethack)(6), [bsdgames](/man/bsdgames)(6)
