# TAGLINE

在终端中查看 Apache Parquet 文件

# TLDR

**查看 Parquet 文件**

```pqviewer [path/to/file.parquet]```

# SYNOPSIS

**pqviewer** [_options_] _file_

# DESCRIPTION

**pqviewer** 是一个 TUI 工具，用于读取 Apache Parquet 文件并以可导航的表格形式展示其内容。它支持方向键导航、上下翻页滚动、主题切换以及基于 Tab 的焦点管理。基于 Textual、Rich 和 PyArrow 构建。

# HISTORY

**pqviewer** 由 **thread53** 创建，使用 **Python** 编写。

# SEE ALSO

[parqeye](/man/parqeye)(1), [parqv](/man/parqv)(1), [csvlens](/man/csvlens)(1)
