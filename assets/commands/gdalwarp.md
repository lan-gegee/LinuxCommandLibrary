# TAGLINE

影像镶嵌、重投影与扭曲处理工具

# TLDR

**将栅格重投影**到不同的坐标系

```gdalwarp -t_srs [EPSG:4326] [input.tif] [output.tif]```

**同时指定源和目标**坐标系进行重投影

```gdalwarp -s_srs [EPSG:32611] -t_srs [EPSG:4326] [input.tif] [output.tif]```

**重投影时改变分辨率**

```gdalwarp -tr [0.001] [0.001] -t_srs [EPSG:4326] [input.tif] [output.tif]```

**使用双线性重采样**方法

```gdalwarp -r bilinear -t_srs [EPSG:4326] [input.tif] [output.tif]```

**将多个栅格镶嵌**为一个输出

```gdalwarp [input1.tif] [input2.tif] [input3.tif] [output.tif]```

**使用 shapefile 切割线裁剪栅格**

```gdalwarp -cutline [boundary.shp] -crop_to_cutline [input.tif] [output.tif]```

**指定输出格式**和数据类型

```gdalwarp -of GTiff -ot Float32 -t_srs [EPSG:4326] [input.tif] [output.tif]```

# SYNOPSIS

**gdalwarp** [_OPTIONS_] _SRCFILE_... _DSTFILE_

# PARAMETERS

**-s_srs** _SRS_
> 源空间参考系统（EPSG 编码、PROJ.4 或 WKT）。

**-t_srs** _SRS_
> 输出的目标空间参考系统。

**-r** _METHOD_
> 重采样方法：near、bilinear、cubic、cubicspline、lanczos、average、mode、max、min、med、q1、q3、sum。

**-tr** _XRES_ _YRES_
> 以地理参考单位表示的目标分辨率。

**-ts** _WIDTH_ _HEIGHT_
> 以像素表示的目标尺寸。

**-te** _XMIN_ _YMIN_ _XMAX_ _YMAX_
> 以地理参考坐标表示的目标范围。

**-of** _FORMAT_
> 输出格式（GTiff、PNG、JPEG 等）。

**-ot** _TYPE_
> 输出波段数据类型（Byte、UInt16、Float32 等）。

**-cutline** _FILE_
> 用于裁剪的矢量文件（shapefile、GeoJSON 等）。

**-crop_to_cutline**
> 将输出范围裁剪到切割线边界。

**-overwrite**
> 覆盖已有的输出文件。

**-multi**
> 使用多线程扭曲处理。

**-co** _NAME_=_VALUE_
> 输出格式的创建选项。

# DESCRIPTION

**gdalwarp** 是 GDAL 库中的影像镶嵌、重投影和扭曲处理工具。它在坐标系之间变换栅格数据集、重采样到不同分辨率、将多个输入镶嵌为单一输出，并可使用矢量边界裁剪栅格。

该工具支持所有 GDAL 栅格格式，可以应用随图像存储的地面控制点（GCP）。提供多种重采样算法，从快速的最近邻插值到高质量的 Lanczos 加窗 sinc 插值。

对于需要坐标系转换、多源数据集成或为特定分析要求准备栅格数据的 GIS 工作流而言，gdalwarp 必不可少。

# CAVEATS

大型栅格可能需要大量内存；使用 **-wm** 可限制内存使用。在高压缩率或使用不当的重采样方法时，重投影可能引入伪影。源坐标系必须已定义或用 -s_srs 指定。NoData 值应通过 -srcnodata 和 -dstnodata 显式处理。

# HISTORY

gdalwarp 是 **GDAL**（Geospatial Data Abstraction Library，地理空间数据抽象库）的一部分，由 Frank Warmerdam 自 **1998 年**起开发。GDAL 后来成为 OSGeo 项目，现已成长为地理空间栅格操作的基础库，被 QGIS、ArcGIS 以及众多专业工具等几乎所有 GIS 软件使用。

# INSTALL

```apt: sudo apt install gdal-bin```

```apk: sudo apk add gdal-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdal_translate](/man/gdal_translate)(1), [gdalinfo](/man/gdalinfo)(1), [ogr2ogr](/man/ogr2ogr)(1), [gdalbuildvrt](/man/gdalbuildvrt)(1)

# RESOURCES

```[Documentation](https://gdal.org/programs/gdalwarp.html)```

```[Source code](https://github.com/OSGeo/gdal)```

<!-- verified: 2026-07-15 -->
