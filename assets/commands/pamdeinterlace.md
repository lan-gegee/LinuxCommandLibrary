# TAGLINE

从隔行扫描视频帧中提取单个场，生成半高图像

# TLDR

**从隔行扫描视频中提取偶数场**

```pamdeinterlace -takeodd=false [input.pam] > [output.pam]```

**从隔行扫描视频中提取奇数场**

```pamdeinterlace -takeodd=true [input.pam] > [output.pam]```

# SYNOPSIS

**pamdeinterlace** [_options_] [_file_]

# PARAMETERS

**-takeodd**
> 取奇数行（true）或偶数行（false）。

# DESCRIPTION

**pamdeinterlace** 从隔行扫描视频帧中提取单个场，生成半高图像。用于处理隔行扫描的视频采集内容。属于 Netpbm 工具集。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pammixinterlace](/man/pammixinterlace)(1), [pamscale](/man/pamscale)(1)
