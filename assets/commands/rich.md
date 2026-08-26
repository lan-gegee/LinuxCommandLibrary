# TAGLINE

在终端中渲染富文本和 Markdown

# TLDR

**查看 markdown 文件**

```python -m rich.markdown [file.md]```

**对代码进行语法高亮**

```python -m rich.syntax [file.py]```

**美化输出 JSON**

```python -m rich.json [file.json]```

**显示可用的加载动画**

```python -m rich.spinner```

**显示调色板**

```python -m rich.color```

**显示 emoji 代码**

```python -m rich.emoji```

**演示所有功能**

```python -m rich```

# SYNOPSIS

**python -m rich** [_module_] [_options_] [_file_]

# MODULES

**rich.markdown** _FILE_
> 渲染 markdown 文件。

**rich.syntax** _FILE_
> 对源代码文件进行语法高亮。

**rich.json** _FILE_
> 美化输出 JSON 文件。

**rich.color**
> 显示终端调色板。

**rich.spinner**
> 显示可用的加载动画。

**rich.emoji**
> 列出 emoji 代码。

**rich.tree**
> 演示树形结构的渲染效果。

# DESCRIPTION

**rich** 是一个用于终端格式化的 Python 库，其 CLI 提供了对这些功能的快速访问。

Markdown 渲染可以展示格式化的文档，标题、列表和代码块都能漂亮地呈现。

语法高亮会为源代码着色，自动支持多种语言。

JSON 美化输出会对数据进行格式化，并用颜色突出结构。

颜色展示用于查看终端的能力，帮助你确认终端支持哪些特性。

# CAVEATS

需要安装 `rich` Python 软件包（`pip install rich`）。终端必须支持 ANSI 颜色。部分功能需要真彩色支持。另有独立的 CLI 工具 `rich-cli`，可通过 `pip install rich-cli` 安装。

# HISTORY

**Rich** 由 **Will McGugan** 于 **2019 年**创建，用于在 Python 中实现漂亮的终端输出。其 CLI 模块提供了各种快捷实用工具。

# INSTALL

```brew: brew install rich```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bat](/man/bat)(1), [glow](/man/glow)(1), [jq](/man/jq)(1), [pygmentize](/man/pygmentize)(1)
