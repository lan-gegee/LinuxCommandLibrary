# TAGLINE

面向分析工程的数据转换工作流工具

# TLDR

**初始化新的 dbt** 项目

```dbt init [project_name]```

**运行所有模型**

```dbt run```

**运行指定模型**

```dbt run --select [model_name]```

**测试数据质量**

```dbt test```

**生成文档**

```dbt docs generate```

在本地**伺服文档**

```dbt docs serve```

**构建**所有资源（运行模型、测试、快照、种子）

```dbt build```

**将 seed CSV 文件加载**到数据仓库

```dbt seed```

只**编译 SQL 而不**执行

```dbt compile```

从失败点**重试**上一条失败的命令

```dbt retry```

# SYNOPSIS

**dbt** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要执行的 dbt 命令（run、test、build、compile 等）。

**--select**, **-s** _MODEL_
> 选择要运行的特定模型。

**--exclude** _MODEL_
> 从运行中排除特定模型。

**--target**, **-t** _TARGET_
> 要使用的目标 profile。

**--profiles-dir** _DIR_
> 包含 profiles.yml 的目录。

**--project-dir** _DIR_
> 包含 dbt_project.yml 的目录。

**--full-refresh**
> 从头重建增量模型。

**--threads** _N_
> 并行运行模型的线程数。

**--vars** _JSON_
> 以 JSON 形式传递变量。

**--help**
> 显示帮助信息。

# CONFIGURATION

**~/.dbt/profiles.yml**
> 数据仓库的连接 profile，包括凭据和连接参数。

**dbt_project.yml**
> 项目配置，定义模型、测试、源以及项目级设置。

# DESCRIPTION

**dbt**（data build tool）是一个转换工作流工具，让数据分析师和工程师能够用 SQL 在数据仓库中转换数据。它为数据转换引入版本控制、测试和文档等软件工程实践。

dbt 配合你现有的数据仓库工作（Snowflake、BigQuery、Redshift、PostgreSQL 等），负责管理 ELT（提取、加载、转换）中的 T。模型被定义为 SQL SELECT 语句，由 dbt 物化为表或视图。

该工具提供模型之间的依赖管理、基于 schema 测试和自定义测试的自动化测试、文档生成，以及对大型数据集高效更新的增量处理。

# CAVEATS

需要 Python 以及与受支持数据仓库的连接。复杂的依赖关系可能导致较长的 DAG 解析时间。资源使用随项目规模增长。大版本之间偶尔会出现破坏性变更。

# HISTORY

dbt 由 **Fishtown Analytics**（现 dbt Labs）创建并于 **2016 年**发布。它开创了"分析工程"方法，将软件开发实践带入数据转换领域，并帮助确立了现代数据栈范式。

# INSTALL

```nix: nix profile install nixpkgs#dbt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [psql](/man/psql)(1), [bq](/man/bq)(1)
