# TAGLINE

DocBook 编写与发布套件

# TLDR

**构建 HTML 文档**

```daps -d [DC-file] html```

**构建 PDF 文档**

```daps -d [DC-file] pdf```

**校验 DocBook XML** 源文件

```daps -d [DC-file] validate```

**构建单个 HTML** 页面

```daps -d [DC-file] html --single```

**构建 EPUB** 格式

```daps -d [DC-file] epub```

**显示文档状态**

```daps -d [DC-file] status```

# SYNOPSIS

**daps** [_global-options_] **-d** _DC-file_ _subcommand_ [_options_]

# PARAMETERS

**-d** _DC-FILE_
> 指定要处理文档的 Doc config 文件。

**-v**[_LEVEL_], **--verbosity**=_LEVEL_
> 设置详细程度（0-3）；单独的 -v 等于级别 1。

**--builddir** _DIR_
> 自定义构建目录。

**--force**
> 强制重新构建所有目标。

**html**
> 构建 HTML 输出（默认分块）。

**pdf**
> 构建 PDF 输出。

**epub**
> 构建 EPUB 输出。

**validate**
> 校验 XML 源文件。

**status**
> 显示文档状态和统计信息。

**--single**
> 生成单页 HTML。

**--help**
> 显示帮助信息。

# DESCRIPTION

**DAPS**（DocBook Authoring and Publishing Suite）是一套用于编写、翻译和发布 DocBook XML 文档的工具链。它提供统一接口，从单一源文件构建多种输出格式。

DAPS 将 DocBook 源文件转换为专业文档的复杂流程自动化。它负责 XSLT 转换、图像转换、通过 FOP 生成 PDF 以及打包分发。该套件借助 XInclude 支持模块化文档，并支持条件化 profile。

该工具面向需要在多种格式间保持一致的高质量输出、同时维护单一事实来源的技术作家和文档团队。

# CAVEATS

需要 DocBook 样式表及配套工具（xmllint、xsltproc、fop）。大文档的构建时间可能较长。生成 PDF 需要额外的 Java 依赖。某些特性专属于 SUSE 的文档工作流。

# HISTORY

DAPS 由 **SUSE** 为其文档团队开发，约在 **2012 年**开源。它从内部工具演化而来，用以满足企业级文档对翻译、版本管理和多种输出格式的复杂需求。

# INSTALL

```zypper: sudo zypper install daps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xmllint](/man/xmllint)(1), [xsltproc](/man/xsltproc)(1), [fop](/man/fop)(1), [asciidoctor](/man/asciidoctor)(1)

# RESOURCES

```[Source code](https://github.com/openSUSE/daps)```

```[Documentation](https://opensuse.github.io/daps/)```

<!-- verified: 2026-07-11 -->
