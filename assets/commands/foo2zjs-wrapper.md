# TAGLINE

PostScript/PDF 转 ZjStream 包装脚本

# TLDR

**打印 PostScript 文件**

```foo2zjs-wrapper [file.ps]```

**设置纸张大小**

```foo2zjs-wrapper -p [a4] [file.ps]```

**彩色打印**

```foo2zjs-wrapper -c [file.ps]```

**设置分辨率**

```foo2zjs-wrapper -r [1200x600] [file.ps]```

**双面打印（长边）**

```foo2zjs-wrapper -d 2 [file.ps]```

**指定打印机型号**

```foo2zjs-wrapper -z [model] [file.ps]```

# SYNOPSIS

**foo2zjs-wrapper** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 要打印的 PostScript 或 PDF 文件。

**-p** _CODE_
> 纸张大小代码（例如 letter、a4、legal）。

**-r** _XxY_
> 设备分辨率（DPI，默认 1200x600）。

**-c**
> 以彩色打印（否则为单色）。

**-n** _COPIES_
> 打印份数。

**-m** _CODE_
> 介质类型代码。

**-d** _MODE_
> 双面打印：1=关闭，2=长边，3=短边。

**-s** _CODE_
> 输入纸槽代码。

**-t**
> 草稿模式（隔一个像素输出一个白色像素）。

**-T** _DENSITY_
> 打印浓度（1-5）。

**-z** _MODEL_
> 打印机型号。

**-g** _OPTIONS_
> 额外的 Ghostscript 选项。

**-D** _LEVEL_
> 设置调试级别。

**--help**
> 显示帮助信息。

# DESCRIPTION

**foo2zjs-wrapper** 将 PostScript/PDF 转换为 HP 和 Minolta/QMS 打印机所需的 ZjStream 格式。它组合了 Ghostscript 栅格化与 foo2zjs 编码。

该包装器处理从文档到打印机的完整流水线，提供简单的打印接口。它将常见选项转换为底层工具所需的参数。

foo2zjs-wrapper 是向 foo2zjs 支持的打印机打印文档的主要方式。

# CAVEATS

需要 Ghostscript。仅限于受支持的打印机型号。彩色支持因打印机而异。

# HISTORY

foo2zjs-wrapper 是 **foo2zjs** 项目的一部分，在 Linux 上为使用 ZjStream 协议的打印机提供易用的文档打印能力。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

```dnf: sudo dnf install foo2zjs```

```nix: nix profile install nixpkgs#foo2zjs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2zjs](/man/foo2zjs)(1), [gs](/man/gs)(1), [lpr](/man/lpr)(1)
