# TAGLINE

将 lzip 文件解压到标准输出

# TLDR

**解压到 stdout**

```lzcat [file.lz]```

**解压多个文件**

```lzcat [file1.lz] [file2.lz]```

**解压并通过管道传递**

```lzcat [archive.tar.lz] | tar -xf -```

**详细输出**

```lzcat -v [file.lz]```

# SYNOPSIS

**lzcat** [_options_] [_files_...]

# PARAMETERS

**-v**, **--verbose**
> 详细输出。

**-q**, **--quiet**
> 抑制警告。

**-t**, **--test**
> 测试完整性。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**lzcat** 将 lzip 文件解压到标准输出。它等价于 "lzip -dc"，作用类似于 gzip 文件的 zcat。

lzcat 适合查看压缩文件，或将解压后的数据通过管道传给其他程序，而无需创建中间文件。

# EXAMPLE USAGE

```bash
# View compressed log
lzcat system.log.lz | less

# Extract tar archive
lzcat archive.tar.lz | tar xvf -

# Compare compressed files
diff <(lzcat file1.lz) <(lzcat file2.lz)
```

# CAVEATS

只能处理 lzip 格式。其他格式请使用 zcat、xzcat、bzcat。不能压缩；压缩请使用 lzip。

# HISTORY

lzcat 是 **Antonio Diaz Diaz** 创建的 **lzip** 软件包的一部分，该项目旨在提供更规范的 LZMA 压缩实现。

# INSTALL

```dnf: sudo dnf install xz```

```pacman: sudo pacman -S xz```

```apk: sudo apk add xz```

```zypper: sudo zypper install xz```

```brew: brew install xz```

```nix: nix profile install nixpkgs#xz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lzip](/man/lzip)(1), [zcat](/man/zcat)(1), [xzcat](/man/xzcat)(1), [bzcat](/man/bzcat)(1)
