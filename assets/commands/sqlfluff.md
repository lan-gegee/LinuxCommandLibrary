# TAGLINE

支持多种方言的模块化 SQL linter 与自动格式化工具

# TLDR

以**指定方言 lint** SQL 文件

```sqlfluff lint --dialect [postgres] [path/to/query.sql]```

**就地自动修复**lint 违规

```sqlfluff fix --dialect [bigquery] [path/to/queries/]```

通过 stdin **格式化** SQL

```cat [query.sql] | sqlfluff format --dialect [snowflake] -```

**显示查询的解析标记树**

```sqlfluff parse --dialect [mysql] [query.sql]```

**只 lint 特定规则**

```sqlfluff lint --rules [LT01,LT02,CP01] [path/to/file.sql]```

在运行中**排除干扰性规则**

```sqlfluff lint --exclude-rules [L034,L036] [path/to/file.sql]```

**渲染**模板化查询（展开 Jinja/dbt）而不执行 lint

```sqlfluff render --dialect [ansi] [query.sql]```

# SYNOPSIS

**sqlfluff** _command_ [_options_] _PATH_...

Commands: **lint**, **fix**, **format**, **parse**, **render**, **rules**, **dialects**, **fluff** (legacy alias)

# PARAMETERS

**--dialect** _NAME_
> 解析所用的 SQL 方言（如 **ansi**、**postgres**、**mysql**、**bigquery**、**snowflake**、**redshift**、**tsql**、**sqlite**、**duckdb**、**databricks**）。运行 **sqlfluff dialects** 可查看完整列表。

**--templater** _NAME_
> 解析前使用的模板引擎：**raw**、**jinja**、**python**、**placeholder** 或 **dbt**。

**--rules** _LIST_
> 要启用的规则（或规则组）列表，以逗号分隔。

**--exclude-rules** _LIST_
> 要跳过的规则列表，以逗号分隔。

**-f**, **--force**
> 对 **fix**：不经确认直接应用更改。

**--FIX-EVEN-UNPARSABLE**
> 允许 **fix** 处理存在模板或解析错误的文件（危险）。

**--processes** _N_
> 并行工作进程数量；**0** 表示使用所有 CPU，负数表示 CPU 数 + N。

**-v**, **-vv**, **-vvv**
> 提高输出详细程度；可叠加使用。

**--nocolor**
> 在输出中禁用 ANSI 颜色。

**--format** _FMT_
> 输出格式：**human**、**json**、**yaml**、**github-annotation**、**github-annotation-native**。

**--config** _FILE_
> 显式指定 **.sqlfluff** 配置文件的路径。

**--encoding** _ENC_
> 读取源文件时使用的编码（默认 **autodetect**）。

**--disable-noqa**
> 忽略嵌入在 SQL 中的 **-- noqa:** 注释。

# DESCRIPTION

**sqlfluff** 是一个具备方言感知能力的 SQL linter 与自动格式化工具。它将查询解析为抽象语法树，应用一组可配置的规则，然后报告或重写违规之处。与基于文本的 linter 不同，AST 方法使它能够强制执行结构性规则，例如逗号位置、关键字大小写、歧义连接以及列引用限定。

该工具支持大量方言（PostgreSQL、MySQL、BigQuery、Snowflake、Redshift、T-SQL、SQLite、DuckDB、Databricks、ANSI 等），并与模板引擎集成，因此无需先渲染即可 lint 用 **Jinja**、**dbt** 或自定义占位符语法编写的查询。

操作按命令划分：**lint** 报告违规，**fix** 就地重写源文件，**format** 只应用布局类修复，**parse** 输出标记树，**render** 展开模板而不执行 lint。配置分层生效：内置默认值会被沿目录树向上找到的 **.sqlfluff** 文件覆盖，其次是 **pyproject.toml** 中的配置节，最后是命令行标志。

# CONFIGURATION

**.sqlfluff**
> 每个项目的 INI 风格配置；查找过程从被 lint 的文件向上遍历。示例：

```
[sqlfluff]
dialect = postgres
templater = jinja
exclude_rules = L034,L036

[sqlfluff:rules:capitalisation.keywords]
capitalisation_policy = upper

[sqlfluff:indentation]
tab_space_size = 2
indent_unit = space
```

**pyproject.toml**
> 设置位于 **[tool.sqlfluff.*]** 配置节中，与 INI 布局一一对应。

**~/.sqlfluff**
> 用户级回退配置，应用于没有自身配置的项目。

**-- noqa:** 注释
> 行内指令，用于在某一行或某个代码块上禁用规则，例如 **SELECT * -- noqa: L044**。

# RULE GROUPS

规则按领域划分命名空间：**LT** 布局、**CP** 大小写、**CV** 惯例、**RF** 引用、**ST** 结构、**AM** 歧义、**AL** 别名、**JJ** Jinja。使用 **sqlfluff rules** 可打印包含代码、名称和描述的完整规则目录。

# CAVEATS

模板化 SQL 必须能在渲染后正常解析；未解析的变量会引发模板错误并抑制大部分 lint 输出。即使底层 SQL 存在细微的语义影响（例如重新起别名导致列顺序变化），**fix** 也会重写文件；提交前请检查 diff。各方言解析器的覆盖程度不一；非常新的厂商语法可能尚无法识别。较旧的数字规则代码（**L001**、**L002** 等）已在 **2.0** 中更名为助记码（**LT01**、**CP01** 等）；旧代码仍可用作别名但已弃用。

# HISTORY

**SQLFluff** 由 **Alan Cruickshank** 于 **2019 年**发起，旨在作为基于文本的 SQL linter 的开源方言感知替代品。版本 **1.0** 于 **2022 年**发布；**2.0**（**2023 年**）带来了采用助记码的全新规则分类体系以及感知模板的修复引擎。该项目以 MIT 许可证托管于 **github.com/sqlfluff/sqlfluff** 并持续维护。

# INSTALL

```pacman: sudo pacman -S sqlfluff```

```brew: brew install sqlfluff```

```nix: nix profile install nixpkgs#sqlfluff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dbt](/man/dbt)(1), [psql](/man/psql)(1)
