# TAGLINE

显示 Adobe 字体度量信息

# TLDR

**显示 AFM 字体度量**

```printafm [font.afm]```

**显示特定字体信息**

```printafm [Times-Roman]```

# SYNOPSIS

**printafm** [_font_]

# PARAMETERS

_FONT_
> AFM 字体文件或名称。

# DESCRIPTION

**printafm** 显示 Adobe Font Metrics（AFM）文件中的详细度量信息，包括字符宽度、边界框、字距调整对以及其他排版属性。AFM 文件随 PostScript Type 1 字体一同提供，描述字体的尺寸信息，供页面布局和排版使用。

这个 Ghostscript 工具适用于在调试 PostScript 或 PDF 渲染时检查字体属性，或在开发需要计算文本尺寸以进行布局的应用时使用。

# CAVEATS

需要 AFM 文件。属于 Ghostscript 套件。

# HISTORY

printafm 是 **Ghostscript** 中用于显示字体度量信息的组件。

# INSTALL

```apt: sudo apt install ghostscript```

```dnf: sudo dnf install ghostscript```

```pacman: sudo pacman -S ghostscript```

```apk: sudo apk add ghostscript```

```zypper: sudo zypper install ghostscript```

```brew: brew install ghostscript```

```nix: nix profile install nixpkgs#ghostscript```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gs](/man/gs)(1), [fc-list](/man/fc-list)(1)
