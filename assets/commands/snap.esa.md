# TAGLINE

ESA 卫星数据处理平台

# TLDR

显示所有**可用更新**

```snap --nosplash --nogui --modules --list --refresh```

显示**帮助**

```snap --help```

**无启动画面**启动

```snap --nosplash```

以**无界面模式**启动

```snap --nogui```

# SYNOPSIS

**snap** [_OPTIONS_]

# PARAMETERS

**--nosplash**
> 启动时不显示启动画面

**--nogui**
> 以无界面/命令行模式运行

**--modules**
> 进入模块管理

**--list**
> 列出可用条目

**--refresh**
> 检查更新

**--help**
> 显示帮助信息

# DESCRIPTION

**SNAP**（Sentinel Application Platform）是 ESA（欧洲空间局）用于处理和分析卫星数据的工具箱。它为来自 Sentinel 卫星及其他任务的地球观测数据提供可视化、分析和处理能力。

该平台支持多种数据格式，包含辐射校正、几何校正、滤波和数据融合等工具。它既可以通过图形界面操作，也可以通过命令行进行批处理。

# CAVEATS

需要 Java 运行时环境。大型卫星数据集对内存和存储要求很高。某些处理操作计算量很大。不要与 Ubuntu/Canonical 的 **snap** 软件包管理器混淆。

# HISTORY

**SNAP** 由**欧洲空间局**开发，是运营 Sentinel 卫星舰队的哥白尼计划的一部分。该平台由 ESA 更早的工具箱（BEAM、NEST）演化而来，发布后用于支持自 **2014 年**起陆续发射的 Sentinel-1、Sentinel-2 和 Sentinel-3 任务。它作为开源软件免费提供。

# SEE ALSO

[gdalinfo](/man/gdalinfo)(1), [gdal_translate](/man/gdal_translate)(1)
