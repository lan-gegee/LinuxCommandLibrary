# TAGLINE

列出……的内容

# TLDR

列出**归档内容**

```lz [path/to/file.tar.gz]```

# SYNOPSIS

**lz** _file.tar.gz_

# DESCRIPTION

**lz** 无需解压即可列出 .tar.gz 压缩归档的内容。它是一个简单的包装器，提供对归档内容的快速访问。

# CAVEATS

专用于 .tar.gz 文件。如需更多选项和控制，请直接使用 tar -tzf。

# INSTALL

```apt: sudo apt install mtools```

```dnf: sudo dnf install mtools```

```pacman: sudo pacman -S mtools```

```apk: sudo apk add mtools```

```zypper: sudo zypper install mtools```

```brew: brew install mtools```

```nix: nix profile install nixpkgs#mtools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tar](/man/tar)(1), [gzip](/man/gzip)(1), [zcat](/man/zcat)(1)
