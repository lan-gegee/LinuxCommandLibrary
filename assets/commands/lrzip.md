# TAGLINE

面向大文件的长程冗余压缩程序

# TLDR

以 **LZMA** 压缩（默认）

```lrzip [path/to/file]```

以 **BZIP2** 压缩

```lrzip --bzip2 [path/to/file]```

以 **ZPAQ** 压缩（极致压缩比）

```lrzip --zpaq [path/to/file]```

以 **LZO** 压缩（快速）

```lrzip --lzo [path/to/file]```

**加密**压缩后的文件

```lrzip --encrypt [path/to/file]```

设置**线程数**

```lrzip --threads 8 [path/to/file]```

**解压**文件

```lrzip -d [path/to/file.lrz]```

压缩并指定**输出文件**

```lrzip -o [output.lrz] [path/to/file]```

# SYNOPSIS

**lrzip** [_options_] [_file_]

# DESCRIPTION

**lrzip**（Long Range ZIP）专为压缩大文件而设计。它先进行长程冗余缩减，再执行压缩，对含有远距离匹配数据的文件能达到很高的压缩比。

# PARAMETERS

**-b, --bzip2**
> 使用 BZIP2 压缩（均衡）

**-z, --zpaq**
> 使用 ZPAQ 压缩（最高压缩比，速度慢）

**-l, --lzo**
> 使用 LZO 压缩（快速）

**-g, --gzip**
> 使用 GZIP 压缩

**-e, --encrypt**
> 用密码加密

**-p, --threads N**
> 处理器线程数

**-o, --outfile FILE**
> 指定输出文件名

**-d, --decompress**
> 解压文件

**-t, --test**
> 测试压缩文件的完整性

**-i, --info**
> 显示压缩文件的信息

**-k, --keep**
> 保留原始文件

**-L** _N_, **--level** _N_
> 设置压缩级别 1-9（默认 7）

**-n, --no-compress**
> 仅执行长程冗余缩减，不做后端压缩

**-q, --quiet**
> 安静模式，减少输出

**-v, --verbose**
> 提高输出详细程度（可多次使用）

# CAVEATS

对含有长程冗余数据的大文件（100 MB 以上）最为有效。ZPAQ 压缩极慢但压缩比最佳。默认的 LZMA 后端在速度和压缩率之间取得了良好平衡。其文件与标准 zip/gzip 工具不兼容；请使用 **lrunzip** 或 **lrzip -d** 解压。默认情况下，原始文件会在压缩后被删除。

# INSTALL

```apt: sudo apt install lrzip```

```pacman: sudo pacman -S lrzip```

```apk: sudo apk add lrzip```

```zypper: sudo zypper install lrzip```

```brew: brew install lrzip```

```nix: nix profile install nixpkgs#lrzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lrunzip](/man/lrunzip)(1), [lrztar](/man/lrztar)(1), [gzip](/man/gzip)(1), [xz](/man/xz)(1), [bzip2](/man/bzip2)(1), [zstd](/man/zstd)(1)
