# TAGLINE

转换和过滤 OpenStreetMap 数据文件

# TLDR

**将 PBF 转换为 OSM XML**

```osmconvert [input.pbf] -o=[output.osm]```

**将 OSM 转换为 PBF**

```osmconvert [input.osm] -o=[output.pbf]```

**按边界框提取**

```osmconvert [input.pbf] -b=[lon1,lat1,lon2,lat2] -o=[output.pbf]```

**按多边形过滤**

```osmconvert [input.pbf] -B=[polygon.poly] -o=[output.pbf]```

**合并文件**

```osmconvert [file1.pbf] [file2.pbf] -o=[merged.pbf]```

**显示统计信息**

```osmconvert [input.pbf] --out-statistics```

# SYNOPSIS

**osmconvert** [_options_] _input_... [-o=_output_]

# PARAMETERS

**-o** _file_
> 输出文件。

**-b** _bbox_
> 边界框过滤器。

**-B** _file_
> 多边形文件过滤器。

**--drop-author**
> 移除作者信息。

**--drop-version**
> 移除版本信息。

**--complete-ways**
> 保留完整的 way。

**--out-statistics**
> 显示统计信息。

# DESCRIPTION

**osmconvert** 用于转换和过滤 OpenStreetMap 数据文件。它支持在 OSM XML、PBF 和 O5M 格式之间转换，并可按边界框或多边形提取区域。

# BOUNDING BOX FORMAT

```
-b=min_lon,min_lat,max_lon,max_lat
-b=-74.1,40.5,-73.7,40.9  # NYC area
```

# CAVEATS

处理大文件时内存占用较高。多边形文件须为 .poly 格式。PBF 格式效率最高。

# HISTORY

osmconvert 由 **Markus Weber** 开发，是针对常见 OSM 数据操作任务的 osmosis 快速替代品。

# INSTALL

```apt: sudo apt install osmctools```

```dnf: sudo dnf install osmctools```

```nix: nix profile install nixpkgs#osmctools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[osm2pgsql](/man/osm2pgsql)(1)
