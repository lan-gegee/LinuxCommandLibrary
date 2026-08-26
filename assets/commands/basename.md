# TAGLINE

从文件名中去除目录部分和后缀。

# TLDR

从路径中**提取**文件名

```basename [/path/to/file.txt]```

**移除**后缀

```basename [/path/to/file.txt] [.txt]```

**多个**文件

```basename -a [/path/to/file1.txt] [/path/to/file2.txt]```

移除**任意后缀**

```basename -s [.txt] [/path/to/file.txt]```

# SYNOPSIS

**basename** _path_ [_suffix_]

# DESCRIPTION

**basename** 从路径名中去除目录部分，只留下最后的文件名。它还可以选择性地去除末尾的后缀，非常适合在 Shell 脚本中提取文件名。

该工具是 GNU coreutils 的一部分，常用于构建脚本和文件处理流水线。

# PARAMETERS

**-a**, **--multiple**
> 处理多个参数

**-s**, **--suffix=**_suffix_
> 移除末尾后缀

**-z**, **--zero**
> 输出以 NUL 而非换行符分隔

# BEHAVIOR

给定 `/path/to/file.txt`：
- **basename** 返回 `file.txt`
- 带 `.txt` 后缀的 **basename** 返回 `file`

# CAVEATS

只精确移除一个与参数完全匹配的末尾后缀——`basename file.tar.gz .gz` 得到的是 `file.tar` 而非 `file`。路径不必真实存在于磁盘上。双参数形式（位置后缀）是 POSIX 行为；`-s` 加 `-a` 是 GNU 扩展，支持多输入和非位置式后缀。在 Bash 脚本中，参数展开形式 `${filepath##*/}` 和 `${name%.txt}` 比启动 `basename` 进程更快。

# HISTORY

**basename** 自早期起就是 Unix 的一部分，已纳入 POSIX 标准，自 **1992** 年起可在 GNU coreutils 中使用。

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

[dirname](/man/dirname)(1), [realpath](/man/realpath)(1), [readlink](/man/readlink)(1)
