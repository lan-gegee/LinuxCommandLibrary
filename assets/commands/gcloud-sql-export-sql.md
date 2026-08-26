# TAGLINE

将 Cloud SQL 数据导出到存储

# TLDR

**将数据库导出到 Cloud Storage**

```gcloud sql export sql [instance] [gs://bucket/file.sql] --database [db_name]```

**导出所有数据库**

```gcloud sql export sql [instance] [gs://bucket/file.sql]```

**异步导出**

```gcloud sql export sql [instance] [gs://bucket/file.sql] --async```

# SYNOPSIS

**gcloud** **sql** **export** **sql** _instance_ _uri_ [_options_]

# PARAMETERS

**--database** _name_
> 要导出的数据库。

**--table** _name_
> 要导出的表。

**--async**
> 不等待完成。

**--offload**
> 将导出任务卸载到只读副本执行。

# DESCRIPTION

**gcloud sql export sql** 将 Cloud SQL 实例中的数据导出为存储在 Google Cloud Storage 中的 SQL 转储文件。该命令以标准 SQL 格式创建数据库备份，可导入其他数据库系统或恢复到 Cloud SQL 实例。

该工具同时支持 MySQL 和 PostgreSQL 实例。导出可以针对特定数据库或表，也可以一次转储所有数据库。异步模式让耗时较长的导出在后台继续进行，不阻塞终端。将导出卸载到只读副本可以最大程度减少对生产实例的性能影响。

# SEE ALSO

