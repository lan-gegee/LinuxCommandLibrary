# TAGLINE

终端扫雷游戏

# TLDR

**开始一局默认游戏**

```freesweep```

**设置棋盘尺寸**

```freesweep --height [16] --width [30]```

**设置地雷数量**

```freesweep --mines [99]```

# SYNOPSIS

**freesweep** [_options_]

# PARAMETERS

**-h**, **--height** _N_
> 行数。

**-w**, **--width** _N_
> 列数。

**-m**, **--mines** _N_
> 地雷数量。

**-%**, **--percent** _N_
> 以棋盘格子的百分比设置地雷数。

**-f**, **--fast**
> 跳过交互式设置对话框。

**-i**, **--interactive**
> 强制显示交互式设置菜单。

**-a**, **--alt-charset**
> 切换用于渲染的备用字符集。

**-b**, **--show-best-times**
> 显示最佳成绩查看器。

**-s**, **--save-prefs**
> 保存当前命令行偏好设置。

**-H**, **--help**
> 显示帮助信息。

# PREVIEW

```
 .  .  1  .  .  .
 .  1  2  1  .  .
 .  1  #  .  .  1
 .  1  1  1  .  1
```

# DESCRIPTION

**freesweep** 是一个基于 curses 的终端扫雷游戏。玩家在网格上翻开格子，借助数字线索避开隐藏的地雷。标记可疑地雷并翻开所有安全格子即可获胜。

使用方向键移动，空格键翻格子，**f** 键标记地雷。按 **q** 退出。

# CAVEATS

需要 ncurses 支持。棋盘尺寸受终端大小限制。

# HISTORY

**freesweep** 是作为免费的终端扫雷克隆版编写的。扫雷因 **1992** 年被收入 **Microsoft Windows 3.1** 而广为流行。

# INSTALL

```nix: nix profile install nixpkgs#freesweep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nbmines](/man/nbmines)(6), [greed](/man/greed)(6)
