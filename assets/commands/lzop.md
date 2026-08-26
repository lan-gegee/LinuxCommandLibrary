# TAGLINE

使用 LZO 库压缩文件

# TLDR

**压缩文件**

```lzop [file]```

**解压文件**

```lzop -d [file.lzo]```

**保留原始文件**

```lzop -k [file]```

**以最大压缩率压缩**

```lzop -9 [file]```

**测试归档完整性**

```lzop -t [file.lzo]```

**压缩到 stdout**

```lzop -c [file]```

**压缩并删除原始文件**

```lzop -U [file]```

# SYNOPSIS

**lzop** [_options_] [_file_...]

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
> 压缩级别（默认：-3）。

**-f**, **--force**
> 强制覆盖已有文件。

**-U**
> 压缩或解压成功后删除输入文件。

**-v**, **--verbose**
> 显示每个被压缩或解压文件的名称。

**-o** _FILE_, **--output=**_FILE_
> 将输出写入指定文件。

**-p** _DIR_, **--path=**_DIR_
> 将输出文件写入指定目录。

**-F**, **--no-checksum**
> 不存储也不校验未压缩数据的校验和。

# DESCRIPTION

**lzop** 使用 LZO 库压缩文件。它强调速度而非压缩比，压缩和解压都非常快，适合实时应用。生成的文件带 .lzo 扩展名。

# INSTALL

```apt: sudo apt install lzop```

```dnf: sudo dnf install lzop```

```pacman: sudo pacman -S lzop```

```apk: sudo apk add lzop```

```zypper: sudo zypper install lzop```

```brew: brew install lzop```

```nix: nix profile install nixpkgs#lzop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gzip](/man/gzip)(1), [bzip2](/man/bzip2)(1), [lzip](/man/lzip)(1), [xz](/man/xz)(1), [zstd](/man/zstd)(1)
