# TAGLINE

将多个文件的行并排合并

# TLDR

**并排合并文件**

```paste [file1.txt] [file2.txt]```

**使用自定义分隔符合并**

```paste -d "," [file1.txt] [file2.txt]```

**合并单个文件内的行**

```paste -s [file.txt]```

**创建以制表符分隔的列**

```paste - - < [file.txt]```

**合并多个文件**

```paste [file1] [file2] [file3]```

# SYNOPSIS

**paste** [_options_] _files_...

# DESCRIPTION

**paste** 将多个文件的行并排合并。第一个文件的每一行会与后续文件的对应行拼接，中间以制表符分隔。

该工具适用于把来自不同来源的数据组合成列式格式。

# PARAMETERS

**-d** _list_
> 使用 list 中的字符作为分隔符。

**-s**, **--serial**
> 一次处理一个文件。

**-z**, **--zero-terminated**
> 使用 NUL 作为行分隔符。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# CAVEATS

要对齐，各文件的行数应相同。分隔符会在列表中循环使用。空行会产生空列。

# HISTORY

**paste** 是传统的 Unix 工具，属于 **POSIX** 和 **GNU coreutils** 的一部分。自早期起就是 Unix 系统的标准组件，用于简单地组装表格数据。

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

[cut](/man/cut)(1), [join](/man/join)(1), [column](/man/column)(1), [pr](/man/pr)(1)
