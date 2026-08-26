# TAGLINE

将 HTML 中的 LaTeX 公式转换为图片

# TLDR

**转换含 LaTeX 的 HTML**

```gladtex [input.htex]```

**指定输出文件**

```gladtex -o [output.html] [input.htex]```

**设置图片目录**

```gladtex -d [images/] [input.htex]```

**设置分辨率**

```gladtex -r [150] [input.htex]```

# SYNOPSIS

**gladtex** [_options_] _file_

# PARAMETERS

_FILE_
> 输入的 .htex 文件。

**-o** _FILE_
> 输出文件。

**-d** _DIR_
> 图片目录。

**-r** _DPI_
> 图片分辨率。

**-b** _COLOR_
> 背景颜色。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gladtex** 将 HTML 文档中嵌入的 LaTeX 公式转换为图片。它处理包含 LaTeX 数学标记的 `.htex` 文件，并生成带有已渲染公式图片的标准 HTML。

该工具通过 LaTeX 渲染公式并将其转换为可在任何浏览器中显示的图片，从而实现在网页中嵌入数学符号。

# CAVEATS

需要安装 LaTeX。输出的是图片而非 MathML。现代网站可考虑使用 MathJax。

# HISTORY

gladtex 的诞生是为了在浏览器广泛支持 MathML 和 JavaScript 数学渲染之前，让 HTML 能够显示数学公式。

# INSTALL

```nix: nix profile install nixpkgs#gladtex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[latex](/man/latex)(1), [pandoc](/man/pandoc)(1)
