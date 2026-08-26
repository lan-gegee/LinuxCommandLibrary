# TAGLINE

转换和变换栅格数据

# TLDR

**转换栅格格式**

```gdal_translate [input.tif] [output.png]```

**以指定格式转换**

```gdal_translate -of GTiff [input.png] [output.tif]```

**按范围裁剪子集**

```gdal_translate -projwin [ulx] [uly] [lrx] [lry] [input.tif] [output.tif]```

**重缩放为 8 位**

```gdal_translate -ot Byte -scale [input.tif] [output.tif]```

**设置压缩**

```gdal_translate -co COMPRESS=LZW [input.tif] [output.tif]```

**提取波段**

```gdal_translate -b 1 -b 2 -b 3 [input.tif] [rgb.tif]```

# SYNOPSIS

**gdal_translate** [_options_] _src_ _dst_

# PARAMETERS

**-of** _format_
> 输出格式（GTiff、PNG、JPEG 等）。

**-ot** _type_
> 输出数据类型（Byte、Int16、Float32 等）。

**-b** _band_
> 选择波段。

**-projwin** _ulx_ _uly_ _lrx_ _lry_
> 按坐标裁剪子集。

**-srcwin** _xoff_ _yoff_ _xsize_ _ysize_
> 按像素裁剪子集。

**-scale** [_src_min_ _src_max_ [_dst_min_ _dst_max_]]
> 缩放数值。

**-co** _NAME=VALUE_
> 创建选项。

**-outsize** _xsize_ _ysize_
> 输出尺寸（像素或百分比）。

**-a_srs** _srs_
> 指定空间参考。

**-a_nodata** _value_
> 指定 nodata 值。

# DESCRIPTION

**gdal_translate** 可在格式之间转换栅格数据、提取子集并应用变换。它属于 GDAL（Geospatial Data Abstraction Library，地理空间数据抽象库），后者是栅格地理空间操作的标准工具集。

常见用途包括格式转换、创建影像金字塔、应用压缩以及从大型数据集中提取区域。

# CAVEATS

大文件可能需要大量内存。某些格式不支持所有特性。有损压缩会丢失数据。请先用 gdalinfo 查看源数据属性。

# HISTORY

GDAL 由 **Frank Warmerdam** 于 **1998 年**发起，现在是 OSGeo 项目。gdal_translate 是 GDAL 的核心实用程序之一，支持超过 150 种栅格格式。

# INSTALL

```apt: sudo apt install gdal-bin```

```apk: sudo apk add gdal-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdalwarp](/man/gdalwarp)(1), [gdalinfo](/man/gdalinfo)(1), [ogr2ogr](/man/ogr2ogr)(1)
