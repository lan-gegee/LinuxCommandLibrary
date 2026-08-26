# TAGLINE

将 Python 源码转换为带语法高亮的 HTML

# TLDR

**将 Python 转换为 HTML**

```pyhtmlizer [file.py]```

**输出到文件**

```pyhtmlizer [file.py] > [output.html]```

# SYNOPSIS

**pyhtmlizer** [_file_]

# PARAMETERS

_FILE_
> 要转换的 Python 文件。

# DESCRIPTION

**pyhtmlizer** 将 Python 源代码文件转换为带语法高亮的 HTML 文档。它作为 Twisted 框架实用工具集的一部分分发，使用 Twisted 内部的分词器解析 Python 语法并应用着色标记。

生成的 HTML 以彩色关键字、字符串、注释和标识符保留原始源码的结构。默认输出到 stdout，方便重定向到 HTML 文件以便嵌入文档或网页。

# CAVEATS

属于 Twisted。仅提供基础高亮。

# HISTORY

pyhtmlizer 是 **Twisted 框架**实用工具的一部分。

# INSTALL

```apk: sudo apk add py3-twisted```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pygmentize](/man/pygmentize)(1), [highlight](/man/highlight)(1)
