# TAGLINE

将 reStructuredText 转换为 HTML

# TLDR

**将 RST 转换为 HTML**

```rst2html [input.rst] [output.html]```

**转换并输出到 stdout**

```rst2html [input.rst]```

**指定样式表**

```rst2html --stylesheet=[style.css] [input.rst] [output.html]```

**生成独立文档**

```rst2html --embed-stylesheet [input.rst] [output.html]```

# SYNOPSIS

**rst2html** [_options_] [_source_] [_destination_]

# PARAMETERS

**--stylesheet** _file_
> CSS 样式表路径。

**--embed-stylesheet**
> 将 CSS 内嵌进 HTML。

**--template** _file_
> 文档模板。

**--no-doc-title**
> 不生成文档标题。

**--strict**
> 严格模式。

**--quiet**, **-q**
> 抑制警告输出。

# DESCRIPTION

**rst2html** 将 reStructuredText 文档转换为 HTML。它是 Docutils 的一部分，提供 RST 处理的参考实现。

# RST SYNTAX

```rst
Title
=====

Subtitle
--------

Paragraph text with **bold** and *italic*.

* List item 1
* List item 2

::

    Code block
```

# CAVEATS

属于 Docutils 软件包（python-docutils）的一部分。存在多个变体：rst2html、rst2html4、rst2html5。

# HISTORY

rst2html 是由 **David Goodger** 及众多贡献者开发的 **Docutils** 项目的组成部分，负责实现 reStructuredText 的处理。

# INSTALL

```apk: sudo apk add py3-docutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sphinx-build](/man/sphinx-build)(1), [pandoc](/man/pandoc)(1)
