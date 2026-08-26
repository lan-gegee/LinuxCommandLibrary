# TAGLINE

解码 PDF 中的 zlib 压缩 JavaScript

# TLDR

**解码 zlib 压缩的 JavaScript**

```zjsdecode [encoded.js] [output.js]```

**从 stdin 解码**

```cat [encoded.js] | zjsdecode > [output.js]```

**解码并美化**

```zjsdecode [encoded.js] | js-beautify```

# SYNOPSIS

**zjsdecode** [_input_file_] [_output_file_]

# PARAMETERS

_input_file_
> 待解码的压缩 JavaScript 文件

_output_file_
> 存放解码后 JavaScript 的输出文件

# DESCRIPTION

**zjsdecode** 用于解码经 zlib 编码压缩的 JavaScript 文件，这种压缩常见于 PDF 文件中。一些恶意 PDF 会嵌入经 zlib 压缩的 JavaScript 以躲避分析。

该工具适用于恶意软件分析、PDF 取证以及从文档中提取嵌入脚本。它可以还原 PDF 流中使用的 FlateDecode 压缩。

zjsdecode 是多个 PDF 分析工具包的组成部分，通常与其他 PDF 检查工具配合使用。

# CAVEATS

这是一个专门用于 PDF 分析的工具。它无法解码采用其他混淆手段（如 eval()、字符串编码或压缩精简）处理的 JavaScript。

解码后的 JavaScript 可能仍是混淆过的，需要进一步分析或去混淆。

分析潜在恶意脚本时务必谨慎。请在隔离环境中运行。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdf-parser](/man/pdf-parser)(1), [pdfid](/man/pdfid)(1), [js-beautify](/man/js-beautify)(1), [zlib-flate](/man/zlib-flate)(1)
