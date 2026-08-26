# TAGLINE

AWK 文本处理器的 GNU 实现

# TLDR

**打印文件中的指定列**

```gawk '{print $1, $3}' [path/to/file]```

**使用不同的字段分隔符**

```gawk -F':' '{print $1}' [/etc/passwd]```

**对某一列求和**

```gawk '{sum += $1} END {print sum}' [file]```

**过滤匹配模式的行**

```gawk '/pattern/ {print}' [file]```

**打印行号**及内容

```gawk '{print NR": "$0}' [file]```

**从文件运行 awk 程序**

```gawk -f [program.awk] [file]```

**使用命令行传入的变量**

```gawk -v name="[value]" '{print name, $0}' [file]```

**打印第 3 列大于 100 的行**

```gawk '$3 > 100 {print}' [file]```

# SYNOPSIS

**gawk** [_-F fs_] [_-v var=val_] [_-f progfile_] [_'program'_] [_file ..._]

# PARAMETERS

**-F** _fs_
> 设置字段分隔符（默认：空白字符）。

**-f** _progfile_
> 从文件读取程序而不是命令行。

**-v** _var=value_
> 在程序执行前为变量赋值。

**-b**, **--characters-as-bytes**
> 将所有输入数据视为单字节字符。

**-c**, **--traditional**
> 以 POSIX 兼容模式运行。

**-e** _'program'_
> 指定程序文本（可多次使用 -e 选项）。

**-i** _file_
> 包含库文件。

**-l** _lib_
> 加载扩展库。

**-n**, **--non-decimal-data**
> 识别输入中的八进制和十六进制数值。

**-o** _file_
> 将程序美化输出到文件。

**-p** _file_
> 启用性能分析，输出到文件。

**-S**, **--sandbox**
> 禁用系统命令和文件访问。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**gawk**（GNU awk）是 AWK 编程语言的 GNU 实现，专为文本处理和数据提取设计。它逐行处理输入，把每行切分成字段进行操作和转换。

AWK 程序由模式和动作组成：**pattern { action }**。当一行匹配某个模式时，对应的动作就会执行。特殊模式 **BEGIN** 和 **END** 分别在处理任何输入之前/之后运行。

内置变量包括：**$0**（整行）、**$1-$n**（字段）、**NR**（记录/行号）、**NF**（字段数）、**FS**（字段分隔符）、**OFS**（输出字段分隔符）以及 **RS**（记录分隔符）。

Gawk 对标准 AWK 做了大量扩展：网络编程（TCP/UDP 连接）、时间函数、位操作、国际化和扩展加载等。它还支持正则表达式、数组、用户自定义函数，以及用于读取文件/管道的 getline。

常见用途包括：日志分析、CSV/TSV 处理、报表生成、数据转换，以及其他语言中会显得繁琐的快捷文本处理任务。

# CAVEATS

复杂程序用 Python 或 Perl 可能更合适。浮点精度可能出人意料。不同 AWK 实现之间存在细微的不兼容。默认的字段切分无法正确处理带引号的 CSV（这类场景建议改用 csvkit）。

# HISTORY

AWK 由贝尔实验室的 Alfred Aho、Peter Weinberger 和 Brian Kernighan 于 **1977 年**创建（名字取自三人姓氏首字母）。**gawk**（GNU AWK）由 GNU 计划自 **1986 年**起开发，在保持兼容的同时增加了大量扩展。它至今仍是功能最丰富的 AWK 实现。

# INSTALL

```apt: sudo apt install gawk```

```dnf: sudo dnf install gawk```

```pacman: sudo pacman -S gawk```

```apk: sudo apk add gawk```

```zypper: sudo zypper install gawk```

```brew: brew install gawk```

```nix: nix profile install nixpkgs#gawk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[awk](/man/awk)(1), [sed](/man/sed)(1), [perl](/man/perl)(1), [cut](/man/cut)(1), [grep](/man/grep)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/gawk/)```

```[Documentation](https://www.gnu.org/software/gawk/manual/)```

<!-- verified: 2026-07-15 -->
