# TAGLINE

支持物理单位的高精度科学计算器

# TLDR

**启动交互式计算器**

```numbat```

**求值表达式**

```numbat -e "[expression]"```

**单位换算**

```numbat -e "5 km -> miles"```

**运行 numbat 脚本文件**

```numbat [path/to/script.nbt]```

# SYNOPSIS

**numbat** [_options_] [_file_]

# PARAMETERS

**-e** _EXPRESSION_
> 求值表达式并打印结果。

**--no-prelude**
> 不加载标准 prelude（数学函数、常量、单位定义）。

**--no-pretty**
> 禁用输出中表达式的美化打印。

# DESCRIPTION

**numbat** 是一种用于科学计算的静态类型编程语言，对物理量纲和单位提供一等公民支持。它既可以作为强大的计算器，也可以作为脚本语言使用。

单位可以以多种格式输入（km/h、kilometer/hour、GiB、gibibytes、m²），并可用 **->** 运算符转换。标准库包括 SI、美制 customary、英制 imperial、航海、天文和原子单位制。还可以定义自定义单位（如 `unit bathtub = 150 L`）。

交互式 REPL 支持命令历史、Ctrl-R 搜索和制表符补全。

# CAVEATS

由于物理量纲检查，包含不兼容单位的表达式会产生类型错误，而不是给出错误结果。

# HISTORY

**numbat** 由 **sharkdp**（David Peter）创建，使用 **Rust** 编写。

# INSTALL

```apt: sudo apt install numbat```

```pacman: sudo pacman -S numbat```

```zypper: sudo zypper install numbat```

```brew: brew install numbat```

```nix: nix profile install nixpkgs#numbat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bc](/man/bc)(1), [kalker](/man/kalker)(1), [qalc](/man/qalc)(1)
