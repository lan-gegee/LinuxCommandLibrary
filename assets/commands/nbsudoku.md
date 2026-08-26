# TAGLINE

终端数独游戏

# TLDR

**玩数独**

```nbsudoku```

**使用更大的棋盘游玩**

```nbsudoku -s [4]```

**启用快速生成谜题**

```nbsudoku -f```

# SYNOPSIS

**nbsudoku** [_options_]

# PARAMETERS

**-s** _SIZE_
> 设置谜题尺寸。网格变为 (size*size) x (size*size)。默认为 3（标准 9x9 网格）；2 为 4x4，4 为 16x16。

**-f**
> 快速（有缺陷）生成模式。生成的谜题可能有多个解，但能在合理时间内完成。尺寸大于 4 时自动启用。

**-h**
> 显示帮助信息。

# PREVIEW

```
 5 3 . | . 7 . | . . .
 6 . . | 1 9 5 | . . .
 . 9 8 | . . . | . 6 .
```

# DESCRIPTION

**nbsudoku** 是 **nbsdgames** 游戏合集中的终端数独游戏。填满网格，使每一行、每一列和每个宫都恰好包含所有数字各一次。

操作方式：方向键或 hjkl 移动光标，数字键输入数字，q 退出。也支持鼠标输入。

# CAVEATS

需要支持 ncurses 的终端。属于 nbsdgames 合集。大棋盘尺寸（超过 4）必须使用快速生成模式。

# HISTORY

**nbsudoku** 属于 **abakh** 创建的 **nbsdgames**——一个包含 18 款文字终端游戏的软件包。数独在 **2004 年**登上《泰晤士报》后风靡全球。

# SEE ALSO

[nudoku](/man/nudoku)(1), [nbmines](/man/nbmines)(1), [nbfifteen](/man/nbfifteen)(1)
