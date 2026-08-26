# TAGLINE

终端中的数字时钟

# TLDR

**显示居中且带秒数的 24 小时制时钟**

```tock -s -m -c```

**自定义颜色和字体尺寸**

```tock -C [4] -W [3] -H [2]```

**自定义日期格式**

```tock -f "[%A, %B %d]"```

# SYNOPSIS

**tock** [_options_]

# PARAMETERS

**-s**, **--second**
> 显示秒数。

**-m**, **--military**
> 使用 24 小时制时间格式。

**-c**, **--center**
> 将时钟居中显示在终端中（覆盖手动定位）。

**-C**, **--color** _COLOR_
> 用 ANSI 值 0-7 设置时钟颜色（默认：2）。

**-x**, **--x** _X_
> 时钟左上角的水平位置（从 0 开始计数，默认：0）。

**-y**, **--y** _Y_
> 时钟左上角的垂直位置（从 0 开始计数，默认：0）。

**-W**, **--width** _WIDTH_
> 字体宽度，以每个字符块的字符数表示（默认：2）。

**-H**, **--height** _HEIGHT_
> 字体高度，以每个字符块的字符数表示（默认：1）。

**-f**, **--format** _FORMAT_
> 自定义日期格式字符串（默认："%F | %Z"）。

**-h**, **--help**
> 显示帮助信息。

# INTERACTIVE KEYS

**q**
> 退出时钟。

**s**
> 切换秒数显示。

**m**
> 切换 24 小时制。

**0**-**7**
> 运行时更改 ANSI 颜色。

# DESCRIPTION

**tock** 是一款受 tty-clock 启发的终端数字时钟。它支持自定义定位、字号大小、12/24 小时制、颜色选择、秒数显示和日期格式化。

# CAVEATS

由于使用了 termios，仅限 UNIX 系统。

# HISTORY

**tock** 由 **nwtnni** 创建，使用 **Rust** 编写。

# INSTALL

```brew: brew install tock```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[date](/man/date)(1), [tty-clock](/man/tty-clock)(1), [figlet](/man/figlet)(1)
