# TAGLINE

支持 Exif、IPTC 和 XMP 的图像元数据读写工具

# TLDR

**显示图像的元数据**

```exiv2 [image.jpg]```

**打印所有 Exif** 数据

```exiv2 -pa [image.jpg]```

**打印 IPTC 数据**

```exiv2 -pi [image.jpg]```

**打印 XMP 数据**

```exiv2 -px [image.jpg]```

**修改 Exif** 数据

```exiv2 -M "set Exif.Photo.UserComment [text]" [image.jpg]```

**删除所有元数据**

```exiv2 -da [image.jpg]```

**按日期重命名**

```exiv2 -r "%Y%m%d_%H%M%S" [*.jpg]```

# SYNOPSIS

**exiv2** [_options_] [_actions_] _files_...

# PARAMETERS

_FILES_
> 要处理的图像文件。

**-pa**
> 打印所有元数据（Exif、IPTC 和 XMP 标签）。

**-pi**
> 打印 IPTC 标签。

**-px**
> 打印 XMP 标签。

**-M** _CMD_
> 修改元数据。

**-da**
> 删除所有元数据。

**-r** _FORMAT_
> 按时间戳重命名文件。

**-e** _FORMAT_
> 提取缩略图。

**--help**
> 显示帮助信息。

# DESCRIPTION

**exiv2** 读取、写入和操作图像元数据，包括 Exif、IPTC 和 XMP。它支持 JPEG、TIFF、PNG 及许多其他图像格式。

该工具可以详细访问相机设置、GPS 坐标、时间戳和描述性元数据。批量操作可以一次修改多个文件的元数据。

exiv2 适用于整理照片、移除敏感元数据以及对图像文件进行取证分析。

# CAVEATS

元数据修改是永久性的。某些格式的元数据支持有限。GPS 数据可能暴露位置信息。批量操作前请备份。

# HISTORY

exiv2 是一个开源项目，提供用于处理 Exif 及其他元数据的库和命令行工具，被众多图像应用使用。

# INSTALL

```apt: sudo apt install exiv2```

```dnf: sudo dnf install exiv2```

```pacman: sudo pacman -S exiv2```

```apk: sudo apk add exiv2```

```zypper: sudo zypper install exiv2```

```brew: brew install exiv2```

```nix: nix profile install nixpkgs#exiv2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[exiftool](/man/exiftool)(1), [identify](/man/identify)(1), [jhead](/man/jhead)(1)

# RESOURCES

```[Source code](https://github.com/Exiv2/exiv2)```

```[Homepage](https://exiv2.org/)```

<!-- verified: 2026-07-15 -->
