# TAGLINE

命令行 PDF 处理工具

# TLDR

**合并 PDF 文件**

```cpdf [input1.pdf] [input2.pdf] -o [output.pdf]```

**提取页面**

```cpdf [input.pdf] [1-10] -o [output.pdf]```

**旋转页面**

```cpdf -rotate [90] [input.pdf] -o [output.pdf]```

**添加密码保护**

```cpdf -encrypt [128bit] [owner_password] [user_password] [input.pdf] -o [output.pdf]```

**移除密码**

```cpdf -decrypt [input.pdf] owner=[password] -o [output.pdf]```

**拆分为单页**

```cpdf -split [input.pdf] -o [page%%%.pdf]```

**缩放页面**

```cpdf -scale-page "[2.0 2.0]" [input.pdf] -o [output.pdf]```

# SYNOPSIS

**cpdf** [_options_] _input.pdf_ [_pages_] **-o** _output.pdf_

# DESCRIPTION

**cpdf**（Coherent PDF）是一个处理 PDF 文件的命令行工具。它可以在无需图形界面的情况下对 PDF 文档进行合并、拆分、加密、解密、旋转、缩放等众多操作。

该工具支持页码范围、加密级别、元数据编辑和各种变换，可对 PDF 操作进行精确控制。它专为批处理、自动化以及不适合使用图形化 PDF 工具的场景而设计。

cpdf 对服务器端 PDF 处理、shell 脚本以及需要可靠、可脚本化 PDF 操作的工作流尤其有用。它还能完成添加水印、盖印页面、操作书签等复杂操作。

# PARAMETERS

**-o** _file_
> 输出文件路径。

**-encrypt** _level_ _owner_ _user_
> 以指定的加密位数和密码加密。

**-decrypt**
> 解密 PDF。

**-rotate** _degrees_
> 按角度旋转页面。

**-split**
> 拆分为单个页面。

**-scale-page** _"x y"_
> 按比例缩放页面。

**-merge**
> 合并多个 PDF。

# INSTALL

```dnf: sudo dnf install cpdf```

```apk: sudo apk add cpdf```

```brew: brew install cpdf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdftk](/man/pdftk)(1), [qpdf](/man/qpdf)(1), [gs](/man/gs)(1)

# RESOURCES

```[Source code](https://github.com/johnwhitington/cpdf-source)```

```[Homepage](https://www.coherentpdf.com/)```

```[Documentation](https://www.coherentpdf.com/cpdfmanual.pdf)```

<!-- verified: 2026-06-23 -->
