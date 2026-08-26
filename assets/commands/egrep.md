# TAGLINE

扩展正则表达式模式搜索工具

# TLDR

**在文件中搜索模式**

```egrep "[pattern]" [file.txt]```

**不区分大小写地搜索**

```egrep -i "[pattern]" [file.txt]```

**带行号搜索**

```egrep -n "[pattern]" [file.txt]```

**递归搜索**

```egrep -r "[pattern]" [directory]```

**搜索多个**模式（交替）

```egrep "[pattern1]|[pattern2]" [file.txt]```

**统计匹配数**

```egrep -c "[pattern]" [file.txt]```

**只显示匹配的**文件名

```egrep -l "[pattern]" [*.txt]```

# SYNOPSIS

**egrep** [_options_] _pattern_ [_file_...]

# PARAMETERS

_PATTERN_
> 扩展正则表达式。

_FILE_
> 要搜索的文件。

**-i**
> 不区分大小写搜索。

**-n**
> 显示行号。

**-r**, **-R**
> 递归搜索。

**-l**
> 只显示文件名。

**-c**
> 统计匹配的行数。

**-v**
> 反向匹配（显示不匹配的行）。

**-o**
> 只显示匹配的部分。

**--help**
> 显示帮助信息。

# DESCRIPTION

**egrep** 在文件中搜索匹配扩展正则表达式模式的行。它等价于 `grep -E`，支持 ERE 语法，包括无需转义的 +、?、| 和 ()。

对于复杂匹配，扩展正则表达式比基本的 grep 模式更易读。交替（|）、分组（）和量词可以直接使用而无需反斜杠。

egrep 已被弃用，推荐使用 `grep -E`，但出于兼容性考虑仍然广泛可用。

# CAVEATS

已弃用——请使用 grep -E。不同实现之间的行为可能不同。大文件可能较慢。二进制文件可能产生乱码输出。

# HISTORY

egrep 最初是一个支持扩展正则表达式的独立程序。现代 grep 通过 -E 标志包含了这一功能，使独立的 egrep 显得多余，但为了兼容性仍被保留。

# INSTALL

```apt: sudo apt install grep```

```dnf: sudo dnf install grep```

```pacman: sudo pacman -S grep```

```apk: sudo apk add grep```

```zypper: sudo zypper install grep```

```brew: brew install grep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [fgrep](/man/fgrep)(1), [sed](/man/sed)(1), [awk](/man/awk)(1)
