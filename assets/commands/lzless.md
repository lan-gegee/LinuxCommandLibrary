# TAGLINE

借助 less 查看 lzip 压缩文件的内容

# TLDR

**查看 lzip 压缩文件**

```lzless [file.lz]```

# SYNOPSIS

**lzless** [_options_] [_file_...]

# DESCRIPTION

**lzless** 借助 less 查看 lzip 压缩文件的内容，查看时会自动解压。所有 less 的导航命令均可使用。按 q 退出。

# INSTALL

```dnf: sudo dnf install xz```

```pacman: sudo pacman -S xz```

```apk: sudo apk add xz```

```zypper: sudo zypper install xz```

```brew: brew install xz```

```nix: nix profile install nixpkgs#xz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lzip](/man/lzip)(1), [less](/man/less)(1), [lzmore](/man/lzmore)(1)
