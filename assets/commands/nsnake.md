# TAGLINE

基于 ncurses 在终端中运行的经典贪吃蛇游戏

# TLDR

**开始**贪吃蛇游戏

```nsnake```

**操控**贪吃蛇移动

```Arrow keys (Up/Down/Left/Right)```

**暂停/继续**游戏

```p```

**退出**游戏

```q```

游戏中显示**帮助**

```h```

# SYNOPSIS

**nsnake** [_options_]

# PARAMETERS

**-h, --help**
> 显示帮助信息

**-v, --version**
> 显示版本信息

# PREVIEW

```
 . . . . . . . . .
 . . ####o . . . .
 . . . . . . . X .
 . . . . . . . . .
```

# DESCRIPTION

**nsnake** 是一款基于 ncurses 在终端中运行的经典贪吃蛇游戏。控制蛇吃食物并不断变长，同时避免撞到墙壁和蛇自身的身体。

游戏内控制包括方向键移动、**p** 暂停、**q** 退出，以及 **h** 查看帮助。随着蛇变长，游戏速度会加快，难度也随之提升。

游戏支持通过游戏内菜单配置速度、边框和显示选项等设置。

# CAVEATS

需要支持 ncurses 的终端。终端大小会影响可玩区域。游戏状态不会在会话之间保存。

# INSTALL

```dnf: sudo dnf install nsnake```

```zypper: sudo zypper install nsnake```

```brew: brew install nsnake```

```nix: nix profile install nixpkgs#nsnake```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sl](/man/sl)(1), [cmatrix](/man/cmatrix)(1), [bastet](/man/bastet)(6)
