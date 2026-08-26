# TAGLINE

将多个 PDF 文件合并为一个文档

# TLDR

**合并 PDF 文件**

```pdfunite [input1.pdf] [input2.pdf] [output.pdf]```

**合并多个 PDF**

```pdfunite [file1.pdf] [file2.pdf] [file3.pdf] [combined.pdf]```

**合并目录中的所有 PDF**

```pdfunite *.pdf [merged.pdf]```

# SYNOPSIS

**pdfunite** [_options_] _input1.pdf_ _input2.pdf_ ... _output.pdf_

# PARAMETERS

**-v**
> 显示版本。

**-h**
> 显示帮助。

# DESCRIPTION

**pdfunite** 将多个 PDF 文件合并为一个文档。最后一个文件名是输出，其余均为输入。

文件按命令行中指定的顺序合并。页码在所有输入文档之间连续编号。

该工具会保留 PDF 内容，包括文本、图像、注释和书签。各文档内部的链接仍然有效。

合并后的文档使用第一个输入文件的元数据，其他输入文件的元数据不会被合并。

Shell 通配符展开后可以一次合并多个文件。默认按字母顺序排序，这对带编号的文件名非常有效。

对于更复杂的操作（如选择页面、旋转或重新排序），请改用 pdftk 或 qpdf。

# CAVEATS

不支持选择页面（总是包含所有页面）。不支持重新排序。加密的 PDF 需要密码。特别大的合并操作可能需要大量内存。

# HISTORY

**pdfunite** 是 **poppler-utils** 的一部分，源自 **Xpdf** 项目。它提供简单的 PDF 合并功能，无需借助较重的 pdftk 或商业工具。

# INSTALL

```apt: sudo apt install poppler-utils```

```dnf: sudo dnf install poppler-utils```

```apk: sudo apk add poppler-utils```

```nix: nix profile install nixpkgs#poppler-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdfseparate](/man/pdfseparate)(1), [pdftk](/man/pdftk)(1), [qpdf](/man/qpdf)(1), [pdfinfo](/man/pdfinfo)(1)
