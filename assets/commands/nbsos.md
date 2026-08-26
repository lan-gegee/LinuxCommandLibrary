# TAGLINE

终端 SOS 棋盘游戏

# TLDR

**玩 SOS 游戏**

```nbsos```

**以指定 AI 难度与电脑对弈**

```nbsos -p [5]```

**双人对弈**（双方均为人类玩家）

```nbsos -1 h -2 h```

**设置棋盘尺寸**

```nbsos -l [10] -w [10]```

# SYNOPSIS

**nbsos** [_options_]

# PARAMETERS

**-1** _type_
> 设置玩家 1 类型：h（人类）或 c（电脑）。

**-2** _type_
> 设置玩家 2 类型：h（人类）或 c（电脑）。

**-p** _depth_
> 设置 AI 难度等级（1-127）。

**-l** _number_
> 设置棋盘长度（0-1000）。

**-w** _number_
> 设置棋盘宽度（0-1000）。

**-n**
> 游戏结束后不询问是否重玩。

**-h**
> 显示帮助信息。

# PREVIEW

```
 S  O  S  .  .
 .  .  S  .  .
 .  .  O  .  .
 .  .  S  .  .
```

# DESCRIPTION

**nbsos** 是 **nbsdgames** 游戏合集中的终端 SOS 棋盘游戏。双方轮流在网格上放置字母 S 或 O。组成直线相连的 S-O-S 序列得一分；得分最高者获胜。

操作方式：方向键或 hjkl 移动光标，S/O 放置字母，q 退出。也支持鼠标输入。

# CAVEATS

需要支持 curses 的终端。棋盘尺寸可以调整，但非常大的棋盘可能显示不佳。属于 nbsdgames 合集。

# HISTORY

**nbsos** 属于 **abakh** 创建的 **nbsdgames**——一个包含 18 款文字终端游戏的软件包。它实现的是经典的纸笔游戏 SOS。

# SEE ALSO

[nbmines](/man/nbmines)(1), [nbfifteen](/man/nbfifteen)(1), [nbmemoblocks](/man/nbmemoblocks)(1)
