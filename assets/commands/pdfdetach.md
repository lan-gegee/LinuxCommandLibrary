# TAGLINE

列出或提取 PDF 文件中的嵌入文件

# TLDR

**列出** PDF 中的所有附件

```pdfdetach -list input.pdf```

按编号**保存**附件

```pdfdetach -save 1 input.pdf```

按**名称**保存附件

```pdfdetach -savefile filename input.pdf```

保存**所有**附件

```pdfdetach -saveall input.pdf```

以**自定义输出**名称保存

```pdfdetach -save 1 -o output.txt input.pdf```

从**密码保护**的 PDF 中提取

```pdfdetach -save 1 -upw password input.pdf```

以指定**编码**列出

```pdfdetach -list -enc UTF-8 input.pdf```

# SYNOPSIS

**pdfdetach** [_options_] _PDF-file_

# DESCRIPTION

**pdfdetach** 列出或提取 PDF 文件中的嵌入文件（附件）。它是 poppler-utils 软件包的一部分。

# PARAMETERS

**-list**
> 列出 PDF 中的所有嵌入文件

**-save NUMBER**
> 按索引号保存嵌入文件

**-savefile FILENAME**
> 按文件名保存嵌入文件

**-saveall**
> 以原始名称保存所有嵌入文件

**-o PATH**
> 设置保存文件的输出文件名或目录

**-enc ENCODING**
> 指定文件名的文本编码（默认：UTF-8）

**-opw PASSWORD**
> 加密 PDF 的所有者密码

**-upw PASSWORD**
> 加密 PDF 的用户密码

**-v**
> 显示版本信息

**-h, --help**
> 显示用法信息

# CAVEATS

退出码：0（成功）、1（PDF 打开错误）、2（输出文件错误）、3（权限问题）、99（其他错误）。附件编号从 1 开始。

# HISTORY

**pdfdetach** 是 **poppler-utils** 的一部分，这是一组基于 Poppler PDF 渲染库的命令行工具。

# INSTALL

```apt: sudo apt install poppler-utils```

```dnf: sudo dnf install poppler-utils```

```apk: sudo apk add poppler-utils```

```nix: nix profile install nixpkgs#poppler-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdfattach](/man/pdfattach)(1), [pdfinfo](/man/pdfinfo)(1), [pdfimages](/man/pdfimages)(1)
