# TAGLINE

创建虚拟栅格镶嵌

# TLDR

**创建虚拟镶嵌**

```gdalbuildvrt [output.vrt] [input1.tif] [input2.tif]```

**从文件列表创建**

```gdalbuildvrt -input_file_list [files.txt] [output.vrt]```

**指定分辨率创建**

```gdalbuildvrt -resolution [average] [output.vrt] [*.tif]```

**覆盖已有文件创建**

```gdalbuildvrt -overwrite [output.vrt] [*.tif]```

**选择波段创建**

```gdalbuildvrt -b [1] -b [2] -b [3] [output.vrt] [input.tif]```

# SYNOPSIS

**gdalbuildvrt** [_options_] _output.vrt_ _inputs_...

# PARAMETERS

**-input_file_list** _file_
> 从文件读取输入列表。

**-resolution** _method_
> 分辨率计算方式（highest、lowest、average、user）。

**-overwrite**
> 覆盖已有的输出。

**-b** _band_
> 选择特定波段。

**-separate**
> 将每个输入放入单独的波段。

**-allow_projection_difference**
> 允许不同的投影。

**-te** _xmin ymin xmax ymax_
> 目标范围。

# DESCRIPTION

**gdalbuildvrt** 创建虚拟栅格数据集（VRT），它引用多个输入文件而不复制数据。VRT 文件是描述如何将源栅格组合成统一数据集的 XML 文档，支持即时镶嵌、堆叠和子集提取。

该工具可以将相邻的瓦片镶嵌为无缝覆盖层，或将来自不同文件的波段堆叠成多波段数据集。分辨率处理方式控制不同像素大小的输入如何组合。VRT 通过适当的标志还支持混合投影。

与创建物理镶嵌相比，虚拟数据集可以节省磁盘空间和处理时间。它非常适合处理大型瓦片集合、时间序列数据和组合方式经常变化的多光谱影像。

# INSTALL

```apt: sudo apt install gdal-bin```

```apk: sudo apk add gdal-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdaladdo](/man/gdaladdo)(1), [gdal_translate](/man/gdal_translate)(1)

# RESOURCES

```[Documentation](https://gdal.org/programs/gdalbuildvrt.html)```

```[Source code](https://github.com/OSGeo/gdal)```

<!-- verified: 2026-07-15 -->
