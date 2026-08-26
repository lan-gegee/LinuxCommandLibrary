# TAGLINE

读取、写入和编辑文件中的元信息

# TLDR

**显示文件的全部元数据**

```exiftool [image.jpg]```

**显示特定标签**

```exiftool -DateTimeOriginal -Model [image.jpg]```

**显示目录中所有文件的元数据**

```exiftool [/path/to/directory]```

**移除所有元数据**

```exiftool -all= [image.jpg]```

**设置特定标签**

```exiftool -Artist="[Name]" [image.jpg]```

**从一个文件复制元数据到另一个文件**

```exiftool -TagsFromFile [source.jpg] [dest.jpg]```

**根据拍摄日期重命名文件**

```exiftool "-FileName<DateTimeOriginal" -d "%Y%m%d_%H%M%S.%%e" [*.jpg]```

**将所有日期向后平移** 1 小时 30 分钟

```exiftool "-AllDates+=0:0:0 1:30:0" [image.jpg]```

**提取内嵌缩略图**

```exiftool -b -ThumbnailImage [image.jpg] > [thumb.jpg]```

# SYNOPSIS

**exiftool** [_options_] [**-**_tag_[=_value_]]... _file_...

# PARAMETERS

**-**_tag_
> 提取特定标签。

**-**_tag_**=** _value_
> 将标签设置为指定值。

**-all=**
> 移除所有可写的元数据。

**-TagsFromFile** _file_
> 从另一个文件复制标签。

**-r**, **-recurse**
> 递归处理目录。

**-overwrite_original**
> 覆盖原文件而不创建备份。

**-d** _fmt_
> 设置日期/时间输出格式（strftime 语法）。

**-FileName<** _tag_
> 根据标签重命名文件。

**-json**
> 以 JSON 输出。

**-csv**
> 以 CSV 输出。

**-b**
> 输出二进制数据。

**-v**
> 详细输出。

**-n**
> 禁用打印转换。

**-s**
> 短格式输出。

**-G**
> 显示每个标签所属的组名。

**-ext** _EXT_
> 只处理具有指定扩展名的文件。

**-X**
> 以 RDF/XML 格式输出。

**-p** _FMT_
> 使用标签名按自定义格式打印输出。

**-if** _EXPR_
> 使用 Perl 表达式有条件地处理文件。

**-q**
> 安静处理（抑制提示性消息）。

# DESCRIPTION

**ExifTool** 是一个强大且跨平台的工具，用于读取、写入和编辑各种文件格式中的元数据。它支持 EXIF、IPTC、XMP、GPS 以及相机和软件使用的众多专有元数据格式。

该工具可处理图像（JPEG、TIFF、PNG、RAW 格式）、音频文件、视频文件、PDF 和文档。它能识别几乎所有相机制造商的元数据，并且对大多数格式既支持读取也支持写入。

ExifTool 对整理照片集的摄影师、检查文件的取证分析师，以及任何需要以编程方式管理文件元数据的人来说都不可或缺。

# CAVEATS

并非所有格式都支持写入元数据。某些专有格式的写入支持有限。批量编辑前请备份重要文件。GPS 时间戳的时区处理可能比较复杂。

# HISTORY

**ExifTool** 由 **Phil Harvey** 于 **2003 年**创建，最初是一个用于操作元数据的 Perl 库和命令行工具。如今它已支持数百种文件格式中的 23000 多个标签。该项目持续更新以支持新相机和新格式，是现有最全面的元数据工具。

# INSTALL

```apk: sudo apk add exiftool```

```zypper: sudo zypper install exiftool```

```brew: brew install exiftool```

```nix: nix profile install nixpkgs#exiftool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[identify](/man/identify)(1), [jhead](/man/jhead)(1), [file](/man/file)(1), [mediainfo](/man/mediainfo)(1)
