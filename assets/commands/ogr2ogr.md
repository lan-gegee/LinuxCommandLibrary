# TAGLINE

在各种格式之间转换矢量地理空间数据

# TLDR

**将 shapefile 转换为 GeoJSON**

```ogr2ogr -f "GeoJSON" [output.json] [input.shp]```

**将 GeoJSON 转换为 GeoPackage**

```ogr2ogr -f "GPKG" [output.gpkg] [input.json]```

**将数据重投影到 WGS84**

```ogr2ogr -t_srs EPSG:4326 [output.shp] [input.shp]```

**将 shapefile 导入 PostGIS**

```ogr2ogr -f "PostgreSQL" PG:"dbname=[db]" [input.shp]```

**用 WHERE 子句过滤要素**

```ogr2ogr -where "[population > 10000]" [output.shp] [input.shp]```

**按边界框裁剪要素**

```ogr2ogr -spat [xmin] [ymin] [xmax] [ymax] [output.shp] [input.shp]```

**向已有的 PostGIS 图层追加数据**

```ogr2ogr -append -f "PostgreSQL" PG:"dbname=[db]" [input.shp]```

**选择特定字段并重命名输出图层**

```ogr2ogr -select [name,population] -nln [cities] [output.gpkg] [input.shp]```

# SYNOPSIS

**ogr2ogr** [_options_] _dst_datasource_ _src_datasource_ [_layer_]

# PARAMETERS

_DST_DATASOURCE_
> 目标数据集（文件路径、数据库连接字符串等）。

_SRC_DATASOURCE_
> 源数据集。

**-f** _FORMAT_
> 输出格式名称（如 "GeoJSON"、"ESRI Shapefile"、"PostgreSQL"、"GPKG"）。

**-t_srs** _SRS_
> 目标空间参考系统（如 EPSG:4326）。

**-s_srs** _SRS_
> 源空间参考系统（源中未定义时用于覆盖）。

**-a_srs** _SRS_
> 为输出指定空间参考系统，但不做重投影。

**-select** _FIELDS_
> 要从源中复制的字段的逗号分隔列表。

**-where** _EXPR_
> 用于过滤源要素的 SQL WHERE 子句。

**-sql** _STATEMENT_
> 针对源执行的 SQL 语句，用于选取要素。

**-spat** _XMIN_ _YMIN_ _XMAX_ _YMAX_
> 空间过滤：只选取与此边界框相交的要素。

**-clipsrc** _XMIN_ _YMIN_ _XMAX_ _YMAX_
> 将几何图形裁剪到指定的边界框或 WKT 几何。

**-overwrite**
> 若输出图层已存在则删除并重建。

**-append**
> 追加到已有图层而不是新建图层。

**-update**
> 以更新模式打开已有的目标数据源。

**-nln** _NAME_
> 为输出图层指定新名称。

**-nlt** _TYPE_
> 定义输出图层的几何类型（如 POINT、POLYGON、MULTILINESTRING）。

**-lco** _NAME=VALUE_
> 图层创建选项（因格式而异）。

**-dsco** _NAME=VALUE_
> 数据集创建选项（因格式而异）。

**-skipfailures**
> 失败后继续处理，跳过失败的要素。

**-progress**
> 在终端上显示进度条。

**-gt** _N_
> 每个事务分组 N 个要素（默认 20000）。使用数据库驱动时增大此值可获得更好的性能。

# DESCRIPTION

**ogr2ogr** 在各种文件格式、数据库和 Web 服务之间转换矢量地理空间数据。它属于 **GDAL/OGR** 库，支持 80 多种矢量格式，包括 Shapefile、GeoJSON、GeoPackage、PostGIS、KML 和 GML。

除了简单的格式转换之外，ogr2ogr 还可以在不同空间参考系统间重投影坐标、按属性或空间范围过滤要素、裁剪几何图形、选择特定字段以及转换几何类型。

# CAVEATS

属于 GDAL 套件，需要单独安装。格式支持情况取决于 GDAL 的编译方式。坐标系重投影需要正确的 SRS 定义。**-skipfailures** 选项会强制事务分组降为 1，这可能严重拖慢数据库写入速度。

# INSTALL

```apt: sudo apt install gdal-bin```

```apk: sudo apk add gdal-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ogrinfo](/man/ogrinfo)(1), [gdal_translate](/man/gdal_translate)(1), [gdalwarp](/man/gdalwarp)(1), [gdalinfo](/man/gdalinfo)(1)
