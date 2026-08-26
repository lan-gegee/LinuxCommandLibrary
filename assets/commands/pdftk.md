# TAGLINE

操作 PDF 文档的命令行工具

# TLDR

**合并 PDF 文件**

```pdftk [file1.pdf] [file2.pdf] cat output [merged.pdf]```

**提取指定页面**

```pdftk [input.pdf] cat [1-5] [10] output [pages.pdf]```

**旋转页面**

```pdftk [input.pdf] cat [1-endeast] output [rotated.pdf]```

**将 PDF 拆分为单页**

```pdftk [input.pdf] burst output [page_%02d.pdf]```

**解密 PDF**

```pdftk [encrypted.pdf] input_pw [password] output [decrypted.pdf]```

**添加密码保护**

```pdftk [input.pdf] output [protected.pdf] owner_pw [pass] user_pw [pass]```

**填写 PDF 表单**

```pdftk [form.pdf] fill_form [data.fdf] output [filled.pdf]```

**获取 PDF 信息**

```pdftk [input.pdf] dump_data```

# SYNOPSIS

**pdftk** _input_ [_input_pw password_] [_operation_] [_output file_] [_encryption options_]

# PARAMETERS

**cat**
> 拼接页面（合并、提取、重排）。

**shuffle**
> 交错混合多个文件的页面。

**burst**
> 拆分为单页 PDF。

**rotate**
> 旋转页面。

**fill_form**
> 用 FDF/XFDF 填写表单字段。

**dump_data**
> 报告 PDF 元数据。

**dump_data_fields**
> 报告表单字段信息。

**update_info**
> 更新 PDF 元数据。

**attach_files**
> 将文件附加到 PDF。

**unpack_files**
> 提取附件。

**background**
> 将 PDF 作为背景应用。

**stamp**
> 将 PDF 作为前景印章应用。

**output**
> 指定输出文件。

**input_pw** _PASS_
> 输入文件密码。

**owner_pw** _PASS_
> 设置所有者密码（完整权限）。

**user_pw** _PASS_
> 设置用户密码（受限权限）。

**allow** _PERMS_
> 设置允许的权限。

**encrypt_40bit**
> 使用 40 位加密。

**encrypt_128bit**
> 使用 128 位加密。

**flatten**
> 压平表单字段。

**compress**
> 压缩输出。

**uncompress**
> 解压输出。

# DESCRIPTION

**pdftk**（PDF Toolkit）是一个操作 PDF 文档的命令行工具。它可以无损地合并、拆分、旋转、加密、解密、填写表单以及修改元数据。

页面选择使用灵活的语法：范围（1-5）、指定页面（3,7,10）、逆序（end-1），以及旋转后缀（north、south、east、west）。多个输入文件可以各自配合页面选择进行组合。

表单处理可从 FDF（Forms Data Format）或 XFDF 数据文件填写交互式 PDF 表单。dump_data_fields 命令可提取字段信息以便准备填充数据。Flatten 会将表单数据永久合入文档。

加密选项通过权限控制设置所有者密码和用户密码。所有者密码授予完全访问权；用户密码可限制权限（禁止打印、禁止复制等）。

stamp 和 background 操作可将 PDF 叠加，适用于水印、信头或内容组合。附件功能可在 PDF 内嵌入文件。

# CAVEATS

某些复杂的 PDF 可能无法正确处理。Java 版本（pdftk-java）与原始 C++ 版本存在差异。加密强度并不总是很高。大文件处理可能较慢。表单填写对 Acrobat 创建的表单效果最佳。部分特性在较新的 PDF 标准中已弃用。

# HISTORY

**pdftk** 由 **Sid Steward** 于 **2003** 年基于 iText 库编写。它曾是 Linux 上标准的命令行 PDF 工具。在原版本停止维护后，**pdftk-java** 作为 Java 移植版出现，在保持兼容性的同时延续了开发。

# INSTALL

```pacman: sudo pacman -S pdftk```

```zypper: sudo zypper install pdftk```

```nix: nix profile install nixpkgs#pdftk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qpdf](/man/qpdf)(1), [poppler-utils](/man/poppler-utils)(1), [ghostscript](/man/ghostscript)(1), [pdfunite](/man/pdfunite)(1)
