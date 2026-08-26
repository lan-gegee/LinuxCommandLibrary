# TAGLINE

归档并压缩文件

# TLDR

从文件**创建归档**

```tar -cvf [archive.tar] [file1] [file2]```

**创建 gzip 压缩的归档**

```tar -czvf [archive.tar.gz] [directory/]```

**创建 bzip2 压缩的归档**

```tar -cjvf [archive.tar.bz2] [directory/]```

**创建 xz 压缩的归档**

```tar -cJvf [archive.tar.xz] [directory/]```

**解压归档**

```tar -xvf [archive.tar]```

**解压压缩归档**

```tar -xzvf [archive.tar.gz]```

**解压到指定目录**

```tar -xvf [archive.tar] -C [directory/]```

**列出归档内容**

```tar -tvf [archive.tar]```

**提取特定文件**

```tar -xvf [archive.tar] [file1] [file2]```

# SYNOPSIS

**tar** [_options_] [_archive_] [_file_...]

# PARAMETERS

**-c**, **--create**
> 创建新归档

**-x**, **--extract**
> 从归档中提取文件

**-t**, **--list**
> 列出归档内容

**-v**, **--verbose**
> 详细输出

**-f** _file_, **--file**=_file_
> 使用指定的归档文件

**-z**, **--gzip**
> 通过 gzip 过滤

**-j**, **--bzip2**
> 通过 bzip2 过滤

**-J**, **--xz**
> 通过 xz 过滤

**-a**, **--auto-compress**
> 根据文件扩展名判断压缩方式

**-C** _dir_, **--directory**=_dir_
> 操作前先切换到指定目录

**-p**, **--preserve-permissions**
> 保留文件权限

**--exclude**=_pattern_
> 排除匹配模式的文件

**-r**, **--append**
> 将文件追加到归档

**-u**, **--update**
> 用较新的文件更新归档

**-k**, **--keep-old-files**
> 解压时不替换已有文件

**--zstd**
> 通过 zstd 压缩过滤

**-T** _FILE_, **--files-from**=_FILE_
> 从 FILE 读取要提取或创建的文件列表

**-X** _FILE_, **--exclude-from**=_FILE_
> 排除 FILE 中列出的模式

**--strip-components**=_N_
> 剥离 N 层前导路径组件

**-h**, **--dereference**
> 跟随符号链接；归档它们指向的文件

**-O**, **--to-stdout**
> 将文件提取到标准输出

# DESCRIPTION

**tar**（tape archive，磁带归档）用于创建、提取和管理归档文件。它把多个文件和目录打包成单个文件，同时保留权限、所有者和目录结构。

tar 本身不压缩；压缩由外部程序（gzip、bzip2、xz）完成，可通过选项调用，或用 **-a** 根据文件扩展名自动选择。

常见扩展名：**.tar**（未压缩）、**.tar.gz** 或 **.tgz**（gzip）、**.tar.bz2**（bzip2）、**.tar.xz**（xz）、**.tar.zst**（zstd）。现代 tar 在解压时会自动检测压缩方式。

使用短选项时顺序很重要。**-cvf** 可行；**-fvc archive.tar** 可能不行，因为 -f 要求其参数紧跟其后。

# CAVEATS

默认情况下，tar 按归档中记录的路径提取。包含绝对路径或 **../** 的归档可能覆盖目标目录之外的文件。请使用 **--strip-components**，或者先解压到一个空目录。

以 root 身份解压会保留原始的所有者信息。以普通用户身份解压时，无论归档元数据如何，文件都归你所有。

GNU tar 与 BSD tar 在某些选项上有所不同。为了可移植性，请坚持使用通用选项，或查阅具体实现的文档。

# HISTORY

Tar 起源于 **1979 年**的 Version 7 Unix，为磁带备份而设计（因此得名 "tape archive"）。它成为标准的 Unix 归档工具并被 POSIX 规范化。GNU tar 加入了许多扩展，包括压缩集成。

# INSTALL

```apt: sudo apt install tar```

```dnf: sudo dnf install tar```

```pacman: sudo pacman -S tar```

```apk: sudo apk add tar```

```zypper: sudo zypper install tar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gzip](/man/gzip)(1), [bzip2](/man/bzip2)(1), [xz](/man/xz)(1), [zstd](/man/zstd)(1), [zip](/man/zip)(1), [cpio](/man/cpio)(1), [ar](/man/ar)(1)
