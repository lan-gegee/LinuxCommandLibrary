# TAGLINE

用 SQL 交互式查询 JSON 和 CSV 的极简 TUI

# TLDR

**交互式查询 JSON 文件**

```cat [file.json] | qo```

直接以参数方式传入并**查询 CSV 文件**

```qo [file.csv]```

不进入 TUI 而**直接运行 SQL 查询**

```cat [file.json] | qo -q "SELECT [column] FROM tmp WHERE [condition]"```

用直接查询**将 JSON 转换为 CSV**

```qo -o csv [file.json] -q "SELECT * FROM [table]"```

**指定输入和输出格式**

```qo -i tsv -o json [file.tsv]```

# SYNOPSIS

**qo** [_options_] [_file_...]

_command_ | **qo** [_options_]

# PARAMETERS

**-i**, **--input** _format_
> 输入格式：`json`、`csv`、`tsv` 或 `psv`（管道分隔）。未指定时根据文件扩展名自动检测。

**-o**, **--output** _format_
> 输出格式：`json`、`jsonl`、`csv`、`tsv`、`psv` 或 `table`。

**-q**, **--query** _sql_
> 直接运行 SQL 查询并跳过交互式 TUI。

**--no-header**
> 将第一行视为数据而非表头。

# DESCRIPTION

**qo** 是一个极简的终端 UI，用于用 SQL 查询 JSON 和 CSV 数据。它从标准输入或文件参数读取数据，并提供交互式 TUI，让你用 SQL 探索结构化数据。

内部表始终命名为 **tmp**。退出时结果会发送到标准输出，因此 **qo** 可以用于管道。

# KEYBOARD SHORTCUTS

**Tab**
> 在查询输入和表格视图之间切换

**Enter**
> 执行当前查询

**Esc**
> 将结果输出到 stdout 并退出

**Ctrl+C**
> 不产生输出直接退出

**j/k** 或 **↑/↓**
> 在表格视图中上下滚动行

**h/l** 或 **←/→**
> 在表格视图中左右滚动列

# HISTORY

**qo** 由 **kiki-ki** 创建，使用 **Go** 编写。项目以 **go-qo** 为名托管在 GitHub 上。

# INSTALL

```brew: brew install qo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [q](/man/q)(1), [miller](/man/miller)(1), [trdsql](/man/trdsql)(1), [sqlite3](/man/sqlite3)(1)
