# TAGLINE

将 PDF 文件转换为 HTML、XML 或 PNG 格式

# TLDR

将 PDF 页面转换为 **HTML**

```pdftohtml [file.pdf] [output.html]```

为整个文档生成**单个 HTML 文件**

```pdftohtml -s [file.pdf] [output.html]```

跳过嵌入**图像**

```pdftohtml -i [file.pdf] [output.html]```

输出 **XML** 而非 HTML

```pdftohtml -xml [file.pdf] [output.xml]```

# SYNOPSIS

**pdftohtml** [_options_] _pdf_file_ [_output_file_]

# PARAMETERS

**-i**
> 忽略图像

**-s**
> 为所有页面生成单个 HTML 文件

**-xml**
> 以 XML 而非 HTML 输出

**-c**
> 生成复杂输出（布局更精确）

**-hidden**
> 强制提取隐藏文本

**-f _n_**
> 要转换的第一页

**-l _n_**
> 要转换的最后一页

**-zoom _factor_**
> 缩放系数（默认：1.5）

**-noframes**
> 不生成框架（单页输出）

**-enc _encoding_**
> 输出编码（默认：UTF-8）

# DESCRIPTION

**pdftohtml** 将 PDF 文件转换为 HTML、XML 或 PNG 格式。它是 **poppler-utils** 软件包的一部分，尽力在生成的 HTML 输出中保留 PDF 页面的视觉版式。

默认情况下它会为每页生成一个 HTML 文件外加一个框架集索引。**-s** 选项会创建包含所有页面的单一文件。除非指定 **-i**，否则图像会被提取为单独的 PNG 文件。

XML 输出模式提供关于文本位置和格式的结构化数据，便于进一步处理或文本提取。

# CAVEATS

复杂的 PDF 版式可能无法准确转换。扫描版 PDF（图像）需要 OCR，无法产生文本输出。字体嵌入和特殊字符可能导致显示问题。不使用 **-s** 选项时，大型 PDF 会生成大量输出文件。

# HISTORY

**pdftohtml** 起源于 **xpdf** 项目，现作为 **poppler-utils** 的一部分维护——该分支为 Linux 系统提供了访问 PDF 渲染功能的共享库。

# INSTALL

```apt: sudo apt install poppler-utils```

```dnf: sudo dnf install poppler-utils```

```apk: sudo apk add poppler-utils```

```brew: brew install pdftohtml```

```nix: nix profile install nixpkgs#poppler-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdftotext](/man/pdftotext)(1), [pdftoppm](/man/pdftoppm)(1), [pdfinfo](/man/pdfinfo)(1), [pandoc](/man/pandoc)(1)
