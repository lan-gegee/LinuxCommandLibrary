# TAGLINE

格式化并提取嵌入在 Python 源文件中的 SQL 字符串

# TLDR

**列出** Python 文件中嵌入的 SQL 块

```py-sql-cleaner list jobs/load_users.py```

使用通用方言**就地格式化** SQL

```py-sql-cleaner format jobs/load_users.py```

不写入文件，只**预览**格式化更改

```py-sql-cleaner format jobs/load_users.py --dry-run```

使用特定方言（mysql、postgres、redshift）进行**格式化**

```py-sql-cleaner format jobs/load_users.py -d postgres```

将 SQL **提取**为独立的 .sql 文件

```py-sql-cleaner extract jobs/load_users.py --out-dir sql```

在 CI 中**检查** SQL 格式（存在差异时以非零值退出）

```py-sql-cleaner check jobs/load_users.py```

**列出**支持的 SQL 方言

```py-sql-cleaner dialects```

# SYNOPSIS

**py-sql-cleaner** _command_ [_options_] _file_

# DESCRIPTION

**py-sql-cleaner** 是一个 Python CLI，用于查找 Python 文件中三引号包裹的 SQL 字符串，并使用 **SQLGlot** 对其重新格式化或提取。它面向 ETL 和数据工程项目——这些项目中 SQL 嵌入在 `.py` 文件中，而不是保存在单独的 `.sql` 文件里。

该工具默认采取保守策略。f-string、Jinja 模板和其他运行时占位符会被检测到但跳过而不重写，因此格式化不会悄然改变依赖插值的查询。

py-sql-cleaner 从不连接数据库，也从不执行 SQL。支持的方言（`generic`、`mysql`、`postgres`、`redshift`）只决定 SQLGlot 的解析器和格式化器模式，并不提供完整的数据库验证。

当格式化会改变文件内容时，`check` 子命令以非零值退出，因此适合作为 pre-commit 钩子或 CI 门禁，与 `black`、`ruff` 等类似格式化工具搭配使用。

# PARAMETERS

**list** _file_
> 显示文件中找到的每个嵌入式 SQL 块。

**format** _file_
> 就地重新格式化嵌入的 SQL。

**extract** _file_
> 将每个 SQL 块写入单独的 `.sql` 文件。

**check** _file_
> 如果格式化会改变该文件，则以非零值退出。

**dialects**
> 打印支持的 SQL 方言。

**-d**, **--dialect** _NAME_
> 选择方言：`generic`、`mysql`、`postgres`、`redshift`。

**--dry-run**
> 打印格式化结果而不写入。

**--out-dir** _DIR_
> `extract` 的输出目录。

**--version**
> 打印已安装的版本。

# INSTALLATION

```pip install py-sql-cleaner```

或使用 pipx 进行隔离安装：

```pipx install py-sql-cleaner```

无需安装即可运行：

```uvx py-sql-cleaner --help```

# CAVEATS

该项目尚处于早期 MVP 阶段。f-string 和模板语法会被有意跳过，以免破坏在运行时构建 SQL 的查询。方言选择仅影响解析，不能保证查询能在目标数据库上执行。

# SEE ALSO

[black](/man/black), [ruff](/man/ruff), [sqlfluff](/man/sqlfluff)
