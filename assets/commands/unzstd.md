# TAGLINE

解压 Zstandard 压缩文件

# TLDR

**解压文件**

```unzstd [file.zst]```

**保留原文件**

```unzstd -k [file.zst]```

**输出到 stdout**

```unzstd -c [file.zst]```

**强制覆盖**

```unzstd -f [file.zst]```

**解压多个文件**

```unzstd [file1.zst] [file2.zst]```

# SYNOPSIS

**unzstd** [_-k_] [_-c_] [_-f_] [_options_] _files_

# PARAMETERS

**-k**
> 保留原始文件。

**-c**
> 写入到 stdout。

**-f**
> 强制覆盖。

**-v**
> 详细输出模式。

**-q**
> 安静模式。

# DESCRIPTION

**unzstd** 用于解压采用 Zstandard（zstd）算法压缩的文件。它在功能上等同于运行 **zstd --decompress**，是 zstd 软件包中为方便使用而提供的独立命令。

Zstandard 在提供极高解压速度的同时，压缩比也能与 zlib 相媲美。默认情况下，unzstd 会用解压结果替换 .zst 压缩文件。**-k** 标志可保留原始压缩文件；**-c** 则写入标准输出，便于通过管道传输。

Zstandard 由 Facebook（现为 Meta）开发并于 2016 年发布，如今已被 Linux 内核、pacman 和 apt 等软件包管理器以及众多其他工具采纳，作为 gzip 的现代替代方案——压缩率更高且解压更快。

# CAVEATS

格式较新。并非在所有环境中都可用。属于 zstd 软件包的一部分。

# HISTORY

**unzstd** 是 **Zstandard**（zstd）的一部分，这是一种由 Facebook 开发的高速压缩算法。

# INSTALL

```apt: sudo apt install zstd```

```dnf: sudo dnf install zstd```

```pacman: sudo pacman -S zstd```

```apk: sudo apk add zstd```

```zypper: sudo zypper install zstd```

```brew: brew install zstd```

```nix: nix profile install nixpkgs#zstd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zstd](/man/zstd)(1), [gzip](/man/gzip)(1), [xz](/man/xz)(1)
