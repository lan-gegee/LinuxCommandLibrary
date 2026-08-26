# TAGLINE

将 bzip2 文件解压到标准输出

# TLDR

**查看**压缩文件

```bzcat [file.txt.bz2]```

**查看**多个文件

```bzcat [file1.bz2] [file2.bz2]```

通过管道输出到 **less**

```bzcat [file.txt.bz2] | less```

# SYNOPSIS

**bzcat** [_file_...]

# DESCRIPTION

**bzcat** 将 bzip2 文件解压到标准输出，而不修改原始压缩文件。它等同于 `bzip2 -dc`，适用于查看或以管道方式处理压缩内容。

该工具让你无需先将压缩文件解压到磁盘即可对其进行操作。

# WORKFLOW

```bash
# View compressed file
bzcat log.txt.bz2

# View with pager
bzcat log.txt.bz2 | less

# Search in compressed file
bzcat log.txt.bz2 | grep "error"

# Concatenate compressed files
bzcat file1.bz2 file2.bz2 > combined.txt

# Count lines in compressed file
bzcat data.txt.bz2 | wc -l
```

# FEATURES

- 保留原始压缩文件
- 流式输出（内存占用低）
- 支持多个文件
- 对管道友好

# CAVEATS

输出总是发送到 stdout。没有压缩级别选项。仅查看时可考虑 bzless。无法处理损坏的文件。

# HISTORY

自 bzip2 于 **1996 年**创建起，**bzcat** 就一直是 bzip2 工具集的一部分。

# INSTALL

```apt: sudo apt install bzip2```

```dnf: sudo dnf install bzip2```

```pacman: sudo pacman -S bzip2```

```apk: sudo apk add bzip2```

```zypper: sudo zypper install bzip2```

```brew: brew install bzip2```

```nix: nix profile install nixpkgs#bzip2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bzip2](/man/bzip2)(1), [bzless](/man/bzless)(1), [bzgrep](/man/bzgrep)(1), [zcat](/man/zcat)(1)

# RESOURCES

```[Source code](https://gitlab.com/bzip2/bzip2)```

```[Homepage](https://sourceware.org/bzip2/)```

<!-- verified: 2026-06-22 -->
