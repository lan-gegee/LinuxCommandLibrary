# TAGLINE

基于 Go 的 Immich 替代 CLI

# TLDR

**上传照片**

```immich-go upload [/path/to/photos]```

**上传 Google Photos Takeout 归档**

```immich-go upload --google-photos [takeout.zip]```

**按文件夹创建相册**

```immich-go upload --create-album-folder [/path/to/photos]```

**试运行以预览上传**

```immich-go upload --dry-run [/path/to/photos]```

**设置服务器和 API 密钥**

```immich-go upload --server [url] --api-key [api-key] [/path/to/photos]```

**带日期范围过滤上传**

```immich-go upload --date-range [2023-01-01,2023-12-31] [/path/to/photos]```

# SYNOPSIS

**immich-go** _command_ [_options_] _path_

# PARAMETERS

**upload**
> 将文件上传到 Immich 服务器。

**archive**
> 将资产从 Immich 服务器导出到本地存储。

**stack**
> 将相关照片整理为堆叠（RAW+JPEG 组合、连拍等）。

**--server** _URL_
> Immich 服务器 URL。

**--api-key** _KEY_
> 用于身份验证的 API 密钥。

**--google-photos**
> 解析 Google Photos Takeout 归档。

**--icloud**
> 解析 iCloud 照片导出。

**--create-album-folder**
> 根据文件夹名称创建相册。

**--dry-run**
> 模拟上传，不做实际更改。

**--date-range** _RANGE_
> 仅上传日期范围内的照片。

**--help**
> 显示帮助信息。

# DESCRIPTION

**immich-go** 是一个基于 Go 的替代 CLI，用于 Immich 自托管照片管理服务器。它提供高效的批量上传，支持 Google Photos Takeout、iCloud 导出和 Picasa 归档。

该工具能从多种元数据来源解析日期，包括 EXIF、JSON sidecar 文件和文件名。它以单个二进制文件分发，没有运行时依赖，与官方基于 Node.js 的 CLI 相比，在大批量上传时部署更快、更简单。

# CAVEATS

非官方社区工具，不由 Immich 项目维护。需要正在运行的 Immich 服务器和有效的 API 密钥。选项语法使用双横线（例如 --server、--api-key）。

# HISTORY

immich-go 由 **simulot** 创建，是一个更快速、无依赖的 **Immich** 替代 CLI，并支持导入 Google Takeout。它用 **Go** 编写。

# INSTALL

```pacman: sudo pacman -S immich-go```

```brew: brew install immich-go```

```nix: nix profile install nixpkgs#immich-go```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[immich-cli](/man/immich-cli)(1), [rclone](/man/rclone)(1)
