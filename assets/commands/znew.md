# TAGLINE

将 compress（.Z）文件转换为 gzip 格式

# TLDR

**将 .Z 文件转换为 .gz**

```znew [file.Z]```

**转换多个文件**

```znew [*.Z]```

**保留原始文件**

```znew -K [file.Z]```

**使用最佳压缩**

```znew -9 [file.Z]```

**即使 .gz 已存在也强制转换**

```znew -f [file.Z]```

# SYNOPSIS

**znew** [**-ftv9PK**] _file.Z_...

# PARAMETERS

**-f**
> 即使 .gz 文件已存在也强制重新压缩

**-t**
> 删除原文件前先测试新文件的完整性

**-v**
> 详细输出

**-9**
> 使用最高压缩级别

**-P**
> 使用管道进行转换（较慢但占用更少磁盘空间）

**-K**
> 保留原始 .Z 文件

# DESCRIPTION

**znew** 将旧的 compress 格式（.Z）文件重新压缩为 gzip 格式（.gz）。compress 工具采用 LZW 压缩，而 gzip 采用 DEFLATE，通常能获得更好的压缩比。

该工具适合将旧式的压缩归档转换为更现代、更高效的 gzip 格式。转换完成后，原始 .Z 文件默认会被删除。

使用 **-t** 标志时，znew 会在删除原文件前校验新 .gz 文件的完整性，从而防范数据损坏。

# HISTORY

compress 工具和 .Z 格式诞生于 20 世纪 80 年代。gzip 创建于 1992 年，是为了规避 LZW 专利问题而推出的自由替代方案。znew 就是为方便从旧格式迁移而生。

# CAVEATS

只能将 .Z 文件转换为 .gz。不处理其他压缩格式。

若不加 **-K**，转换成功后原始文件会被删除。

**-P** 选项消耗更多 CPU 但占用更少的临时磁盘空间。

现代系统很少遇到 .Z 文件，因此该工具主要用于归档工作。

# INSTALL

```apt: sudo apt install gzip```

```dnf: sudo dnf install gzip```

```pacman: sudo pacman -S gzip```

```apk: sudo apk add gzip```

```zypper: sudo zypper install gzip```

```brew: brew install gzip```

```nix: nix profile install nixpkgs#gzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gzip](/man/gzip)(1), [gunzip](/man/gunzip)(1), [zcat](/man/zcat)(1), [compress](/man/compress)(1)
