# TAGLINE

分析并可视化地形高程

# TLDR

**从 DEM 生成山体阴影**

```gdaldem hillshade [dem.tif] [hillshade.tif]```

**创建以度为单位的坡度图**

```gdaldem slope [dem.tif] [slope.tif]```

**生成坡向图**

```gdaldem aspect [dem.tif] [aspect.tif]```

**使用颜色表文件创建彩色地貌渲染**

```gdaldem color-relief [dem.tif] [colors.txt] [relief.tif]```

**用自定义**光照方向和高度角生成山体阴影

```gdaldem hillshade -az [315] -alt [45] [dem.tif] [hillshade.tif]```

**计算地形崎岖度指数（TRI）**

```gdaldem TRI [dem.tif] [tri.tif]```

# SYNOPSIS

**gdaldem** _mode_ [_options_] _input_ _output_

# PARAMETERS

_MODE_
> 操作模式：hillshade、slope、aspect、color-relief、TRI、TPI、roughness。

_INPUT_
> 输入的 DEM 栅格。

_OUTPUT_
> 输出的栅格文件。

**-az** _DEGREES_
> 山体阴影的光照方位角。

**-alt** _DEGREES_
> 山体阴影的光照高度角。

**-s** _SCALE_
> 垂直单位与水平单位之比（例如度坐标配合英尺时为 111120）。

**-z** _FACTOR_
> 垂直夸张系数。

**-of** _FORMAT_
> 输出栅格格式（默认：GTiff）。

**-compute_edges**
> 在栅格边缘和 nodata 边界处也计算数值。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gdaldem** 分析和可视化数字高程模型。它生成多种地形衍生产品，包括山体阴影、坡度、坡向以及各种崎岖度指数。

该工具从原始高程数据生成可直接用于可视化的输出。山体阴影营造逼真的地形光照效果。坡度和坡向则服务于地形分析。

gdaldem 是制图地形表达和地貌分析的重要工具。

# CAVEATS

要求 DEM 具备正确的比例尺度。边界处存在边缘效应。大文件需要更多内存。

# HISTORY

gdaldem 是 **GDAL**（Geospatial Data Abstraction Library，地理空间数据抽象库）的一部分，提供用于地形可视化与分析的 DEM 分析工具。

# INSTALL

```apt: sudo apt install gdal-bin```

```apk: sudo apk add gdal-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdal_contour](/man/gdal_contour)(1), [gdalinfo](/man/gdalinfo)(1), [ogr2ogr](/man/ogr2ogr)(1)
