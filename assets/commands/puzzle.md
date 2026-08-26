# TAGLINE

经典逻辑游戏合集

# TLDR

**启动拼图合集**启动器

```puzzle```

**按名称玩指定谜题**

```puzzle [fifteen]```

**使用自定义游戏 ID 玩谜题**（预设大小/难度）

```puzzle [solo] --generate [3x3]```

# SYNOPSIS

**puzzle** [_name_]

# DESCRIPTION

**puzzle** 指各种拼图游戏合集，最常见的是 Simon Tatham's Portable Puzzle Collection。合集中的每个谜题都是一个独立的可执行文件。合集包括经典谜题，如数独、扫雷变体、滑块拼图和逻辑游戏。在许多系统上，各个二进制文件带有 **sgt-** 前缀（例如数独为 **sgt-solo**）。

# COMMON PUZZLES

```
blackbox    - Find hidden balls
bridges     - Connect islands
fifteen     - Sliding tile puzzle
galaxies    - Divide grid into galaxies
lightup     - Place lights
loopy       - Draw loops
mines       - Minesweeper
net         - Rotate tiles to connect
pattern     - Nonogram puzzle
pearl       - Draw masyu loop
singles     - Circle numbers
solo        - Sudoku
tents       - Place tents
towers      - Latin square with heights
undead      - Place monsters
unequal     - Futoshiki puzzle
```

# EXAMPLES

```bash
# Play the fifteen sliding tile puzzle
puzzle fifteen

# Play Sudoku (9x9 by default)
puzzle solo

# Play Minesweeper
puzzle mines

# On Debian/Ubuntu with sgt- prefix
sgt-solo
sgt-mines
```

# CAVEATS

具体的二进制文件名因发行版和软件包而异。在 Debian/Ubuntu 上，谜题以带 **sgt-** 前缀的独立二进制文件形式安装（例如 **sgt-solo**）。在 Arch Linux 上，软件包名为 **puzzles**，二进制文件没有前缀。在 macOS 上，该合集可通过 Homebrew 以 **puzzles** 安装。

# HISTORY

Simon Tatham's Portable Puzzle Collection 由 **Simon Tatham**（PuTTY 的作者）创建，提供跨平台的谜题游戏。

# SEE ALSO

[gnome-sudoku](/man/gnome-sudoku)(1), [gnome-mines](/man/gnome-mines)(1)
