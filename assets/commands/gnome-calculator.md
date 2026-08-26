# TAGLINE

GNOME 桌面计算器应用程序

# TLDR

启动 **GNOME 计算器图形界面**

```gnome-calculator```

不启动图形界面直接**求解**方程

```gnome-calculator --solve "[2^5 * 2 + 5]"```

以**编程模式**启动

```gnome-calculator --mode programming```

以**财务模式**启动

```gnome-calculator --mode financial```

显示**版本**

```gnome-calculator --version```

# SYNOPSIS

**gnome-calculator** [_options_]

# PARAMETERS

**-s**, **--solve** _EQUATION_
> 求解方程并打印结果，不启动图形界面。

**-e** _EQUATION_
> 等同于 --solve。

**-m**, **--mode** _MODE_
> 以指定模式启动：basic、advanced、financial、programming。

**--version**
> 显示版本信息。

**--help**
> 显示帮助消息。

# DESCRIPTION

**gnome-calculator** 是 GNOME 桌面环境的官方计算器应用。它提供多种模式：Basic 用于简单算术运算，Advanced 用于科学函数和三角函数，Financial 用于利息计算和货币换算，Programming 用于位运算和进制转换。

该计算器支持变量、单位换算和复杂数学表达式。**--solve** 选项让它可以充当命令行计算器，无需打开图形窗口。

# CAVEATS

需要 GTK 和 GLib 库。部分高级功能可能需要额外的库。货币换算需要联网获取最新汇率。

# HISTORY

gnome-calculator 由早期的 gcalctool 演化而来，后者自 GNOME 早期版本起就是其组成部分。现代的 gnome-calculator 用 Vala 重写，随 GNOME 3.0 于 **2011** 年推出，提供了更简洁的界面和更完善的功能。

# INSTALL

```apt: sudo apt install gnome-calculator```

```dnf: sudo dnf install gnome-calculator```

```pacman: sudo pacman -S gnome-calculator```

```apk: sudo apk add gnome-calculator```

```zypper: sudo zypper install gnome-calculator```

```nix: nix profile install nixpkgs#gnome-calculator```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bc](/man/bc)(1), [dc](/man/dc)(1), [qalc](/man/qalc)(1), [expr](/man/expr)(1)
