# TAGLINE

不使用正则的固定字符串搜索

# TLDR

**搜索字面**字符串

```fgrep "[search string]" [file.txt]```

**搜索多个文件**

```fgrep "[pattern]" [file1.txt] [file2.txt]```

**不区分大小写搜索**

```fgrep -i "[pattern]" [file.txt]```

**显示行号**

```fgrep -n "[pattern]" [file.txt]```

**递归搜索**

```fgrep -r "[pattern]" [directory]```

# SYNOPSIS

**fgrep** [_options_] _pattern_ [_files_...]

# PARAMETERS

_PATTERN_
> 要搜索的固定字符串。

_FILES_
> 要搜索的文件。

**-i**, **--ignore-case**
> 不区分大小写匹配。

**-n**, **--line-number**
> 显示行号。

**-r**, **--recursive**
> 递归搜索目录。

**-l**, **--files-with-matches**
> 仅显示文件名。

**-c**, **--count**
> 统计匹配的行数。

**-v**, **--invert-match**
> 显示不匹配的行。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fgrep** 搜索的是固定字符串而非正则表达式。它等价于 grep -F，在搜索不含正则元字符的字面文本时速度更快。

该工具把模式当作普通字符串处理，因此 .、* 和 [ 等字符不具有特殊含义。这使它非常适合搜索日志文件、代码或任何包含正则元字符的文本。

当搜索模式来自用户输入或可能包含特殊字符的变量时，fgrep 尤其实用。

# CAVEATS

设计上不支持正则表达式。已被弃用，建议改用 grep -F；GNU grep 3.8（2022 年）及更高版本在以 fgrep 身份调用时会打印弃用警告。要指定多个模式需使用 -f 选项。

# HISTORY

fgrep（fast grep）起源于 **Unix Version 7**，是一个针对字面字符串优化过的 grep 变体。现代实现通常是指向 grep 并附带 -F 标志的链接。

# INSTALL

```apt: sudo apt install grep```

```dnf: sudo dnf install grep```

```pacman: sudo pacman -S grep```

```apk: sudo apk add grep```

```zypper: sudo zypper install grep```

```brew: brew install grep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [egrep](/man/egrep)(1), [rg](/man/rg)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/grep/)```

<!-- verified: 2026-07-15 -->
