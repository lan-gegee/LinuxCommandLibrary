# TAGLINE

将 PAM 图像转换为 Windows 的 ICO 或 CUR 格式

# TLDR

**将 PAM 转换为 Windows 图标**

```pamtowinicon [input.pam] > [output.ico]```

**创建带热点的光标**

```pamtowinicon -xhotspot [16] -yhotspot [16] [input.pam] > [output.cur]```

# SYNOPSIS

**pamtowinicon** [_options_] [_file_]

# PARAMETERS

**-xhotspot** _n_
> 光标热点的 X 坐标。

**-yhotspot** _n_
> 光标热点的 Y 坐标。

**-truetransparent**
> 使用真正的透明度而不是颜色键。

# DESCRIPTION

**pamtowinicon** 将 PAM 图像转换为 Windows 的 ICO（图标）或 CUR（光标）格式。支持在同一个文件中包含多种尺寸，并支持透明度。属于 Netpbm 工具集。

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

[winicontopam](/man/winicontopam)(1), [ppmtowinicon](/man/ppmtowinicon)(1)
