# TAGLINE

终端西洋跳棋游戏

# TLDR

**与电脑对弈跳棋**

```nbcheckers```

**设置 AI 难度等级**

```nbcheckers -p [5]```

**双人对弈**

```nbcheckers -1 h -2 h```

**对局结束后不询问重玩**

```nbcheckers -n```

# SYNOPSIS

**nbcheckers** [_options_]

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
 . x . x . x . x
 x . x . x . x .
 . . . . . . . .
 o . o . o . o .
 . o . o . o . o
```

# DESCRIPTION

**nbcheckers** 是 **nbsdgames** 游戏合集中的终端西洋跳棋游戏。双方轮流沿对角线移动棋子，跳过对方棋子即可将其吃掉。到达棋盘另一端的棋子升为王，可以向后移动。

操作方式：方向键或 hjkl 移动光标，ENTER 选择并移动棋子，q 退出。也支持鼠标输入。

# CAVEATS

需要支持 ncurses 的终端。属于 nbsdgames 合集。

# HISTORY

**nbcheckers** 属于 **abakh** 创建的 **nbsdgames**——一个包含 18 款文字终端游戏的软件包。西洋跳棋是最古老的棋盘游戏之一，其起源可追溯至约**公元前 3000 年**。

# SEE ALSO

[nbreversi](/man/nbreversi)(1), [nbsos](/man/nbsos)(1), [gnuchess](/man/gnuchess)(1)
