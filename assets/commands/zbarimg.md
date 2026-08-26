# TAGLINE

从图像文件读取条形码

# TLDR

**扫描图像中的条形码**

```zbarimg [image.png]```

**扫描多张图像**

```zbarimg [image1.png] [image2.jpg]```

**只输出原始数据**

```zbarimg --raw [image.png]```

**只扫描二维码**（先禁用全部，再启用 qrcode）

```zbarimg -Sdisable -Sqrcode.enable [image.png]```

**安静模式**（不显示统计和警告）

```zbarimg -q [image.png]```

**显示图像并高亮检测到的条形码**

```zbarimg -d [image.png]```

**XML 输出**

```zbarimg --xml [image.png]```

**输出检测到的条形码的多边形顶点**

```zbarimg --polygon [image.png]```

# SYNOPSIS

**zbarimg** [_-qv_] [_--raw_] [_-dD_] [_--xml_] [_-S[symbology.]config[=value]_] _image..._

# PARAMETERS

**--raw**
> 输出原始符号数据，不带编码类型前缀。

**-q**, **--quiet**
> 安静模式；只输出解码的符号数据。抑制统计行以及 stderr 上无条形码的警告。

**-d**, **--display**
> 启用图像显示，并将已解码的符号高亮。

**-D**, **--nodisplay**
> 禁用图像显示。

**--xml**, **--noxml**
> 启用或禁用 XML 输出格式，其中包含扫描元数据包裹的解码数据。

**--polygon**
> 以 SVG 格式输出条形码边界的多边形顶点。

**-S** _[symbology.]config[=value]_
> 设置解码器配置。编码类型包括：ean13、ean8、upca、upce、isbn13、isbn10、i25、codabar、code39、code93、code128、qrcode，或 * 表示全部。

**-v**, **--verbose**[=_n_]
> 提高调试输出级别。可多次使用 -v 获取更多细节，或直接指定 n。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# SUPPORTED FORMATS

**QR-Code**
> 二维矩阵条形码。

**EAN-13**、**EAN-8**
> 欧洲商品编号（European Article Number）。

**UPC-A**、**UPC-E**
> 通用产品代码（Universal Product Code）。

**Code-128**、**Code-93**、**Code-39**
> 一维线性条形码。

**Interleaved 2 of 5** (i25)
> 仅数字的线性条形码。

**Codabar**
> 图书馆和血库使用的数字条形码。

**ISBN-10**、**ISBN-13**
> 图书标识符。

**DataBar**、**DataBar Expanded**
> GS1 DataBar 编码体系。

# DESCRIPTION

**zbarimg** 从图像文件读取条形码，检测并解码包括二维码在内的多种条形码格式。

系统会自动检测多种条形码类型。可通过设置禁用特定类型以加快扫描。

输出显示条形码类型和解码数据。原始模式只输出数据，不带类型前缀。

一张图像中的多个条形码都会被检测到，每个条目单独占一行报告。

display 选项会显示图像并高亮检测到的条形码，有助于确认检测结果是否正确。

支持的图像格式包括 PNG、JPEG 以及 ImageMagick 支持的任何格式。

# CAVEATS

检测效果取决于图像质量。模糊或对比度低的图像可能失败。某些条形码类型需要显式启用。

# HISTORY

**zbar** 和 **zbarimg** 由 **Jeff Brown** 于 **2007 年**前后创建。该库为图像和视频提供条形码扫描功能，并提供多种语言的绑定。

# INSTALL

```apt: sudo apt install zbar-tools```

```dnf: sudo dnf install zbar```

```pacman: sudo pacman -S zbar```

```apk: sudo apk add zbar```

```zypper: sudo zypper install zbar```

```brew: brew install zbar```

```nix: nix profile install nixpkgs#zbar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zbarcam](/man/zbarcam)(1), [qrencode](/man/qrencode)(1), [dmtxread](/man/dmtxread)(1)
