# TAGLINE

经典终端贪吃蛇游戏

# TLDR

**启动 worm 游戏**

```worm```

# SYNOPSIS

**worm**

# IN-GAME CONTROLS

**方向键**或 **h j k l**
> 移动蠕虫（左、下、上、右）

**q**
> 退出游戏

# PREVIEW

```
 . . . . . . . . .
 . . ooooo . . . .
 . . . . o . . 6 .
 . . . . o . . . .
 . . . . . . . . .
```

# DESCRIPTION

**worm** 是来自 BSD games 集合的经典终端贪吃蛇游戏。玩家控制一条不断变长的蠕虫在屏幕上移动，吃掉数字来变长并获得分数。

数字随机出现在屏幕上，蠕虫会按所吃数字的值增长。目标是吃到尽可能多的数字，同时不撞到墙壁或蠕虫自己的身体。随着蠕虫变长，速度会加快，游戏难度也逐渐提升。

游戏以简单的 ASCII 终端界面显示，可以在任何文本终端上玩。它正是诺基亚手机上流行的 "Snake" 游戏的最初灵感来源。

# CAVEATS

需要安装 **bsdgames** 软件包。终端必须支持光标定位。游戏速度可能因终端模拟器的性能而有所不同。

# HISTORY

Worm 是 **BSD games** 集合的一部分，这是一组经典文本游戏，最初随 BSD Unix 系统于 20 世纪七八十年代分发。这些游戏诞生于终端只有文本的 Unix 早期，后来成为 Unix 文化的标志性内容。贪吃蛇/蠕虫游戏的概念后来因诺基亚在 20 世纪 90 年代末手机上的实现而广为人知。

# INSTALL

```dnf: sudo dnf install bsd-games```

```pacman: sudo pacman -S bsd-games```

```apk: sudo apk add bsd-games```

```zypper: sudo zypper install bsd-games```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rogue](/man/rogue)(6), [nethack](/man/nethack)(6), [tetris-bsd](/man/tetris-bsd)(6)
