# TAGLINE

用于探索数据的终端电子表格多功能工具

# TLDR

**打开 CSV 文件**

```vd [data.csv]```

**浏览管道传入的 JSON 数据**

```curl [https://api.example.com/data] | vd```

**浏览 SQLite 数据库**

```vd [database.db]```

# SYNOPSIS

**vd** [_options_] _input_

# DESCRIPTION

**VisiData** 将电子表格的直观、终端的高效与 Python 的强大融为一体，是一个能处理数百万行数据的轻量级工具。它支持数十种格式，包括 CSV、JSON、Excel、SQLite、HDF5 等。功能包括排序、过滤、聚合、频率分析和交互式绘图。

# HISTORY

**VisiData** 由 **Saul Pwanson** 开发，使用 **Python** 编写。

# INSTALL

```dnf: sudo dnf install visidata```

```pacman: sudo pacman -S visidata```

```brew: brew install visidata```

```nix: nix profile install nixpkgs#visidata```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[csvkit](/man/csvkit)(1), [xsv](/man/xsv)(1), [miller](/man/miller)(1)
