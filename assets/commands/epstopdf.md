# TAGLINE

封装 PostScript（EPS）转 PDF 转换器

# TLDR

**将 EPS 转换为 PDF**

```epstopdf [image.eps]```

**指定输出文件**

```epstopdf --outfile=[output.pdf] [image.eps]```

**附带 Ghostscript 选项转换**

```epstopdf --gsopt=[-dPDFSETTINGS=/prepress] [image.eps]```

**受限模式**（更安全）

```epstopdf --restricted [image.eps]```

**嵌入字体**

```epstopdf --embed [image.eps]```

**从标准输入读取 EPS，将 PDF 写到标准输出**

```cat [image.eps] | epstopdf --filter > [out.pdf]```

**使用 HiResBoundingBox**

```epstopdf --hires [image.eps]```

# SYNOPSIS

**epstopdf** [_options_] _file.eps_

# DESCRIPTION

**epstopdf** 将 Encapsulated PostScript（EPS）文件转换为 PDF 格式。它借助 Ghostscript 完成转换，常用于 TeX/LaTeX 工作流。

该工具处理包围盒计算和字体嵌入，生成适合插入文档的 PDF 输出。

# PARAMETERS

**-o**, **--outfile=** _file_
> 输出 PDF 文件名。

**--filter**
> 从标准输入读取 EPS，并将 PDF 写到标准输出。

**--restricted**
> 受限模式（不允许 shell 逃逸或不安全选项）。

**--gsopt=** _option_
> 向 Ghostscript 传递单个选项（可重复）。

**--gsopts=** _options_
> 向 Ghostscript 传递多个以空格分隔的选项。

**--gscmd=** _command_
> 要使用的 Ghostscript 命令。

**--gs**, **--nogs**
> 运行 Ghostscript（默认），或改为输出中间 PostScript。

**--hires**
> 扫描并使用 HiResBoundingBox。

**--exact**
> 扫描并使用 ExactBoundingBox。

**--embed**, **--noembed**
> 控制字体嵌入。

**--compress**, **--nocompress**
> 开关输出压缩。

**--gray**, **--nogray**
> 将输出转换为灰度。

**--autorotate=** _MODE_
> 设置页面旋转行为（None、All 或 PageByPage）。

**--pdfsettings=** _LEVEL_
> Ghostscript PDF 质量预设（如 screen、ebook、printer、prepress）。

**--res=** _DPI_
> 设置光栅图像分辨率。

**--safer**, **--nosafer**
> 开关 Ghostscript 安全限制。

**--quiet**, **--noquiet**
> 抑制或显示输出消息。

**--debug**
> 启用调试输出。

**--version**
> 显示版本信息。

**--help**
> 显示帮助。

# CAVEATS

需要安装 Ghostscript。源 EPS 中的包围盒必须有效。某些 PostScript 特性可能无法正确转换。输出质量取决于源文件。

# HISTORY

**epstopdf** 是 **TeX Live** 发行版的一部分，对于需要在 PDF 文档中插入 EPS 图形的 LaTeX 用户不可或缺。多年来它由多位 TeX 开发者维护，**Karl Berry** 等人为其开发做出了贡献。

# INSTALL

```apk: sudo apk add texlive-dvi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gs](/man/gs)(1), [ps2pdf](/man/ps2pdf)(1), [pdflatex](/man/pdflatex)(1), [convert](/man/convert)(1)
