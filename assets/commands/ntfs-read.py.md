# TAGLINE

无需挂载即可读取 NTFS 卷的 Impacket 工具

# TLDR

**从 NTFS 分区读取文件**

```ntfs-read.py [/dev/sda1] [/path/to/file]```

**列出目录内容**

```ntfs-read.py [/dev/sda1] -l [/path/to/dir]```

**将文件提取到本地输出文件**

```ntfs-read.py [/dev/sda1] [/path/to/file] -o [output]```

**列出根目录**

```ntfs-read.py [/dev/sda1] -l /```

# SYNOPSIS

**ntfs-read.py** [_options_] _device_ [_path_]

# PARAMETERS

_DEVICE_
> NTFS 分区设备（如 /dev/sda1）。

_PATH_
> NTFS 卷内要读取或列出的路径。

**-l**
> 列出目录内容而不是读取文件。

**-o** _FILE_
> 将输出写入指定文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ntfs-read.py** 是一个 Impacket 工具，可以直接从块设备读取 NTFS 文件系统而无需挂载。它在低层解析 NTFS 结构，提供对 NTFS 分区上文件和目录的访问。

这对于挂载文件系统不可取或不可行的取证分析和数据恢复场景非常有用。该工具可以列出目录、读取单个文件并提取其内容。

它是 **Impacket** 安全工具集的一部分，该工具集提供了用于处理网络协议和 Windows 相关结构的 Python 类。

# CAVEATS

需要原始设备访问权限，因此通常需要 root 权限。作为 Impacket 的 Python 脚本，它需要安装 Impacket 库。面向安全研究和取证用途；不适合作为通用的 NTFS 访问工具。

# HISTORY

ntfs-read.py 属于 **Impacket**——一套最初由 **SecureAuth**（现为 **Fortra**）开发的、用于处理网络协议的 Python 类集合。它为安全研究和数字取证提供底层 NTFS 访问能力。

# INSTALL

```apk: sudo apk add py3-impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ntfs-3g](/man/ntfs-3g)(1), [ntfsfix](/man/ntfsfix)(1), [ntfsclone](/man/ntfsclone)(1), [impacket](/man/impacket)(1)
