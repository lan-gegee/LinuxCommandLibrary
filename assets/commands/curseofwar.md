# TAGLINE

快节奏终端实时战略游戏

# TLDR

开始游戏

```curseofwar```

以指定难度开始

```curseofwar -d [5]```

指定电脑对手数量开始

```curseofwar -q [4]```

用指定的地图种子开始游戏

```curseofwar -r [12345]```

# SYNOPSIS

**curseofwar** [_options_]

# PARAMETERS

**-d** _NUM_
> 难度等级（1-9）。

**-q** _NUM_
> 电脑对手的数量。

**-r** _NUM_
> 地图生成的随机种子。

**-T** _NUM_
> 时间轴速度。

**-i**
> 启用不平等模式。

**-h**
> 显示帮助。

# PREVIEW

```
 ~~~~~~~~.....####
 ~~~~~...1....####
 ~~~....111...####
 ~~.....12....####
 ~......1.....####
```

# DESCRIPTION

**curseofwar** 是一款快节奏的动作类实时战略游戏，运行于终端。玩家在基于网格的地图上组建和指挥军队，通过引导人口流向敌方位置来占领领土。

操作方式：方向键移动光标，空格放置旗帜（引导部队移动），**r** 移除旗帜，**p** 暂停。游戏包含多种地形类型（平原、森林、山地、水域），会影响移动和战斗。

# CAVEATS

需要支持 ncurses 和颜色的终端。游戏实时进行，需要快速决策。

# HISTORY

**curseofwar** 是作为一款独特的终端 RTS 游戏而创作的，在保持领土控制与资源管理带来的策略深度的同时，简化了操作。

# INSTALL

```brew: brew install curseofwar```

```nix: nix profile install nixpkgs#curseofwar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nethack](/man/nethack)(6), [rogue](/man/rogue)(6)
