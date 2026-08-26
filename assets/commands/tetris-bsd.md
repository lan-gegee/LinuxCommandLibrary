# TAGLINE

面向终端的 BSD 俄罗斯方块游戏

# TLDR

**开始一局** tetris 游戏

```tetris-bsd```

**从指定等级开始**

```tetris-bsd -l [level]```

**启用下一个形状的预览**

```tetris-bsd -p```

**自定义控制键**（左移、旋转、右移、下落、暂停、退出）

```tetris-bsd -k "[jkl pq]"```

**指定随机种子**以获得可复现的游戏

```tetris-bsd -s [seed]```

# SYNOPSIS

**tetris-bsd** [**-ps**] [**-k** _keys_] [**-l** _level_] [**-s** _seed_]

# PARAMETERS

**-l** _level_
> 设置起始等级（默认：2）。等级越高方块下落越快（N 级时每秒下落 N 次）。

**-k** _keys_
> 自定义控制键。按顺序提供六个字符：左移、旋转、右移、下落、暂停、退出。

**-p**
> 启用下一个将出现形状的预览。

**-s** _seed_
> 设置随机种子，使方块序列可复现。

# PREVIEW

```
    []
    [][]
      []

  [][][]
    [][]
  [][][][]
  [][][][]
```

# DESCRIPTION

**tetris-bsd** 是 BSD 游戏合集中的终端版俄罗斯方块实现。游戏中下落的四格方块必须被排列成完整的水平行。完成的行会消失；当方块堆到顶部时游戏结束。

默认控制采用 vi 风格按键：**j**（左移）、**k**（旋转）、**l**（右移）、**space**（下落）、**p**（暂停）、**q**（退出）。下落速度与等级数成正比。

计分规则为每放置一个方块得一分，每下落一格得一分。最终得分乘以当前等级。高分记录保存在 **/var/games/bsdgames/tetris-bsd.scores** 中。

# CAVEATS

游戏必须在兼容 CRT 的终端上玩。习惯方向键的用户可能对 vi 风格的默认控制键感到陌生。

# HISTORY

最初的俄罗斯方块由 **Alexey Pajitnov** 于 **1984** 年在前苏联创造。这个 BSD 实现改编自 **1989** 年国际 C 语言混乱代码大赛（IOCCC）获奖作品，作者为 **Chris Torek** 和 **Darren F. Provine**。预览模式由 **Hubert Feyrer** 于 **1999** 年加入。该游戏是许多类 Unix 发行版所附带的 **bsdgames** 软件包的一部分。

# INSTALL

```apk: sudo apk add micro-tetris```

```nix: nix profile install nixpkgs#tetris```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tetris](/man/tetris)(6), [bcd](/man/bcd)(6), [worm](/man/worm)(6)
