# TAGLINE

带样式的终端 Markdown 查看器

# TLDR

使用默认主题**查看 Markdown 文件**

```mdv [path/to/file.md]```

从标准输入**管道输入 Markdown**

```echo "# Hello" | mdv -```

**监视文件**并在变化时重新显示

```mdv -m [path/to/file.md]```

使用指定主题**渲染**（例如 729.8953 为较暗样式）

```mdv -t [729.8953] [path/to/file.md]```

**预览所有可用主题**

```mdv -t all [path/to/file.md]```

不使用 ANSI 颜色**渲染**（纯文本）

```mdv -A [path/to/file.md]```

将列宽固定为 80

```mdv -c [80] [path/to/file.md]```

以 HTML 而非 ANSI **渲染**

```mdv -H [path/to/file.md]```

# SYNOPSIS

**mdv** [_options_] _MDFILE_

# PARAMETERS

**-A**
> 去除所有 ANSI 转义码；适用于管道输出到不支持颜色的文件或分页工具。

**-C** _mode_
> 源代码高亮模式（_all_、_code_、_doc_、_mod_）。

**-H**
> 将渲染后的文档输出为 HTML。

**-L**
> **-u i** 的快捷方式（行内链接样式）。

**-M** _dir_
> 监视 _dir_ 目录中 Markdown 文件的变化。

**-T** _theme_
> 代码块的颜色主题（接受 _random_ 或 _all_）。

**-X** _lexer_
> 默认 Pygments 词法分析器名称（默认：_python_）。

**-b** _n_
> 制表符长度（默认：_4_）。

**-c** _cols_
> 将列宽固定为 _cols_ 个字符。

**-f** _from_
> 从子串 _from_ 处开始渲染；支持 _HEADING:N_ 以限制为标题后 _N_ 行。

**-h**
> 显示帮助。

**-i**
> 在渲染的同时显示所选主题的元数据。

**-l**
> 实验性的浅色背景模式。

**-m**
> 监视输入文件并在其变化时重新显示。

**-n** _NRS_
> 启用标题编号（例如 _-3_、_1-_、_1-5_）。

**-t** _theme_
> Markdown 颜色主题。接受数字 ID（例如 _729.8953_）、_random_ 或 _all_。

**-u** _style_
> 链接渲染样式：_it_（行内表格）、_h_（隐藏）、_i_（行内）。

**-x**
> 禁用对代码块的自动词法分析器猜测。

# CONFIGURATION

默认值从 **~/.mdv**（YAML）读取作为 CLI 参数；若存在 **~/.mdv.py**（Python），则会执行它以进行动态覆盖。

环境变量：

**MDV_THEME**
> 默认 Markdown 主题 ID。

**MDV_CODE_THEME**
> 代码块的默认 Pygments 主题。

# DESCRIPTION

**mdv** 是一个 Python 工具，可在 256 色终端中直接渲染 Markdown 文档。它解析标题、列表、表格、引用块和围栏代码块，并输出带样式的 ANSI 文本，语法高亮由 Pygments 驱动。它内置了大量颜色主题，可用 **-t all** 预览。

除一次性渲染外，**mdv** 还可以用 **-m**/**-M** 监视文件或目录，并在源文件变化时刷新视图，这在使用另一个窗口编辑 Markdown 时非常有用。作为 Python 库调用时，同样的渲染功能可通过 **mdv.main()** 使用，因此可以嵌入其他程序中（例如用于美化 CLI 帮助文本的输出）。

# CAVEATS

需要 **256 色终端**，且大多数主题假定**深色背景**——浅色背景请使用 **-l**。渲染使用 unicode 制表字符，建议使用支持这些字符的字体。该项目以 Python 编写；在较新的发行版上可通过 **pip install mdv** 或 **brew install mdv** 安装。

# HISTORY

由 **axiros** 编写，最初于 **2015 年**发布，名为 _terminal_markdown_viewer_。该项目以 BSD 许可证发布并持续获得零星更新；版本 _1.7.5_ 发布于 **2023 年 9 月**。同一作者后来还创建了一个更轻量的姊妹项目 **mdvl**，面向极简环境。

# INSTALL

```brew: brew install mdv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[glow](/man/glow)(1), [bat](/man/bat)(1), [pygmentize](/man/pygmentize)(1), [pandoc](/man/pandoc)(1)
