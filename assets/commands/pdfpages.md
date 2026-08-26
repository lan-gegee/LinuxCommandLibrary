# TAGLINE

用于引入外部 PDF 文档的 LaTeX 宏包

# TLDR

**在 LaTeX 中引入 PDF**

```\includepdf{[document.pdf]}```

**引入指定页面**

```\includepdf[pages={1,3,5}]{[document.pdf]}```

**每张纸多页**

```\includepdf[nup=2x2]{[document.pdf]}```

**引入所有页面**

```\includepdf[pages=-]{[document.pdf]}```

# SYNOPSIS

**\\usepackage**{pdfpages}

**\\includepdf**[_options_]{_filename_}

# PARAMETERS

**pages**
> 页面选择（-、1-5、{1,3,5}、last）。

**nup**
> 每张纸的页面布局（2x2、3x2）。

**landscape**
> 横向方向。

**frame**
> 在页面周围绘制边框。

**scale**
> 缩放系数。

**offset**
> 位置偏移。

# DESCRIPTION

**pdfpages** 是一个用于引入外部 PDF 文档的 LaTeX 宏包。它支持多页引入、n-up 打印和页面选择，是组合文档的必备工具。

# EXAMPLE

```latex
\documentclass{article}
\usepackage{pdfpages}

\begin{document}
% Include entire PDF
\includepdf[pages=-]{external.pdf}

% Include pages 1-3, scaled
\includepdf[pages={1-3},scale=0.8]{slides.pdf}

% 2x2 layout
\includepdf[nup=2x2,pages=-]{handout.pdf}
\end{document}
```

# CAVEATS

仅适用于 pdfLaTeX、XeLaTeX 或 LuaLaTeX。PDF 必须有效。大型 PDF 会增加编译时间。

# HISTORY

pdfpages 由 **Andreas Matthias** 为 LaTeX 项目创建，实现了无缝的 PDF 引入。

# SEE ALSO

[pdflatex](/man/pdflatex)(1), [pdfjam](/man/pdfjam)(1), [pdfbook](/man/pdfbook)(1)
