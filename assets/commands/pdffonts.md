# TAGLINE

列出 PDF 文档中使用的字体

# TLDR

**列出 PDF 中的字体**

```pdffonts [document.pdf]```

**按页码范围列出字体**

```pdffonts -f [1] -l [10] [document.pdf]```

**显示替换字体**

```pdffonts -subst [document.pdf]```

**从指定页面开始列出**

```pdffonts -f [5] [document.pdf]```

# SYNOPSIS

**pdffonts** [_-f first_] [_-l last_] [_-subst_] [_options_] _file.pdf_

# PARAMETERS

**-f** _PAGE_
> 要检查的第一页。

**-l** _PAGE_
> 要检查的最后一页。

**-subst**
> 显示字体替换情况。

**-opw** _PASSWORD_
> 所有者密码。

**-upw** _PASSWORD_
> 用户密码。

**-v**
> 打印版本。

**-h**
> 打印帮助。

# OUTPUT COLUMNS

**name**
> 字体名称。

**type**
> 字体类型（Type 1、TrueType、CID 等）。

**emb**
> 是否嵌入（yes/no）。

**sub**
> 是否为子集（yes/no）。

**uni**
> 是否有 Unicode 映射（yes/no）。

**object ID**
> PDF 对象标识符。

# DESCRIPTION

**pdffonts** 列出 PDF 文档中使用的字体。它显示字体名称、类型和嵌入状态。

嵌入字体包含在 PDF 中，无论系统安装了什么字体都能保证一致的显示效果。未嵌入的字体依赖系统字体，可能导致外观差异。

子集字体只包含文档中用到的字符，可减小文件体积。完整字体则包含所有字形。

字体类型包括 Type 1（PostScript）、TrueType、CID 字体（用于亚洲语言）以及 Type 3（位图/用户自定义）。

Unicode 映射指示文本能否被可靠地提取或搜索。缺少 Unicode 映射会影响复制/粘贴和无障碍访问。

页码范围选项可以只检查特定部分，而无需处理整个文档。

# CAVEATS

属于 poppler-utils 软件包的一部分。可能不会显示全部字体细节。加密的 PDF 需要密码。子集字体的名称可能难以辨认。

# HISTORY

**pdffonts** 是 **poppler-utils** 的一部分，源自 **Derek Noonburg** 创建的 **Xpdf** 项目。Poppler 已成为许多开源应用的标准 PDF 渲染库。

# INSTALL

```apt: sudo apt install poppler-utils```

```dnf: sudo dnf install poppler-utils```

```apk: sudo apk add poppler-utils```

```nix: nix profile install nixpkgs#poppler-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdfinfo](/man/pdfinfo)(1), [pdftotext](/man/pdftotext)(1), [pdftops](/man/pdftops)(1), [pdftocairo](/man/pdftocairo)(1)
