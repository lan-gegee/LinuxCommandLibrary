# TAGLINE

比较 CSV 文件并显示差异

# TLDR

比较两个 CSV 文件的差异

```csv-diff [old.csv] [new.csv]```

以指定的键列进行比较

```csv-diff [old.csv] [new.csv] --key [id]```

以 JSON 格式输出

```csv-diff [old.csv] [new.csv] --json```

**只显示变化**

```csv-diff [old.csv] [new.csv] --show-unchanged```

# SYNOPSIS

**csv-diff** [_options_] _old.csv_ _new.csv_

# PARAMETERS

**--key** _column_
> 用作唯一标识的列。

**--json**
> 以 JSON 格式输出。

**--show-unchanged**
> 在输出中包含未变化的行。

**--singular** _name_
> 行的单数名词。

**--plural** _name_
> 行的复数名词。

# DESCRIPTION

**csv-diff** 比较两个 CSV、TSV 或 JSON 文件，显示新增、删除和修改的行。它适合用来跟踪数据导出、数据库转储或任何表格数据的变化。

必须指定 **--key** 列，才能跨文件匹配行。默认输出便于人类阅读；通过 **--json** 可获得机器可读的 JSON。

该工具是 **Simon Willison** 开发的独立 Python 包，可通过 `pip install csv-diff` 安装。它与 csvkit 无关。

# CAVEATS

没有稳定唯一键的行无法进行有意义的比较；请选择两侧都保证存在的列。大文件会被完整加载进内存。

# SEE ALSO

[csvkit](/man/csvkit)(1), [diff](/man/diff)(1), [jq](/man/jq)(1)
