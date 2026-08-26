# TAGLINE

分页查看 xz 压缩文件

# TLDR

**查看 xz 压缩文件**

```xzless [file.xz]```

**查看多个文件**

```xzless [file1.xz] [file2.xz]```

# SYNOPSIS

**xzless** [_options_] [_files_...]

# DESCRIPTION

**xzless** 分页查看 xz 压缩文件。它会解压并通过管道传给 less。支持所有 less 导航命令。适合浏览大型压缩日志文件。

# INSTALL

```apt: sudo apt install xz-utils```

```dnf: sudo dnf install xz```

```pacman: sudo pacman -S xz```

```apk: sudo apk add xz```

```zypper: sudo zypper install xz```

```brew: brew install xz```

```nix: nix profile install nixpkgs#xz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xz](/man/xz)(1), [less](/man/less)(1), [xzmore](/man/xzmore)(1)
