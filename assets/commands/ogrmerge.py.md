# TAGLINE

合并矢量数据集

# TLDR

**合并 shapefile**

```ogrmerge.py -o [output.shp] [input1.shp] [input2.shp]```

**合并为 GeoPackage**

```ogrmerge.py -f GPKG -o [output.gpkg] [*.shp]```

**合并为单一图层**

```ogrmerge.py -single -o [output.shp] [*.shp]```

**覆盖输出文件**

```ogrmerge.py -overwrite_ds -o [output.shp] [input*.shp]```

**指定坐标参考系统**

```ogrmerge.py -a_srs [EPSG:4326] -o [output.shp] [*.shp]```

**将源图层名作为字段合并**

```ogrmerge.py -single -src_layer_field_name [source] -o [output.gpkg] [*.shp]```

# SYNOPSIS

**ogrmerge.py** [_options_] -o _output_ _inputs_...

# PARAMETERS

**-o** _FILE_
> 输出文件。

**-f** _FORMAT_
> 输出格式。

**-single**
> 合并为单一图层。

**-overwrite_ds**
> 覆盖已有的输出。

**-a_srs** _SRS_
> 指定坐标参考系统。

**-src_layer_field_name** _NAME_
> 添加一个记录源图层名的字段（与 -single 配合使用）。

**-src_layer_field_content** _CONTENT_
> 指定源图层字段的内容。

**-nln** _NAME_
> 合并后输出图层的名称（与 -single 配合使用）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ogrmerge.py** 用于合并矢量数据集，把多个文件组合成一个。

该脚本用于整合地理空间数据，属于 GDAL Python 实用工具的一部分。

# CAVEATS

属于 GDAL。是 Python 脚本。合并为单一图层时要求各输入的模式兼容。

# HISTORY

ogrmerge.py 被加入 **GDAL**，用于便捷地合并矢量数据。

# INSTALL

```apt: sudo apt install gdal-bin```

```apk: sudo apk add gdal-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ogr2ogr](/man/ogr2ogr)(1), [ogrinfo](/man/ogrinfo)(1), [gdalinfo](/man/gdalinfo)(1)
