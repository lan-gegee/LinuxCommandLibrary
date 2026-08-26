# TAGLINE

GNOME 扫雷益智游戏

# TLDR

**启动 GNOME Mines**

```gnome-mines```

# SYNOPSIS

**gnome-mines** [_options_]

# PARAMETERS

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**GNOME Mines** 是经典扫雷益智游戏的 GNOME 实现。游戏目标是借助标示相邻地雷数量的数字提示清除雷区，且不触任何地雷。

游戏提供从初级到专家的多个难度级别以及自定义棋盘尺寸。它还记录高分和游戏统计数据。

# GAMEPLAY

- 左键点击翻开方格
- 右键点击标记疑似地雷
- 数字表示相邻地雷的数量
- 清除所有非地雷方格即获胜

# CAVEATS

需要 GNOME 库。游戏状态不在会话之间保存。自定义尺寸受屏幕空间限制。

# HISTORY

扫雷起源于 **20 世纪 60 年代**，后因 Microsoft Windows 而广为人知。GNOME Mines 属于 gnome-games 游戏合集，遵循 GNOME 设计规范提供了 Linux 原生版本。

# INSTALL

```dnf: sudo dnf install gnome-mines```

```pacman: sudo pacman -S gnome-mines```

```apk: sudo apk add gnome-mines```

```zypper: sudo zypper install gnome-mines```

```nix: nix profile install nixpkgs#gnome-mines```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnome-sudoku](/man/gnome-sudoku)(1)
