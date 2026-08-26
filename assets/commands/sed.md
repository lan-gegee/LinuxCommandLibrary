# TAGLINE

用于文本转换的流编辑器

# TLDR

在所有行中**替换**所有出现的 "apple" 为 "mango"

```[command] | sed 's/apple/mango/g'```

在文件中**就地替换**（覆盖原文件）

```sed -i 's/apple/mango/g' [path/to/file]```

在一条命令中执行**多次替换**

```[command] | sed -e 's/apple/mango/g' -e 's/orange/lime/g'```

使用**自定义分隔符**（模式包含斜杠时很有用）

```[command] | sed 's#////#____#g'```

**删除第 1 到 5 行**并以 .orig 扩展名备份原文件

```sed -i.orig '1,5d' [path/to/file]```

仅将第一行**打印**到 stdout

```[command] | sed -n '1p'```

在文件开头**插入**新行

```sed -i '1i\your new line text' [path/to/file]```

从文件中**删除空行**

```sed -i '/^[[:space:]]*$/d' [path/to/file]```

# SYNOPSIS

**sed** [_options_] '_script_' [_input-file_...]

# PARAMETERS

**-i**[_suffix_], **--in-place**[=_suffix_]
> 就地编辑文件；可选使用后缀创建备份

**-e** _script_, **--expression=**_script_
> 添加要执行的脚本命令

**-f** _file_, **--file=**_file_
> 从文件读取脚本

**-n**, **--quiet**, **--silent**
> 抑制自动打印；仅在使用 p 命令时打印

**-r**, **-E**, **--regexp-extended**
> 使用扩展正则表达式

**-s**, **--separate**
> 将各文件视为独立流而非单一数据流

**-z**, **--null-data**
> 用 NUL 字符分隔行

**--sandbox**
> 禁止输入/输出命令（e/w/r）；处理不受信任的脚本时使用

**--posix**
> 禁用所有 GNU 扩展以符合 POSIX

**--debug**
> 注解程序执行过程

# DESCRIPTION

**sed**（stream editor，流编辑器）是一款强大的文本处理工具，可对输入流（文件或管道数据）执行基本的转换。它逐行读取输入、应用指定的编辑命令，并将结果写入标准输出。

常见操作包括查找替换（s///）、删除（d）、插入（i）和打印（p）。sed 使用正则表达式进行模式匹配，同时支持基本和扩展正则语法。地址范围（行号或模式）可用于定位特定行。

# CAVEATS

**-i** 选项直接修改文件；务必先输出到 stdout 测试，或使用备份后缀。不带后缀的 **-i** 在 GNU sed 和 BSD sed 中行为不同。基本（默认）和扩展（**-r**）模式的正则表达式语法有所差异。

# HISTORY

由 Lee McMahon 于 **1973-1974 年**在贝尔实验室创建，是 Unix 的一部分。它基于 ed 编辑器的脚本能力，但专为非交互式流处理而设计。GNU sed 通过就地编辑和扩展正则支持等特性对原始版本进行了扩展。

# INSTALL

```apt: sudo apt install sed```

```dnf: sudo dnf install sed```

```pacman: sudo pacman -S sed```

```apk: sudo apk add sed```

```zypper: sudo zypper install sed```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[awk](/man/awk)(1), [grep](/man/grep)(1), [tr](/man/tr)(1), [ed](/man/ed)(1), [perl](/man/perl)(1)
