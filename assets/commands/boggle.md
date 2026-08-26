# TAGLINE

在字母方块网格上进行的找词游戏

# TLDR

**开始一局 Boggle 游戏**

```boggle```

**以自定义时限（秒）进行游戏**

```boggle -t [180]```

**设置最小单词长度**

```boggle -w [4]```

**以指定的棋盘布局开始**

```boggle [abcdefghijklmnop]```

**允许方块重复使用（但不能连续使用）**

```boggle +```

# SYNOPSIS

**boggle** [**-bd**] [**-s** _seed_] [**-t** _time_] [**-w** _length_] [**+**] [**++**] [_boardspec_]

# PREVIEW

```
 D  O  G  S
 R  A  T  E
 L  I  N  K
 P  U  M  P
```

# DESCRIPTION

**boggle** 是 BSD games 合集中的找词游戏。目标是在三分钟时限内，在 4x4 的字母方块网格中找出尽可能多的单词。

单词由水平、垂直或对角相邻的方块连接而成。每个方块在同一个单词中只能使用一次，且单词长度至少为 3 个字母。游戏会用词典检查找到的单词。

游戏过程中输入 **?** 可获取帮助。包含 'q' 的单词后面必须紧跟 'u'。

# PARAMETERS

**-b**
> 批处理模式。需要提供 boardspec。从 stdin 读取词典，并将匹配的单词输出到 stdout。

**-d**
> 启用调试输出。

**-s** _seed_
> 使用指定的随机种子而不是当前时间。

**-t** _time_
> 设置时间限制（秒）（默认：180）。

**-w** _length_
> 设置最小单词长度（默认：3）。

**+**
> 允许方块重复使用，但不能连续使用。

**++**
> 允许将方块视为与其自身相邻。

**boardspec**
> 以 16 个字母指定起始棋盘，按从左到右、从上到下的顺序排列。

# HISTORY

Boggle 是一款字词游戏，最初由 Parker Brothers 于 **1972 年**发行。BSD games 版本是其终端实现，收录在源自 Berkeley Software Distribution 的经典 Unix 游戏合集中。

# SEE ALSO

[hangman](/man/hangman)(6), [quiz](/man/quiz)(6)
