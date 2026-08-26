# TAGLINE

将 HTML 文件转换为 PDF 或 PostScript

# TLDR

**将 HTML 转换为 PDF**

```htmldoc --webpage -f [output.pdf] [input.html]```

**转换为 PostScript**

```htmldoc --webpage --format ps -f [output.ps] [input.html]```

**转换多个文件**

```htmldoc --book -f [output.pdf] [chapter1.html] [chapter2.html]```

**设置页面尺寸**

```htmldoc --webpage --size [letter] -f [output.pdf] [input.html]```

**添加页眉**

```htmldoc --webpage --header [.t.] -f [output.pdf] [input.html]```

# SYNOPSIS

**htmldoc** [_options_] _files_...

# PARAMETERS

**--webpage**
> 单页模式。

**--book**
> 多章节书籍模式。

**-f** _file_
> 输出文件名。

**--format** _format_
> 输出格式：pdf、ps、html。

**--size** _size_
> 页面尺寸：letter、a4、legal。

**--landscape**
> 横向排版。

**--header** _format_
> 页眉格式。

**--footer** _format_
> 页脚格式。

**--title**
> 包含标题页。

**--toc**
> 包含目录。

**--numbered**
> 为标题编号。

**--gray**
> 灰度输出。

# DESCRIPTION

**HTMLDOC** 将 HTML 文件转换为 PDF 或 PostScript。它可以处理单个页面，也可以将多个 HTML 文件合并成一本带目录和页眉/页脚的书。

该工具适合从 HTML 源生成可打印的文档。它处理基础的 HTML 和 CSS，生成排版良好的输出。

# HEADER/FOOTER FORMAT

```
.   - Blank
t   - Title
h   - Heading
c   - Chapter
d   - Date
T   - Time
D   - Date/time
/   - Page number
:   - Total pages
```

# CAVEATS

CSS 支持有限。复杂布局可能无法正确渲染。不执行 JavaScript。最适合简单、结构化的 HTML。

# HISTORY

HTMLDOC 由 **Michael Sweet** 创建，最初由 Easy Software Products 发布。它一直被用于文档生成，现在是一个开源项目。

# INSTALL

```apt: sudo apt install htmldoc```

```pacman: sudo pacman -S htmldoc```

```apk: sudo apk add htmldoc```

```zypper: sudo zypper install htmldoc```

```brew: brew install htmldoc```

```nix: nix profile install nixpkgs#htmldoc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wkhtmltopdf](/man/wkhtmltopdf)(1), [weasyprint](/man/weasyprint)(1), [pandoc](/man/pandoc)(1)

# RESOURCES

```[Source code](https://github.com/michaelrsweet/htmldoc)```

```[Homepage](https://www.msweet.org/htmldoc/)```

```[Documentation](https://www.msweet.org/htmldoc/htmldoc.html)```

<!-- verified: 2026-07-19 -->
