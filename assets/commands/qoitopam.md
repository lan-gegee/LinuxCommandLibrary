# TAGLINE

将 QOI 图像转换为 PAM 格式

# TLDR

**将 QOI 文件转换为 PAM**

```qoitopam [input.qoi] > [output.pam]```

**从 stdin 转换**

```qoitopam < [input.qoi] > [output.pam]```

**转换并通过管道传给其他 Netpbm 工具**

```qoitopam [input.qoi] | pamtopng > [output.png]```

# SYNOPSIS

**qoitopam** [_qoifile_]

# PARAMETERS

_qoifile_
> 输入的 QOI 文件。省略时从标准输入读取。

**-quiet**
> libnetpbm 通用选项；抑制提示性消息。

# DESCRIPTION

**qoitopam** 将 QOI（Quite OK Image）格式的图像转换为 PAM（Portable Arbitrary Map）格式。QOI 是一种追求简单和高速的无损图像压缩格式，而 PAM 是 Netpbm 图像处理工具包使用的灵活容器格式。

该工具从指定的参数读取 QOI 文件，未给出文件时则从标准输入读取。它将 PAM 数据写入标准输出，便于与其他 Netpbm 工具串联进行进一步的图像处理和格式转换。

本程序属于 Netpbm 的一部分。

# CAVEATS

只接受与格式无关的 libnetpbm 选项（主要是 **-quiet**）。要转换为 PNG 或 JPEG 等常见格式，请通过管道传给 **pamtopng** 等其他 Netpbm 工具。

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

[pamtoqoi](/man/pamtoqoi)(1), [pngtopam](/man/pngtopam)(1)
