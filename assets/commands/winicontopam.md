# TAGLINE

将 Windows 图标转换为 PAM 格式

# TLDR

**将 Windows 图标转换为 PAM**（默认选择质量最高的图像）

```winicontopam [input.ico] > [output.pam]```

**提取特定索引的图像**

```winicontopam -image=[0] [input.ico] > [output.pam]```

**将所有图像提取为多图像 PAM**

```winicontopam -allimages [input.ico] > [output.pam]```

**包含 AND 掩码作为第五个通道**

```winicontopam -andmasks [input.ico] > [output.pam]```

# SYNOPSIS

**winicontopam** [_options_] [_file_]

# PARAMETERS

**-image=**_N_
> 提取索引为 _N_ 的图像（从零开始）。不能与 **-allimages** 同时使用。

**-allimages**
> 将 ICO/CUR 文件中的每一幅图像都提取为多图像 PAM 流。

**-andmasks**
> 输出五通道 PAM，将 AND 掩码作为第五个平面（在 RGBA 之外）。

**-verbose**
> 打印关于输入文件的提示信息。

**-quiet**
> 抑制提示性输出（标准 libnetpbm 选项）。

# DESCRIPTION

**winicontopam** 将 Microsoft Windows 的 ICO 或 CUR 文件转换为带 alpha 通道的 Netpbm PAM 图像。Windows 图标文件可能包含多幅不同分辨率和颜色深度的图像；默认情况下，winicontopam 会挑选质量最高的一幅（先看尺寸最大，再看每像素位数最多）。

属于 **Netpbm** 工具集。未指定文件时从 stdin 读取。

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

[pamtowinicon](/man/pamtowinicon)(1), [winicontoppm](/man/winicontoppm)(1)

