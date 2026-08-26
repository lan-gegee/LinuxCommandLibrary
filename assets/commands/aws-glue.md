# TAGLINE

管理无服务器 ETL 任务和数据目录

# TLDR

**创建爬虫以发现数据模式**

```aws glue create-crawler --name [my-crawler] --role [arn:aws:iam::account:role/glue-role] --database-name [my-database] --targets S3Targets=[{Path=s3://my-bucket/data/}]```

**启动爬虫**

```aws glue start-crawler --name [my-crawler]```

**列出 Data Catalog 中的所有数据库**

```aws glue get-databases```

**列出数据库中的表**

```aws glue get-tables --database-name [my-database]```

**从目录获取表模式**

```aws glue get-table --database-name [my-database] --name [my-table]```

**创建并启动 Glue 任务**

```aws glue create-job --name [my-job] --role [arn:aws:iam::account:role/glue-role] --command Name=glueetl,ScriptLocation=s3://my-bucket/scripts/job.py```

**带参数启动任务运行**

```aws glue start-job-run --job-name [my-job] --arguments '{"--input_path":"s3://bucket/input","--output_path":"s3://bucket/output"}'```

**查看任务运行状态**

```aws glue get-job-run --job-name [my-job] --run-id [jr_abc123]```

# SYNOPSIS

**aws glue** _command_ [_options_]

# DESCRIPTION

**aws glue** 是 AWS Glue 的 AWS CLI 接口。AWS Glue 是一项面向 ETL（提取、转换、加载）工作负载的无服务器数据集成服务，可为分析、机器学习和应用开发发现、准备和整合数据。

关键组件包括 **Data Catalog**（中央元数据存储库）、**Crawler（爬虫）**（自动发现模式）、**Job（任务）**（以 Python 或 Scala 编写的 ETL 脚本）和 **Trigger（触发器）**（任务编排）。Glue 与 S3、Redshift、RDS 及其他数据存储集成。

# COMMANDS

**create-database**
> 在 Data Catalog 中创建数据库

**create-table**
> 在目录中注册表定义

**create-crawler**
> 创建用于模式发现的爬虫

**start-crawler**
> 运行爬虫填充目录

**get-databases**
> 列出 Data Catalog 中的数据库

**get-tables**
> 列出数据库中的表

**get-table**
> 获取表的模式详情

**create-job**
> 创建 ETL 任务

**start-job-run**
> 执行任务

**get-job-run**
> 查看任务运行状态

**create-trigger**
> 创建任务触发器

**get-crawlers**
> 列出所有爬虫

# CAVEATS

爬虫处理大型数据集时可能耗时较长。任务冷启动会增加延迟；可使用作业书签（job bookmark）做增量处理。DPU（数据处理单元）费用会在任务运行期间持续累积。Data Catalog 对每个数据库的表数量有限制（200,000 个）。

# HISTORY

AWS Glue 于 **2017 年 8 月** 作为无服务器 ETL 服务推出。用于可视化编写 ETL 的 Glue Studio 于 **2020 年** 推出。数据质量功能于 **2022 年** 加入，面向数据科学工作负载的 Glue for Ray（分布式 Python）于 **2023 年** 推出。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-athena](/man/aws-athena)(1), [aws-s3](/man/aws-s3)(1), [aws-redshift](/man/aws-redshift)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/glue/index.html)```

<!-- verified: 2026-06-18 -->
