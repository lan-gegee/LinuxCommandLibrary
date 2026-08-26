# TAGLINE

将 AsciiDoc 标记转换为 HTML 和 DocBook

# TLDR

**将 AsciiDoc 文件转换**为 HTML

```asciidoc [document.txt]```

**转换为 HTML5** 格式

```asciidoc -b html5 [document.txt]```

**转换为 DocBook** 格式

```asciidoc -b docbook [document.txt]```

**生成 man page**

```asciidoc -b html5 -d manpage [command.1.txt]```

**设置文档属性**（目录、图标）

```asciidoc -a toc -a icons [document.txt]```

**指定输出文件**

```asciidoc -o [output.html] [document.txt]```

**启用章节编号**

```asciidoc --section-numbers [document.txt]```

# SYNOPSIS

**asciidoc** [_options_] _FILE_

# PARAMETERS

**-b** _backend_, **--backend=**_backend_
> 输出格式：html、html5、xhtml11、html4、docbook、docbook45、docbook5、slidy、wordpress、latex

**-d** _doctype_, **--doctype=**_doctype_
> 文档类型：article（默认）、book、manpage

**-o** _file_, **--out-file=**_file_
> 将输出写入文件（默认：输入文件名换用新扩展名）

**-a** _name=value_, **--attribute=**_name=value_
> 设置一个文档属性

**-f** _file_, **--conf-file=**_file_
> 使用额外的配置文件

**-e**, **--no-conf**
> 不加载隐式加载的配置文件

**-n**, **--section-numbers**
> 为章节标题自动编号

**-s**, **--no-header-footer**
> 只输出文档主体（不含 HTML head/body 标签）

**--safe**
> 启用安全模式（禁用有潜在危险的功能）

**-v**, **--verbose**
> 向 stderr 打印处理信息

**--help** _topic_
> 打印帮助（主题：syntax、manpage）

**--version**
> 打印版本号

# DESCRIPTION

**asciidoc** 将以 AsciiDoc 标记编写的纯文本文档转换为 HTML、DocBook 等格式。AsciiDoc 是一种轻量级标记语言，适合编写文档、文章、书籍和 man page。

默认后端为 HTML（xhtml11）。DocBook 输出可进一步使用 **dblatex**（生成 PDF）或 **xmlto**（生成各种格式）等工具处理。该工具从 **/etc/asciidoc/** 和 **~/.asciidoc/** 读取配置。

文档属性控制输出特性，例如目录（**-a toc**）、内嵌图片（**-a data-uri**）、图标（**-a icons**）和最大宽度（**-a max-width=55em**）。属性也可以在文档内部设置。

如果 FILE 为 **-**，则从标准输入读取内容，从而支持管道处理。

# CONFIGURATION

**/etc/asciidoc/**
> 系统级配置文件、过滤器以及后端模板。

**~/.asciidoc/**
> 用户专属配置文件和自定义后端。

# CAVEATS

最初的 Python 版 **asciidoc** 已被视为遗留软件。**Asciidoctor**（Ruby 编写）是积极维护的实现，功能更多、处理更快。某些高级特性在两种实现之间存在差异。

# HISTORY

AsciiDoc 由 **Stuart Rackham** 于 **2002** 年创建，作为比 DocBook XML 更易读的替代方案。这种格式在设计上既便于人类阅读，又能生成专业级的文档。现代化的重实现 **Asciidoctor** 由 **Dan Allen** 于 **2012** 年启动，如今已是主要的实现，被 GitHub、GitLab 和 Eclipse 基金会等项目采用。

# INSTALL

```dnf: sudo dnf install asciidoc```

```pacman: sudo pacman -S asciidoc```

```apk: sudo apk add asciidoc```

```zypper: sudo zypper install asciidoc```

```brew: brew install asciidoc```

```nix: nix profile install nixpkgs#asciidoc```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[asciidoctor](/man/asciidoctor)(1), [pandoc](/man/pandoc)(1), [markdown](/man/markdown)(1), [rst2html](/man/rst2html)(1)

# RESOURCES

```[Source code](https://github.com/asciidoc-py/asciidoc-py)```

```[Homepage](https://asciidoc.org)```

```[Documentation](https://asciidoc-py.github.io)```

<!-- verified: 2026-06-16 -->
