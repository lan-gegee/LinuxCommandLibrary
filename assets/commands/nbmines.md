# TAGLINE

来自 nbsdgames 合集的终端扫雷游戏

# TLDR

**开始默认对局**

```nbmines```

**自定义棋盘尺寸**

```nbmines -c [10] -r [10]```

**设置地雷数量**

```nbmines -m [15]```

**以简单模式游玩**

```nbmines -e```

# SYNOPSIS

**nbmines** [_options_]

# PARAMETERS

**-c** _COLS_
> 列数。

**-r** _ROWS_
> 行数。

**-m** _MINES_
> 地雷数量。

**-e**
> 简单模式。

**--help**
> 显示帮助信息。

# PREVIEW

```
 .  .  1  .  .  .  .
 .  1  2  1  .  .  .
 .  1  #  .  .  1  1
 .  1  1  1  .  1  F
```

# DESCRIPTION

**nbmines** 是来自 **nbsdgames** 软件包（文字游戏合集）的终端扫雷游戏。目标是翻开所有不含地雷的格子，同时避开有雷的格子。

游戏使用 ncurses 界面，支持键盘和鼠标。用方向键或 hjkl 移动，ENTER 翻开格子，SPACE 标记/取消标记格子。按 q 退出。

# CAVEATS

需要支持 ncurses 的终端。属于 nbsdgames 合集。棋盘尺寸受终端大小限制。

# HISTORY

nbmines 属于 **nbsdgames** 软件包——由 abakh 创建、受经典游戏启发的 18 款文字游戏合集。扫雷本身因 **1992 年**被收录进 Microsoft Windows 3.1 而广为流行。

# SEE ALSO

[nbfifteen](/man/nbfifteen)(1), [nbsos](/man/nbsos)(1), [gnome-mines](/man/gnome-mines)(1)
