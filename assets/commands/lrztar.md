# TAGLINE

简化目录压缩的 lrzip 封装工具

# TLDR

以默认 LZMA 压缩**归档并压缩**目录

```lrztar [path/to/directory]```

以 **LZO** 压缩（最快）

```lrztar -l [path/to/directory]```

以 **bzip2** 压缩

```lrztar -b [path/to/directory]```

以 **gzip** 压缩

```lrztar -g [path/to/directory]```

以 **ZPAQ** 压缩（压缩比最高，速度最慢）

```lrztar -z [path/to/directory]```

指定**输出文件**

```lrztar -o [path/to/output.tar.lrz] [path/to/directory]```

以**详细输出**压缩并**强制**覆盖

```lrztar -v -f [path/to/directory]```

# SYNOPSIS

**lrztar** [_lrzip-options_] _directory_

# DESCRIPTION

**lrztar** 是 lrzip 的封装工具，用于简化目录压缩。它先创建 tar 归档，再用 lrzip 的长程压缩算法进行压缩。输出默认为 DIRECTORY.tar.lrz。lrztar 接受与 lrzip 相同的选项。

# PARAMETERS

**-l, --lzo**
> 使用超快的 LZO 压缩

**-b, --bzip2**
> 使用 bzip2 压缩

**-g, --gzip**
> 使用 gzip 压缩

**-z, --zpaq**
> 使用 ZPAQ 压缩（压缩比最高，非常慢）

**-n, --no-compress**
> 仅执行长程冗余缩减（不做第二阶段压缩）

**-o, --outfile** _FILE_
> 指定输出文件名

**-p, --threads** _N_
> 处理器线程数

**-f, --force**
> 强制覆盖已有文件

**-v, --verbose**
> 提高输出详细程度（-vv 更详细）

**-D, --delete**
> 压缩成功后删除源文件

# CAVEATS

默认压缩算法为 LZMA。ZPAQ 压缩比最高，但速度约慢 4 倍。LZO 以接近文件复制的速度提供接近 bzip2 的压缩比。

# INSTALL

```apt: sudo apt install lrzip```

```pacman: sudo pacman -S lrzip```

```apk: sudo apk add lrzip-extra-scripts```

```zypper: sudo zypper install lrzip```

```brew: brew install lrzip```

```nix: nix profile install nixpkgs#lrzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lrzip](/man/lrzip)(1), [lrzuntar](/man/lrzuntar)(1), [lrunzip](/man/lrunzip)(1), [tar](/man/tar)(1)
