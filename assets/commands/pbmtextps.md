# TAGLINE

通过 Ghostscript 使用 PostScript 字体将文本渲染为 PBM 位图

# TLDR

**使用 PostScript 字体渲染文本**

```pbmtextps -font [Times-Roman] "[Hello World]" > [output.pbm]```

**以指定字号渲染**

```pbmtextps -fontsize [48] "[text]" > [output.pbm]```

# SYNOPSIS

**pbmtextps** [_options_] _text_

# PARAMETERS

**-font** _name_
> PostScript 字体名称。

**-fontsize** _n_
> 字号（磅）。

**-resolution** _n_
> 输出分辨率（DPI）。

# DESCRIPTION

**pbmtextps** 通过 Ghostscript 使用 PostScript 字体将文本渲染为 PBM 位图。可配合任意 PostScript 字体实现高质量文本渲染。属于 Netpbm 工具集。

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

[pbmtext](/man/pbmtext)(1), [ppmlabel](/man/ppmlabel)(1)
