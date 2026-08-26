# TAGLINE

对文本文件的行进行排序

# TLDR

**按字母顺序排序文件**

```sort [file]```

**逆序排序**

```sort -r [file]```

**按数值排序**

```sort -n [file]```

**按指定列排序**（如第 2 列）

```sort -k2 [file]```

**按多列排序**

```sort -k1,1 -k2,2n [file]```

**只保留唯一行排序**

```sort -u [file]```

**忽略大小写排序**

```sort -f [file]```

**排序并保存到文件**

```sort [file] -o [output_file]```

**按人类可读大小排序**（1K, 2M, 3G）

```sort -h [file]```

# SYNOPSIS

**sort** [_options_] [_file_...]

# PARAMETERS

**-r**, **--reverse**
> 反转排序顺序

**-n**, **--numeric-sort**
> 按字符串数值比较

**-h**, **--human-numeric-sort**
> 按人类可读数值比较（2K, 1G）

**-f**, **--ignore-case**
> 将小写折叠为大写（忽略大小写）

**-u**, **--unique**
> 只输出唯一行

**-k** _KEYDEF_
> 按指定的键/列排序

**-t** _SEP_
> 使用 SEP 作为字段分隔符

**-o** _FILE_
> 将结果写入 FILE 而非标准输出

**-c**, **--check**
> 检查输入是否已排序；并以状态码退出

**-s**, **--stable**
> 通过禁用最后手段比较来稳定排序

**-m**, **--merge**
> 合并已排序的文件

**-b**, **--ignore-leading-blanks**
> 忽略键的前导空白

**-d**, **--dictionary-order**
> 只考虑空白和字母数字字符

**-g**, **--general-numeric-sort**
> 按一般数值比较

**-i**, **--ignore-nonprinting**
> 只考虑可打印字符

**-M**, **--month-sort**
> 比较（未知）< 'JAN' < ... < 'DEC'

**-R**, **--random-sort**
> 随机打乱，但相同键归为一组

**-V**, **--version-sort**
> 版本号的自然排序

**-z**, **--zero-terminated**
> 行分隔符为 NUL 而非换行符

**-S**, **--buffer-size**=_SIZE_
> 使用 SIZE 作为主内存缓冲区大小

**-T**, **--temporary-directory**=_DIR_
> 使用 DIR 存放临时文件，而非 $TMPDIR 或 /tmp

**--parallel**=_N_
> 使用 N 个并行线程

**--debug**
> 标注所使用的排序键并对可疑用法发出警告

# KEY DEFINITION

**-k** _POS1_[,_POS2_]: 从 POS1 到 POS2 的字段排序
格式：**F**[**.**_C_][_OPTS_]
- F = 字段编号（从 1 开始）
- C = 字段内的字符位置
- OPTS = 排序选项（n, r, b, f 等）

示例：
- **-k2**: 按第 2 个字段排到末尾
- **-k2,2**: 仅按第 2 个字段排序
- **-k2n**: 按第 2 个字段按数值排序
- **-k1,1 -k2,2n**: 主排序按字母序，次排序按数值

# DESCRIPTION

**sort** 根据指定的条件对文本文件的行进行排序。默认情况下，它按照当前 locale 执行字典序排序。

多个输入文件会被合并后一起排序。输出默认到标准输出；使用 **-o** 写入文件（可以安全地与输入文件同名）。

对于结构化数据，**-k** 选项非常强大。结合 **-t** 设置分隔符，它可以按特定字段对 CSV、TSV 及其他列式数据进行排序。

对于大文件，sort 会自动使用临时文件，并可通过 **--parallel** 利用多个 CPU 核心。

# CAVEATS

locale 会影响排序顺序。使用 **LC_ALL=C** 可按字节值排序，这对机器处理来说更快且更可预测。

数值排序（**-n**）处理整数和小数。对于像 "1.10" 与 "1.9" 这样的版本号，请使用 **-V**（版本排序）。

大文件的内存占用可能很高。使用 **-S** 限制缓冲区大小或 **-T** 指定临时目录。

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

[uniq](/man/uniq)(1), [join](/man/join)(1), [comm](/man/comm)(1), [cut](/man/cut)(1), [tsort](/man/tsort)(1)
