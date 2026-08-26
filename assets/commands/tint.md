# TAGLINE

终端版俄罗斯方块克隆

# TLDR

**开始游戏**

```tint```

**从指定关卡开始**

```tint -l [5]```

**显示高分榜**

```tint -s```

**显示版本**

```tint -v```

# SYNOPSIS

**tint** [_options_]

# PARAMETERS

**-l** _level_
> 从指定关卡开始（1-9）。

**-s**
> 显示高分表。

**-n**
> 禁用颜色。

**-d**
> 在方块内部绘制点。

**-h**
> 显示帮助。

**-v**
> 显示版本。

# CONTROLS

**j**：向左移动方块。

**l**：向右移动方块。

**k**：顺时针旋转方块。

**Space**：瞬间下落方块。

**p**：暂停游戏。

**q**：退出游戏。

# DESCRIPTION

**tint**（TINT Is Not Tetris）是一款使用 ncurses 的经典俄罗斯方块终端克隆。它的目标是尽可能忠实地重现原版玩法，同时运行在文本终端中。

游戏有九个难度等级，等级越高方块下落速度越快。它包含本地保存的高分系统，可记录玩家姓名。统计功能会跟踪游戏中每种四格骨牌出现的次数。

与一些俄罗斯方块变体不同，tint 不显示下一块方块的预览，以保持对原版游戏设计的忠实。

# CAVEATS

需要 ncurses 库。高分保存在本地且不会共享。没有下一块预览功能。终端必须支持所需的显示尺寸。

# HISTORY

**tint** 是为忠实重现 Alexey Pajitnov 的原版俄罗斯方块而开发的终端版本。其递归缩写名称（TINT Is Not Tetris）既致敬了 GNU 的命名传统，也顾及了商标方面的考虑。它成为精简 Linux 系统和服务器上流行的俄罗斯方块选择。

# INSTALL

```zypper: sudo zypper install tint```

```nix: nix profile install nixpkgs#tint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tetrinet](/man/tetrinet)(1), [bastet](/man/bastet)(1), [vitetris](/man/vitetris)(1), [moon-buggy](/man/moon-buggy)(1)
