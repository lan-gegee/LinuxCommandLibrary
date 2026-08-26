# TAGLINE

终端版太空侵略者游戏

# TLDR

**开始游戏**

```ninvaders```

**设置难度等级**

```ninvaders -l [5]```

**显示版本**

```ninvaders -v```

# SYNOPSIS

**ninvaders** [_options_]

# PARAMETERS

**-l** _LEVEL_
> 起始难度等级。

**-v**
> 显示版本。

**--help**
> 显示帮助信息。

# PREVIEW

```
 /\ /\ /\ /\ /\
 <> <> <> <> <>
 {} {} {} {} {}

      /A\
```

# DESCRIPTION

**ninvaders** 是终端上的太空侵略者（Space Invaders）游戏，在终端中重现经典街机玩法。

该工具使用 ncurses 进行显示，是一款由键盘控制的射击游戏。

# CAVEATS

终端游戏。基于 ncurses。操作简单。

# HISTORY

ninvaders 把 **Space Invaders** 这款 1978 年的经典街机游戏搬到了终端上。

# INSTALL

```zypper: sudo zypper install ninvaders```

```brew: brew install ninvaders```

```nix: nix profile install nixpkgs#ninvaders```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[moon-buggy](/man/moon-buggy)(1), [bastet](/man/bastet)(1), [netris](/man/netris)(1)
