# TAGLINE

终端数字推盘游戏（15 Puzzle）

# TLDR

**玩数字推盘游戏**

```nbfifteen```

**对局结束后不询问重玩**

```nbfifteen -n```

**使用 5x5 棋盘游玩**

```nbfifteen -s 5```

# SYNOPSIS

**nbfifteen** [_options_]

# PARAMETERS

**-s** _SIZE_
> 设置棋盘尺寸（3 到 7）。默认为 4（标准 15 数字推盘）。

**-n**
> 完成拼图后不询问是否重玩。

**-h**
> 显示帮助信息。

# PREVIEW

```
+--+--+--+--+
| 1| 2| 3| 4|
| 5| 6| 7| 8|
| 9|10|11|12|
|13|14|15|  |
+--+--+--+--+
```

# DESCRIPTION

**nbfifteen** 是一款终端数字推盘游戏。滑动数字块，将它们按顺序排列。

该工具是经典的滑块拼图。使用 ncurses 进行显示。

# CAVEATS

属于 nbsdgames 软件包。终端游戏。用方向键移动。

# HISTORY

nbfifteen 实现了经典的**15 Puzzle**（数字推盘），由 Noyes Palmer Chapman 于 1874 年前后发明。

# SEE ALSO

[nbmines](/man/nbmines)(1), [nbsos](/man/nbsos)(1), [puzzle](/man/puzzle)(1)
