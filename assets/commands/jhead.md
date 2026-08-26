# TAGLINE

显示和操作 JPEG 图像中 EXIF 元数据的工具

# TLDR

显示全部 **EXIF 数据**

```jhead image.jpg```

将**文件日期设置为 EXIF** 日期

```jhead -ft image.jpg```

将 **EXIF 日期设置为文件**日期

```jhead -dsft image.jpg```

根据 EXIF 日期重命名文件

```jhead -n%Y_%m_%d-%H_%M_%S *.jpg```

根据 EXIF 方向标记自动旋转图像

```jhead -autorot *.jpg```

调整 EXIF 时间戳

```jhead -ta-1:00:00 *.jpg```

删除全部 EXIF 数据

```jhead -purejpg image.jpg```

仅删除缩略图

```jhead -dt image.jpg```

# SYNOPSIS

**jhead** [_options_] [_file_...]

# DESCRIPTION

**jhead** 是一个用于显示和操作数码相机 JPEG 图像中 EXIF 元数据的工具。它可以调整时间戳、移除缩略图、自动旋转图像，并在文件之间转移 EXIF 头。

# PARAMETERS

**-ft**
> 将文件修改时间设为 EXIF 创建日期

**-dsft**
> 将 EXIF 时间戳设为文件修改时间

**-n FORMAT**
> 基于 EXIF 日期，使用 strftime 格式重命名文件

**-autorot**
> 根据 EXIF 方向标记无损旋转图像

**-ta OFFSET**
> 按偏移量调整 EXIF 时间（格式：+/-HH:MM:SS）

**-da NEWDATE-OLDDATE**
> 校正较大的日期偏差

**-purejpg**
> 删除所有非必要区段和元数据

**-de**
> 删除整个 EXIF 头

**-dt**
> 从 EXIF 头中删除缩略图

**-dc**
> 删除注释字段

**-te FILE**
> 从另一个文件转移 EXIF 头

**-ce**
> 在文本编辑器中编辑注释字段

**-cl STRING**
> 从命令行设置注释

**-st FILE**
> 将缩略图保存到文件

**-rgt SIZE**
> 以指定尺寸重新生成缩略图

**-mkexif**
> 创建最小化的 EXIF 头

# CAVEATS

-autorot 选项使用 jpegtran 进行无损旋转。-n 重命名使用 strftime 格式代码。除非另行指定，更改将直接写入原始文件。

# HISTORY

**jhead** 由 Matthias Wandel 开发，用于处理数码相机 JPEG 文件中的 EXIF 数据。

# INSTALL

```apt: sudo apt install jhead```

```dnf: sudo dnf install jhead```

```pacman: sudo pacman -S jhead```

```brew: brew install jhead```

```nix: nix profile install nixpkgs#jhead```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[exiftool](/man/exiftool)(1), [exiv2](/man/exiv2)(1), [jpegtran](/man/jpegtran)(1)
