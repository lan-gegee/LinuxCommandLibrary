# TAGLINE

解压 Unix compress（.Z）文件

# TLDR

**解压**文件

```uncompress [path/to/file1.Z] [path/to/file2.Z]```

忽略**不存在**的文件

```uncompress -f [path/to/file1.Z] [path/to/file2.Z]```

写入 **stdout**

```uncompress -c [path/to/file1.Z]```

**详细输出**模式

```uncompress -v [path/to/file1.Z]```

# SYNOPSIS

**uncompress** [_OPTIONS_] [_FILE_...]

# PARAMETERS

**-c**
> 写入 stdout，不修改文件

**-f**
> 强制执行，忽略不存在的文件

**-v**
> 详细输出，显示压缩百分比

# DESCRIPTION

**uncompress** 解压使用 Unix compress 命令压缩的文件。这类文件通常带有 .Z 扩展名。除非使用 -c，否则原始压缩文件会被解压后的版本替换。

该格式使用 LZW 压缩，在 gzip 成为标准之前常见于较早的 Unix 系统。

# CAVEATS

LZW 压缩格式已基本过时。大多数系统现在使用 gzip 或更新的压缩方式。默认安装中可能不包含 compress/uncompress 命令。

# HISTORY

**uncompress** 是传统 Unix compress 工具集的一部分，使用 LZW 压缩，比更常见的 gzip 格式出现得更早。

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

[compress](/man/compress)(1), [gzip](/man/gzip)(1), [gunzip](/man/gunzip)(1)
