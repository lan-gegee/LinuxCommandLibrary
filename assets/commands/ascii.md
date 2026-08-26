# TAGLINE

显示 ASCII 字符表和别名

# TLDR

显示字符的**别名**

```ascii a```

**适合脚本**的输出

```ascii -t a```

处理**多个**字符

```ascii -s tldr```

以**十进制**显示表

```ascii -d```

以**十六进制**显示表

```ascii -x```

以**二进制**显示表

```ascii -b```

# SYNOPSIS

**ascii** [_OPTIONS_] [_characters_]

# DESCRIPTION

**ascii** 显示 ASCII 字符信息，包括别名和各种进制的数值编码，可作为字符编码参考，快速查询 ASCII 表。

# PARAMETERS

**-t**
> 简洁模式，输出适合脚本处理

**-s**
> 处理字符串中的多个字符

**-d**
> 以十进制显示 ASCII 表

**-x**
> 以十六进制显示 ASCII 表

**-o**
> 以八进制显示 ASCII 表

**-b**
> 以二进制显示 ASCII 表

**-h**, **-?**
> 显示选项摘要和一张简易 ASCII 表

**-v**
> 显示程序版本

# CAVEATS

不带参数时，显示选项摘要和完整的 ASCII 表。进制选项（**-d**、**-x**、**-o**、**-b**）具有双重行为：不带参数时按该进制打印完整表格；带参数时则按该进制解释这些值，只打印匹配的字符记录。字符别名包括控制字符的常见名称，如 NUL、TAB、LF、CR、ESC、DEL。

# HISTORY

**ascii** 由 Eric S. Raymond 编写，是一款便捷的 ASCII 参考工具。

# INSTALL

```apt: sudo apt install ascii```

```dnf: sudo dnf install ascii```

```pacman: sudo pacman -S ascii```

```zypper: sudo zypper install ascii```

```brew: brew install ascii```

```nix: nix profile install nixpkgs#ascii```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[man](/man/man)(1), [charmap](/man/charmap)(1)

# RESOURCES

```[Source code](https://gitlab.com/esr/ascii)```

```[Homepage](http://www.catb.org/~esr/ascii/)```

```[Documentation](http://www.catb.org/~esr/ascii/ascii.html)```

<!-- verified: 2026-06-16 -->
