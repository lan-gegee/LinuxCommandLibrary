# TAGLINE

将 YUY2 打包视频转换为 PAM

# TLDR

**将 YUY2 视频转换为 PAM**

```yuy2topam [width] [height] [input.yuy2] > [output.pam]```

# SYNOPSIS

**yuy2topam** _width_ _height_ [_file_]

# PARAMETERS

_width_
> 图像宽度。

_height_
> 图像高度。

# DESCRIPTION

**yuy2topam** 将 YUY2（YUYV）打包 YUV 格式转换为 PAM。YUY2 是网络摄像头和视频采集常用的视频格式。属于 Netpbm 工具集。

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

[yuvtoppm](/man/yuvtoppm)(1)
