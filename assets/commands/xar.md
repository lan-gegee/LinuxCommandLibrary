# TAGLINE

可扩展归档格式工具

# TLDR

**创建归档**

```xar -cf [archive.xar] [files]```

**解压归档**

```xar -xf [archive.xar]```

**列出内容**

```xar -tf [archive.xar]```

**详细模式解压**

```xar -xvf [archive.xar]```

**解压到目录**

```xar -xf [archive.xar] -C [directory]```

# SYNOPSIS

**xar** [_-c_] [_-x_] [_-t_] [_-f archive_] [_options_] [_files_]

# PARAMETERS

**-c**
> 创建归档。

**-x**
> 解压归档。

**-t**
> 列出内容。

**-f** _FILE_
> 归档文件。

**-v**
> 详细输出。

**-C** _DIR_
> 目标目录。

# DESCRIPTION

**xar**（eXtensible ARchive）使用由 Apple 开发的格式创建和解压归档，主要用于 macOS 安装程序包。该格式使用基于 XML 的目录表，支持丰富的元数据以及每个文件使用不同的压缩算法。

该归档格式还包含用于代码签名和完整性验证的签名支持。虽然主要与 macOS 相关联，但 xar 也可在 Linux 上使用，用于处理 macOS 软件包文件和其他 XAR 归档。

# CAVEATS

面向 macOS。在 Linux 上较少见。存在 XML 开销。

# HISTORY

**xar**（eXtensible ARchive）由 **Apple** 为 macOS 安装程序包开发。

# INSTALL

```apt: sudo apt install xar```

```dnf: sudo dnf install xar```

```apk: sudo apk add xar```

```zypper: sudo zypper install xar```

```nix: nix profile install nixpkgs#xar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tar](/man/tar)(1), [pkgutil](/man/pkgutil)(1), [ar](/man/ar)(1)
