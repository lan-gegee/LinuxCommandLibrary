# TAGLINE

向现有 PDF 文件添加新的嵌入文件

# TLDR

向 PDF **添加**附件

```pdfattach input.pdf file_to_attach output.pdf```

**替换**同名的现有附件

```pdfattach -replace input.pdf file_to_attach output.pdf```

显示**帮助**

```pdfattach --help```

显示**版本**

```pdfattach -v```

# SYNOPSIS

**pdfattach** [_options_] _PDF-file_ _file-to-attach_ _output-PDF-file_

# DESCRIPTION

**pdfattach** 向现有 PDF 文件添加新的嵌入文件（附件）。附件存储在 PDF 内部，可使用 pdfdetach 提取。

# PARAMETERS

**-replace**
> 若存在同名附件则替换之

**-h, --help**
> 显示用法信息

**-v**
> 显示版本信息

# CAVEATS

原 PDF 文件不会被修改；会创建包含附件的新输出文件。若要就地更新文件，可先输出到临时文件再重命名。

# HISTORY

**pdfattach** 是 **poppler-utils** 的一部分，这是一组基于 Poppler PDF 渲染库的命令行工具，用于处理 PDF 文件。

# INSTALL

```apt: sudo apt install poppler-utils```

```dnf: sudo dnf install poppler-utils```

```apk: sudo apk add poppler-utils```

```nix: nix profile install nixpkgs#poppler-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdfdetach](/man/pdfdetach)(1), [pdfinfo](/man/pdfinfo)(1), [pdfunite](/man/pdfunite)(1)
