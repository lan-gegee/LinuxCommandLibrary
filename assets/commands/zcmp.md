# TAGLINE

逐字节比较 gzip 压缩文件

# TLDR

**比较压缩文件**

```zcmp [file1.gz] [file2.gz]```

**显示差异**

```zcmp -l [file1.gz] [file2.gz]```

**安静模式**

```zcmp -s [file1.gz] [file2.gz]```

# SYNOPSIS

**zcmp** [_-l_] [_-s_] _file1_ _file2_

# PARAMETERS

**-b**, **--print-bytes**
> 打印不同的字节（以八进制值表示）。

**-l**, **--verbose**
> 对所有差异输出字节序号和不同的字节值。

**-s**, **--quiet**, **--silent**
> 抑制所有输出，仅通过退出状态传递结果。

**-i** _SKIP_, **--ignore-initial=**_SKIP_
> 跳过每个（解压后）输入的前 _SKIP_ 字节。

**-n** _LIMIT_, **--bytes=**_LIMIT_
> 最多比较 _LIMIT_ 字节。

# DESCRIPTION

**zcmp** 无需手动解压即可逐字节比较 gzip 压缩文件。它对解压后的内容调用 **cmp**，并将所有给定选项直接传给它。

默认情况下，zcmp 只报告发现的第一个差异。**-l** 标志显示所有不同字节的位置和值。安静模式（**-s**）抑制所有输出，只通过退出码传递结果：文件相同为 0，不同为 1，出错为 2。

该命令是 gzip 软件包的一部分，是一个便捷封装。要按行比较压缩文件，请改用 **zdiff**。

# CAVEATS

针对 gzip 格式的 .gz 文件。属于 gzip 软件包。

# HISTORY

**zcmp** 是 gzip 软件包的一部分，为压缩文件提供类似 cmp 的功能。

# INSTALL

```apt: sudo apt install gzip```

```dnf: sudo dnf install gzip```

```pacman: sudo pacman -S gzip```

```apk: sudo apk add gzip```

```zypper: sudo zypper install gzip```

```brew: brew install gzip```

```nix: nix profile install nixpkgs#gzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmp](/man/cmp)(1), [zdiff](/man/zdiff)(1), [zcat](/man/zcat)(1)
