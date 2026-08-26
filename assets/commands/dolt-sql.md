# TAGLINE

在版本化数据库上执行 SQL 查询

# TLDR

**运行 SQL 查询**

```dolt sql -q "[SELECT * FROM table]"```

**启动交互式** SQL Shell

```dolt sql```

**执行 SQL 文件**

```dolt sql --file [script.sql]```

**运行查询**并选择结果格式

```dolt sql -q "[SELECT * FROM table]" -r [csv]```

**查询其他分支或提交时点的表**

```dolt sql -q "[SELECT * FROM table AS OF 'main']"```

某条语句失败后**继续执行**

```dolt sql --continue --file [script.sql]```

**将查询保存**到目录中，之后按名称运行

```dolt sql -q "[SELECT * FROM table]" -s [my_query]```

```dolt sql -x [my_query]```

# SYNOPSIS

**dolt sql**

**dolt sql** < _script.sql_

**dolt sql** **-q** _query_ [**-r** _format_] [**-s** _name_ **-m** _message_]

**dolt sql** **-x** _name_

**dolt sql** **--list-saved**

# PARAMETERS

**-q**, **--query** _QUERY_
> 运行单条查询后退出。

**-r**, **--result-format** _FORMAT_
> 输出的格式：`tabular`（默认）、`csv`、`json`、`vertical` 或 `parquet`。

**-f**, **--file** _FILE_
> 执行 _FILE_ 中的语句。

**-c**, **--continue**
> 某条语句失败后继续运行剩余的查询。

**-s**, **--save** _NAME_
> 将查询以 _NAME_ 保存到查询目录中。

**-m**, **--message** _MSG_
> 为保存的查询附带一段描述性说明。

**-x**, **--execute** _NAME_
> 执行给定名称的已保存查询。

**-l**, **--list-saved**
> 列出所有已保存的查询。

**--binary-as-hex** / **--skip-binary-as-hex**
> 是否以十六进制打印二进制数据。在交互式终端上默认启用。

**--disable-auto-gc**
> 本次调用不执行自动垃圾回收。

**-b**, **--batch**
> 为兼容性保留的无操作选项；批量处理已不再是单独的模式。

# DESCRIPTION

**dolt sql** 是读写 Dolt 数据库的主要方式。它支持 MySQL 兼容的 SQL，因此绝大多数现有的查询、客户端和 ORM 都无需修改即可使用。

不带参数时会打开一个带历史记录和 Tab 补全的交互式 Shell。配合 **-q** 则执行单条语句后退出，这是脚本中常用的形式。结果既可以渲染为表格，也可以输出为 CSV、JSON 或 Parquet，便于通过管道交给其他工具处理。

Dolt 的版本控制是通过 SQL 而非额外命令暴露的。`AS OF` 可以读取任意分支、标签或提交时刻的表；`dolt_diff_<table>` 和 `dolt_history_<table>` 提供行级的变更历史；`dolt_log`、`dolt_branches`、`dolt_status` 等系统表则与 CLI 功能一一对应。借助 `CALL DOLT_COMMIT(...)`、`CALL DOLT_MERGE(...)` 这类存储过程，应用程序不用离开 SQL 就能提交与合并。

在此执行的写入会落入工作集，与你在 Git 检出目录里编辑文件完全一样：在被暂存并提交之前，它们并不属于历史。

# CAVEATS

与 MySQL 的兼容性很高但并非完备：部分函数、存储引擎和边缘行为存在差异，触发器、视图和存储过程的支持程度也因版本而异。**-b**/**--batch** 仍可解析但不起任何作用。独立的 `dolt sql-server` 进程会持有数据库锁，因此在服务器运行期间用 CLI Shell 访问同一数据库时，实际连接的是该服务器而不是直接打开文件。

# HISTORY

Dolt 的 SQL 引擎是 **go-mysql-server**——一个由 DoltHub 接手并深度扩展的 MySQL 兼容引擎。选择 SQL 而不是自创查询语言作为接口，让 Dolt 得以无缝嵌入现有工具链；随后版本控制能力又被下沉到 SQL 层，成为系统表和存储过程，应用程序无需调用外部命令即可对数据进行分支、diff 和合并。

# INSTALL

```pacman: sudo pacman -S dolt```

```brew: brew install dolt```

```nix: nix profile install nixpkgs#dolt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dolt](/man/dolt)(1), [dolt-commit](/man/dolt-commit)(1), [dolt-merge](/man/dolt-merge)(1), [mysql](/man/mysql)(1), [sqlite3](/man/sqlite3)(1)

# RESOURCES

```[Source code](https://github.com/dolthub/dolt)```

```[Documentation](https://www.dolthub.com/docs/cli-reference/cli/)```

<!-- verified: 2026-07-14 -->
