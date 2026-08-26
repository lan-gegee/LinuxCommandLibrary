# TAGLINE

比较 xz 压缩文件

# TLDR

**比较 xz 压缩文件**

```xzcmp [file1.xz] [file2.xz]```

**将压缩文件与未压缩文件比较**

```xzcmp [file.xz] [file]```

# SYNOPSIS

**xzcmp** [_options_] _file1_ [_file2_]

# DESCRIPTION

**xzcmp** 比较 xz 压缩文件。它会先解压再用 cmp 比较文件。若只给出一个文件，则与标准输入或未压缩版本进行比较。它是 cmp 针对 xz 文件的封装。

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

[xz](/man/xz)(1), [xzdiff](/man/xzdiff)(1), [cmp](/man/cmp)(1)
