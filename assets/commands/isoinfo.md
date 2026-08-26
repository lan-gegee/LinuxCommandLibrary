# TAGLINE

检查 ISO 9660 文件系统映像并提取其中的信息

# TLDR

**列出** ISO 映像中的所有文件

```isoinfo -f -i [path/to/image.iso]```

将 ISO 中的某个文件**解压**到 stdout

```isoinfo -i [path/to/image.iso] -x [/PATH/TO/FILE.EXT]```

显示 ISO 的**头信息**

```isoinfo -d -i [path/to/image.iso]```

# SYNOPSIS

**isoinfo** [_options_] **-i** _filename_

# PARAMETERS

**-i** _FILE_
> 输入的 ISO 映像文件

**-f**
> 列出 ISO 中的所有文件

**-d**
> 显示头信息（卷描述符）

**-x** _PATH_
> 将指定路径的文件提取到 stdout

**-l**
> 长列表格式（类似 ls -l）

**-R**
> 使用 Rock Ridge 扩展

**-J**
> 使用 Joliet 扩展

# DESCRIPTION

**isoinfo** 用于检查 ISO 9660 文件系统映像并从中提取信息。它可以列出文件、显示卷信息，并在不挂载映像的情况下提取单个文件。

该工具支持 ISO 9660 扩展，包括 Rock Ridge（Unix 权限和长文件名）和 Joliet（Windows 长文件名）。这在刻录或挂载前检查 ISO 映像时很有用。

# CAVEATS

ISO 映像内的文件路径通常是大写的。可能需要 Rock Ridge 或 Joliet 扩展才能看到原始文件名。提取的内容输出到 stdout；请用重定向保存。

# HISTORY

isoinfo 是 cdrtools/cdrkit 软件包的一部分，最初由 Joerg Schilling 开发。ISO 9660 是 CD-ROM 介质的标准文件系统，于 **1988 年**定义。

# INSTALL

```apt: sudo apt install genisoimage```

```dnf: sudo dnf install genisoimage```

```apk: sudo apk add cdrkit```

```nix: nix profile install nixpkgs#cdrkit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[genisoimage](/man/genisoimage)(1), [mount](/man/mount)(8)
