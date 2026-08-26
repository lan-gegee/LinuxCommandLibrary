# TAGLINE

使用 LZMA 算法的无损数据压缩器

# TLDR

**压缩文件**

```lzip [file]```

**解压文件**

```lzip -d [file.lz]```

**以最大压缩率压缩**

```lzip -9 [file]```

**保留原始文件**

```lzip -k [file]```

**测试归档完整性**

```lzip -t [file.lz]```

**压缩到 stdout**

```lzip -c [file] > [output.lz]```

# SYNOPSIS

**lzip** [_options_] [_file_...]

# PARAMETERS

**-d**, **--decompress**
> 解压文件。

**-k**, **--keep**
> 保留输入文件。

**-c**, **--stdout**
> 写入标准输出。

**-t**, **--test**
> 测试归档完整性。

**-1** 至 **-9**
> 压缩级别（默认 6）。

**-v**, **--verbose**
> 详细输出模式。

# DESCRIPTION

**lzip** 是使用 LZMA 算法的无损数据压缩器，提供与 xz 相近的高压缩比，但格式更简单。生成的文件带 .lz 扩展名。专为长期归档而设计。

# INSTALL

```dnf: sudo dnf install lzip```

```pacman: sudo pacman -S lzip```

```apk: sudo apk add lzip```

```zypper: sudo zypper install lzip```

```brew: brew install lzip```

```nix: nix profile install nixpkgs#lzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xz](/man/xz)(1), [gzip](/man/gzip)(1), [lzop](/man/lzop)(1)
