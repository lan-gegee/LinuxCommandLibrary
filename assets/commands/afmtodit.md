# TAGLINE

Adobe 字体度量到 groff 字体描述文件转换器

# TLDR

**将 AFM 文件转换为** groff 字体

```afmtodit [font.afm] [textmap] [fontname]```

生成**斜体修正量**（以千分之一 em 为单位）

```afmtodit -i [50] [font.afm] [textmap] [fontname]```

使用**编码**文件转换

```afmtodit -e [encoding.enc] [font.afm] [textmap] [fontname]```

# SYNOPSIS

**afmtodit** [_-ckmnsvx_] [_-a n_] [_-d desc_] [_-e enc_] [_-f name_] [_-i n_] [_-o out_] _afm-file_ _map-file_ _font_

# DESCRIPTION

**afmtodit** 将 Adobe 字体度量（AFM）文件转换为适合 groff 排版系统使用的字体描述文件。它创建的字体度量文件是 groff 的 PostScript 驱动在排版文档时正确定位字符和控制间距所必需的。

该工具使用用户提供的映射文件把 PostScript 字形名称映射为 groff 字符名称，默认还会在输出中加入字距调整对和连字信息。此外它会计算一个倾斜参数（取自 AFM 的 ItalicAngle 或 **-a** 选项），groff 用它在斜体字形上放置重音符号。

# PARAMETERS

**-a** _n_
> 写入字体文件的倾斜值，groff 用它放置重音符号（默认：AFM 文件中 ItalicAngle 的相反数）。

**-c**
> 在输出中包含标识 PostScript 字体的注释。

**-d** _file_
> 使用替代的设备描述（DESC）文件，而非默认文件。

**-e** _file_
> 使用给定的编码文件对 PostScript 字体重新编码。

**-f** _name_
> groff 字体的内部名称。

**-i** _n_
> 根据 _n_ 生成斜体修正和下标修正（单位为千分之一 em）。

**-k**
> 省略字距调整数据；只用于等宽（固定宽度）字体。

**-m**
> 防止出现负的左侧斜体修正值。

**-n**
> 不输出连字（ligatures）命令；用于等宽字体。

**-o** _file_
> 输出文件名

**-s**
> 将字体标记为特殊（special）字体。

**-v**
> 打印版本信息并退出。

**-x**
> 不使用内置的 Adobe Glyph List。

# CAVEATS

需要字体厂商提供的有效 AFM 文件。文本映射文件必须正确映射 PostScript 字形名称。输出专用于 groff 的 PostScript 驱动。

# HISTORY

**afmtodit** 是 GNU groff 的一部分，自 **1989** 年起持续开发。它让 groff 文档得以使用 PostScript 字体，将排版系统的可用字体扩展到了其原始字体集之外。

# INSTALL

```apt: sudo apt install groff```

```dnf: sudo dnf install groff```

```pacman: sudo pacman -S groff```

```apk: sudo apk add groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[groff](/man/groff)(1), [addftinfo](/man/addftinfo)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/groff.git)```

```[Homepage](https://www.gnu.org/software/groff/)```

```[Documentation](https://www.gnu.org/software/groff/manual/)```

<!-- verified: 2026-06-11 -->
