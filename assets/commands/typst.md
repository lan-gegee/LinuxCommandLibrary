# TAGLINE

现代排版系统与编译器

# TLDR

**编译文档为 PDF**

```typst compile [document.typ]```

**以指定输出编译**

```typst compile [document.typ] [output.pdf]```

**监视并在更改时重新编译**

```typst watch [document.typ]```

**编译为 PNG**

```typst compile [document.typ] [output.png]```

**编译为 SVG**

```typst compile [document.typ] [output.svg]```

**列出可用字体**

```typst fonts```

**以自定义字体路径编译**

```typst compile --font-path [/path/to/fonts] [document.typ]```

**初始化新项目**

```typst init```

# SYNOPSIS

**typst** _command_ [_--font-path path_] [_options_] _input_ [_output_]

# PARAMETERS

**compile** _INPUT_ [_OUTPUT_]
> 将文档编译为输出文件。

**watch** _INPUT_
> 监视更改并重新编译。

**fonts**
> 列出可用字体。

**init** [_TEMPLATE_]
> 初始化新项目。

**query** _INPUT_ _SELECTOR_
> 查询文档元数据。

**--root** _DIR_
> 项目根目录。

**--font-path** _PATH_
> 额外的字体搜索路径。

**-f**, **--format** _FORMAT_
> 强制指定输出格式（pdf、png、svg）。通常会根据输出扩展名推断。

**--ppi** _NUM_
> 光栅输出的每英寸像素数（默认 144）。

**--pages** _RANGE_
> 要导出的页面列表，逗号分隔（例如 1-3,5）。

**--diagnostic-format** _FMT_
> 诊断信息格式：human、short。

**--input** _KEY=VALUE_
> 设置输入变量。

**--open**
> 编译后打开输出文件。

**-h**, **--help**
> 显示帮助。

**-V**, **--version**
> 显示版本。

# DESCRIPTION

**Typst** 是一个现代排版系统，设计目标是对标 LaTeX。它兼具 LaTeX 的强大能力与更简单的语法、更快的编译速度。

文档使用 .typ 文件，其标记语法类似 Markdown。标题、列表、强调和链接都采用熟悉的语法。数学公式使用受 LaTeX 启发但更简洁的记法。

编译是增量式的且极其快速——文档可在毫秒内完成编译。监视模式在编辑期间提供近乎即时的预览更新。

样式采用函数式方法。set 规则配置默认值；show 规则变换元素。这门语言是图灵完备的，可以通过脚本编写复杂文档。

模板和软件包可扩展功能。参考文献支持 BibTeX 或 Hayagriva 格式。多栏布局、插图和表格的使用都很直观。

输出格式包括 PDF（默认）、PNG 页面和 SVG。字体嵌入确保文档在任何地方都能正确渲染。

# CAVEATS

生态较新，软件包比 LaTeX 少。部分高级特性仍在开发中。并非所有 LaTeX 软件包都有对应物。尚不支持用于存档的 PDF/A。与 LaTeX 相比 IDE 集成有限。

# HISTORY

**Typst** 由 **Martin Haug** 和 **Laurenz Mädje** 于 **2019 年**前后作为硕士论文项目创建。目标是打造一个与 LaTeX 同样强大但更平易近人的排版系统。在 Typst GmbH 开发一段时间后，它于 **2023 年**开源并迅速获得广泛采用。

# INSTALL

```pacman: sudo pacman -S typst```

```apk: sudo apk add typst```

```zypper: sudo zypper install typst```

```brew: brew install typst```

```nix: nix profile install nixpkgs#typst```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdflatex](/man/pdflatex)(1), [pandoc](/man/pandoc)(1), [groff](/man/groff)(1), [asciidoctor](/man/asciidoctor)(1)
