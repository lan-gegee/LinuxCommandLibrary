# TAGLINE

高精度科学计算器

# TLDR

**启动计算器**

```speedcrunch```

**打开会话文件**

```speedcrunch [session.sch]```

# SYNOPSIS

**speedcrunch** [_options_] [_file_]

# PARAMETERS

_file_
> 要打开的会话文件。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**SpeedCrunch** 是一款高精度桌面科学计算器，专为键盘操作设计。它计算输入行中键入的数学表达式，支持变量、自定义函数，以及涵盖三角、统计等领域的丰富内置函数库。

界面为表达式提供语法高亮、函数名自动补全，以及可滚动的计算历史记录。结果以任意精度计算，应用还支持常用度量单位之间的换算。

会话可保存到文件并从中恢复，保留计算历史和已定义的变量。SpeedCrunch 跨平台，基于 Qt 构建，可用于 Linux、Windows 和 macOS。

# FEATURES

- 键盘驱动
- 自动补全
- 单位换算
- 自定义函数
- 会话保存

# CAVEATS

GUI 应用程序。需要 Qt。需要桌面环境。

# HISTORY

**SpeedCrunch** 的设计目标是打造一款快速、高精度、以键盘操作为核心的科学计算器。

# INSTALL

```dnf: sudo dnf install speedcrunch```

```pacman: sudo pacman -S speedcrunch```

```zypper: sudo zypper install speedcrunch```

```nix: nix profile install nixpkgs#speedcrunch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bc](/man/bc)(1), [calc](/man/calc)(1), [qalc](/man/qalc)(1)
