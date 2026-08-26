# TAGLINE

将 Markdown 文档转换为 PDF

# TLDR

**将 Markdown 文件转换为 PDF**

```markdown2pdf -p [input.md] -o [output.pdf]```

**直接转换 Markdown 字符串**

```markdown2pdf -s "# Hello" -o [output.pdf]```

**应用内置主题**

```markdown2pdf -p [input.md] --theme [github] -o [output.pdf]```

**添加页码**

```markdown2pdf -p [input.md] --page-numbers -o [output.pdf]```

**从 URL 获取并转换 Markdown**

```markdown2pdf -u [https://example.com/readme.md] -o [output.pdf]```

**预览最终配置而不实际渲染**

```markdown2pdf -p [input.md] --dry-run```

# SYNOPSIS

**markdown2pdf** (**-p** _file_ | **-s** _string_ | **-u** _url_) [**-o** _output_] [_options_]

# PARAMETERS

**-p** _file_
> 从给定文件读取 Markdown。

**-s** _string_
> 从给定字符串读取 Markdown。

**-u**, **--url** _url_
> 从 URL 获取 Markdown（需要 fetch 特性）。

**-o** _file_
> 输出 PDF 路径（默认：./output.pdf）。

**--theme** _name_
> 使用内置主题，如 github 或 academic。

**--page-numbers**
> 在输出中添加页码。

**-c** _file_
> 从 TOML 配置文件加载设置。

**-V** _key=value_
> 覆盖单个配置值。

**--dry-run**
> 显示将要渲染的内容而不写出 PDF。

**--print-effective-config**
> 打印合并后的配置并退出。

**--verbose**
> 启用详细输出。

**--quiet**
> 抑制错误以外的输出。

# DESCRIPTION

**markdown2pdf** 将 Markdown 文档转换为 PDF。最知名的实现是一个纯 Rust 转译器，它通过 printpdf 直接渲染为 PDF，不经过中间的 HTML 步骤，也不依赖 Pandoc 或 wkhtmltopdf 等外部程序。

输入通过 **-p**（文件）、**-s**（字符串）或 **-u**（URL）标志之一提供，而不是作为裸位置参数。样式由内置主题（**--theme**）和 TOML 配置文件（**-c**）控制，个别值可通过 **-V** 覆盖。

# CAVEATS

有多个互不相关的工具共用 **markdown2pdf** 这个名字（Rust、Node.js 和 Python 版本），它们的标志各不相同。本页面记录的是 Rust 实现。与基于 HTML 的转换器不同，它不接受任意 CSS；外观由主题和配置驱动。

# HISTORY

Rust 版 **markdown2pdf** crate 由 **theiskaa** 创建，发布在 crates.io 上。可通过 `cargo install markdown2pdf` 或 Homebrew tap 安装。

# INSTALL

```aur: yay -S markdown2pdf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pandoc](/man/pandoc)(1), [wkhtmltopdf](/man/wkhtmltopdf)(1)
