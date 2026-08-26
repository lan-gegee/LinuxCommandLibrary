# TAGLINE

管理 AWS 成本与使用率报告的定义。

# TLDR

**列出账户中的所有报告定义**

```aws cur describe-report-definitions```

**创建传送到 S3 的新成本与使用率报告**

```aws cur put-report-definition --report-definition ReportName=[my-report],TimeUnit=DAILY,Format=textORcsv,Compression=GZIP,AdditionalSchemaElements=RESOURCES,S3Bucket=[my-bucket],S3Prefix=[reports/],S3Region=[us-east-1]```

**按名称删除报告定义**

```aws cur delete-report-definition --report-name [my-report]```

**修改现有报告定义**

```aws cur modify-report-definition --report-name [my-report] --report-definition ReportName=[my-report],TimeUnit=HOURLY,Format=Parquet,Compression=Parquet,AdditionalSchemaElements=RESOURCES,S3Bucket=[my-bucket],S3Prefix=[reports/],S3Region=[us-east-1]```

**列出报告资源的标签**

```aws cur list-tags-for-resource --resource-arn [arn:aws:cur:us-east-1:123456789012:definition/my-report]```

# SYNOPSIS

**aws cur** _command_ [_options_]

# DESCRIPTION

**aws cur** 是 AWS Cost and Usage Reports（成本与使用率报告）的 AWS CLI 接口，可以编程方式管理账单报告定义。成本与使用率报告提供关于 AWS 使用情况的全面成本数据，以 CSV 或 Parquet 格式传送到 S3 存储桶。

报告可配置不同的时间粒度（每小时、每天、每月），并可包含资源级明细。这些数据可与 Athena、Redshift 或 QuickSight 等分析服务集成，用于成本分析。

# COMMANDS

**put-report-definition**
> 创建新的成本与使用率报告定义

**describe-report-definitions**
> 列出账户中的所有报告定义

**modify-report-definition**
> 更新现有的报告定义

**delete-report-definition**
> 删除报告定义

**tag-resource**
> 为报告资源添加标签

**untag-resource**
> 移除报告资源上的标签

**list-tags-for-resource**
> 列出报告资源的标签

# CAVEATS

报告创建后最长可能需要 24 小时才会出现在 S3 中。API 端点（cur.us-east-1.amazonaws.com）仅在 **us-east-1** 区域可用。在 **--report-definition** 中，ReportName、TimeUnit、Format、Compression、AdditionalSchemaElements、S3Bucket、S3Prefix 和 S3Region 字段均为必填；Format 的有效值为 textORcsv 和 Parquet，Compression 的有效值为 ZIP、GZIP 和 Parquet。报告数据可能存在延迟，不适合用于实时成本监控。在控制台中创建的旧版报告可能无法通过 API 查看。

# HISTORY

AWS 成本与使用率报告于 **2015 年** 推出，由 Detailed Billing Reports 演进而来。CUR API 于 **2017 年** 加入，支持以编程方式进行管理。Parquet 格式支持于 **2018 年** 引入，以便更好地与分析工具集成；此后资源级数据逐步覆盖了更多服务。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-ce](/man/aws-ce)(1), [aws-budgets](/man/aws-budgets)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/cur/index.html)```

<!-- verified: 2026-06-18 -->
