# TAGLINE

基于公共字段合并两个文件

# TLDR

**按第一个字段连接**

```join [file1] [file2]```

**按指定字段连接**

```join -1 [2] -2 [1] [file1] [file2]```

**输出特定字段**

```join -o 1.1,2.2 [file1] [file2]```

**忽略大小写**

```join -i [file1] [file2]```

**显示未匹配的行**

```join -a 1 [file1] [file2]```

**自定义分隔符**

```join -t "," [file1.csv] [file2.csv]```

# SYNOPSIS

**join** [_options_] _file1_ _file2_

# PARAMETERS

_FILE1_ _FILE2_
> 要连接的文件（必须已按连接字段排序）。

**-1** _FIELD_
> 按文件 1 的第 N 个字段连接。

**-2** _FIELD_
> 按文件 2 的第 N 个字段连接。

**-o** _FORMAT_
> 输出格式说明。

**-t** _CHAR_
> 字段分隔符。

**-i**
> 忽略大小写差异。

**-a** _FILENUM_
> 打印无法配对的行。

**--help**
> 显示帮助信息。

# DESCRIPTION

**join** 基于公共字段合并两个文件。它对文本文件执行关系数据库式的连接操作。

文件必须按连接字段排好序。该工具支持内连接、左连接和右连接。

# CAVEATS

文件必须先排序。基于字段进行连接。默认以空白字符作为分隔符。

# HISTORY

join 是 **POSIX** 和传统 Unix 工具集的组成部分，用于对文本文件执行关系连接操作。

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

[sort](/man/sort)(1), [cut](/man/cut)(1), [paste](/man/paste)(1), [awk](/man/awk)(1)
