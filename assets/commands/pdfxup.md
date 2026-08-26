# TAGLINE

将多个 PDF 页面排布到单张纸面上

# TLDR

创建 **2-up** PDF

```pdfxup -o [path/to/output.pdf] [path/to/input.pdf]```

创建带 **3 列 2 行**的 PDF

```pdfxup -x 3 -y 2 -o [path/to/output.pdf] [path/to/input.pdf]```

创建**小册子**（可折叠成书的格式）

```pdfxup -b -o [path/to/output.pdf] [path/to/input.pdf]```

# SYNOPSIS

**pdfxup** [**-o** _output_] [**-x** _cols_] [**-y** _rows_] [**-b**|**--booklet**] _input.pdf_

# PARAMETERS

**-o, --output _file_**
> 输出 PDF 文件路径

**-x, --columns _num_**
> 每页的列数

**-y, --rows _num_**
> 每页的行数

**-b, --booklet**
> 小册子模式，折叠后即成一书

**-p, --paper _size_**
> 输出纸张尺寸

**-l, --landscape**
> 横向方向

# DESCRIPTION

**pdfxup** 将多个 PDF 页面排布到单张纸面上（n-up 打印）。它会缩放并旋转页面以适应网格布局，适合制作讲义、小册子，或在打印时节省纸张。

小册子模式会对页面进行排布，使得双面打印并折叠之后能形成一本顺序正确的书。这适合用 PDF 文档制作小型出版物。

# CAVEATS

需要 LaTeX 和 pdfpages 软件包。包含表单或注释的复杂 PDF 可能无法正确渲染。输出质量取决于缩放因子。过小的 n-up 布局可能难以阅读。

# HISTORY

**pdfxup** 属于 **TeX Live** 发行版，内部使用 LaTeX 和 pdfpages 软件包。它为打印准备工作中常见的 PDF 页面拼版任务提供了便捷的命令行界面。

# INSTALL

```pacman: sudo pacman -S texlive-binextra```

```apk: sudo apk add texlive-binextra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdfjam](/man/pdfjam)(1), [pdfnup](/man/pdfnup)(1), [pdfbook](/man/pdfbook)(1)
