# TAGLINE

用于纠正拼写错误的蒸汽火车动画

# TLDR

**显示蒸汽火车**动画

```sl```

**显示一列更小的火车**

```sl -l```

**让火车飞起来**

```sl -F```

**显示事故场景**（有人呼救）

```sl -a```

**显示 C51 火车**而非 D51

```sl -c```

**允许用 Ctrl+C 中断**

```sl -e```

**组合选项**：会出事故的飞行小火车

```sl -alF```

# SYNOPSIS

**sl** [**-alFce**]

# PARAMETERS

**-a**
> 发生事故；出现呼救的人

**-l**
> 显示更小（little）的火车

**-F**
> 火车飞过屏幕

**-c**
> 显示 C51 火车而非默认的 D51

**-e**
> 允许用 Ctrl+C 中断；通常必须等动画结束

# DESCRIPTION

**sl**（Steam Locomotive）在终端中显示一列横穿屏幕的 ASCII 艺术蒸汽火车动画。它是对误把 **ls**（列出目录内容）敲成 **sl** 的用户的一种幽默惩罚。

执行后，一列精细的 ASCII 火车动画会从右向左驶过屏幕。默认情况下程序会忽略 Ctrl+C，迫使用户看完整列火车驶过——这是提醒你打字要更仔细的温和方式。

默认的火车是 **D51**（一款日本蒸汽机车）。**-c** 选项显示替代车型 **C51**。各选项可以组合，实现诸如载着遇险乘客的飞行迷你火车之类的效果。

# CAVEATS

默认忽略 Ctrl+C，你必须等待动画播完。使用 **-e** 可提前终止。在尺寸非常小的终端中，动画可能无法正常显示。

# HISTORY

**sl** 由 **Toyoda Masashi** 于 **1993 年**在东京大学创建。它被设计成一个玩笑程序，用来遏制把 sl 误敲成 ls 这一常见笔误。该程序已成为广受喜爱的 Unix 幽默作品，收录于多数 Linux 发行版的软件仓库。

# INSTALL

```dnf: sudo dnf install sl```

```pacman: sudo pacman -S sl```

```apk: sudo apk add sl```

```zypper: sudo zypper install sl```

```brew: brew install sl```

```nix: nix profile install nixpkgs#sl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ls](/man/ls)(1), [cowsay](/man/cowsay)(1), [fortune](/man/fortune)(1), [figlet](/man/figlet)(1)
