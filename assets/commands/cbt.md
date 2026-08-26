# TAGLINE

Google Cloud Bigtable 命令行界面

# TLDR

**列出实例中的所有表**

```cbt -project [project_id] -instance [instance_id] ls```

**读取表中的行**

```cbt -project [project_id] -instance [instance_id] read [table_name]```

**统计表中的行数**

```cbt -project [project_id] -instance [instance_id] count [table_name]```

**创建新表**

```cbt -project [project_id] -instance [instance_id] createtable [table_name]```

**创建列族**

```cbt -project [project_id] -instance [instance_id] createfamily [table_name] [family_name]```

**向单元格写入值**

```cbt -project [project_id] -instance [instance_id] set [table_name] [row_key] [family]:[column]=[value]```

# SYNOPSIS

**cbt** [**-project** _project_] [**-instance** _instance_] [**-creds** _file_] [**-timeout** _duration_] _command_ [_arguments..._]

# DESCRIPTION

**cbt** 是 Google Cloud Bigtable（一项全托管的 NoSQL 数据库服务）的命令行界面。它可以对 Bigtable 实例、表、列族和行执行管理和数据操作。

该工具可通过包含项目和实例默认值的 **~/.cbtrc** 文件进行配置，也可以直接传递标志。

# PARAMETERS

**-project** _project_id_
> Google Cloud 项目 ID。未设置时使用 gcloud 默认值

**-instance** _instance_id_
> Cloud Bigtable 实例名称

**-creds** _file_
> 凭据 JSON 文件的路径

**-timeout** _duration_
> 操作超时时间（例如 10s、5m）

**常用命令：**

**ls** - 列出表
**read** _table_ - 读取表中的行
**count** _table_ - 统计表中的行数
**createtable** _table_ - 创建表
**deletetable** _table_ - 删除表
**createfamily** _table_ _family_ - 创建列族
**set** _table_ _row_ _family:col=val_ - 写入单元格值
**deleterow** _table_ _row_ - 删除一行
**help** - 打印帮助文本

# CONFIGURATION

**~/.cbtrc**
> 默认的项目和实例设置，免去每次调用都传 -project 和 -instance 标志。

# CAVEATS

cbt CLI 没有实现智能重试或高级错误处理。生产环境请改用 Bigtable 客户端库或 Google Cloud 控制台。

Bash Shell 的语法规则同样适用：包含空格或运算符的值需要加引号，任意字节值需要用美元符号前缀加单引号。

# HISTORY

**cbt** 工具由 Google 作为 Cloud Bigtable 生态的一部分开发，使用 Go 语言编写，基于 Bigtable 官方 Go 客户端库。它为开发和调试目的提供了一种与 Bigtable 快速交互的方式。

# SEE ALSO

[gcloud](/man/gcloud)(1), [bq](/man/bq)(1)

# RESOURCES

```[Source code](https://github.com/googleapis/google-cloud-go/tree/main/bigtable/cmd/cbt)```

```[Documentation](https://cloud.google.com/bigtable/docs/cbt-reference)```

<!-- verified: 2026-06-22 -->
