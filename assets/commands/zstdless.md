# TAGLINE

用分页器查看 zstd 压缩文件

# TLDR

**查看 zstd 压缩文件**

```zstdless [file.zst]```

# SYNOPSIS

**zstdless** [_files_...]

# DESCRIPTION

**zstdless** 让你可以借助 **less** 分页器查看 Zstandard（.zst）压缩文件。它会即时解压文件并把输出通过管道传给 less，从而获得完整的交互式浏览体验，包括前后滚动、搜索和跳转到指定行。

这对于浏览压缩的日志文件和数据尤为有用，无需先将其解压到磁盘。它是 zstd 压缩工具套件的一部分。

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

[zstd](/man/zstd)(1), [zstdcat](/man/zstdcat)(1), [less](/man/less)(1)
