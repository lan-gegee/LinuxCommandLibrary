# TAGLINE

将多幅单平面图像合并为一幅多平面 PAM

# TLDR

**将图像作为图层堆叠**

```pamstack [red.pgm] [green.pgm] [blue.pgm] > [rgb.pam]```

**堆叠并加入 Alpha 通道**

```pamstack [image.ppm] [alpha.pgm] > [rgba.pam]```

# SYNOPSIS

**pamstack** [_options_] _files_...

# PARAMETERS

_files_
> 输入图像文件（尺寸必须相同）。

**-tupletype** _type_
> 输出的元组类型。

# DESCRIPTION

**pamstack** 将多幅单平面图像合并为一幅多平面 PAM。可以用分离的红、绿、蓝文件合成 RGB，也可以添加 Alpha 通道。属于 Netpbm 工具集。

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

[pamsplit](/man/pamsplit)(1)
