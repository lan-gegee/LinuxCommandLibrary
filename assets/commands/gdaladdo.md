# TAGLINE

构建栅格概览金字塔

# TLDR

**构建概览**

```gdaladdo [image.tif]```

**构建指定级别**

```gdaladdo [image.tif] [2] [4] [8] [16]```

**使用平均重采样构建**

```gdaladdo -r average [image.tif]```

**构建外部概览**

```gdaladdo -ro [image.tif]```

**带压缩构建**

```gdaladdo --config COMPRESS_OVERVIEW JPEG [image.tif]```

# SYNOPSIS

**gdaladdo** [_options_] _filename_ [_levels_...]

# PARAMETERS

**-r** _method_
> 重采样方法（nearest、average、gauss、cubic）。

**-ro**
> 创建外部概览文件。

**--config** _key_ _value_
> 设置配置选项。

**-b** _band_
> 仅为特定波段构建。

**-clean**
> 移除现有概览。

# DESCRIPTION

**gdaladdo** 为栅格数据集构建或重建概览图像（也称为金字塔）。概览是原始图像在多个分辨率下的降采样版本，可在不同缩放级别下高效显示和处理。

不指定级别时，该工具会生成默认金字塔。自定义级别定义降采样因子（例如 2、4、8 表示二分之一、四分之一、八分之一分辨率）。不同的重采样方法会影响质量和性能：nearest 最快，average 产生更平滑的结果，cubic 质量最高。

概览可以存储在文件内部，也可以作为单独的 .ovr 附带文件存储。压缩设置可减小概览文件大小。对于 GIS 应用和 Web 地图服务中处理大型影像而言，gdaladdo 至关重要。

# INSTALL

```apt: sudo apt install gdal-bin```

```apk: sudo apk add gdal-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdal_translate](/man/gdal_translate)(1), [gdalinfo](/man/gdalinfo)(1)

# RESOURCES

```[Documentation](https://gdal.org/programs/gdaladdo.html)```

```[Source code](https://github.com/OSGeo/gdal)```

<!-- verified: 2026-07-15 -->
