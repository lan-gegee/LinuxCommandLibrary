# TAGLINE

Google BigQuery 命令行界面

# TLDR

**查询**数据（使用标准 SQL）

```bq query --use_legacy_sql=false "SELECT * FROM [dataset.table] LIMIT 10"```

**列出**当前项目中的数据集

```bq ls```

**列出**某个数据集中的表

```bq ls [dataset]```

**显示**表结构与元数据

```bq show [dataset.table]```

将 CSV 文件**加载**到表中

```bq load --source_format=CSV [dataset.table] [data.csv] [schema.json]```

将表**导出**到 Cloud Storage

```bq extract [dataset.table] gs://[bucket]/[file.csv]```

在不执行的情况下**估算**查询将处理的数据量（字节）

```bq query --dry_run --use_legacy_sql=false "[SELECT ...]"```

# SYNOPSIS

**bq** [_options_] _command_

# DESCRIPTION

**bq** 是基于 Python 的 Google BigQuery 命令行界面，随 Google Cloud CLI (gcloud) 一同提供。它可以通过统一的界面查询海量数据集、管理表和数据集、加载数据以及控制访问权限。

资源以 **PROJECT:DATASET.TABLE** 的形式寻址；配置了默认项目时可省略项目前缀。命令的形式为 **bq COMMAND [FLAGS] [ARGUMENTS]**，其中全局选项（如 **--project_id**）对所有命令生效，而命令专属选项只作用于单个命令。

# PARAMETERS

**--project_id** _id_
> 项目 ID。

**--dataset_id** _id_
> 数据集 ID。

**--format** _format_
> 输出格式（json、csv、prettyjson）。

**--max_rows** _n_
> 返回的最大行数。

**--use_legacy_sql=false**
> 使用 GoogleSQL（标准 SQL）而非旧版方言。推荐使用。

**--location** _region_
> 作业或资源所在的区域或多区域（例如 US、EU、asia-northeast1）。

**--dry_run**
> 校验查询并报告将处理的数据量（字节），但不执行。

**--apilog** _file_
> 将 API 请求和响应记录到文件以便调试（用 - 表示标准输出）。

# COMMON COMMANDS

**query** _sql_
> 执行 SQL 查询。

**ls** [_dataset_]
> 列出数据集或表。

**show** _resource_
> 显示资源详情。

**mk** _dataset_
> 创建数据集。

**rm** _resource_
> 删除资源。

**load** _table_ _source_
> 将数据加载到表中。

**extract** _table_ _destination_
> 导出表数据。

**cp** _source_ _destination_
> 复制表。

# WORKFLOW

```bash
# Run query
bq query --use_legacy_sql=false \
  'SELECT name, count FROM `project.dataset.table` LIMIT 10'

# Create dataset
bq mk --dataset project:mydataset

# Create table
bq mk --table mydataset.mytable schema.json

# Load CSV
bq load --source_format=CSV \
  mydataset.mytable \
  gs://bucket/data.csv \
  name:STRING,age:INTEGER

# Export to GCS
bq extract mydataset.mytable gs://bucket/export.csv
```

# FEATURES

- 交互式与批量查询
- 数据集和表管理
- 从多种来源加载数据
- 将数据导出到 Cloud Storage
- 访问控制管理
- 计划查询
- 数据传输服务

# CONFIGURATION

**~/.bigqueryrc**
> 存储默认项目、数据集、格式以及各命令选项默认值的默认配置文件。可用 **--bigqueryrc** 覆盖其位置。

# CAVEATS

需要 Google Cloud 项目并进行身份验证。查询费用按处理的数据量计费。大型导出操作依赖 Cloud Storage。旧版 SQL 与标准 SQL 存在差异。查询费用可能快速累积。

# HISTORY

**bq** 由 Google 在 **2011** 年前后随 BigQuery 一起发布，是该数据仓库服务的主要命令行界面。

# SEE ALSO

[gcloud](/man/gcloud)(1), [gsutil](/man/gsutil)(1), [psql](/man/psql)(1)

# RESOURCES

```[Homepage](https://cloud.google.com/bigquery/docs/bq-command-line-tool)```

```[Documentation](https://cloud.google.com/bigquery/docs/reference/bq-cli-reference)```

<!-- verified: 2026-06-19 -->
