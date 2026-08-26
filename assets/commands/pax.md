# TAGLINE

POSIX 归档工具

# TLDR

**创建归档**

```pax -wf [archive.pax] [directory]```

**解压归档**

```pax -rf [archive.pax]```

**列出归档内容**

```pax -f [archive.pax]```

**复制目录**

```pax -rw [source] [destination]```

**创建压缩归档**

```pax -wf - [directory] | gzip > [archive.pax.gz]```

# SYNOPSIS

**pax** [_options_] [_pattern_...]

# PARAMETERS

**-r**
> 读取（解压）归档。

**-w**
> 写入（创建）归档。

**-f** _FILE_
> 归档文件。

**-v**
> 详细输出。

**-d**
> 仅匹配目录。

**-k**
> 不覆盖已有文件。

# DESCRIPTION

**pax** 是 POSIX 标准的归档工具。它结合了 tar 和 cpio 的功能。

该工具用于创建和解压归档。采用可移植归档交换格式（portable archive exchange）。

# CAVEATS

POSIX 标准。不如 tar 常见。格式可移植。

# HISTORY

pax 作为 tar 和 cpio 的 **POSIX 标准**替代品而创建。

# INSTALL

```apt: sudo apt install pax```

```dnf: sudo dnf install pax```

```pacman: sudo pacman -S pax```

```apk: sudo apk add pax```

```brew: brew install pax```

```nix: nix profile install nixpkgs#pax```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tar](/man/tar)(1), [cpio](/man/cpio)(1), [gzip](/man/gzip)(1)
