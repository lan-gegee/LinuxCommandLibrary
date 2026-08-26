# TAGLINE

总是给你最糟糕方块的俄罗斯方块克隆

# TLDR

**启动** Bastet 俄罗斯方块游戏

```bastet```

# SYNOPSIS

**bastet**

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

**bastet**（Bastard Tetris）是一个别具一格的俄罗斯方块克隆——它会针对你当前的局势挑选最糟糕的方块。游戏会分析你的棋盘，故意给你最难放置的方块，使其比标准俄罗斯方块更具挑战性。

这款游戏以幽默而艰难的方式重新演绎了经典益智游戏。

# FEATURES

- "对抗性"方块选择算法
- 经典俄罗斯方块玩法
- 高分记录
- 基于终端的界面
- ncurses 图形

# CONTROLS

- **Left/Right arrows** - 移动方块
- **Up arrow** - 旋转
- **Down arrow** - 软降
- **Space** - 硬降
- **p** - 暂停
- **q** - 退出

# CAVEATS

比普通俄罗斯方块难得多。需要支持颜色的终端。包含于某些游戏软件包中。其设计本身就容易让人沮丧。

# HISTORY

**bastet** 由 Federico Poloni 于 **2005** 年前后创建，它使用一种专门挑选最坏情况方块的算法，是刻意设计的高难度俄罗斯方块变体。

# INSTALL

```dnf: sudo dnf install bastet```

```aur: yay -S bastet```

```brew: brew install bastet```

```nix: nix profile install nixpkgs#bastet```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[vitetris](/man/vitetris)(6), [tetris](/man/tetris)(6), [nethack](/man/nethack)(6)
