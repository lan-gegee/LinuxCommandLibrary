# TAGLINE

为 Quickemu 虚拟机下载操作系统镜像

# TLDR

**列出**所有受支持的操作系统

```quickget --list```

以 **CSV/JSON** 格式列出

```quickget --list-csv```

**下载**并创建虚拟机配置

```quickget [os] [release] [edition]```

下载 **Windows 11**

```quickget windows 11```

下载 **macOS**

```quickget macos [sonoma]```

显示 **ISO URL**

```quickget --url [os] [release]```

**检查** ISO 是否可用

```quickget --check [os] [release]```

仅**下载**而不创建配置

```quickget --download [os] [release]```

# SYNOPSIS

**quickget** [**--list**|**--url**|**--check**|**--download**] [_os_] [_release_] [_edition_]

# PARAMETERS

**--list, --list-csv, --list-json**
> 列出受支持的操作系统

**--url _os_ _release_**
> 显示 ISO 下载 URL

**--check _os_ _release_**
> 检查 ISO 是否可用

**--download _os_ _release_**
> 仅下载而不创建配置

**--create-config _os_ _iso_**
> 从现有 ISO 创建配置

**os**
> 操作系统名称

**release**
> 版本号

**edition**
> 版本变体（可选）

# DESCRIPTION

**quickget** 用于下载操作系统镜像并创建 Quickemu 配置文件。它支持数百种操作系统，包括 Linux 发行版、Windows、macOS 和各种 BSD 变体。

该工具会自动选择合适的下载镜像，并根据操作系统的要求创建优化的虚拟机配置。

# CAVEATS

大体积下载可能耗时较长。某些操作系统版本需要特定的 release 版本。macOS 下载的是恢复镜像。Windows 需要 virtio 驱动。

# HISTORY

**quickget** 是 **quickemu** 的配套工具，由 **Martin Wimpress** 开发。它简化了为各种操作系统获取和准备虚拟机镜像的过程。

# INSTALL

```apt: sudo apt install quickemu```

```dnf: sudo dnf install quickemu```

```nix: nix profile install nixpkgs#quickemu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[quickemu](/man/quickemu)(1), [wget](/man/wget)(1), [aria2c](/man/aria2c)(1)
