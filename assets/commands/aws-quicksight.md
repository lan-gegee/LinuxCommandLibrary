# TAGLINE

管理商业智能仪表板和分析

# TLDR

**列出账户中的所有仪表板**

```aws quicksight list-dashboards --aws-account-id [account-id]```

**描述仪表板**

```aws quicksight describe-dashboard --aws-account-id [account-id] --dashboard-id [dashboard-id]```

从 RDS **创建数据源**

```aws quicksight create-data-source --aws-account-id [account-id] --data-source-id [source-id] --name [my-source] --type RDS --data-source-parameters file://[rds-params.json]```

从数据源**创建数据集**

```aws quicksight create-data-set --aws-account-id [account-id] --data-set-id [dataset-id] --name [my-dataset] --physical-table-map file://[table-map.json] --import-mode SPICE```

为仪表板**生成嵌入 URL**

```aws quicksight generate-embed-url-for-registered-user --aws-account-id [account-id] --user-arn [arn:aws:quicksight:region:account:user/default/username] --experience-configuration Dashboard={InitialDashboardId=[dashboard-id]}```

**注册新用户**

```aws quicksight register-user --aws-account-id [account-id] --namespace default --email [user@example.com] --identity-type IAM --user-role READER --iam-arn [arn:aws:iam::account:user/username]```

# SYNOPSIS

**aws quicksight** _command_ [_options_]

# DESCRIPTION

**aws quicksight** 是 AWS CLI 中用于管理 Amazon QuickSight 的接口。QuickSight 是一项无服务器的商业智能服务，用于创建可视化、仪表板以及执行即席分析。QuickSight 使用 SPICE（Super-fast Parallel In-memory Calculation Engine）实现快速查询性能。

QuickSight 支持连接多种数据源，包括 S3、Athena、Redshift、RDS 和第三方数据库。仪表板可以嵌入应用程序中，并与组织内的用户共享。

# COMMANDS

**list-dashboards**
> 列出账户中的所有仪表板

**describe-dashboard**
> 获取仪表板详情

**create-data-source**
> 创建到数据源的连接

**create-data-set**
> 基于数据源定义数据集

**create-analysis**
> 创建用于探索的分析

**create-dashboard**
> 将分析发布为仪表板

**register-user**
> 添加 QuickSight 用户

**generate-embed-url-for-registered-user**
> 获取用于嵌入仪表板的 URL

**create-ingestion**
> 刷新 SPICE 数据集

**list-data-sources**
> 列出已配置的数据源

**list-data-sets**
> 列出账户中的所有数据集

**delete-dashboard**
> 删除仪表板

**update-dashboard**
> 更新现有仪表板

**describe-data-source**
> 获取数据源详情

# CAVEATS

SPICE 数据集的存储上限取决于订阅级别。仪表板的刷新取决于数据源的刷新计划。嵌入仪表板需要正确配置 CORS 和域名。用户管理与 IAM 相互独立；QuickSight 有自己的用户注册体系。

# HISTORY

Amazon QuickSight 于 **2016 年 11 月**上线，是一项云原生 BI 服务。Q（自然语言查询）于 **2020 年**推出。该服务此后扩展了分页报表、以编程方式创建仪表板的 API 以及机器学习驱动的洞察等功能。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-athena](/man/aws-athena)(1), [aws-redshift](/man/aws-redshift)(1)
