# TAGLINE

显示 xz 压缩文件的差异

# TLDR

**显示 xz 文件的差异**

```xzdiff [file1.xz] [file2.xz]```

**将压缩文件与原文件比较**

```xzdiff [file.xz] [file]```

# SYNOPSIS

**xzdiff** [_diff_options_] _file1_ [_file2_]

# DESCRIPTION

**xzdiff** 显示 xz 压缩文件之间的差异。它会解压后对内容运行 diff。支持所有 diff 选项。它是 diff 针对 xz 文件的封装。

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

[xz](/man/xz)(1), [xzcmp](/man/xzcmp)(1), [diff](/man/diff)(1)
