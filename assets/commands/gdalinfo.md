# TAGLINE

显示栅格数据集信息

# TLDR

**显示栅格信息**

```gdalinfo [file.tif]```

**显示统计信息**

```gdalinfo -stats [file.tif]```

**以 JSON 格式显示**

```gdalinfo -json [file.tif]```

**检查特定数据集**

```gdalinfo [file.vrt]```

**显示元数据**

```gdalinfo -mm [file.tif]```

# SYNOPSIS

**gdalinfo** [_options_] _datasetname_

# PARAMETERS

_DATASETNAME_
> 输入的栅格文件。

**-json**
> 以 JSON 格式输出。

**-stats**
> 计算并显示统计信息。

**-mm**
> 计算最小值/最大值。

**-hist**
> 计算直方图。

**-nogcp**
> 不输出 GCP（地面控制点）。

**-nomd**
> 不输出元数据。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gdalinfo** 显示栅格数据集的信息。它会列出地理空间栅格文件的格式、尺寸、坐标系、波段和元数据。

该工具读取文件头信息，并可选择计算统计值。它通过 GDAL 驱动支持数百种栅格格式。

gdalinfo 是理解和校验地理空间栅格数据的第一步。

# CAVEATS

统计信息计算会读取整个文件。某些格式的元数据有限。大文件可能较慢。

# HISTORY

gdalinfo 是 **GDAL**（Geospatial Data Abstraction Library，地理空间数据抽象库）的一部分，提供对数百种格式的栅格检查能力。

# INSTALL

```apt: sudo apt install gdal-bin```

```apk: sudo apk add gdal-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdalwarp](/man/gdalwarp)(1), [gdal_translate](/man/gdal_translate)(1), [ogrinfo](/man/ogrinfo)(1)

# RESOURCES

```[Documentation](https://gdal.org/programs/gdalinfo.html)```

```[Source code](https://github.com/OSGeo/gdal)```

<!-- verified: 2026-07-15 -->
