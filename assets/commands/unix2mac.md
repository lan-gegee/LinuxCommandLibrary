# TAGLINE

将 Unix 换行符转换为经典 Mac 格式

# TLDR

**将文件原地转换**为经典 Mac 换行符（CR）

```unix2mac [path/to/file]```

**将**转换后的输出**写入**新文件

```unix2mac -n [path/to/file] [path/to/new_file]```

不转换，仅**显示**文件信息

```unix2mac -i [path/to/file]```

**转换并保留**原文件的时间戳

```unix2mac -k [path/to/file]```

**强制转换**二进制文件

```unix2mac -f [path/to/file]```

# SYNOPSIS

**unix2mac** [_options_] [_file_...]

# PARAMETERS

**-n, --newfile** _INFILE_ _OUTFILE_
> 写入新文件而不是原地修改。

**-o, --oldfile** _FILE_
> 原地转换（默认模式）。

**-i, --info** [_FLAGS_]
> 不转换，仅显示文件信息。

**-k, --keepdate**
> 使输出文件的日期与输入相同。

**-f, --force**
> 强制转换二进制文件。

**-s, --safe**
> 跳过二进制文件（默认）。

**-b, --keep-bom**
> 保留字节顺序标记（BOM）。

**-m, --add-bom**
> 添加 UTF-8 字节顺序标记（BOM）。

**-r, --remove-bom**
> 移除字节顺序标记（BOM）。

**-q, --quiet**
> 安静模式，抑制警告。

**-v, --verbose**
> 显示详细的转换信息。

**-l, --newline**
> 追加额外的换行符。

**-F, --follow-symlink**
> 转换符号链接指向的目标。

# DESCRIPTION

**unix2mac** 将文本文件从 Unix 换行格式（LF）转换为经典 Mac 格式（CR）。该格式曾被 Mac OS 9 及更早版本使用。现代 macOS 使用 Unix 风格的 LF 换行符。

该工具主要用于与旧版 Mac 软件的兼容，或处理明确要求 CR 换行符的文件。

# CAVEATS

如今很少需要经典 Mac 换行符（仅 CR），因为现代 macOS 使用 LF。不要处理二进制文件。属于 dos2unix 软件包的一部分。

# INSTALL

```apt: sudo apt install dos2unix```

```dnf: sudo dnf install dos2unix```

```pacman: sudo pacman -S dos2unix```

```apk: sudo apk add dos2unix```

```zypper: sudo zypper install dos2unix```

```brew: brew install dos2unix```

```nix: nix profile install nixpkgs#dos2unix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dos2unix](/man/dos2unix)(1), [unix2dos](/man/unix2dos)(1), [mac2unix](/man/mac2unix)(1), [iconv](/man/iconv)(1), [file](/man/file)(1)
