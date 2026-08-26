# TAGLINE

多格式条形码生成器

# TLDR

**生成 QR 码**

```zint -b 58 -d "[data]" -o [output.png]```

**生成 Code 128 条形码**

```zint -b 20 -d "[data]" -o [output.png]```

**生成 EAN-13 条形码**

```zint -b 13 -d "[1234567890123]"```

**设置输出格式**

```zint -b 58 -d "[data]" -o [output.svg]```

**缩放条形码尺寸**

```zint -b 58 -d "[data]" --scale [3]```

**生成带人类可读文本的条形码**

```zint -b 20 -d "[data]" --notext=0```

# SYNOPSIS

**zint** [_options_]

# PARAMETERS

**-b** _type_
> 条形码类型（编号或名称）

**-d** _data_
> 要编码的数据

**-o** _file_
> 输出文件名

**--scale** _factor_
> 输出的缩放系数

**--height** _value_
> 条形码高度（用于一维条形码）

**--fg** _color_
> 前景色（十六进制）

**--bg** _color_
> 背景色（十六进制）

**--notext**
> 禁用人类可读文本

**-i** _file_
> 从文件读取数据

**--batch**
> 处理来自文件的批量数据

**--dump**
> 输出十六进制转储而非图像

**-e**
> 显示符号信息

# BARCODE TYPES

常见类型：**1**（Code 11）、**13**（EAN-13）、**20**（Code 128）、**29**（UPC-A）、**55**（PDF417）、**58**（QR Code）、**71**（Data Matrix）、**92**（Aztec Code）、**142**（MaxiCode）

使用 **zint -t** 列出所有支持的类型。

# DESCRIPTION

**zint** 是一款支持 50 多种条形码类型的生成器。它可创建一维条形码（Code 128、EAN、UPC）、二维条形码（QR Code、Data Matrix、PDF417）以及专用格式（邮政编码、医药条码）。

输出格式包括 PNG、BMP、GIF、PCX、SVG、EPS 和 EMF。该工具还可输出原始十六进制转储，用于调试或自定义渲染。

zint 同时提供命令行界面和 GUI（zint-qt）。还提供库（libzint）以便集成到应用程序中。

# CAVEATS

不同的条形码类型有不同的数据要求。有些只接受数字，有些有长度限制。

QR 码等二维条形码具有纠错级别，会在容量与冗余之间权衡。

并非所有条码扫描器都支持所有符号体系。请验证与目标读取设备的兼容性。

# INSTALL

```apt: sudo apt install zint```

```dnf: sudo dnf install zint```

```pacman: sudo pacman -S zint```

```apk: sudo apk add zint```

```zypper: sudo zypper install zint```

```brew: brew install zint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qrencode](/man/qrencode)(1), [barcode](/man/barcode)(1), [dmtxwrite](/man/dmtxwrite)(1)
