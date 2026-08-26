# TAGLINE

压缩和解压归档文件

# TLDR

**压缩文件**

```ouch compress [file1] [file2] [archive.tar.gz]```

**解压归档**

```ouch decompress [archive.zip]```

**列出归档内容**

```ouch list [archive.tar.gz]```

**解压到目录**

```ouch decompress [archive.zip] -d [output/]```

# SYNOPSIS

**ouch** [_command_] [_options_] _files_

# PARAMETERS

**compress** _FILES_ _ARCHIVE_
> 创建归档。

**decompress** _ARCHIVE_
> 解压归档。

**list** _ARCHIVE_
> 列出内容。

**-d** _DIR_
> 输出目录。

**-y**
> 对所有提示回答"是"。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ouch** 用于压缩和解压归档文件，可智能检测格式。

该工具支持多种归档格式，是一款基于 Rust 的压缩工具。

# CAVEATS

通过扩展名检测格式。使用 Rust 编写，支持多种格式。

# HISTORY

ouch 作为一款具有智能格式检测功能的**易用压缩工具**而创建。

# INSTALL

```pacman: sudo pacman -S ouch```

```zypper: sudo zypper install ouch```

```brew: brew install ouch```

```nix: nix profile install nixpkgs#ouch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tar](/man/tar)(1), [zip](/man/zip)(1), [7z](/man/7z)(1)
