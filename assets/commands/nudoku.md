# TAGLINE

基于 ncurses 的数独游戏

# TLDR

**以默认难度开始新游戏**

```nudoku```

**以指定难度开始游戏**

```nudoku -d [easy|normal|hard]```

**以黑白模式开始游戏**

```nudoku -c```

**加载用户提供的数据流格式谜题**（空格用点表示）

```nudoku -s [..5.3..8.1...6..2.4....7...]```

**将谜题导出为 PDF 文件**

```nudoku -p [output.pdf]```

**将多个谜题导出到一个 PDF 文件**

```nudoku -p [output.pdf] -n [10]```

# SYNOPSIS

**nudoku** [_options_]

# PARAMETERS

**-d** _DIFFICULTY_
> 设置难度：easy、normal 或 hard。默认为 normal。

**-c**
> 无颜色模式（黑白）。适用于不支持颜色的终端。

**-s** _STREAM_
> 提供用户自定义的数据流格式谜题。空格用点（.）表示，已填格用数字表示，全部写在同一行（81 个字符）。

**-p** _FILE_
> 将谜题输出为 PDF 文件。

**-n** _COUNT_
> 放入 PDF 的谜题数量。仅与 **-p** 配合使用。

**-i** _FILE_
> 将单个谜题输出为 PNG 图片文件。

**-h**
> 显示帮助信息。

**-v**
> 显示版本信息。

# PREVIEW

```
 5 3 . | . 7 . | . . .
 6 . . | 1 9 5 | . . .
 . 9 8 | . . . | . 6 .
-------+-------+------
 8 . . | . 6 . | . . 3
 4 . . | 8 . 3 | . . 1
 7 . . | . 2 . | . . 6
```

# DESCRIPTION

**nudoku** 是一个使用 ncurses 进行显示的终端数独游戏。它可以生成三种难度级别的谜题，并提供键盘驱动的解题界面。

方向键用于在九宫格中移动，数字键用于填充格子。游戏还可以把谜题导出为 PDF 或 PNG 文件以便打印或分享。

# CAVEATS

需要 ncurses。终端必须至少支持 80 列。PDF 和 PNG 导出需要在编译期启用相应功能。

# HISTORY

**nudoku** 由 **Michael Jubalh** 创建，是一款轻量的终端数独游戏。该项目托管于 GitHub，并已为大多数 Linux 发行版打包。

# INSTALL

```dnf: sudo dnf install nudoku```

```zypper: sudo zypper install nudoku```

```brew: brew install nudoku```

```nix: nix profile install nixpkgs#nudoku```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[moon-buggy](/man/moon-buggy)(1), [nsnake](/man/nsnake)(1), [bastet](/man/bastet)(1), [tetris-bsd](/man/tetris-bsd)(1)
