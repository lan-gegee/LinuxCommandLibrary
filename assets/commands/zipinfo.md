# TAGLINE

显示 ZIP 归档信息

# TLDR

**显示归档信息**

```zipinfo [archive.zip]```

**简短列表**

```zipinfo -1 [archive.zip]```

**长列表**

```zipinfo -l [archive.zip]```

**中等列表**

```zipinfo -m [archive.zip]```

**显示头部信息**

```zipinfo -h [archive.zip]```

**只显示总计**

```zipinfo -t [archive.zip]```

**显示特定文件信息**

```zipinfo [archive.zip] [file.txt]```

# SYNOPSIS

**zipinfo** [_-1_] [_-l_] [_-m_] [_-h_] [_-t_] [_options_] _archive_ [_members_]

# PARAMETERS

**-1**
> 只显示文件名，每行一个。

**-2**
> 只显示文件名，允许配合头部（-h）、总计（-t）和注释（-z）。

**-s**
> 简短的 Unix ls -l 格式（默认）。

**-m**
> 中等格式：增加压缩率百分比。

**-l**
> 长格式：以字节显示压缩后的尺寸。

**-h**
> 打印归档头部（名称、大小、文件数量）。

**-t**
> 打印总计（文件数量、总大小、压缩比）。

**-T**
> 以可排序的十进制格式打印时间戳（yymmdd.hhmmss）。

**-z**
> 打印归档注释。

**-v**
> 详细的多页格式，包含所有可用信息。

**-M**
> 将输出通过内置分页器管道显示（类似 more）。

**-x** _PATTERN_
> 排除匹配模式的文件。

# OUTPUT FIELDS

长列表显示：
- 权限
- 版本
- 操作系统
- 大小（未压缩）
- 压缩类型
- 大小（已压缩）
- 压缩比
- 日期/时间
- 文件名

# DESCRIPTION

**zipinfo** 无需解压即可显示 ZIP 归档的信息。它展示结构、压缩和元数据。

简短列表（-1）只提供文件名，便于脚本使用。每个文件独占一行。

长列表（-l）类似 ls -l 的输出。它显示权限、大小、压缩和日期信息。

头部（-h）显示归档级信息：文件名、大小和条目数量。

总计（-t）汇总归档情况：文件数量、总大小和压缩比。

模式匹配用于选择要显示的特定文件。通配符可用于过滤大型归档。

# CAVEATS

属于 Info-ZIP 软件包。某些加密归档可能无法显示全部信息。非常大的归档可能较慢。

# HISTORY

**zipinfo** 是 **Info-ZIP** 的一部分，由 Info-ZIP 组织自 20 世纪 **90 年代初**开始开发。它提供无需解压的归档查看功能。

# INSTALL

```apt: sudo apt install unzip```

```dnf: sudo dnf install unzip```

```pacman: sudo pacman -S unzip```

```apk: sudo apk add unzip```

```zypper: sudo zypper install unzip```

```brew: brew install unzip```

```nix: nix profile install nixpkgs#unzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[unzip](/man/unzip)(1), [zip](/man/zip)(1), [zipgrep](/man/zipgrep)(1), [zipcloak](/man/zipcloak)(1)
