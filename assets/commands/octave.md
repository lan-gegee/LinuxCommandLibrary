# TAGLINE

GNU Octave，一种数值计算语言

# TLDR

**启动交互式会话**（带 GUI）

```octave```

**启动不带 GUI 的交互式 CLI 会话**

```octave --no-gui```

**运行脚本文件**

```octave [path/to/script.m]```

**求值表达式后退出**

```octave --eval "[diag([1,2,3])]"```

**安静地运行脚本**（抑制启动消息）

```octave --quiet [path/to/script.m]```

**以批处理模式运行**（非交互式，适用于脚本）

```octave --no-gui --silent [path/to/script.m]```

# SYNOPSIS

**octave** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要执行的脚本文件（.m）。

**--eval** _CODE_
> 求值 CODE 后退出（除非同时给出 --persist）。

**--gui**
> 启动图形用户界面。

**--no-gui**
> 使用命令行界面代替 GUI。

**-q**, **--quiet**, **--silent**
> 抑制启动消息和版本信息。

**-i**, **--interactive**
> 强制交互模式（通过管道或远程 shell 运行时有用）。

**--no-init-file**
> 不读取 ~/.octaverc 或 .octaverc 初始化文件。

**--persist**
> 在 --eval 或运行脚本文件之后保持交互状态。

**--path** _dir_
> 将目录添加到函数搜索路径的开头。

**--jit-compiler**
> 启用 JIT 编译器以加速循环执行。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**GNU Octave** 是一种高级解释型语言，主要面向数值计算。它提供便捷的命令行界面和 GUI，用于以数值方法求解线性与非线性问题，并与 MATLAB 高度兼容。

Octave 提供丰富的工具，覆盖矩阵运算、方程组求解、数值积分、统计、优化以及二维/三维绘图。它可以借助 Octave Forge 的软件包进行扩展，还支持调用 C、C++ 和 Fortran 代码。

# CAVEATS

对 MATLAB 的兼容性较广但并不完整；某些 MATLAB 工具箱函数不可用或行为不同。大规模矩阵运算可能占用大量内存。JIT 编译器在某些版本中仍属实验性功能。

# HISTORY

GNU Octave 由 **John W. Eaton** 自 **1988** 年起创建，最初是一本化学反应器设计教科书的配套工具。它于 **1993** 年首次作为独立应用程序发布，目前作为 GNU 项目持续开发。

# INSTALL

```apt: sudo apt install octave```

```dnf: sudo dnf install octave```

```pacman: sudo pacman -S octave```

```apk: sudo apk add octave```

```zypper: sudo zypper install octave```

```brew: brew install octave```

```nix: nix profile install nixpkgs#octave```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[matlab](/man/matlab)(1), [gnuplot](/man/gnuplot)(1), [python](/man/python)(1)
