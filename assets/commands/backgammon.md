# TAGLINE

文字版西洋双陆棋盘游戏

# TLDR

**开始**西洋双陆棋游戏

```backgammon```

以**红方**玩家开始（跳过说明）

```backgammon -r```

开始**双人**游戏

```backgammon -b```

**恢复**已保存的游戏

```backgammon -s [savefile]```

# SYNOPSIS

**backgammon** [_-_] [_-nrwb_] [_-pr_] [_-pw_] [_-pb_] [_-t term_] [_-s file_]

# PREVIEW

```
 13 14 15 16 17 18
  O        X  X  O
  O           X  O
                 O
```

# DESCRIPTION

**backgammon** 是 BSD games 合集中经典的文字版西洋双陆棋游戏。它提供基于文本的界面，可以与计算机或其他玩家对弈西洋双陆棋。玩家根据掷骰结果移动棋子，力争在对手之前将所有棋子移出棋盘。

配套程序 **teachgammon** 用于讲授西洋双陆棋的规则与策略。

# PARAMETERS

**-n**
> 不询问规则或说明

**-r**
> 玩家为红方（隐含 -n）

**-w**
> 玩家为白方（隐含 -n）

**-b**
> 双人模式，红白双方（隐含 -n）

**-pr**
> 在红方回合前打印棋盘

**-pw**
> 在白方回合前打印棋盘

**-pb**
> 在双方每个回合前都打印棋盘

**-t** _term_
> 指定终端类型

**-s** _file_
> 从文件恢复已保存的游戏

# CONTROLS

**space** / **return**
> 掷骰子

**d**
> 加倍

**p**
> 打印棋盘

**q**
> 退出游戏

**s**
> 保存游戏

走法用"起点-终点"表示（如 3-5）。

# CAVEATS

仅有文字界面。在多数系统上属于 bsd-games 软件包的一部分。

# HISTORY

**backgammon** 由 **Alan Char** 于 **1980** 年在加州大学伯克利分校编写，此后一直是 BSD games 发行版的一部分。

# SEE ALSO

[adventure](/man/adventure)(6), [nethack-console](/man/nethack-console)(6)
