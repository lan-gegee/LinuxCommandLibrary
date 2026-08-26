# TAGLINE

位图字体转 SFNT 转换器

# TLDR

**将 BDF 转换为** sfnt

```fonttosfnt -o [output.ttf] [input.bdf]```

**转换 PCF 字体**

```fonttosfnt -o [output.otb] [input.pcf]```

**详细输出**

```fonttosfnt -v -o [output.ttf] [input.bdf]```

**处理多个字体**

```fonttosfnt -o [output.ttf] [font1.bdf] [font2.bdf]```

# SYNOPSIS

**fonttosfnt** [_options_] _input-files_...

# PARAMETERS

_INPUT-FILES_
> BDF 或 PCF 字体文件。

**-o** _FILE_
> 输出文件名。

**-v**
> 详细输出。

**-g** _N_
> 伽马校正值。

**-m**
> 将字形合并为单一字体。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fonttosfnt** 将位图字体（BDF、PCF）转换为 SFNT 格式（含位图数据的 TrueType/OpenType）。它在保留位图字形的同时采用现代字体文件格式。

该工具将位图 strike 封装进 SFNT 容器，使旧式位图字体可用于要求现代字体格式的系统。多个输入字体可以合并。

fonttosfnt 在经典 X11 位图字体与当代字体基础设施之间架起桥梁。

# CAVEATS

输出仍是位图而非矢量。字体元数据支持有限。最适合特定尺寸。

# HISTORY

fonttosfnt 是 **X.Org** 字体工具的一部分，用于在传统 X11 位图格式与现代 SFNT 容器之间进行转换，以兼容较新的系统。

# INSTALL

```apt: sudo apt install xfonts-utils```

```dnf: sudo dnf install fonttosfnt```

```zypper: sudo zypper install fonttosfnt```

```nix: nix profile install nixpkgs#fonttosfnt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bdftopcf](/man/bdftopcf)(1), [fontforge](/man/fontforge)(1)
