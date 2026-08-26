# TAGLINE

从 reStructuredText 生成文档

# TLDR

**构建 HTML 文档**

```sphinx-build -b html [source/] [build/html]```

**构建 PDF 文档**

```sphinx-build -b latex [source/] [build/latex]```

**清理后重新构建**

```sphinx-build -E -b html [source/] [build/html]```

**详细输出**

```sphinx-build -v -b html [source/] [build/html]```

**将警告视为错误构建**

```sphinx-build -W -b html [source/] [build/html]```

**检查链接**

```sphinx-build -b linkcheck [source/] [build/linkcheck]```

**设置配置选项**

```sphinx-build -D [key=value] -b html [source/] [build/]```

# SYNOPSIS

**sphinx-build** [_-b builder_] [_options_] _sourcedir_ _outputdir_

# PARAMETERS

**-b** _BUILDER_
> 输出格式构建器。

**-E**
> 重建所有文件。

**-a**
> 重建有改动的文件。

**-W**
> 将警告视为错误。

**-v**
> 详细输出。

**-D** _KEY=VALUE_
> 覆盖配置。

**-c** _PATH_
> 配置目录。

**-j** _N_
> 并行任务数。

# BUILDERS

**html** - HTML 页面
**latex** - LaTeX/PDF
**epub** - EPUB 电子书
**man** - Man 手册页
**linkcheck** - 检查链接

# DESCRIPTION

**sphinx-build** 是 Sphinx 的构建命令。Sphinx 是 Python 项目标准的文档生成器。它读取 reStructuredText 或 MyST Markdown 源文件，生成多种格式的输出，包括 HTML 网站、LaTeX/PDF 文档、ePub 电子书和 Unix man 手册页。

构建过程由源码目录中的 **conf.py** 配置文件控制，其中定义项目名称、主题、启用的扩展和输出设置。Sphinx 支持文档间的自动交叉引用、索引生成和代码语法高亮。**autodoc** 扩展可以直接从 Python docstring 中提取文档。

可通过 **-b** 标志选择多个构建器。增量构建默认只处理有改动的文件；**-E** 标志强制完整重建。配合 **-j** 并行构建可加快大型文档项目的速度。

# CONFIGURATION

**conf.py**
> 源码目录中的 Sphinx 配置文件，定义项目元数据、主题、扩展、模板路径和构建选项。

**SPHINXOPTS**
> 通过 Makefile 调用 sphinx-build 时传递附加选项的环境变量。

# CAVEATS

需要 Python。reStructuredText 有学习曲线。大型项目构建较慢。

# HISTORY

**Sphinx** 由 **Georg Brandl** 为 Python 文档创建。2008 年发布后成为 Python 项目文档的标准工具。

# INSTALL

```apk: sudo apk add py3-sphinx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[make](/man/make)(1), [rst2html](/man/rst2html)(1), [doxygen](/man/doxygen)(1)
