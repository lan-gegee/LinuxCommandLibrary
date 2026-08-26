# TAGLINE

将 AsciiDoc 文档转换为多种输出格式

# TLDR

**转换**为 HTML

```asciidoctor [document.adoc]```

转换为 **PDF**

```asciidoctor-pdf [document.adoc]```

以**自定义输出**转换

```asciidoctor -o [output.html] [document.adoc]```

以指定**后端**转换

```asciidoctor -b [docbook] [document.adoc]```

启用**安全模式**

```asciidoctor -S [secure] [document.adoc]```

# SYNOPSIS

**asciidoctor** [_-b backend_] [_-o output_] [_-a attribute=value_] [_options_] _files_

# DESCRIPTION

**asciidoctor** 是一个快速的文本处理器，用于将 AsciiDoc 标记转换为 HTML、DocBook、man page 等格式。它是 AsciiDoc 标准的 Ruby 实现，支持扩展和定制。

AsciiDoc 是一种轻量级标记语言，适合编写文档、文章、书籍和技术内容。

# PARAMETERS

**-b** _backend_
> 输出后端（html5、docbook5、manpage）

**-o** _file_
> 输出文件

**-D** _dir_
> 输出目录

**-a** _attr=val_
> 设置文档属性

**-r** _lib_
> 加载库/扩展

**-S** _level_
> 安全模式（unsafe、safe、server、secure）

**-v**, **--verbose**
> 详细输出

**--trace**
> 出错时显示回溯信息

**-s**, **--no-header-footer**
> 不带 HTML 包装输出

**-e**, **--embedded**
> 输出可嵌入的文档（只含主体，无头部、页脚和样式）

**-n**, **--section-numbers**
> 为章节标题自动编号

# CAVEATS

PDF 输出需要 asciidoctor-pdf gem。部分功能需要额外的 gem。安全模式会限制某些特性。

# HISTORY

**Asciidoctor** 由 Dan Allen 和 Ryan Waldron 创建，于 **2012** 年首次发布，是比最初的 Python 版 AsciiDoc 实现更快的 Ruby 替代方案。

# INSTALL

```pacman: sudo pacman -S asciidoctor```

```apk: sudo apk add asciidoctor```

```brew: brew install asciidoctor```

```nix: nix profile install nixpkgs#asciidoctor```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[asciidoc](/man/asciidoc)(1), [pandoc](/man/pandoc)(1), [markdown](/man/markdown)(1)

# RESOURCES

```[Source code](https://github.com/asciidoctor/asciidoctor)```

```[Homepage](https://asciidoctor.org)```

```[Documentation](https://docs.asciidoctor.org)```

<!-- verified: 2026-06-16 -->
