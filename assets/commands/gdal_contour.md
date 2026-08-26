# TAGLINE

从高程数据生成等高线

# TLDR

**生成等高线**

```gdal_contour -a [elev] -i [10] [dem.tif] [contours.shp]```

**指定间隔**

```gdal_contour -i [100] [dem.tif] [contours.shp]```

**固定等高线级别**

```gdal_contour -fl [100] [500] [1000] [dem.tif] [contours.shp]```

**输出为 GeoJSON**

```gdal_contour -f "GeoJSON" -i [10] [dem.tif] [contours.geojson]```

**生成三维等高线多边形**

```gdal_contour -p -3d -a [elev] -i [50] [dem.tif] [contours.shp]```

# SYNOPSIS

**gdal_contour** [_options_] _input_ _output_

# PARAMETERS

_INPUT_
> 输入的高程栅格（DEM）。

_OUTPUT_
> 输出的矢量文件。

**-a** _NAME_
> 高程属性的名称。

**-i** _INTERVAL_
> 等高线间隔。

**-fl** _LEVELS_
> 固定的等高线级别。

**-f** _FORMAT_
> 输出格式。

**-b** _BAND_
> 源波段编号（默认：1）。

**-3d**
> 强制生成三维矢量而非二维。

**-p**
> 生成等高线多边形而非等高线。

**-off** _OFFSET_
> 相对零点的偏移量，用于解释间隔。

**-snodata** _VALUE_
> 要忽略的输入 nodata 值。

**-nln** _NAME_
> 输出图层名称。

**-q**
> 安静模式，抑制进度输出。

# DESCRIPTION

**gdal_contour** 从高程栅格（DEM）生成等高线。它创建表示等高线的矢量要素。

该工具支持规则间隔或指定级别的等高线。输出包含用于标注的高程属性。支持多种输出格式。

gdal_contour 用于制图、地形分析和高程数据可视化。

# CAVEATS

质量取决于 DEM 分辨率。密集的等高线可能较慢。输出大小随复杂程度而变化。

# HISTORY

gdal_contour 是 **GDAL**（Geospatial Data Abstraction Library，地理空间数据抽象库）的一部分，用于从数字高程模型生成等高线以供制图和分析。

# INSTALL

```apt: sudo apt install gdal-bin```

```apk: sudo apk add gdal-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdaldem](/man/gdaldem)(1), [gdalinfo](/man/gdalinfo)(1), [ogr2ogr](/man/ogr2ogr)(1)
