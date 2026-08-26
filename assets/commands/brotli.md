# TAGLINE

使用 Brotli 算法压缩和解压文件

# TLDR

**压缩**文件（默认保留原文件）

```brotli [file.txt]```

**解压**文件

```brotli -d [file.txt.br]```

**压缩并删除**原文件

```brotli --rm [file.txt]```

**压缩到标准输出**

```brotli -c [file.txt] > [file.txt.br]```

以较快的质量级别**压缩**（0=最快，11=最佳）

```brotli -q [4] [file.txt]```

**压缩到指定输出文件**

```brotli -o [output.br] [file.txt]```

测试压缩文件的完整性

```brotli -t [file.txt.br]```

# SYNOPSIS

**brotli** [_options_] [_file_...]

# DESCRIPTION

**brotli** 是一款采用 Google 开发的 Brotli 算法的压缩工具。它的压缩率优于 gzip 和 deflate，对网页内容尤其有效，因此在 HTTP 压缩中广受欢迎。与 gzip 不同，它默认保留源文件。

该工具支持 0（快速）到 11（最大压缩）的压缩级别。

# PARAMETERS

**-d**, **--decompress**
> 解压文件。

**-c**, **--stdout**
> 写入标准输出。

**-f**, **--force**
> 覆盖已有文件。

**-j**, **--rm**
> 处理后删除源文件。

**-k**, **--keep**
> 保留输入文件（默认行为）。

**-o** _FILE_, **--output=**_FILE_
> 输出到指定文件。

**-q** _NUM_, **--quality=**_NUM_
> 压缩质量（0-11，默认：11）。

**-S** _SUFFIX_, **--suffix=**_SUFFIX_
> 输出文件名后缀（默认：.br）。

**-v**, **--verbose**
> 显示详细的状态信息。

**-V**, **--version**
> 显示版本。

**-w** _NUM_, **--lgwin=**_NUM_
> LZ77 窗口大小（0、10-24，默认：24）。

**-t**, **--test**
> 测试压缩文件的完整性。

# CAVEATS

最大压缩时比 gzip 慢。在较老的系统上支持不够广泛。质量级别 11 可能非常慢。某些系统通过 `br` 命令使用 brotli。

# HISTORY

**Brotli** 由 Google 的 Jyrki Alakuijala 和 Zoltán Szabadka 开发，于 **2013** 年发布，并于 **2016** 年标准化为 RFC 7932。

# INSTALL

```apt: sudo apt install brotli```

```dnf: sudo dnf install brotli```

```pacman: sudo pacman -S brotli```

```apk: sudo apk add brotli```

```zypper: sudo zypper install brotli```

```brew: brew install brotli```

```nix: nix profile install nixpkgs#brotli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gzip](/man/gzip)(1), [zstd](/man/zstd)(1), [xz](/man/xz)(1)
