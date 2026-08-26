# TAGLINE

终端俄罗斯方块克隆

# TLDR

**启动**游戏

```yetris```

# SYNOPSIS

**yetris** [_OPTIONS_]

# PARAMETERS

**Arrow Left/Right**
> 左右移动方块

**Arrow Down**
> 软降

**Space**
> 硬降

**x/z**
> 顺时针/逆时针旋转

**c**
> 暂存方块

**p**
> 暂停/继续

**q**
> 退出

# DESCRIPTION

**yetris** 是一个基于终端的俄罗斯方块克隆。它具有彩色 ncurses 图形、方块暂存、投影方块和计分功能。

游戏完全在终端中运行，支持键盘控制。

# CAVEATS

需要 ncurses 支持。终端大小会影响显示。不支持鼠标。

# INSTALL

```brew: brew install yetris```

```nix: nix profile install nixpkgs#yetris```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tetris](/man/tetris)(6), [bastet](/man/bastet)(6)
