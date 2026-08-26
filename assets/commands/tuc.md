# TAGLINE

增强的文本字段切割与拆分工具

# TLDR

**切割第一个字段**（制表符分隔）

```echo "[a\tb\tc]" | tuc -f 1```

**切割字段 1 到 3**

```echo "[a:b:c:d]" | tuc -d ':' -f 1:3```

**重排字段顺序**

```echo "[a,b,c]" | tuc -d ',' -f 3,1,2```

**使用负索引**（最后一个字段）

```echo "[a b c]" | tuc -d ' ' -f -1```

**使用正则表达式作为分隔符**

```echo "[a1b2c3]" | tuc -e '[0-9]' -f 1:```

**替换输出中的分隔符**

```echo "[a:b:c]" | tuc -d ':' -r '-' -f 1:```

**选择指定字符**

```echo "[hello]" | tuc -c 1:3```

**用模板格式化输出**

```echo "[a,b,c]" | tuc -d ',' --format '{1} - {2}'```

# SYNOPSIS

**tuc** [_flags_] [_options_] [_file_]

# PARAMETERS

**-f**, **--fields** _bounds_
> 要选择的字段（默认：1:）

**-b**, **--bytes** _bounds_
> 选择指定字节

**-c**, **--characters** _bounds_
> 选择字符（支持 UTF-8）

**-l**, **--lines** _bounds_
> 选择行

**-d**, **--delimiter** _delim_
> 字段分隔符（默认：tab）

**-e**, **--regex** _pattern_
> 使用正则表达式作为分隔符

**-r**, **--replace-delimiter** _text_
> 用自定义文本替换分隔符

**-t**, **--trim** _type_
> 去除分隔符：l（左）、r（右）、b（两侧）

**-g**, **--greedy-delimiter**
> 将连续的分隔符视为一个匹配

**-p**, **--compress-delimiter**
> 切割前合并连续的分隔符

**-s**, **--only-delimited**
> 只显示包含分隔符的行

**-m**, **--complement**
> 反转字段选择

**-j**, **--join**
> 用分隔符重新拼接选中的部分

**-z**, **--zero-terminated**
> 使用 NUL 而不是换行符作为行结束符

**--format** _template_
> 使用 {1}、{2} 等字段占位符格式化输出

**--json**
> 以 JSON 数组形式输出各字段

**--no-mmap**
> 禁用内存映射

# DESCRIPTION

**tuc** 是经典 **cut** 命令的现代化替代品，用 Rust 编写。它提供增强的字段选择功能，包括负索引、正则表达式分隔符、多字符分隔符和字段重排序。

字段语法支持范围（**1:3**）、列表（**1,3,5**）、负索引（**-1** 表示最后一个）以及组合。配合 **{1}**、**{2}** 的模板格式化可实现自定义输出。

与 cut 不同，tuc 可以重排字段顺序、用正则表达式模式拆分，并能正确处理 Unicode 字符。**-g** 选项将连续的分隔符视为一个，适合处理间距不定的空白分隔数据。

# CAVEATS

正则表达式支持会增加二进制体积；使用 **--no-default-features** 构建可得到更小的二进制文件。字段编号从 1 开始而不是 0。默认分隔符是 tab 而不是空白。

# HISTORY

**tuc** 由 **Riccardo Attilio Galli**（riquito）创建，是对传统 cut 工具的 Rust 增强。名字是 "cut" 的趣味反转。项目源于 cut 在正则分隔符、字段重排序和负索引方面的局限。

# INSTALL

```apk: sudo apk add tuc```

```zypper: sudo zypper install tuc```

```brew: brew install tuc```

```nix: nix profile install nixpkgs#tuc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cut](/man/cut)(1), [awk](/man/awk)(1), [choose](/man/choose)(1), [sed](/man/sed)(1)
