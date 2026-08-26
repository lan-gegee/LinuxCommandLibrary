# TAGLINE

将 PDF 文件的页面排成 2 合 1 印张以便小册子打印

# TLDR

**从 PDF 文件创建小册子**

```pdfbook [input.pdf]```

**指定输出文件**

```pdfbook -o [booklet.pdf] [input.pdf]```

**创建 A4 纸的小册子**

```pdfbook --paper a4paper [input.pdf]```

**创建 16 页一帖的小册子**

```pdfbook --signature [16] [input.pdf]```

**创建短边翻页双面打印的小册子**

```pdfbook --short-edge [input.pdf]```

# SYNOPSIS

**pdfbook** [**--short-edge**] [_options_] _file_...

# PARAMETERS

**-o** _file_
> 输出文件名。默认为输入文件名加 "-book" 后缀。

**--paper** _size_
> 纸张大小（例如 a4paper、letterpaper、legalpaper）。

**--signature** _num_
> 每帖的页数（必须是 4 的倍数，默认 4）。

**--signature*** _num_
> 右边装订时每帖的页数。

**--short-edge**
> 为短边翻页双面打印排版。必须是第一个参数。需要 LaTeX 包 everyshi。

**--booklet** _bool_
> 启用或禁用小册子重排（默认 true）。

# DESCRIPTION

**pdfbook** 是 **pdfjam** 的简单封装，将 PDF 页面排成适合小册子打印的 2 合 1 印张。页面会被重新排序，使双面打印并折叠后能形成顺序正确的小册子。

默认输出适用于长边装订。短边装订请使用 **--short-edge**。上面未列出的所有选项都会透传给 **pdfjam**。

# CAVEATS

需要安装带 **pdfpages** 包的 LaTeX。页数为 4 的倍数时效果最佳。输出文件默认为输入文件名加 "-book" 后缀。**--short-edge** 选项需要 **everyshi** LaTeX 包。

# HISTORY

pdfbook 属于 **pdfjam**——由 **David Firth** 创建的一组使用 **pdfpages** LaTeX 包的 shell 脚本。它已在很大程度上被提供边距控制等额外特性的 **pdfbook2** 取代。

# SEE ALSO

[pdfjam](/man/pdfjam)(1), [pdfnup](/man/pdfnup)(1), [pdflatex](/man/pdflatex)(1), [pdfbook2](/man/pdfbook2)(1)
