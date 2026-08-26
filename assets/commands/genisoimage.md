# TAGLINE

ISO9660 文件系统镜像创建工具

# TLDR

从给定的源目录创建 **ISO 镜像**

```genisoimage -o myimage.iso [path/to/source_directory]```

创建包含**大于 2 GiB 文件**的 ISO 镜像

```genisoimage -allow-limited-size -o myimage.iso [path/to/source_directory]```

创建带 Rock Ridge 和 Joliet 扩展的**可引导 ISO**

```genisoimage -R -J -V "[VOLUME_LABEL]" -b [boot/isolinux.bin] -c [boot/boot.cat] -no-emul-boot -boot-load-size 4 -boot-info-table -o myimage.iso [path/to/source_directory]```

# SYNOPSIS

**genisoimage** [_options_] _-o output.iso_ _pathspec_

# PARAMETERS

**-o** _FILE_
> 输出的 ISO 文件名

**-R**, **-rock**
> 生成 Rock Ridge 扩展（Unix 权限/符号链接）

**-J**, **-joliet**
> 生成 Joliet 扩展（Windows 长文件名）

**-V** _ID_
> 设置卷 ID（卷标）

**-b** _FILE_
> 为可引导 CD/DVD 设置 El Torito 引导镜像

**-c** _FILE_
> 设置 El Torito 引导目录文件

**-allow-limited-size**
> 通过报告较小的表观大小来允许超过 2 GiB 的文件

**-udf**
> 生成 UDF 文件系统（支持更大的文件）

**-iso-level** _LEVEL_
> 设置 ISO9660 一致性级别（1-4）

**-input-charset** _CHARSET_
> 设置输入字符集

**-v**, **-verbose**
> 启用详细输出

# DESCRIPTION

**genisoimage** 创建适合 CD/DVD 刻录或作为回环设备挂载的 ISO9660 文件系统镜像。它支持多种文件系统扩展，包括 Rock Ridge（Unix）、Joliet（Windows）和 HFS（Mac），以实现跨平台兼容性。

该工具可以按照 El Torito 规范创建可引导镜像，通过适当的配置同时支持传统 BIOS 和 UEFI 引导方式。

genisoimage 是 cdrtools 软件包中 mkisofs 的一个分支，在 Debian 和 Ubuntu 软件仓库中独立维护。

# CAVEATS

标准 ISO9660 有 4 GiB 的文件大小限制。更大的文件请使用 **-udf** 或 **-allow-limited-size**。文件名长度和字符限制因扩展类型而异。创建引导镜像需要仔细配置。

# HISTORY

genisoimage 是 mkisofs 的分支，于 **2006 年**因原 cdrtools 软件包的许可证问题而创建。它作为 cdrkit 项目的一部分维护，是基于 Debian 的系统上默认的 ISO 创建工具。

# INSTALL

```apt: sudo apt install genisoimage```

```dnf: sudo dnf install genisoimage```

```apk: sudo apk add cdrkit```

```nix: nix profile install nixpkgs#cdrkit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkisofs](/man/mkisofs)(1), [wodim](/man/wodim)(1), [mount](/man/mount)(8)
