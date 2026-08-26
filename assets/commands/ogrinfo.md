# TAGLINE

显示矢量数据信息

# TLDR

**列出数据源的图层和摘要**

```ogrinfo [file.shp]```

**仅查看特定图层的摘要**（不含要素）

```ogrinfo -so [file.shp] [layer_name]```

**转储所有图层和所有要素**

```ogrinfo -al [file.shp]```

**按 FID 显示单个要素**

```ogrinfo [file.shp] [layer_name] -fid [feature_id]```

**用 WHERE 子句过滤要素**

```ogrinfo -al -where "[field = 'value']" [file.shp]```

**执行 SQL 查询**

```ogrinfo [file.shp] -sql "[SELECT * FROM layer]"```

**以 JSON 输出**

```ogrinfo -json [file.shp]```

# SYNOPSIS

**ogrinfo** [_options_] _datasource_ [_layer_ ...]

# PARAMETERS

_DATASOURCE_
> OGR 支持的矢量数据源（文件、目录、连接字符串或 URL）。

_LAYER_
> 要报告的一个或多个图层名。配合 **-al** 使用且省略时，报告所有图层。

**-al**
> 列出所有图层的所有要素（与 **-so** 相对）。

**-so**
> 仅摘要：省略逐个要素的报告。

**-fl**
> 启用要素列举（与 **-so** 相对）。

**-json**
> 以 JSON 格式输出报告。

**-fid** _ID_
> 只报告具有给定 FID 的要素。

**-sql** _STATEMENT_
> 执行 SQL 语句并返回结果。也可以是 @filename 引用。

**-dialect** _DIALECT_
> 使用的 SQL 方言（如 OGRSQL、SQLITE）。

**-where** _QUERY_
> 应用于每个图层的属性过滤器。

**-spat** _xmin_ _ymin_ _xmax_ _ymax_
> 空间过滤：只报告与此边界框相交的要素。

**-geom** _{YES|NO|SUMMARY|WKT|ISO_WKT}_
> 几何信息的报告方式（默认：YES）。

**-limit** _N_
> 限制每个图层的要素数量。

**-if** _FORMAT_
> 打开输入时强制使用特定驱动。

**-oo** _NAME=VALUE_
> 向驱动传递数据集打开选项。

**-ro**
> 以只读模式打开数据源。

**-nomd**
> 不打印元数据。

**-listmdd**
> 列出数据集可用的所有元数据域。

**-mdd** _domain_
> 报告指定域的元数据。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ogrinfo** 将 OGR 支持的矢量数据源的信息列出到标准输出。它报告图层、模式（schema）、坐标参考系统、范围、要素数量，也可以选择输出要素本身。通过 **-sql** 执行 SQL 语句，它还能编辑受支持驱动的数据。

# CAVEATS

属于 GDAL 套件。格式支持取决于你的 GDAL 构建中编译了哪些 OGR 驱动；可用 `ogrinfo --formats` 查看。对超大数据集使用 **-al** 可能产生海量输出。

# HISTORY

**ogrinfo** 随 **GDAL/OGR** 一同发布，后者是由 **OSGeo** 基金会维护的开源地理空间数据库。OGR 最初是一个独立的矢量数据库，在 2.0 版本中并入 GDAL。

# INSTALL

```apt: sudo apt install gdal-bin```

```apk: sudo apk add gdal-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ogr2ogr](/man/ogr2ogr)(1), [gdalinfo](/man/gdalinfo)(1)
