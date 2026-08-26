# TAGLINE

借助 more 查看 lzip 压缩文件的内容

# TLDR

**查看 lzip 压缩文件**

```lzmore [file.lz]```

**查看多个文件**

```lzmore [file1.lz] [file2.lz]```

# SYNOPSIS

**lzmore** [_options_] [_file_...]

# DESCRIPTION

**lzmore** 借助 more 查看 lzip 压缩文件的内容，查看时会自动解压。按空格翻页，按 q 退出。如需更好的导航体验，请改用 lzless。

# INSTALL

```dnf: sudo dnf install xz```

```pacman: sudo pacman -S xz```

```apk: sudo apk add xz```

```zypper: sudo zypper install xz```

```brew: brew install xz```

```nix: nix profile install nixpkgs#xz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lzip](/man/lzip)(1), [more](/man/more)(1), [lzless](/man/lzless)(1)
