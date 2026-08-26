# TAGLINE

使用 Lempel-Ziv 编码算法压缩文件

# TLDR

**压缩文件**

```gzip [file]```

**解压文件**

```gzip -d [file.gz]```

**压缩并保留原文件**

```gzip -k [file]```

**以最高压缩率压缩**

```gzip -9 [file]```

**以最快速度压缩**

```gzip -1 [file]```

**列出压缩信息**

```gzip -l [file.gz]```

**测试压缩文件完整性**

```gzip -t [file.gz]```

**压缩到标准输出**（管道）

```gzip -c [file] > [file.gz]```

**解压到标准输出**

```gzip -dc [file.gz]```

# SYNOPSIS

**gzip** [_options_] [_files_...]

# DESCRIPTION

**gzip** 使用 Lempel-Ziv（LZ77）编码算法压缩文件。每个文件都会被替换为带 .gz 后缀的压缩版本，同时保留所有者、权限和时间戳。

默认情况下，gzip 在压缩后会删除原文件。压缩文件可用 gzip -d（或 gunzip）恢复。该工具还可以从标准输入读取数据并写入标准输出，以便在管道中使用。

gzip 得到广泛支持，常用于压缩单个文件、配合 tar 创建归档以及传输数据。其格式定义于 RFC 1952。

# PARAMETERS

**-d**, **--decompress**
> 解压文件。

**-c**, **--stdout**
> 写入标准输出，保留原始文件。

**-k**, **--keep**
> 保留原始文件。

**-l**, **--list**
> 列出压缩信息。

**-t**, **--test**
> 测试完整性。

**-f**, **--force**
> 强制压缩/解压。

**-r**, **--recursive**
> 递归处理目录。

**-n**, **--no-name**
> 不保存原始文件名/时间戳。

**-N**, **--name**
> 保存/恢复原始文件名/时间戳。

**-1** 到 **-9**
> 压缩级别（从最快到最佳）。

**--best**
> 最高压缩率（-9）。

**--fast**
> 最快速度（-1）。

**-v**, **--verbose**
> 详细输出。

**-q**, **--quiet**
> 抑制警告信息。

# CAVEATS

无法直接压缩目录（需先用 tar）。除非使用 -k，否则默认删除原始文件。链接会被跟随解引用（不会作为链接本身压缩）。对目录使用 gzip -r 会分别压缩其中的每个文件。

# HISTORY

**gzip** 由 **Jean-loup Gailly** 和 **Mark Adler** 于 **1992 年**编写，是受专利困扰的 Unix compress 工具的自由替代品。gzip 格式成为 Unix 系统上文件压缩的标准，并被 HTTP 用于内容编码。底层的 DEFLATE 算法也用于 ZIP 文件和 PNG 图像。

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

[gunzip](/man/gunzip)(1), [zcat](/man/zcat)(1), [bzip2](/man/bzip2)(1), [xz](/man/xz)(1), [tar](/man/tar)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/gzip/)```

```[Source code](https://git.savannah.gnu.org/cgit/gzip.git)```

```[Documentation](https://www.gnu.org/software/gzip/manual/gzip.html)```

<!-- verified: 2026-07-17 -->
