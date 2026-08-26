# TAGLINE

从 nhentai 下载画册

# TLDR

**按 ID 下载**

```nhentai --id [123456]```

**下载到指定目录**

```nhentai --id [123456] --output [downloads/]```

**以 CBZ 格式下载**

```nhentai --id [123456] --cbz```

**搜索内容**

```nhentai --search "[query]"```

**下载收藏**

```nhentai --favorites```

# SYNOPSIS

**nhentai** [_options_]

# PARAMETERS

**--id** _ID_
> 要下载的画册 ID。

**--output** _DIR_
> 输出目录。

**--cbz**
> 保存为 CBZ 归档。

**--search** _QUERY_
> 搜索画册。

**--favorites**
> 下载收藏内容。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nhentai** 用于从 nhentai 下载画册，是一款命令行下载工具。

该工具会把图片保存到本地，并支持批量下载。

# CAVEATS

面向成人内容网站。请遵守其服务条款。依赖网络连接。

# HISTORY

nhentai CLI 的创建目的是从 nhentai 网站**下载画册**。

# INSTALL

```nix: nix profile install nixpkgs#nhentai```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gallery-dl](/man/gallery-dl)(1), [wget](/man/wget)(1), [curl](/man/curl)(1)
