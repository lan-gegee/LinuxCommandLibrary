# TAGLINE

创建和解压 ARC 格式归档

# TLDR

**创建**归档

```arc a [archive.arc] [files]```

**解压**归档

```arc x [archive.arc]```

**列出**归档内容

```arc l [archive.arc]```

**测试**归档完整性

```arc t [archive.arc]```

# SYNOPSIS

**arc** _command_ [_archive_] [_files_]

# DESCRIPTION

**arc** 创建和操作 ARC 格式的归档。该格式在 1980 年代的 MS-DOS 时代曾广为流行。它支持创建新归档、提取文件、列出内容和测试归档完整性。

该工具支持历史 ARC 文件中使用的多种压缩方法，包括 Squeeze、Crunch 和 LZW 变体。如今主要用于访问旧版归档文件而非创建新归档，因为 zip 和 tar.gz 等现代格式在压缩率和功能上都明显更优。

# PARAMETERS

**a**
> 向归档添加文件

**x**
> 提取文件

**e**
> 提取到当前目录

**l**
> 列出内容

**t**
> 测试归档

**d**
> 从归档中删除文件

**p**
> 打印文件内容

**v**
> 查看详细信息

# CAVEATS

ARC 格式已过时；新归档请使用 zip 或 tar.gz 等现代格式。压缩能力与现代算法相比很有限。主要用于旧格式兼容。

# HISTORY

ARC 格式由 System Enhancement Associates 于 **1985** 年创建，是最早流行于个人计算机的文件压缩格式之一。

# INSTALL

```apt: sudo apt install arc```

```dnf: sudo dnf install arc```

```aur: yay -S arc```

```zypper: sudo zypper install arc```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[unzip](/man/unzip)(1), [tar](/man/tar)(1), [gzip](/man/gzip)(1)

# RESOURCES

```[Source code](https://github.com/hyc/arc)```

<!-- verified: 2026-06-11 -->
