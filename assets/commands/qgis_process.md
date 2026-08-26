# TAGLINE

从命令行运行 QGIS Processing 算法

# TLDR

**列出所有可用的** processing 算法

```qgis_process list```

**显示指定算法的帮助**

```qgis_process help [algorithm_id]```

**对矢量图层执行缓冲区**操作

```qgis_process run native:buffer -- INPUT=[input.shp] DISTANCE=[10] OUTPUT=[buffered.shp]```

**以 JSON 输出运行**算法

```qgis_process run [algorithm_id] --json -- [PARAM]=[VALUE]```

**列出可用插件**及其状态

```qgis_process plugins```

**启用插件**提供者（例如 GRASS）

```qgis_process plugins enable [grassprovider]```

# SYNOPSIS

**qgis_process** [_--json_] [_--verbose_] [_--no-python_] [_--skip-loading-plugins_] \<_command_\> [_algorithm_id_] [**--** _PARAM=VALUE ..._]

# PARAMETERS

**list**
> 列出所有可用的 processing 算法，按提供者分组。

**help** _algorithm_id_
> 显示特定算法的帮助和参数说明。

**run** _algorithm_id_ [**--** _PARAM=VALUE ..._]
> 以给定参数执行算法。参数跟在 **--** 之后，采用 **KEY=VALUE** 语法。结尾的 **-** 表示从 stdin 以 JSON 形式读取参数。

**plugins**
> 列出可用且处于激活状态的 processing 提供者插件。

**plugins enable** _name_
> 激活指定的插件提供者。

**plugins disable** _name_
> 停用指定的插件提供者。

**--json**
> 以 JSON 格式输出。

**--verbose**
> 启用详细日志输出。

**--no-python**
> 禁用 Python 支持，加快启动速度。

**--skip-loading-plugins**
> 跳过插件加载，加快启动速度。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本详情。

# DESCRIPTION

**qgis_process** 是一个独立的命令行工具，无需启动 QGIS 图形界面即可运行 QGIS Processing 算法。它让你在终端中使用完整的 Processing 框架，包括原生 QGIS 算法、GDAL、GRASS GIS、SAGA 以及任何第三方插件算法。

借助该工具，可以通过 shell 脚本批量处理地理空间数据、用 cron 任务实现自动化、与外部工具和流水线集成，以及在无头服务器上运行地理处理工作流。算法参数放在 **--** 分隔符之后，采用 **PARAM=VALUE** 语法，重复的参数构成有序列表。特殊参数包括 **--ELLIPSOID**、**--PROJECT_PATH**、**--distance_units** 和 **--area_units**，用于控制坐标参考和测量设置。

该工具随 QGIS 3.14 及更高版本的标准安装一同提供。

# CONFIGURATION

在没有显示器的无头服务器上，先设置环境变量再运行：

```export QT_QPA_PLATFORM=offscreen```

在从未启动过 QGIS 图形界面的全新安装中，GRASS 或 SAGA 等插件提供者可能需要显式启用：

```qgis_process plugins enable grassprovider```

只有 metadata.txt 中含有 **hasProcessingProvider=yes** 的插件才会被识别。

# CAVEATS

在无头系统上必须设置 **QT_QPA_PLATFORM=offscreen**，否则工具无法启动。在从未启动过 QGIS 图形界面的系统上，processing 提供者插件（GRASS、SAGA）不会自动加载，必须手动启用。加载 Python 和插件会增加启动开销；不需要这些功能时可用 **--no-python** 和 **--skip-loading-plugins**。此工具只暴露 Processing 框架，不能替代完整的 QGIS 桌面应用程序。

# HISTORY

**qgis_process** 由 **Nyall Dawson** 于 **2019 年 2 月**作为 QGIS Enhancement Proposal #140 提出，最初命名为 **qgis_transform**，后经社区讨论更名。该项目由瑞典 QGIS 用户组赞助。相关 pull request 于 **2020 年 4 月**合并，该工具随 **QGIS 3.14 "Pi"** 于 **2020 年 6 月**首次发布。此后在后续版本中持续增强，陆续加入插件管理和 JSON 输入输出等功能。

# INSTALL

```apt: sudo apt install qgis```

```dnf: sudo dnf install qgis```

```pacman: sudo pacman -S qgis```

```zypper: sudo zypper install qgis```

```nix: nix profile install nixpkgs#qgis```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qgis](/man/qgis)(1), [gdalinfo](/man/gdalinfo)(1), [ogr2ogr](/man/ogr2ogr)(1), [ogrinfo](/man/ogrinfo)(1), [gdalwarp](/man/gdalwarp)(1), [gdal_translate](/man/gdal_translate)(1)
