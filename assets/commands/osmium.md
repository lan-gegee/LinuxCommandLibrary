# TAGLINE

处理 OpenStreetMap 数据的命令行工具

# TLDR

**从 OSM 文件提取区域**

```osmium extract -b [left],[bottom],[right],[top] [input.osm.pbf] -o [output.osm.pbf]```

**转换格式**

```osmium cat [input.osm.pbf] -o [output.osm.xml]```

**合并多个文件**

```osmium merge [file1.osm.pbf] [file2.osm.pbf] -o [merged.osm.pbf]```

**按标签过滤**

```osmium tags-filter [input.osm.pbf] -o [output.osm.pbf] nwr/[highway]```

**显示文件信息**

```osmium fileinfo [file.osm.pbf]```

**检查文件完整性**

```osmium check-refs [file.osm.pbf]```

**排序 OSM 数据**

```osmium sort [input.osm] -o [sorted.osm]```

**获取文件之间的差异**

```osmium diff [old.osm.pbf] [new.osm.pbf]```

**使用多边形文件提取**

```osmium extract -p [boundary.poly] [input.osm.pbf] -o [output.osm.pbf]```

**应用 OsmChange 文件**

```osmium apply-changes [input.osm.pbf] [changes.osc] -o [output.osm.pbf]```

# SYNOPSIS

**osmium** _command_ [_-o output_] [_options_] _files_

# PARAMETERS

**cat**
> 连接/转换文件。

**extract**
> 从文件中提取区域。

**merge**
> 合并已排序的文件。

**tags-filter**
> 按标签过滤。

**sort**
> 排序 OSM 数据。

**diff**
> 比较文件。

**fileinfo**
> 显示文件信息。

**check-refs**
> 检查引用完整性。

**apply-changes**
> 应用 OsmChange 文件。

**renumber**
> 重新编号对象 ID。

**getid**
> 按 ID 获取对象。

**time-filter**
> 按时间戳过滤。

**-o** _FILE_
> 输出文件。

**-b** _BBOX_
> 边界框（left,bottom,right,top）。

**-p** _POLYGON_
> 用于提取的多边形文件。

**--overwrite**
> 覆盖已有的输出。

**-f** _FORMAT_
> 输出格式。

**-v**, **--verbose**
> 详细输出。

**--progress**
> 显示进度条。

**-e** _STRATEGY_, **--strategy** _STRATEGY_
> 提取策略：simple、complete_ways 或 smart。

# DESCRIPTION

**osmium** 是一款处理 OpenStreetMap 数据的命令行工具，可以高效地处理、过滤和变换 OSM 文件。

extract 可从较大的文件创建区域子集。边界框定义矩形区域。多边形文件则支持提取行政边界等复杂形状。

tags-filter 可创建仅包含特定要素类型的文件。标签表达式可以选择公路、建筑物、兴趣点或自定义组合。

merge 将多个文件合并为一个，并能正确处理重叠数据。合并要求文件已排序。sort 命令用于对未排序的数据进行预处理。

格式转换支持 PBF（Protocol Buffer 二进制格式）、OSM XML 和 OPL（Object Per Line）格式。PBF 经过压缩且高效；XML 则便于人类阅读。

diff 展示不同文件版本之间的变化，适合跟踪地图编辑历史。

# CAVEATS

大文件需要大量内存。某些操作要求输入已排序。提取可能包含不完整的 relation。复杂过滤器有一定学习曲线。

# HISTORY

**osmium** 和 libosmium 库由 **Jochen Topf** 自 **2013 年**前后开始开发。它凭借更好的性能和可靠性取代了较旧的工具，成为处理 OSM 数据的标准命令行工具。

# INSTALL

```apt: sudo apt install osmium-tool```

```dnf: sudo dnf install osmium-tool```

```brew: brew install osmium-tool```

```nix: nix profile install nixpkgs#osmium-tool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[osm2pgsql](/man/osm2pgsql)(1), [osmconvert](/man/osmconvert)(1), [ogr2ogr](/man/ogr2ogr)(1)
