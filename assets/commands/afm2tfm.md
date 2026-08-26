# TAGLINE

Adobe 字体度量到 TeX 字体度量转换器

# TLDR

**将 AFM 文件转换为 TFM** 格式

```afm2tfm [font.afm] [font.tfm]```

为输出字体**使用 TeX 编码进行转换**

```afm2tfm [font.afm] -t [encoding.enc] [font.tfm]```

在生成 TFM 的同时**生成虚拟字体**

```afm2tfm [font.afm] -v [font.vpl] [font.tfm]```

**以倾斜变换进行转换**（伪斜体）

```afm2tfm [font.afm] -s [0.167] [font.tfm]```

**以拉伸变换进行转换**（加宽字体）

```afm2tfm [font.afm] -e [1.2] [font.tfm]```

# SYNOPSIS

**afm2tfm** _afmfile_ [_options_] [_tfmfile_]

# PARAMETERS

**-e** _ratio_
> 按给定比例拉伸（加宽）字体。

**-s** _slant_
> 施加人工倾斜以模拟斜体。

**-c** _height_
> 为 **-V** 生成的小型大写字母使用给定高度（以设计尺寸的比例表示）。

**-a**
> 在输出中省略所有连字和字距调整信息。

**-v** _vplfile_
> 生成虚拟属性列表（VPL）文件。

**-V** _vplfile_
> 与 **-v** 类似，但包含原始字体编码。

**-T** _encfile_
> 对输入和输出都使用该编码文件。

**-p** _encfile_
> 为 PostScript 字体（输入）使用编码。

**-t** _encfile_
> 为 TeX 字体（输出）使用编码。

**-u**
> 只使用指定的编码，忽略 AFM 编码。

# DESCRIPTION

**afm2tfm** 将 Adobe 字体度量（AFM）文件转换为 TeX 字体度量（TFM）格式，使 PostScript Type 1 字体能用于 TeX 和 LaTeX 排版系统。TFM 文件包含 TeX 正确排版文本所需的字符尺寸和字距调整信息。

该工具可以在转换过程中施加变换，包括用于伪斜体的倾斜，以及人为加宽字体的拉伸。当用 **-v** 生成虚拟字体时，它会创建一个 VPL（虚拟属性列表）文件，将 TeX 字符代码映射为 PostScript 字形名称，从而实现编码转换。

此实用程序属于标准 TeX 发行版，是将自定义字体集成到 TeX 工作流中的必备工具。虚拟字体的输出可能还需用 **vptovf** 做进一步处理。

# CAVEATS

生成的 TFM 文件只包含度量信息，并不含实际的字体轮廓。要完整地安装字体，还需要 PFB/PFA 字体文件以及供 dvips 或 pdfTeX 使用的 map 文件条目。虚拟字体在使用前必须先用 **vptovf** 编译。

# HISTORY

**afm2tfm** 由 **Tom Rokicki** 于 **1980** 年代末编写，是 dvips 软件包的一部分。随着 PostScript 打印机普及，用户希望在 TeX 中使用专业 Type 1 字体来取代有限的 Computer Modern 字体家族，该工具由此变得不可或缺。如今它仍是 TeX Live 和 MiKTeX 发行版的组成部分。

# INSTALL

```apt: sudo apt install texlive-binaries```

```apk: sudo apk add texlive-dvi```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[dvips](/man/dvips)(1)

# RESOURCES

```[Homepage](https://ctan.org/pkg/dvips)```

<!-- verified: 2026-06-11 -->
