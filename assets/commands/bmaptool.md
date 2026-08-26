# TAGLINE

使用块映射高效地写入磁盘镜像

# TLDR

使用 bmap **将镜像复制到设备**

```sudo bmaptool copy [image.img] [/dev/sdX]```

**复制压缩镜像**

```sudo bmaptool copy [image.img.xz] [/dev/sdX]```

**显式指定 bmap 文件进行复制**

```sudo bmaptool copy --bmap [image.bmap] [image.img] [/dev/sdX]```

**不使用 bmap 复制**（退化为类似 dd 的行为）

```sudo bmaptool copy --nobmap [image.img] [/dev/sdX]```

为镜像**创建 bmap 文件**

```bmaptool create -o [image.bmap] [image.img]```

**从 URL 复制**

```sudo bmaptool copy [https://example.com/image.img.xz] [/dev/sdX]```

# SYNOPSIS

**bmaptool** _command_ [_options_] [_arguments_]

# DESCRIPTION

**bmaptool** 是一个用于创建块映射（bmap）并高效地将镜像复制到块设备的实用工具。它只写入实际的数据块，跳过空白或全零区域，因此在处理稀疏镜像时比 **dd** 快得多。

该工具使用 SHA256 校验和提供完整性验证，并包含防止意外写入已挂载设备的安全机制。它支持压缩镜像，可在复制过程中即时解压。

# SUBCOMMANDS

**copy**
> 使用 bmap 将镜像文件复制到块设备。

**create**
> 为镜像生成 bmap 文件。

# PARAMETERS

**--bmap** _file_
> bmap 文件的路径（未指定时自动检测）。

**--nobmap**
> 不使用 bmap 进行复制（整个镜像都会被写入）。

**-o, --output** _file_
> create 命令的输出文件。

**--no-verify**
> 跳过 SHA256 校验和验证。

**--no-sig-verify**
> 跳过 OpenPGP 签名验证。

# CAVEATS

写入块设备需要 root 权限。bmap 文件必须与镜像文件匹配；不匹配会导致验证失败。保护机制会阻止向已挂载的设备写入。没有 bmap 文件时，该工具会退化为像 dd 一样复制整个镜像。

# HISTORY

bmaptool 最初由 **Intel** 开发，用于高效的嵌入式 Linux 镜像部署，解决了使用 **dd** 刷写大型磁盘镜像（尤其是包含大量空白区域的镜像）时速度慢且不安全的问题。该项目于 **2024 年**移交至 **Yocto Project**；Intel 的原始仓库现已归档。

# INSTALL

```nix: nix profile install nixpkgs#bmaptool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dd](/man/dd)(1), [pv](/man/pv)(1), [xzcat](/man/xzcat)(1)

# RESOURCES

```[Source code](https://github.com/yoctoproject/bmaptool)```

<!-- verified: 2026-06-19 -->
