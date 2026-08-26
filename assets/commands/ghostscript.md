# TAGLINE

用于 PostScript 和 PDF 文件处理的解释器

# TLDR

**将 PDF 转换为图片**

```gs -dNOPAUSE -dBATCH -sDEVICE=png16m -r300 -sOutputFile=[page-%d.png] [input.pdf]```

**合并 PDF**

```gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=[merged.pdf] [file1.pdf] [file2.pdf]```

**压缩 PDF**

```gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -sOutputFile=[small.pdf] [large.pdf]```

**将 PS 转换为 PDF**

```gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=[output.pdf] [input.ps]```

**从 PDF 中提取页面**

```gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dFirstPage=[2] -dLastPage=[5] -sOutputFile=[extract.pdf] [input.pdf]```

# SYNOPSIS

**gs** [_options_] [_files_]

# PARAMETERS

**-dNOPAUSE**
> 不在页面之间暂停。

**-dBATCH**
> 处理完毕后退出。

**-sDEVICE** _device_
> 输出设备（pdfwrite、png16m、jpeg 等）。

**-sOutputFile** _file_
> 输出文件名（用 %d 表示页码）。

**-r** _resolution_
> 分辨率（DPI）。

**-dPDFSETTINGS** _setting_
> PDF 质量：/screen、/ebook、/printer、/prepress。

**-dFirstPage** _n_
> 起始页。

**-dLastPage** _n_
> 结束页。

**-dCompatibilityLevel** _ver_
> PDF 版本（1.4、1.5 等）。

**-q**
> 安静模式；抑制启动消息。

**-dSAFER**
> 出于安全考虑限制文件操作（近期版本中为默认行为）。

# DESCRIPTION

**Ghostscript**（gs）是一个 PostScript 和 PDF 解释器。它可以将文档渲染为多种输出格式、在不同格式之间转换，并处理打印作业。它是 Unix/Linux 上许多 PDF 工具和打印系统背后的引擎。

该工具支持多种输出设备，可用于光栅化、格式转换和打印处理。PDF 操作包括合并、拆分、压缩以及不同质量级别之间的转换。

# CONFIGURATION

**/etc/ghostscript/**
> 系统级配置目录，存放字体映射、资源文件和初始化脚本。

**~/.ghostscript**
> 用户特定的 Ghostscript 资源与配置覆盖。

# CAVEATS

命令行语法复杂。某些操作需要特定的设备驱动。字体处理可能需要配置。安全设置会限制文件操作。

# HISTORY

Ghostscript 由 **L. Peter Deutsch** 于 **1988 年**发起，最初是一个自由的 PostScript 解释器。现由 Artifex Software 开发，至今仍是 Unix/Linux 打印和 PDF 处理的基础。

# INSTALL

```apt: sudo apt install ghostscript```

```dnf: sudo dnf install ghostscript```

```pacman: sudo pacman -S ghostscript```

```zypper: sudo zypper install ghostscript```

```brew: brew install ghostscript```

```nix: nix profile install nixpkgs#ghostscript```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdf2ps](/man/pdf2ps)(1), [ps2pdf](/man/ps2pdf)(1), [pdftk](/man/pdftk)(1), [convert](/man/convert)(1)
