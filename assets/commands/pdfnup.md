# TAGLINE

将多个 PDF 页面排到单张纸上

# TLDR

**每张纸放 2 页**

```pdfnup [input.pdf]```

**每张纸放 4 页**

```pdfnup --nup 2x2 [input.pdf]```

**指定输出文件**

```pdfnup -o [output.pdf] [input.pdf]```

**横向方向**

```pdfnup --landscape [input.pdf]```

# SYNOPSIS

**pdfnup** [_options_] _file_...

# PARAMETERS

**--nup** _cols_x_rows_
> 每张纸的页面布局。

**-o** _file_
> 输出文件名。

**--landscape**
> 横向方向。

**--paper** _size_
> 纸张大小。

**--frame** _true_|_false_
> 在页面周围绘制边框。

**--delta** _x_ _y_
> 页面之间的间距。

# DESCRIPTION

**pdfnup** 将多个 PDF 页面排到单张纸上（n-up 打印）。适用于讲义、省纸或制作审阅版。

属于使用 pdfpages LaTeX 宏包的 pdfjam 套件。
# 2 pages per sheet (default)
pdfnup document.pdf

# 4-up on A4
pdfnup --nup 2x2 --paper a4paper slides.pdf

# 6-up with frames
pdfnup --nup 3x2 --frame true handout.pdf
```

# CAVEATS

需要带 pdfpages 的 LaTeX。输出文件默认为 input-nup.pdf。复杂的布局可能需要手动调整。

# HISTORY

pdfnup 是 **David Firth** 的 **pdfjam** 的一部分，通过 **pdfpages** LaTeX 宏包提供 n-up 功能。

# SEE ALSO

[pdfjam](/man/pdfjam)(1), [pdfbook](/man/pdfbook)(1)
