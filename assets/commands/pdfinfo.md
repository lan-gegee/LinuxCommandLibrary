# TAGLINE

显示 PDF 文件的元数据和属性

# TLDR

**显示 PDF 信息**

```pdfinfo [document.pdf]```

**显示详细元数据**

```pdfinfo -meta [document.pdf]```

**显示 JavaScript 信息**

```pdfinfo -js [document.pdf]```

**显示结构信息**

```pdfinfo -struct [document.pdf]```

**显示第一页的页面框尺寸**

```pdfinfo -box [document.pdf]```

**显示加密 PDF 的信息**

```pdfinfo -upw [password] [document.pdf]```

# SYNOPSIS

**pdfinfo** [_-meta_] [_-box_] [_-js_] [_-struct_] [_options_] _file.pdf_

# PARAMETERS

**-meta**
> 显示文档元数据（XMP）。

**-box**
> 显示页面框尺寸。

**-js**
> 显示 JavaScript。

**-struct**
> 显示结构信息。

**-f** _PAGE_
> 信息起始页。

**-l** _PAGE_
> 信息结束页。

**-enc** _ENCODING_
> 文本编码。

**-opw** _PASSWORD_
> 所有者密码。

**-upw** _PASSWORD_
> 用户密码。

**-rawdates**
> 显示原始日期字符串。

**-isodates**
> 显示 ISO-8601 格式日期。

# OUTPUT FIELDS

**Title**
> 文档标题。

**Author**
> 文档作者。

**Creator**
> 创建应用程序。

**Producer**
> PDF 生成器。

**CreationDate**
> 创建日期。

**ModDate**
> 修改日期。

**Pages**
> 页数。

**Page size**
> 页面尺寸。

**PDF version**
> PDF 规范版本。

**Encrypted**
> 加密状态。

# DESCRIPTION

**pdfinfo** 显示 PDF 文件的元数据和属性。它无需查看实际内容即可提取文档信息。

基本信息包括标题、作者、创建日期、页数和尺寸。这有助于识别和归档 PDF 文件。

页面框信息显示 MediaBox、CropBox 及其他影响打印和显示的页面框尺寸。

加密信息揭示设置了哪些权限：打印、复制、修改。它还会显示加密方法。

XMP 元数据（-meta）包含应用程序写入的扩展信息，可能包括版权、关键词和应用特定数据。

JavaScript 检测（-js）揭示嵌入的脚本，这在不可信的 PDF 中可能是安全隐患。

# CAVEATS

需要 poppler-utils 软件包。若 PDF 制作不规范，某些元数据可能不准确。加密的 PDF 需要正确的密码。

# HISTORY

**pdfinfo** 是 **poppler-utils** 的一部分，源自 **Derek Noonburg** 创建的 **Xpdf** 项目。这些工具已成为类 Unix 系统上处理 PDF 的标准工具。

# INSTALL

```apt: sudo apt install poppler-utils```

```dnf: sudo dnf install poppler-utils```

```apk: sudo apk add poppler-utils```

```nix: nix profile install nixpkgs#poppler-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdffonts](/man/pdffonts)(1), [pdfimages](/man/pdfimages)(1), [pdftotext](/man/pdftotext)(1), [exiftool](/man/exiftool)(1)
