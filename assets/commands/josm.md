# TAGLINE

Java OpenStreetMap 编辑器，功能丰富的桌面编辑应用

# TLDR

**启动 JOSM 编辑器**

```josm```

**打开 OSM 文件**

```josm [file.osm]```

**按边界框下载区域**

```josm --download=[minlat],[minlon],[maxlat],[maxlon]```

**以离线模式启动**

```josm --offline=all```

**设置窗口几何参数**

```josm --geometry=[800]x[600]+[100]+[100]```

# SYNOPSIS

**josm** [_options_] [_file_...]

# PARAMETERS

**--download=**_bounds_
> 下载边界框范围（minlat,minlon,maxlat,maxlon）。

**--downloadgps=**_bounds_
> 下载该区域的 GPS 轨迹。

**--offline=**_mode_
> 以离线模式启动（osm_api、josm_website、all）。

**--geometry=**_WxH+X+Y_
> 设置窗口大小和位置。

**--language=**_lang_
> 设置界面语言。

**--selection=**_query_
> 选中匹配搜索条件的对象。

**--version**
> 显示版本信息。

# DESCRIPTION

**josm** 即 Java OpenStreetMap Editor（Java 版 OpenStreetMap 编辑器），是一款功能丰富的桌面应用程序，用于编辑 OpenStreetMap 数据。它支持加载和保存 OSM 数据文件、GPS 轨迹和影像图层，并提供高级制图编辑工具。

# INSTALL

```pacman: sudo pacman -S josm```

```nix: nix profile install nixpkgs#josm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[osmium](/man/osmium)(1), [osm2pgsql](/man/osm2pgsql)(1)
