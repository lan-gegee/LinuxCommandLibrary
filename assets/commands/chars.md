# TAGLINE

显示 Unicode 字符信息

# TLDR

**显示字符信息**

```chars [character]```

**按 Unicode 码点查找**

```chars [U+1F63C]```

**按数字编码查找**（匹配可能有歧义）

```chars [10]```

**查找控制字符**

```chars "[^C]"```

**按名称搜索字符**

```chars [query]```

# SYNOPSIS

**chars** [_options_] [_character|codepoint|query_]...

# PARAMETERS

_CHARACTER_
> 字符字面量、Unicode 码点（如 U+1F63C）、数字编码或控制字符记号（如 ^C）。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**chars** 是一款显示 ASCII 和 Unicode 字符及码点详细信息的命令行工具。它受 `ascii(1)` 和 `unicode.py` 启发，支持空白字符和控制字符。

对每个字符，它会打印 Unicode 码点、各种编码表示（十六进制、八进制、UTF-8、UTF-16）、显示宽度、Unicode 名称和别名、大小写变体以及转义序列。字符可以通过字面形式、`U+` 码点、数字编码或控制字符记号来查找。

它用 Rust 编写，适合处理 Unicode 文本或调试编码问题的开发者使用。

# INSTALL

```brew: brew install chars```

```nix: nix profile install nixpkgs#chars```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chardet](/man/chardet)(1), [iconv](/man/iconv)(1), [hexdump](/man/hexdump)(1)
