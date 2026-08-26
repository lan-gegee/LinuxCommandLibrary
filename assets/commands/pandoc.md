# TAGLINE

转换文档格式

# TLDR

**将 Markdown 转换为 HTML**

```pandoc [input.md] -o [output.html]```

**转换为 PDF**

```pandoc [input.md] -o [output.pdf]```

**转换为 Word**

```pandoc [input.md] -o [output.docx]```

**指定输入格式**

```pandoc -f [latex] -t [html] [input.tex] -o [output.html]```

**附带目录**

```pandoc [input.md] --toc -o [output.html]```

**使用模板**

```pandoc [input.md] --template=[template.html] -o [output.html]```

# SYNOPSIS

**pandoc** [_options_] [_input_...]

# PARAMETERS

_INPUT_
> 输入文件（可多个）。

**-o** _FILE_
> 输出文件。

**-f** _FORMAT_
> 输入格式。

**-t** _FORMAT_
> 输出格式。

**--toc**
> 包含目录。

**--template** _FILE_
> 使用模板。

**--help**
> 显示帮助信息。

# DESCRIPTION

**pandoc** 转换文档格式。通用的文档转换器。

该工具支持多种格式：Markdown、LaTeX、HTML、DOCX、PDF 等。

# CAVEATS

PDF 输出需要 LaTeX 或 wkhtmltopdf。对不同格式的支持程度不一。

# HISTORY

Pandoc 由 **John MacFarlane** 开发，定位为通用文档转换器。

# INSTALL

```apt: sudo apt install pandoc```

```dnf: sudo dnf install pandoc-cli```

```pacman: sudo pacman -S pandoc-cli```

```apk: sudo apk add pandoc-cli```

```zypper: sudo zypper install pandoc-cli```

```brew: brew install pandoc```

```nix: nix profile install nixpkgs#pandoc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[markdown](/man/markdown)(1), [latex](/man/latex)(1), [groff](/man/groff)(1)
