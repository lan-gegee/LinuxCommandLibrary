# TAGLINE

将文本渲染为 PBM 位图图像

# TLDR

**创建文本图像**

```pbmtext "[Hello World]" > [output.pbm]```

**使用指定字体创建**

```pbmtext -font [fixed] "[Hello]" > [output.pbm]```

**使用内置字体创建**

```pbmtext -builtin [fixed] "[Hello]" > [output.pbm]```

# SYNOPSIS

**pbmtext** [_options_] [_text_]

# PARAMETERS

**-font** _file_
> BDF 字体文件。

**-builtin** _name_
> 内置字体（fixed、bdf）。

**-space** _pixels_
> 字符间距。

**-lspace** _pixels_
> 行距。

**-nomargins**
> 文本周围不留边距。

# DESCRIPTION

**pbmtext** 将文本渲染为 PBM 位图图像。属于 Netpbm 工具集，用于创建文字图形。支持 BDF 字体和内置字体。

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

[pbmtextps](/man/pbmtextps)(1), [ppmlabel](/man/ppmlabel)(1)
