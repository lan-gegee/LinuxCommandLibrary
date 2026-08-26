# TAGLINE

从栅格数据生成网络地图瓦片

# TLDR

**从图像生成瓦片**

```gdal2tiles.py [input.tif] [output_dir]```

**指定缩放级别**

```gdal2tiles.py -z [5-18] [input.tif] [output_dir]```

**为 Leaflet 生成**

```gdal2tiles.py -w leaflet [input.tif] [output_dir]```

**使用多进程**

```gdal2tiles.py --processes=[4] [input.tif] [output_dir]```

**指定瓦片格式**

```gdal2tiles.py --tileformat=[png] [input.tif] [output_dir]```

# SYNOPSIS

**gdal2tiles.py** [_options_] _input_ _output_directory_

# PARAMETERS

_INPUT_
> 输入栅格文件（GeoTIFF 等）。

_OUTPUT_DIRECTORY_
> 输出瓦片的目录。

**-z** _LEVELS_
> 缩放级别（例如 5-18）。

**-w** _WEBVIEWER_
> Web 查看器：leaflet、openlayers、none。

**--processes** _N_
> 并行处理。

**--tileformat** _FORMAT_
> 瓦片格式：png、jpeg、webp。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gdal2tiles.py** 从带有地理参考的栅格图像生成地图瓦片。它创建与 Leaflet 和 OpenLayers 等 Web 地图库兼容的瓦片金字塔。

该工具生成 XYZ 或 TMS 瓦片结构，并可选择生成 HTML 查看器页面。它通过以适当重采样方式生成多个缩放级别来处理大图。

gdal2tiles.py 让大型地理空间影像可以作为 Web 地图瓦片提供服务。

# CAVEATS

大图需要大量磁盘空间。处理时间随缩放级别增加。源数据必须具有地理参考。

# HISTORY

gdal2tiles.py 是 **GDAL**（Geospatial Data Abstraction Library，地理空间数据抽象库）的一部分，用于从地理空间栅格数据生成 Web 地图瓦片。

# INSTALL

```apt: sudo apt install gdal-bin```

```apk: sudo apk add gdal-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdalinfo](/man/gdalinfo)(1), [gdal_translate](/man/gdal_translate)(1)

# RESOURCES

```[Documentation](https://gdal.org/programs/gdal2tiles.html)```

```[Source code](https://github.com/OSGeo/gdal)```

<!-- verified: 2026-07-15 -->
