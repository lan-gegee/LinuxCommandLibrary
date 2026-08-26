# TAGLINE

开源地理信息系统

# TLDR

**启动 QGIS**

```qgis```

**打开指定的项目文件**

```qgis --project [path/to/project.qgs]```

**打开 QGIS 并加载指定图层**

```qgis [path/to/file.shp] [path/to/raster.tif]```

**将地图快照导出**为图像文件

```qgis --snapshot [output.png] --width [1024] --height [768] --project [project.qgs]```

**启动时不显示启动画面**且不加载插件

```qgis --nologo --noplugins```

**将项目图层导出为 DXF**

```qgis --dxf-export [output.dxf] --project [project.qgs]```

**使用指定的用户配置文件**

```qgis --profile [profilename]```

**启动时运行 Python 脚本**

```qgis --code [path/to/script.py]```

# SYNOPSIS

**qgis** [_options_] [_file_ ...]

# PARAMETERS

**-p**, **--project** _projectfile_
> 加载给定的 QGIS 项目文件。

**-s**, **--snapshot** _filename_
> 将已加载数据集的快照输出到指定图像文件。

**-w**, **--width** _width_
> 快照的宽度。

**-h**, **--height** _height_
> 快照的高度。

**-e**, **--extent** _xmin,ymin,xmax,ymax_
> 设置初始地图范围。

**-n**, **--nologo**
> 启动时隐藏启动画面。

**-V**, **--noversioncheck**
> 启动时不检查新版本。

**-P**, **--noplugins**
> 启动时不恢复插件。

**--nopython**
> 完全禁用 Python 支持。

**-B**, **--skipbadlayers**
> 缺失图层时不弹出提示。

**-C**, **--nocustomization**
> 不应用 GUI 自定义设置。

**-z**, **--customizationfile** _path_
> 使用给定的 ini 文件作为 GUI 自定义配置。

**-f**, **--code** _path_
> 加载时运行给定的 Python 文件。

**--profile** _name_
> 从 profiles 文件夹加载指定的命名配置。

**-S**, **--profiles-path** _path_
> 存储用户 profile 文件夹的路径。

**-l**, **--lang** _language_
> 界面使用指定的语言。

**-d**, **--defaultui**
> 将用户界面设置重置为默认值。

**--hide-browser**
> 隐藏浏览器部件。

**--dxf-export** _filename.dxf_
> 将已加载的数据集输出为 DXF。

**--dxf-extent** _xmin,ymin,xmax,ymax_
> 设置 DXF 导出的范围。

**--dxf-symbology-mode** _mode_
> DXF 导出的符号模式：none、symbollayer 或 feature。

**-v**, **--version**
> 显示版本信息并退出。

**--help**
> 显示帮助文本。

# DESCRIPTION

**QGIS** 是一个跨平台、免费开源的地理信息系统，基于 GNU GPLv2+ 许可证授权。它支持地理空间数据的查看、编辑和分析。QGIS 主要用 C++ 编写并基于 Qt 框架，同时具备丰富的 Python 插件支持。

QGIS 可以处理矢量格式（Shapefiles、GeoJSON、GML、KML、GeoPackage、PostGIS 以及所有 OGR 支持的格式）、栅格格式（GeoTIFF、ERDAS IMG 以及所有 GDAL 支持的格式）和数据库数据源。它与 GRASS GIS 集成以提供高级分析功能，并使用 GDAL/OGR 进行数据格式转换。其特性包括地图制图、空间分析、数字化、地理处理，以及丰富的插件生态。

如需无头模式或批处理，请改用配套工具 **qgis_process**。

# CONFIGURATION

用户设置存储在 **~/.config/QGIS/qgis.conf** 中。QGIS 支持多个用户 profile，每个 profile 拥有独立的设置、插件和项目模板。使用 **--profile** 在各 profile 间切换，或使用 **--profiles-path** 指定自定义的 profiles 目录。

# CAVEATS

QGIS 主要是一个 GUI 应用程序；命令行用法仅限于带选项启动、截取快照以及 DXF 导出。Python 插件可能影响启动时间；需要更快启动时可用 **--noplugins** 或 **--nopython**。包含大量图层的大型项目会消耗大量内存。QGIS 2.x 的 **--configpath** 选项在 QGIS 3.x 中已被 **--profiles-path** 取代。

# HISTORY

开发始于 **2002 年 2 月**，由 **Gary Sherman** 发起，项目最初名为 **Quantum GIS**，起初只是 Linux 上一个简单的 PostGIS 数据查看器。首个公开发布版本于 **2002 年 7 月**推出。**2007 年**它成为 **OSGeo** 孵化项目，1.0 版本于 **2009 年 1 月**发布。**2013 年 9 月**发布 2.0 版本，项目正式由 Quantum GIS 更名为 **QGIS**。Gary Sherman 因其对开源 GIS 的贡献于 **2014 年**获得 **Sol Katz 奖**。

# INSTALL

```apt: sudo apt install qgis```

```dnf: sudo dnf install qgis```

```pacman: sudo pacman -S qgis```

```zypper: sudo zypper install qgis```

```nix: nix profile install nixpkgs#qgis```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdalinfo](/man/gdalinfo)(1), [ogr2ogr](/man/ogr2ogr)(1), [ogrinfo](/man/ogrinfo)(1), [gdalwarp](/man/gdalwarp)(1), [gdal_translate](/man/gdal_translate)(1)
