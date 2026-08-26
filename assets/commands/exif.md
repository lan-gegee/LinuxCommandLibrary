# TAGLINE

EXIF 元数据查看器和编辑器

# TLDR

显示图像中的所有 **EXIF 信息**

```exif [path/to/image.jpg]```

以表格形式**列出**已知的 EXIF 标签

```exif [-l|--list-tags] [path/to/image.jpg]```

**提取**缩略图到文件

```exif [-e|--extract-thumbnail] [-o|--output] [path/to/thumbnail.jpg] [path/to/image.jpg]```

显示标签的**原始内容**

```exif --ifd [0] [-t|--tag] "[Model]" [-m|--machine-readable] [path/to/image.jpg]```

**修改**标签的值

```exif [-o|--output] [path/to/new.jpg] --ifd [0] [-t|--tag] "[Artist]" --set-value "[John Smith]" --no-fixup [path/to/image.jpg]```

从图像中**移除**某个标签

```exif --remove --ifd [0] [-t|--tag] "[Artist]" [-o|--output] [path/to/new.jpg] [path/to/image.jpg]```

在没有 EXIF 数据时**创建** EXIF 数据

```exif [-c|--create-exif] [-o|--output] [path/to/new.jpg] [path/to/image.jpg]```

# SYNOPSIS

**exif** [_options_] _files_

# PARAMETERS

**-v**, **--version**
> 显示版本号。

**-l**, **--list-tags**
> 列出已知的 EXIF 标签。

**-e**, **--extract-thumbnail**
> 提取内嵌的缩略图。

**-r**, **--remove-thumbnail**
> 从图像中移除缩略图。

**-n**, **--insert-thumbnail** _file_
> 将文件作为缩略图插入。

**-o**, **--output** _file_
> 操作的输出文件。

**-t**, **--tag** _tag_
> 指定标签名称或编号。

**-s**, **--show-description**
> 显示标签的描述。

**--set-value** _value_
> 将标签设置为指定值。

**--remove**
> 移除标签或整个 IFD。

**--ifd** _ifd_
> 选择 IFD（0、1、EXIF、GPS、Interoperability）。

**-c**, **--create-exif**
> 在没有 EXIF 数据时创建。

**-m**, **--machine-readable**
> 输出机器可读的制表符分隔格式。

**-x**, **--xml-output**
> 生成 XML 输出。

**-i**, **--ids**
> 显示 ID 编号而非标签名称。

**--no-fixup**
> 不修复违反 EXIF 规范之处。

**-d**, **--debug**
> 显示调试消息。

**-w**, **--width** _n_
> 设置最大输出宽度（默认 80）。

# DESCRIPTION

**exif** 显示和修改 JPEG 文件中的 EXIF 元数据。EXIF 数据包含相机设置、日期时间、GPS 坐标及其他图像信息。

这是一个用于快速检查和修改 EXIF 的命令行工具。它可以列出标签、提取和管理缩略图、读写单个标签的值，以及从零创建 EXIF 数据。

# CAVEATS

仅支持 JPEG 文件。某些标签是只读的。修改时应使用 --no-fixup 以保留原始数据结构。--machine-readable 与 --xml-output 选项互斥。

# INSTALL

```apt: sudo apt install exif```

```dnf: sudo dnf install exif```

```zypper: sudo zypper install exif```

```brew: brew install exif```

```nix: nix profile install nixpkgs#exif```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[exiftool](/man/exiftool)(1), [jhead](/man/jhead)(1), [identify](/man/identify)(1)
