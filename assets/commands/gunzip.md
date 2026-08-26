# TAGLINE

解压由 gzip、zip、compress 或 pack 压缩的文件

# TLDR

**解压文件**

```gunzip [file.gz]```

**解压并保留原文件**

```gunzip -k [file.gz]```

**解压到标准输出**

```gunzip -c [file.gz]```

**解压多个文件**

```gunzip [file1.gz] [file2.gz]```

**测试压缩文件完整性**

```gunzip -t [file.gz]```

**列出压缩信息**

```gunzip -l [file.gz]```

**强制解压**（忽略警告）

```gunzip -f [file.gz]```

**详细输出**，显示压缩比

```gunzip -v [file.gz]```

**解压使用自定义后缀的文件**

```gunzip -S [.zz] [file.zz]```

**递归解压**目录中的文件

```gunzip -r [directory/]```

# SYNOPSIS

**gunzip** [_options_] [_files_...]

# DESCRIPTION

**gunzip** 用于解压由 gzip、zip、compress 或 pack 压缩的文件。它等价于 `gzip -d`。对每个压缩文件，gunzip 会创建解压后的版本并移除 .gz 后缀。

该工具会自动检测压缩格式，处理 .gz、.z、.Z 和 .tgz 等后缀。即使文件损坏，gzip 创建的文件也可以恢复，gunzip 会用零替换损坏的数据块。

gunzip 会保留压缩文件头中存储的原文件名、时间戳和权限。

# PARAMETERS

**-c**, **--stdout**
> 写入标准输出，保留原始文件。

**-f**, **--force**
> 即使有警告也强制解压。

**-k**, **--keep**
> 保留压缩文件。

**-l**, **--list**
> 列出压缩比。

**-n**, **--no-name**
> 不恢复原始文件名/时间戳。

**-N**, **--name**
> 恢复原始文件名/时间戳（默认行为）。

**-q**, **--quiet**
> 抑制警告信息。

**-r**, **--recursive**
> 递归处理目录。

**-t**, **--test**
> 测试完整性。

**-S** _suffix_, **--suffix** _suffix_
> 使用指定后缀代替 .gz。

**-v**, **--verbose**
> 详细输出，显示文件名和压缩比。

**-1** 到 **-9**
> 被 gunzip 忽略；为与 gzip 兼容而接受。

# CAVEATS

默认会删除原始压缩文件。无法直接解压为其他文件名（需配合 -c 和重定向）。不加 -v 选项时对损坏的文件可能静默失败。

# HISTORY

**gunzip** 是 **gzip** 软件包的一部分，由 **Jean-loup Gailly** 和 **Mark Adler** 于 **1992 年**创建。它被设计为 gzip 文件的免费解压器，出于兼容性考虑也能处理其他压缩格式。在从受专利困扰的 compress 工具迁移的过程中，该工具成为 Unix 系统上的标准配置。

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

[gzip](/man/gzip)(1), [zcat](/man/zcat)(1), [compress](/man/compress)(1), [bunzip2](/man/bunzip2)(1), [unxz](/man/unxz)(1)
