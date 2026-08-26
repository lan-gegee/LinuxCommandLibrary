# TAGLINE

将 PDF 拆分为单独的页面

# TLDR

**提取所有页面**

```pdfseparate [document.pdf] [output_%d.pdf]```

**提取指定页面范围**

```pdfseparate -f [1] -l [10] [document.pdf] [output_%d.pdf]```

**提取单页**

```pdfseparate -f [5] -l [5] [document.pdf] [page5.pdf]```

# SYNOPSIS

**pdfseparate** [_-f first_] [_-l last_] [_options_] _input.pdf_ _output_pattern_

# PARAMETERS

**-f** _PAGE_
> 开始提取的第一页。

**-l** _PAGE_
> 结束提取的最后一页。

**-v**
> 打印版本。

**-h**
> 打印帮助。

# OUTPUT PATTERN

输出模式中的 %d 代表页码：
- `page_%d.pdf` 会生成 page_1.pdf、page_2.pdf 等。
- `output-%03d.pdf` 会生成 output-001.pdf、output-002.pdf 等。

# DESCRIPTION

**pdfseparate** 将 PDF 拆分为单独的页面。每一页都会成为一个独立的 PDF 文件。

输出模式必须包含 %d（或 %03d 之类的变体），它会被替换为页码。这使输出文件得以有序命名。

页面范围选项可以只提取文档的一个子集。结合具体的页码，还可以提取单个页面。

生成的文件都是各自只含一页的独立 PDF。它们可以用 pdfunite 重新组合，也可以单独使用。

所有页面内容都会被保留，包括注释、链接和嵌入资源。

# CAVEATS

无法选择非连续页面。每页都是一个单独的文件（不能把多页提取到同一个文件中）。加密的 PDF 需要密码。

# HISTORY

**pdfseparate** 是 **poppler-utils** 的一部分，这是源自 **Xpdf** 的开源 PDF 工具集。它提供简单的页面提取功能且没有复杂的依赖。

# INSTALL

```apt: sudo apt install poppler-utils```

```dnf: sudo dnf install poppler-utils```

```apk: sudo apk add poppler-utils```

```nix: nix profile install nixpkgs#poppler-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdfunite](/man/pdfunite)(1), [pdftk](/man/pdftk)(1), [qpdf](/man/qpdf)(1), [pdfinfo](/man/pdfinfo)(1)
