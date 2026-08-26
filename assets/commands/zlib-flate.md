# TAGLINE

原始 zlib 压缩与解压工具

# TLDR

**压缩数据**

```zlib-flate -compress < [input] > [output.zz]```

**解压数据**

```zlib-flate -uncompress < [input.zz] > [output]```

**以指定级别压缩（1=最快，9=最佳）**

```zlib-flate -compress=[9] < [input] > [output.zz]```

**解压 PDF 中的原始 zlib 流**

```zlib-flate -uncompress < [stream.bin] > [decoded.txt]```

# SYNOPSIS

**zlib-flate** **-compress**[=_level_] | **-uncompress**

# PARAMETERS

**-compress**
> 压缩数据。

**-uncompress**
> 解压数据。

**=**_LEVEL_
> 压缩级别（1-9）。

# DESCRIPTION

**zlib-flate** 执行原始 zlib 压缩与解压。它从标准输入读取并向标准输出写入，因此适合在 shell 管道中使用。

该工具使用原始 zlib 压缩格式，这一点与 **gzip** 这类会添加包装头部的工具不同。可以通过 **-compress=** 选项指定 1（最快）到 9（压缩率最高）的压缩级别。

zlib-flate 作为实用工具包含在 **QPDF** 软件包中，主要用于调试原始 zlib 流，例如 PDF 文件内部的那些流。不应把它当作通用压缩工具；通用用途请改用 **gzip**。

# CAVEATS

仅支持原始 zlib 格式，没有 gzip 或其他包装头部。属于 qpdf 软件包的一部分。不适合作为通用压缩工具。

# HISTORY

**zlib-flate** 随 **QPDF** 一同提供，用于原始 zlib deflate 压缩与解压。

# INSTALL

```apt: sudo apt install qpdf```

```dnf: sudo dnf install qpdf```

```pacman: sudo pacman -S qpdf```

```apk: sudo apk add qpdf```

```zypper: sudo zypper install qpdf```

```brew: brew install qpdf```

```nix: nix profile install nixpkgs#qpdf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qpdf](/man/qpdf)(1), [gzip](/man/gzip)(1), [zcat](/man/zcat)(1), [pigz](/man/pigz)(1)
