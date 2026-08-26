# TAGLINE

从文件行中提取片段

# TLDR

按字段**提取**

```cut -f [1,3] [file.txt]```

按字符**提取**列

```cut -c [1-10] [file.txt]```

自定义分隔符

```cut -d [:] -f [1,7] [/etc/passwd]```

按字节**提取**

```cut -b [1-5] [file.txt]```

# SYNOPSIS

**cut** [_options_] [_file_...]

# DESCRIPTION

**cut** 从文件的每一行中删除若干片段。它可按字符位置、字节位置或字段分隔符提取列，适合处理结构化文本数据。

该命令常用于 Shell 脚本中解析列状数据。

# PARAMETERS

**-f**, **--fields** _list_
> 选择字段（以分隔符划分）

**-c**, **--characters** _list_
> 选择字符

**-b**, **--bytes** _list_
> 选择字节

**-d**, **--delimiter** _char_
> 字段分隔符（默认：TAB）

**--output-delimiter** _string_
> 输出分隔符

**-s**, **--only-delimited**
> 不打印不含分隔符的行

**--complement**
> 取所选范围的反集

# RANGE SPECIFICATION

- **N** - 第 N 项
- **N-** - 从第 N 项到末尾
- **N-M** - 从第 N 项到第 M 项
- **-M** - 从开头到第 M 项
- **N,M** - 第 N 和第 M 项

# WORKFLOW

```bash
# Extract first field (default TAB delimiter)
cut -f 1 data.tsv

# Extract multiple fields
cut -f 1,3,5 data.tsv

# CSV with custom delimiter
cut -d ',' -f 2 data.csv

# Extract username from /etc/passwd
cut -d ':' -f 1 /etc/passwd

# Extract characters 1-10
cut -c 1-10 file.txt

# Extract first 20 bytes
cut -b 1-20 file.txt

# Change output delimiter
cut -d ',' -f 1,2 --output-delimiter=':' data.csv
```

# COMMON USES

**Parse CSV:**
```bash
cut -d ',' -f 2,4 data.csv
```

**Extract columns from ps:**
```bash
ps aux | cut -c 1-20,50-70
```

**Get usernames:**
```bash
cut -d ':' -f 1 /etc/passwd
```

**Field range:**
```bash
cut -f 2-5 data.tsv
```

# CAVEATS

无法处理数量不一的空白字符（请改用 awk）。分隔符只能是单个字符。不能对字段重新排序（可用 awk）。不支持正则表达式。CSV 的引号处理需要其他工具。只能操作字节/字符/字段，不能按列宽切分。

# HISTORY

**cut** 自 20 世纪 80 年代初起就是 Unix 的一部分，属于 System III 及后续 POSIX 标准。

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

[paste](/man/paste)(1), [awk](/man/awk)(1), [tr](/man/tr)(1), [column](/man/column)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/coreutils.git)```

```[Homepage](https://www.gnu.org/software/coreutils/)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html)```

<!-- verified: 2026-06-26 -->
