# TAGLINE

以 PostScript 格式生成条形码。

# TLDR

**生成 PostScript 条形码**

```barcode -b "[data]" -o [output.ps]```

**生成 EPS 条形码**

```barcode -b "[data]" -E -o [output.eps]```

**生成 Code 39 条形码**

```barcode -e code39 -b "[DATA123]" -o [output.ps]```

**生成 EAN-13 条形码**

```barcode -e ean -b "[5901234123457]" -o [output.ps]```

**生成 Code 128 条形码**

```barcode -e code128 -b "[data]" -o [output.ps]```

**生成不带文字标签的条形码**

```barcode -b "[data]" -n -o [output.ps]```

**设置自定义尺寸**

```barcode -b "[data]" -g [100x50] -o [output.ps]```

# SYNOPSIS

**barcode** [**-e** _encoding_] [**-b** _string_] [**-o** _file_] [_options_]

# PARAMETERS

**-b** _string_
> 要编码为条形码的数据。

**-e** _encoding_
> 条形码编码类型（ean、upc、code39、code128 等）。默认取 **BARCODE_ENCODING** 环境变量或自动检测。

**-i** _file_
> 从文件读取要编码的字符串（默认：stdin）。

**-o** _file_
> 输出文件（默认：stdout）。

**-g** _geometry_
> 条形码几何参数，格式为 _WxH+x+y_（大小和位置）。

**-n**
> 数字输出：只打印条纹，不打印人类可读标签。

**-c**
> 对允许省略校验位的编码，省略校验字符。

**-t** _WxH_
> 表格模式：每页生成多个条形码。

**-m** _margin_
> 条形码周围的边距大小。

**-p** _pagesize_
> 页面尺寸（a4、letter 等）。

**-u** _unit_
> 尺寸单位（mm、in、pt）。

**-E**
> 以 EPS（Encapsulated PostScript）格式输出。

**-P**
> 以 PCL 格式输出（用于 HP 打印机）。

# SUPPORTED ENCODINGS

**ean** / **ean13**: 欧洲商品编码（13 位数字）
**upc** / **upc-a**: 通用产品代码
**isbn**: 国际标准书号
**code39**: Code 39（字母数字）
**code128**: Code 128（高密度）
**code93**: Code 93
**i25**: Interleaved 2 of 5
**cbr** / **codabar**: Codabar
**msi**: MSI Plessey
**pls**: Plessey

# DESCRIPTION

**barcode** 是一款 GNU 工具，可将文本数据生成多种格式的条形码。它输出可直接打印的 PostScript 或 EPS，也可转换为其他格式或嵌入文档。

该工具支持零售、物流和库存管理中使用的所有主流一维条形码符号体系。每种编码对有效字符和可选校验位都有特定规则。对于需要校验位的格式，工具会自动计算校验位。

输出可通过不同的大小、边距和标签选项进行定制。表格模式可以批量生成整页标签用于批量打印。

# CAVEATS

输出仅为 PostScript/EPS；要转换为 PNG 或其他光栅格式需要 Ghostscript 或 ImageMagick 之类的工具。并非所有编码都接受所有字符：Code 39 只支持大写字母，EAN/UPC 要求特定的位数。校验位验证会自动执行，但数据必须符合所选编码的要求。

# HISTORY

GNU barcode 由 **Alessandro Rubini** 编写，于 **20 世纪 90 年代末**作为 GNU 项目的一部分首次发布。它专为 Unix 打印系统和文档准备工作流设计。虽然后来出现了各种格式的条形码生成新工具和新库，但 GNU barcode 凭借其简单性和 PostScript 输出质量依然有用武之地。

# INSTALL

```apt: sudo apt install barcode```

```dnf: sudo dnf install barcode```

```pacman: sudo pacman -S barcode```

```apk: sudo apk add barcode```

```zypper: sudo zypper install barcode```

```nix: nix profile install nixpkgs#barcode```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[qrencode](/man/qrencode)(1), [zint](/man/zint)(1), [gs](/man/gs)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/barcode/)```

```[Source code](https://git.savannah.gnu.org/cgit/barcode.git)```

<!-- verified: 2026-06-19 -->
