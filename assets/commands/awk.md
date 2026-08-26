# TAGLINE

模式扫描与文本处理语言

# TLDR

打印以空格分隔的文件中的**第五列**（即字段）

```awk '{print $5}' [path/to/file] ```

打印以空格分隔的文件中**包含 "foo" 的行**的第二列

```awk '/[foo]/ {print $2}' [path/to/file] ```

打印文件中每行的**最后一列**，使用**逗号**（而不是空格）作为字段分隔符

```awk -F ',' '{print $NF}' [path/to/file]```

**求文件第一列的值的和**并打印总数

```awk '{s+=$1} END {print s}' [path/to/file]```

**根据条件**打印不同的值

```awk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}' [path/to/file]```

打印第 10 列的值**介于最小值与最大值之间**的所有行

```awk '($10 >= [min_value] && $10 <= [max_value])'```

# SYNOPSIS

**awk** [_-F fs_] [_-v var=val_] [_-f progfile_] [_--posix_] [_--_] '_program_' [_files_]

# PARAMETERS

**-F  _fs_**  
> 字段分隔符（_fs_）；默认为空白或制表符  
  
**-f  _file_**  
> 从 _file_ 读取 awk 程序而不是命令行  
  
**-v  _var_=_val_**  
> 在程序运行前将 _val_ 赋给 _var_（可重复使用）  
  
**--**  
> 结束选项；其后内容视为文件名  
  
**-V**  
> 打印版本并退出（gawk）  
  
**--help**  
> 打印帮助并退出（gawk）  
  
**--posix**  
> 强制 POSIX 兼容（gawk）  
  
**-mf  _n_**  
> 将函数参数数量限制为 _n_（调试用；gawk）  
  
**-mr  _n_**  
> 将记录大小限制为 _n_ 字节（调试用；gawk）  
  
**-W  _traditional_**  
> 使用原始 awk 行为（gawk）

# DESCRIPTION

**awk** 是一种模式扫描与文本处理语言，专为提取和转换结构化数据而设计。它逐行读取输入，把每行拆分成字段，然后应用由模式和动作组成的用户自定义规则。

awk 程序是一系列 **pattern { action }** 规则。对每一行输入，awk 会测试各模式并对匹配者执行相应的动作。如果没有给出模式，动作会作用于每一行；如果没有给出动作，则打印匹配的行。

字段通过 **$1**、**$2** 等访问，**$0** 代表整行。默认的字段分隔符是空白字符，可用 **-F** 更改。内置变量包括 **NR**（当前行号）、**NF**（当前行的字段数）、**FS**（字段分隔符）和 **OFS**（输出字段分隔符）。

特殊模式 **BEGIN** 和 **END** 分别在处理所有输入之前和之后执行动作，常用于初始化和汇总输出。awk 支持变量、数组、算术运算、字符串函数、printf 格式化和流程控制语句，是一门完整的文本处理编程语言。

# FIELD ACCESS

**\$0**：整行
**\$1**：第一个字段
**NF**：字段数
**NR**：记录（行）号
**FILENAME**：当前输入文件
**FS** / **OFS**：输入 / 输出字段分隔符
**RS** / **ORS**：输入 / 输出记录分隔符
第 n 个字段用 **\$(n)** 表示

# CAVEATS

不同的 awk 实现（gawk、mawk、nawk）功能集各异。正则表达式和字符串函数在不同实现之间可能行为不同。关联数组是无序的。浮点运算可能产生舍入误差。处理超大文件效率很高，但包含大量数组的复杂程序可能消耗大量内存。

# HISTORY

**awk** 由 **Alfred Aho**、**Peter Weinberger** 和 **Brian Kernighan** 于 **1977** 年在贝尔实验室创建，名字取自三人姓氏的首字母。它在 **1985** 年被重新设计并扩展为"new awk"（nawk）。**GNU awk**（gawk）增加了网络和国际化的诸多扩展。awk 是标准的 POSIX 工具，几乎所有类 Unix 系统都可用。

# INSTALL

```dnf: sudo dnf install gawk```

```pacman: sudo pacman -S gawk```

```apk: sudo apk add gawk```

```zypper: sudo zypper install gawk```

```brew: brew install gawk```

```nix: nix profile install nixpkgs#gawk```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[sed](/man/sed)(1), [grep](/man/grep)(1), [cut](/man/cut)(1), [perl](/man/perl)(1), [gawk](/man/gawk)(1)

# RESOURCES

```[Source code](https://cgit.git.savannah.gnu.org/cgit/gawk.git)```

```[Homepage](https://www.gnu.org/software/gawk/)```

```[Documentation](https://www.gnu.org/software/gawk/manual/)```

<!-- verified: 2026-06-09 -->
