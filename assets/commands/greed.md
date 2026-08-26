# TAGLINE

终端吃数字解谜游戏

# TLDR

**开始新游戏**

```greed```

**使用方向键移动**

```# Use arrow keys or hjkl to move```

# SYNOPSIS

**greed** [_options_]

# PARAMETERS

**-s**
> 显示高分列表。

**--help**
> 显示帮助信息。

# PREVIEW

```
 4 7 2 9 1 3 8 5
 5 1 8 3 6 2 7 4
 9 3 @ 7 4 8 1 6
 2 6 5 1 9 4 3 7
```

# DESCRIPTION

**greed** 是一款基于终端的解谜游戏，玩家在网格中移动并收集数字。朝任意方向移动会消耗掉相应数量的格子，目标是清除尽可能多的格子。

玩家使用方向键或 vi 风格的 hjkl 键移动。策略在于规划移动路线以避免被困住。当没有可用的移动时游戏结束。

# CAVEATS

纯文本界面。需要支持光标控制的终端。游戏进度不会保存。

# HISTORY

greed 最初由 **Matt Day** 创作，目前由 **Eric S. Raymond** 维护。它是一款独立的终端游戏，不属于 BSD 游戏合集。

# INSTALL

```nix: nix profile install nixpkgs#greed```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[worm](/man/worm)(1), [bsdgames](/man/bsdgames)(6)
