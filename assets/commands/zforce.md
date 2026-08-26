# TAGLINE

为 gzip 文件补上缺失的 .gz 扩展名

# TLDR

添加 **.gz** 扩展名

```zforce [path/to/file1 path/to/file2 ...]```

# SYNOPSIS

**zforce** [_FILE..._]

# DESCRIPTION

**zforce** 为缺少扩展名的 gzip 压缩文件添加 .gz 扩展名。它会检查文件，只重命名那些有效的 gzip 文件。

已有 .gz 扩展名或不是 gzip 压缩的文件会被忽略。

# CAVEATS

只处理没有 .gz 扩展名的 gzip 文件。不会压缩文件，只进行重命名。

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

[gzip](/man/gzip)(1), [gunzip](/man/gunzip)(1), [zcat](/man/zcat)(1)
