# TAGLINE

带交互式 TUI 的快速终端 Excel 查看器

# TLDR

**在交互式 TUI 中打开 Excel 文件**

```xleak [report.xlsx]```

**按名称打开指定工作表**

```xleak [report.xlsx] --sheet "[Q3 Results]"```

**将电子表格导出为 CSV**

```xleak [data.xlsx] --export csv > [output.csv]```

**将电子表格导出为 JSON**

```xleak [data.xlsx] --export json > [output.json]```

**列出工作簿中的所有表**

```xleak [workbook.xlsx] --list-tables```

**默认显示公式**

```xleak [data.xlsx] --formulas```

# SYNOPSIS

**xleak** [_options_] _file_

# PARAMETERS

**--sheet** _NAME|NUMBER_
> 按名称或索引打开指定工作表。

**-n**, **--num-rows** _COUNT_
> 限制显示的行数。`0` 表示显示所有行。

**-w**, **--width** _WIDTH_
> 设置列宽。

**-H**
> 启用水平滚动并自动调整列宽。

**--formulas**
> 默认显示单元格公式而非计算结果。

**--export** _FORMAT_
> 将电子表格以 `csv`、`json` 或 `text`（制表符分隔）格式导出到 stdout。

**--table** _NAME_
> 提取指定的命名 Excel 表格（仅限 .xlsx）。

**--list-tables**
> 列出工作簿中的所有表并退出。

**--config** _PATH_
> 使用自定义配置文件，而非 `~/.config/xleak/config.toml` 默认配置。

# KEYBOARD SHORTCUTS

**方向键**
> 在单元格之间移动。

**/**
> 在所有单元格中搜索。

**n** / **N**
> 跳到下一条 / 上一条搜索结果。

**Enter**
> 查看单元格详情和公式。

**c**
> 将单元格值复制到剪贴板。

**C**
> 将整行复制到剪贴板。

**Tab** / **Shift+Tab**
> 在工作表之间切换。

**Ctrl+G**
> 跳转到特定单元格或行号。

**t**
> 循环切换配色主题。

**?**
> 显示帮助。

**q**
> 退出。

# DESCRIPTION

**xleak** 是一个基于终端的 Excel 查看器，支持 .xlsx、.xls、.xlsm、.xlsb 和 .ods 文件。功能包括跨单元格全文搜索、公式显示、大文件懒加载、剪贴板支持以及导出 CSV 和 JSON。

# HISTORY

**xleak** 由 **Brandon Greenwell**（bgreenwell）创建，使用 **Rust** 编写。

# INSTALL

```brew: brew install xleak```

```nix: nix profile install nixpkgs#xleak```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sc-im](/man/sc-im)(1), [csvlens](/man/csvlens)(1)
