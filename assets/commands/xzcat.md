# TAGLINE

将 xz 文件解压输出到 stdout

# TLDR

**查看** xz 压缩文件的内容

```xzcat [file.xz]```

**查看 .lzma 文件的内容**

```xzcat [file.lzma]```

**通过管道传给其他命令**

```xzcat [file.xz] | grep "[pattern]"```

不解压的情况下**测试文件完整性**

```xzcat -t [file.xz]```

显示文件名的**详细输出**

```xzcat -v [file.xz]```

**解压多个文件**

```xzcat [file1.xz] [file2.xz]```

# SYNOPSIS

**xzcat** [_options_] [_file ..._]

# PARAMETERS

**-f**, **--force**
> 即使输入看起来不是 .xz 格式也强制解压。

**-k**, **--keep**
> 保留输入文件（xzcat 本来就不会删除它们）。

**-t**, **--test**
> 测试压缩文件的完整性而不输出数据。

**-q**, **--quiet**
> 抑制警告和非致命错误消息。

**-v**, **--verbose**
> 处理过程中显示文件名和统计信息。

**--memlimit=**_limit_
> 设置解压时的内存使用限制。

**--format=**_format_
> 限制为特定格式：xz、lzma、raw、auto。

**-h**, **--help**
> 显示帮助信息并退出。

**-V**, **--version**
> 显示版本信息并退出。

# DESCRIPTION

**xzcat** 解压 .xz 和 .lzma 文件，并将解压后的数据写入标准输出。它等同于运行 **xz --decompress --stdout** 或 **xz -dc**。

XZ 格式采用 LZMA2 压缩算法，压缩率优于 gzip 或 bzip2，代价是压缩速度较慢。解压相对较快。

如果未指定文件或文件名为 **-**，xzcat 会从标准输入读取。

# CAVEATS

xzcat 只负责解压；无法处理 tar 归档（.tar.xz 文件请使用 **tar -xJf**）。用高设置压缩的文件可能占用大量内存；可用 **--memlimit** 控制。该命令属于 XZ Utils，后者在 2024 年曾发生影响 5.6.0-5.6.1 版本的安全事件。

# HISTORY

xzcat 属于 **XZ Utils**，由 **Lasse Collin** 开发，于 **2009 年**首次发布，是 LZMA Utils 的后继者。.xz 格式旨在取代 .lzma 并提供更好的特性，包括完整性检查（CRC32/CRC64/SHA-256）。XZ Utils 被广泛采用为软件分发的标准压缩工具，尤其是 Linux 内核和发行版的 tar 包。

# INSTALL

```apt: sudo apt install xz-utils```

```dnf: sudo dnf install xz```

```pacman: sudo pacman -S xz```

```apk: sudo apk add xz```

```zypper: sudo zypper install xz```

```brew: brew install xz```

```nix: nix profile install nixpkgs#xz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xz](/man/xz)(1), [unxz](/man/unxz)(1), [zcat](/man/zcat)(1), [bzcat](/man/bzcat)(1), [lzcat](/man/lzcat)(1)
