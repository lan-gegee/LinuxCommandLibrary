# TAGLINE

从目录树创建 EROFS 镜像

# TLDR

基于根目录创建 **EROFS 文件系统**

```mkfs.erofs [image.erofs] [root/]```

创建带**指定 UUID** 的 EROFS 镜像

```mkfs.erofs -U [UUID] [image.erofs] [root/]```

创建**压缩**的 EROFS 镜像

```mkfs.erofs -zlz4hc [image.erofs] [root/]```

创建**所有文件归 root 所有**的 EROFS 镜像

```mkfs.erofs --all-root [image.erofs] [root/]```

# SYNOPSIS

**mkfs.erofs** [_options_] _image_ _source_

# PARAMETERS

**-U _uuid_**
> 设置指定的文件系统 UUID

**-z _algorithm_**
> 启用压缩（lz4、lz4hc、lzma、deflate、zstd）

**--all-root**
> 使所有文件归 root 所有（UID/GID 为 0）

**-L _label_**
> 设置卷标

**-T _timestamp_**
> 对所有文件使用固定时间戳（可复现构建）

**--exclude-path _pattern_**
> 排除匹配模式的文件

**-E _options_**
> 用于精细调整的扩展选项

# DESCRIPTION

**mkfs.erofs** 从目录树创建 EROFS（Enhanced Read-Only File System）镜像。EROFS 是一款轻量级只读文件系统，专为 Android 系统分区、容器镜像和嵌入式系统等性能敏感场景设计。

该文件系统支持透明压缩，在保持快速随机读取的同时显著节省空间。与 SquashFS 不同，EROFS 因其固定大小块的设计而提供更好的随机访问性能。

输出是一个包含完整文件系统镜像的文件，可通过回环方式挂载或写入只读分区。

# CAVEATS

EROFS 是只读的；源目录不会被修改。启用压缩时处理大目录可能耗时。挂载镜像需要内核支持（CONFIG_EROFS_FS）。最适合数据在创建后不再变化的场景。

# HISTORY

EROFS 由华为开发，于 Linux 内核 4.19 版（2018 年）合入主线。此后被 Android 采用为系统分区格式，也被多种嵌入式 Linux 发行版采用。

# INSTALL

```apt: sudo apt install erofs-utils```

```dnf: sudo dnf install erofs-utils```

```pacman: sudo pacman -S erofs-utils```

```apk: sudo apk add erofs-utils```

```zypper: sudo zypper install erofs-utils```

```brew: brew install erofs-utils```

```nix: nix profile install nixpkgs#erofs-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mksquashfs](/man/mksquashfs)(1), [mount](/man/mount)(8), [losetup](/man/losetup)(8)
