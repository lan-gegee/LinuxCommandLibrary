# TAGLINE

命令行 BitTorrent 元信息工具

# TLDR

**创建 torrent 文件**

```imdl torrent create --input [path/to/content]```

**查看 torrent 文件信息**

```imdl torrent show [path/to/file.torrent]```

**校验 torrent 内容**

```imdl torrent verify --input [path/to/content] [path/to/file.torrent]```

**以指定 tracker 创建**

```imdl torrent create --input [path/to/content] --announce [udp://tracker.example.com:6969]```

# SYNOPSIS

**imdl** _command_ [_options_]

# DESCRIPTION

**intermodal**（二进制名为 **imdl**）是一款易用且功能丰富的命令行 BitTorrent 元信息工具。它支持 **.torrent** 文件的创建、查看和校验。该工具可处理单文件和多文件种子，支持多个 tracker，并能创建 v1 和 v2 两种 torrent 文件。

imdl 提供详细的输出，包括文件列表、分片信息、tracker URL 和内容哈希，因此很适合种子的创建、检查和调试。

# CAVEATS

只处理 torrent 元信息文件；不能下载或做种。为大型文件创建 torrent 时，由于需要计算分片哈希，可能耗时较长。

# HISTORY

**intermodal** 由 **Casey Rodarmor**（**just** 和 **ord** 的作者）创建，用 **Rust** 编写。它以 **Creative Commons Zero** 公有领域贡献方式发布。

# INSTALL

```brew: brew install intermodal```

```nix: nix profile install nixpkgs#intermodal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[transmission-cli](/man/transmission-cli)(1), [aria2c](/man/aria2c)(1)
