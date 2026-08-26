# TAGLINE

输出数字序列

# TLDR

**生成 1 到 10 的数字**

```seq 10```

**生成 5 到 10 的数字**

```seq 5 10```

**按步长生成数字**（每次递增 2）

```seq 0 2 10```

**反向生成数字**（递减）

```seq 10 -1 1```

**生成带前导零的数字**（等宽）

```seq -w 1 100```

**使用自定义分隔符生成**

```seq -s ", " 1 5```

**使用 printf 风格的格式生成**

```seq -f "file%03g.txt" 1 10```

# SYNOPSIS

**seq** [_options_] [_first_ [_increment_]] _last_

# PARAMETERS

_last_
> 从 1 生成到 last

_first_ _last_
> 从 first 生成到 last

_first_ _increment_ _last_
> 以指定步长从 first 生成到 last

**-f**, **--format**=_format_
> 使用 printf 风格的格式输出（例如 %g、%f、%e）

**-s**, **--separator**=_string_
> 使用 string 作为分隔符（默认：换行符）

**-w**, **--equal-width**
> 用前导零补齐至等宽

**--help**
> 显示帮助并退出

**--version**
> 显示版本并退出

# DESCRIPTION

**seq** 输出一段数字序列，默认每行一个数字。它常用于在 shell 脚本中生成编号列表、循环计数器和格式化序列。

未指定起始数字时，seq 从 1 开始。步长默认为 1（若 first > last 则为 -1）。所有参数都支持浮点数。

**-f** 选项接受 printf 风格的格式说明符：**%g** 表示通用数字，**%f** 表示定点数，**%e** 表示指数记法。宽度和精度修饰符与 printf 中一致。

常见于 bash 循环中：**for i in $(seq 1 10); do echo $i; done**，或使用花括号展开的等价写法：**for i in {1..10}; do echo $i; done**。

# CAVEATS

对于大序列，seq 比花括号展开更省内存，因为它按需生成数字，而不是一次性全部展开。

浮点步长可能累积舍入误差。如需精确的小数序列，建议使用其他工具或语言。

当 shell 支持时，对简单的整数序列而言，bash 花括号展开 **{1..10}** 通常更快。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jot](/man/jot)(1), [yes](/man/yes)(1), [printf](/man/printf)(1), [bash](/man/bash)(1)
