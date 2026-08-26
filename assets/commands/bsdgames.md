# TAGLINE

源自经典 BSD Unix 的文本游戏合集

# TLDR

游玩巨洞冒险文字游戏

```bsdgames-adventure```

玩俄罗斯方块克隆版

```tetris-bsd```

玩贪吃蛇

```snake```

玩 Worm（贪吃蛇变体）

```worm```

玩猜单词（hangman）

```hangman```

玩文字地牢探险

```hack```

与计算机对弈双陆棋

```backgammon```

**查询 "wtf" 缩写的含义**（缩写查询）

```wtf [lol]```

# INCLUDED GAMES

**bsdgames-adventure**
> 经典的 Colossal Cave 文字冒险游戏（从 **adventure** 更名以避免命名冲突）。

**tetris-bsd**
> 终端版俄罗斯方块克隆。

**snake** / **worm**
> 经典贪吃蛇游戏。

**hangman**
> 猜单词游戏。

**hack**
> NetHack 类 Rogue 游戏的前身。

**backgammon**
> 经典双陆棋。

**battlestar**
> 太空题材的文字冒险游戏。

**boggle**
> 找词拼图游戏。

**canfield** / **cribbage**
> 纸牌游戏。

**gomoku**
> 五子棋策略游戏。

**mille**
> 纸牌赛车游戏。

**phantasia**
> 多人奇幻游戏。

**quiz**
> 教育问答游戏。

**robots**
> 躲避机器人的策略游戏。

**sail**
> 帆船时代的海战游戏。

**trek**
> 星际迷航主题的策略游戏。

**wtf**
> 查询常见的网络缩写。

**wargames**
> 致敬 1983 年同名电影；启动时打印一句经典提示语。

**morse**, **caesar**, **rot13**, **primes**, **arithmetic**, **bcd**, **ppt**
> 随游戏一同提供的经典小型 Unix 工具。

# DESCRIPTION

**bsdgames** 是一组源自 BSD Unix 系统的经典文本游戏合集。这些游戏承载了数十年的 Unix 游戏历史，从最早的文字冒险到终端街机游戏，应有尽有。

该合集包含解谜、纸牌、棋盘、文字冒险和动作游戏——全部可以在终端中游玩。其中许多影响了后来的游戏：Adventure 开创了互动小说，Hack 催生了 NetHack 和类 Rogue 游戏，Worm 则是早期的贪吃蛇游戏。

这些游戏通常使用键盘操作和 ASCII 图形。大多数游戏可通过 **?** 或 man 页面访问内置帮助。配置和高分记录通常保存在用户主目录中。

# CAVEATS

部分游戏需要功能完备的终端模拟器。多人游戏在缺少额外配置时可能无法运行。具体收录的游戏因发行版打包而异。有些游戏在不同系统上名称不同（tetris 与 tetris-bsd）。

# HISTORY

BSD 游戏合集自 **1970** 年代起随 Unix 在 **UC Berkeley** 一同演进。许多游戏由学生和教职员贡献，成为 BSD Unix 发行版的一部分。该合集记录了终端作为主要交互界面时代早期计算机游戏的样貌。这些游戏早在"开源"一词出现之前就已开放源码，并由 Linux 社区保存至今。

# INSTALL

```nix: nix profile install nixpkgs#bsdgames```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nethack](/man/nethack)(6), [angband](/man/angband)(6), [cowsay](/man/cowsay)(1)
