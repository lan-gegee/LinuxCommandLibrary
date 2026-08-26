# TAGLINE

用于查看和查询表格数据的轻量级 TUI

# TLDR

在查看器中**打开 CSV 文件**

```tw [data.csv]```

以自定义分隔符**打开**

```tw [data.csv] --separator '|'```

从 stdin **管道传入**数据

```curl -s "[https://example.com/data.csv]" | tw```

# SYNOPSIS

**tw** [_options_] _file_...

# DESCRIPTION

**tabiew** 是一个用于查看和查询表格数据文件的终端应用，支持 CSV、TSV、Parquet、JSON、JSONL、Arrow、SQLite、Excel 和 Logfmt 等格式。它具备 SQL 查询能力、Vim 风格导航、模糊搜索以及自动文件格式检测。

# HISTORY

**tabiew** 由 **shshemi** 创建，采用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S tabiew```

```brew: brew install tabiew```

```nix: nix profile install nixpkgs#tabiew```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[csvlens](/man/csvlens)(1), [xsv](/man/xsv)(1), [visidata](/man/visidata)(1)
