# TAGLINE

终端中的盲文与 ASCII 世界地图渲染器

# TLDR

**启动交互式世界地图**

```mapscii```

**通过 telnet 连接**，无需安装

```telnet mapscii.me```

# SYNOPSIS

**mapscii** [_options_]

# DESCRIPTION

**mapscii** 是一个基于 node.js 的矢量瓦片到盲文/ASCII 渲染器，它使用 OpenStreetMap 数据把交互式世界地图带到你的终端中。你可以用方向键或鼠标拖动来平移，用 **a**/**z** 键或鼠标滚轮缩放，并按 **c** 在 Unicode 盲文和原始 ASCII 渲染之间切换。

该地图支持 Mapbox Styles 以自定义图层样式，并可连接到任何公开或私有的矢量瓦片服务器。它还支持离线使用本地 VectorTile/MBTiles 数据源。

# CAVEATS

盲文渲染需要支持 Unicode 的终端和字体。细节程度取决于终端大小和缩放级别。

# HISTORY

**mapscii** 由 **rastapasta** 创建，使用 **JavaScript**（Node.js）编写。无需安装即可通过 `telnet mapscii.me` 远程访问。

# INSTALL

```brew: brew install mapscii```

```nix: nix profile install nixpkgs#mapscii```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[telnet](/man/telnet)(1)
