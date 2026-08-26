# TAGLINE

用于可视化和检查 Parquet 文件的终端工具

# TLDR

**检查 Parquet 文件**

```parqeye [path/to/file.parquet]```

# SYNOPSIS

**parqeye** [_options_] _file_

# DESCRIPTION

**parqeye** 是一个基于终端的 Apache Parquet 文件检查工具。它提供支持键盘导航的交互式数据可视化、用于探索列类型和嵌套结构的模式视图、文件级元数据查看，以及行组统计信息。界面通过标签页在不同的视图之间切换。

# HISTORY

**parqeye** 由 **Kaushik Srini**（kaushiksrini）开发，使用 **Rust** 编写。

# INSTALL

```brew: brew install parqeye```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[parqv](/man/parqv)(1), [csvlens](/man/csvlens)(1)
