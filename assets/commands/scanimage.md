# TAGLINE

从兼容 SANE 的扫描仪扫描图像

# TLDR

**列出**可用的扫描仪

```scanimage -L```

扫描图像并**保存**到文件

```scanimage --format png > image.png```

使用**指定设备**扫描

```scanimage -d device_name > image.pnm```

以**高分辨率**扫描

```scanimage --resolution 300 > image.pnm```

以**彩色模式**扫描

```scanimage --mode Color > image.pnm```

扫描指定的**区域**

```scanimage -l 0 -t 0 -x 210 -y 297 > image.pnm```

# SYNOPSIS

**scanimage** [_-d device_] [_--format format_] [_--resolution dpi_] [_-L_]

# DESCRIPTION

**scanimage** 使用 SANE（Scanner Access Now Easy）接口扫描图像。它提供对图像扫描仪的命令行访问，支持多种输出格式和扫描仪特定选项。

# PARAMETERS

**-L, --list-devices**
> 列出可用的扫描仪设备

**-d, --device-name device**
> 使用指定的扫描仪设备

**--format format**
> 输出格式（pnm、tiff、png、jpeg、pdf）

**--resolution dpi**
> 设置扫描分辨率，单位为 DPI（默认：75）

**--mode mode**
> 扫描模式（Lineart、Gray、Color）

**-l, --left mm**
> 扫描区域左边缘（毫米）

**-t, --top mm**
> 扫描区域上边缘（毫米）

**-x, --width mm**
> 扫描区域宽度（毫米）

**-y, --height mm**
> 扫描区域高度（毫米）

**--brightness value**
> 设置亮度级别

**--contrast value**
> 设置对比度级别

**-b, --batch**
> 启用批量扫描模式

**-p, --progress**
> 扫描时显示进度

**-v, --verbose**
> 启用详细输出

**-A, --all-options**
> 列出该设备的所有可用选项

# CAVEATS

扫描仪特定选项因设备而异。使用 **-A** 查看你的扫描仪的可用选项。根据 USB 权限的不同，某些功能可能需要 root 权限。

# HISTORY

**scanimage** 是 **SANE**（Scanner Access Now Easy）项目的一部分，自 1996 年起为类 Unix 系统上的图像扫描仪提供标准化接口。

# INSTALL

```apt: sudo apt install sane-utils```

```apk: sudo apk add sane-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scanadf](/man/scanadf)(1), [sane-find-scanner](/man/sane-find-scanner)(1), [saned](/man/saned)(8)
