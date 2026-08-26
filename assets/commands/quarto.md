# TAGLINE

科学与技术出版系统

# TLDR

**将文档渲染为输出格式**

```quarto render [document.qmd]```

**渲染整个项目**

```quarto render```

**实时预览文档**

```quarto preview [document.qmd]```

**创建新项目**

```quarto create project [website]```

**发布到 Quarto Pub**

```quarto publish quarto-pub```

**将 Jupyter notebook 转换为 Quarto**

```quarto convert [notebook.ipynb]```

**安装扩展**

```quarto add [quarto-ext/fontawesome]```

**检查安装**

```quarto check```

# SYNOPSIS

**quarto** _command_ [_options_] [_arguments_]

# PARAMETERS

**render** [_input_]
> 渲染文档或项目。

**preview** [_input_]
> 支持自动重载的实时预览。

**create** _type_ [_name_]
> 创建项目或扩展。

**publish** _provider_
> 发布到托管服务。

**add** _extension_
> 安装扩展。

**remove** _extension_
> 移除扩展。

**update** _extension_
> 更新扩展。

**convert** _file_
> 在格式之间转换。

**check** [_component_]
> 校验安装。

**install** _tool_
> 安装可选工具。

**--to** _FORMAT_
> 输出格式（html、pdf、docx 等）。

**--output** _FILE_
> 输出文件名。

**--execute**
> 执行代码单元。

**--no-execute**
> 跳过代码执行。

**--cache**
> 缓存代码执行结果。

**--port** _NUM_
> 预览服务器端口。

**--browser**
> 在浏览器中打开。

# DESCRIPTION

**Quarto** 是一款面向技术和科学文档的开源出版系统。它在 Pandoc 的基础上扩展，支持 Python、R、Julia 和 Observable JS 的可执行代码单元。

文档使用 .qmd（Quarto Markdown）格式，将叙述性文字与代码单元结合。代码在渲染时执行，其输出（图表、表格、结果）会嵌入最终文档中。

输出格式包括 HTML、PDF、Word、演示文稿（RevealJS、Beamer）、网站和书籍。项目可将多个文档组织在一起并共享配置。

preview 命令提供实时开发体验，文件更改时自动重新渲染。热模块替换无需整页刷新即可更新浏览器内容。

扩展可添加功能：自定义格式、短代码、过滤器和主题。扩展生态提供了期刊、演示文稿和专业输出的模板。

发布功能与 Quarto Pub、GitHub Pages、Netlify、Posit Connect 等平台集成。一条命令即可部署并更新托管内容。

# CAVEATS

代码执行需要 Jupyter 或 knitr。计算量大的大文档会拖慢渲染速度。PDF 输出需要安装 LaTeX。部分扩展可能随 Quarto 更新而失效。预览服务器可能占用较多资源。

# HISTORY

**Quarto** 由 **Posit**（前身为 RStudio）于 **2022 年**发布，是 R Markdown 的新一代版本。它被设计为与语言无关，对 Python 和 Julia 的支持不亚于 R。"quarto" 这个名字指的是一种书籍开本，延续了 R Markdown 的印刷/出版主题。

# INSTALL

```nix: nix profile install nixpkgs#quarto```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pandoc](/man/pandoc)(1), [jupyter](/man/jupyter)(1), [rmarkdown](/man/rmarkdown)(1), [marp](/man/marp)(1)
