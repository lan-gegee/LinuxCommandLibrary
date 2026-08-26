# TAGLINE

GNOME 数独益智游戏

# TLDR

**启动 GNOME Sudoku**

```gnome-sudoku```

# SYNOPSIS

**gnome-sudoku** [_options_]

# PARAMETERS

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**GNOME Sudoku** 是一款益智游戏，玩家需要在 9x9 的网格中填入数字，使每行、每列和每个 3x3 宫都恰好包含数字 1-9 各一次。

游戏可以生成各种难度的谜题，并提供提示、笔记（铅笔标记）、错误高亮等功能。它会自动保存游戏进度。

# FEATURES

- 多个难度级别
- 铅笔标记笔记
- 提示系统
- 错误高亮
- 游戏计时器
- 打印谜题

# CAVEATS

需要 GNOME 库。即使在同一难度级别内，生成的谜题难度也可能有所差异。

# HISTORY

数独在日本流行开来后，于 **21 世纪初**成为风靡全球的益智游戏。GNOME Sudoku 属于 GNOME Games 游戏合集，提供了简洁现代的实现。

# INSTALL

```dnf: sudo dnf install gnome-sudoku```

```pacman: sudo pacman -S gnome-sudoku```

```apk: sudo apk add gnome-sudoku```

```zypper: sudo zypper install gnome-sudoku```

```nix: nix profile install nixpkgs#gnome-sudoku```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnome-mines](/man/gnome-mines)(1)
