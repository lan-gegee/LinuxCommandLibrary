# TAGLINE

终端黑白棋（Reversi/Othello）游戏

# TLDR

**与电脑对弈黑白棋**

```nbreversi```

**设置 AI 难度等级**

```nbreversi -p [5]```

**双人对弈**

```nbreversi -1 h -2 h```

**对局结束后不询问重玩**

```nbreversi -n```

# SYNOPSIS

**nbreversi** [_options_]

# PARAMETERS

**-1** _type_
> 设置玩家 1 类型：h（人类）或 c（电脑）。

**-2** _type_
> 设置玩家 2 类型：h（人类）或 c（电脑）。

**-p** _depth_
> 设置 AI 难度/搜索深度（1-127）。

**-n**
> 游戏结束后不询问是否重玩。

**-h**
> 显示帮助信息。

# PREVIEW

```
 . . . . . . . .
 . . . . . . . .
 . . . O X . . .
 . . . X O . . .
 . . . . . . . .
```

# DESCRIPTION

**nbreversi** 是 **nbsdgames** 游戏合集中的终端黑白棋（Reversi/Othello）游戏。双方轮流在棋盘上放置棋子。当落子使对方一枚或多枚棋子在一条直线上被夹住时，这些棋子会被翻转。当无法继续落子时，棋子最多的一方获胜。

操作方式：方向键或 hjkl 移动光标，ENTER 放置棋子，q 退出。也支持鼠标输入。

# CAVEATS

需要支持 ncurses 的终端。属于 nbsdgames 合集。

# HISTORY

**nbreversi** 属于 **abakh** 创建的 **nbsdgames**——一个包含 18 款文字终端游戏的软件包。Reversi 由 Lewis Waterman 于 **1883 年**发明，后来由长谷川五郎在 **1971 年**以 **Othello** 之名推广开来。

# SEE ALSO

[nbcheckers](/man/nbcheckers)(1), [nbsos](/man/nbsos)(1), [nbmines](/man/nbmines)(1)
