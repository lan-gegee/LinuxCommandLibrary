# TAGLINE

New BSD Games 合集的交互式菜单

# TLDR

**打开游戏选择菜单**

```nbsdgames```

**直接启动特定游戏**

```nbmines```

```nbsudoku```

```nbreversi```

# SYNOPSIS

**nbsdgames**

# PREVIEW

```
 New BSD Games
 1 Jewels  2 Sudoku
 3 Mines   4 Reversi
 > Select a game:
```

# DESCRIPTION

**nbsdgames** 为 New BSD Games 软件包启动一个 ncurses 菜单，该软件包是面向 Unix、DOS 和 Plan 9 的轻量级终端游戏合集。不带参数运行该命令会显示可用游戏的编号列表；选中某项即可启动对应游戏。

各款游戏也可以按名称直接调用。合集包含 **nbmines**、**nbsudoku**、**nbreversi**、**nbbattleship**、**nbcheckers**、**nbfifteen**、**nbpipes** 等益智和棋盘游戏。许多游戏接受命令行选项来调整棋盘大小、难度或尺寸。

需要 **ncurses**（在基于 Debian 的系统上：编译需 **libncurses5-dev**，运行时需 **libncurses**）。游戏以可移植的 C 语言编写，已为大多数主流 Linux 发行版、BSD 系统、Alpine 和 Homebrew 打包。

# PARAMETERS

软件包中的各款游戏接受各自的选项。常见模式包括用于列数和行数的 **-c** 和 **-r**、用于地雷数量的 **-m**，以及显示单个游戏用法的 **--help**。详见每个游戏的手册条目。

# CAVEATS

需要支持 ncurses 的终端。某些发行版软件包可能附带较旧的版本，游戏数量少于上游发布版。在 Windows 上，游戏可以通过 PDCurses 运行；也存在 Plan 9 和 DOS 移植版。

# HISTORY

New BSD Games 合集由 abakh 创建，作为经典 BSD 游戏的现代延续，加入了原创和改进的文字模式实现。6.0.2 版于 **2026 年 6 月**发布，包含 21 款游戏。软件包中的各款游戏在本命令库中单独收录。

# INSTALL

```zypper: sudo zypper install nbsdgames```

```brew: brew install nbsdgames```

```nix: nix profile install nixpkgs#nbsdgames```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nbmines](/man/nbmines)(1), [nbsudoku](/man/nbsudoku)(1), [nbreversi](/man/nbreversi)(1), [nbbattleship](/man/nbbattleship)(1), [bsdgames](/man/bsdgames)(6)

# RESOURCES

```[Source code](https://github.com/abakh/nbsdgames)```

<!-- verified: 2026-06-11 -->
