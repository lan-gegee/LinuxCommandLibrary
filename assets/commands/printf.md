# TAGLINE

使用格式说明符格式化并打印数据

# TLDR

**打印格式化输出**

```printf "%s\n" "Hello"```

**使用变量打印**

```printf "Name: %s, Age: %d\n" "[name]" [25]```

**打印十六进制**

```printf "%x\n" [255]```

**带填充打印**

```printf "%10s\n" "text"```

**打印浮点数**

```printf "%.2f\n" [3.14159]```

# SYNOPSIS

**printf** _format_ [_arguments_]

# PARAMETERS

_FORMAT_
> 格式字符串。

_ARGUMENTS_
> 要格式化的值。

**%s**
> 字符串。

**%d**
> 整数。

**%f**
> 浮点数。

**%x**
> 十六进制。

**%o**
> 八进制。

# DESCRIPTION

**printf** 根据格式字符串格式化并打印数据，类似于同名的 C 库函数。格式字符串可以包含字面文本、**\n** 和 **\t** 等转义序列，以及 **%s**（字符串）、**%d**（整数）、**%f**（浮点数）、**%x**（十六进制）等转换说明符。

与 **echo** 不同，printf 对输出格式提供精确控制，并且在各种 shell 和平台上行为一致。如果提供的参数多于格式字符串所消耗的数量，格式字符串会被重复使用，因此很容易处理列表。除非在格式字符串中显式包含 **\n**，该命令不会追加末尾换行符。

printf 是 GNU coreutils 的一部分，在大多数 shell 中也可作为内建命令使用。它是可移植 shell 脚本中生成格式化输出的首选工具。

# CAVEATS

必须提供格式字符串。比 echo 更具可移植性。

# HISTORY

printf 源自 **C 编程语言**的格式化函数。

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

[echo](/man/echo)(1), [print](/man/print)(1), [fmt](/man/fmt)(1)
