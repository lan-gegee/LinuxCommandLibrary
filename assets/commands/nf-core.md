# TAGLINE

nf-core 社区 Nextflow 流水线合集的命令行工具

# TLDR

**列出所有可用的 nf-core 流水线**

```nf-core pipelines list```

**下载流水线供离线使用**

```nf-core pipelines download [pipeline-name]```

**以交互方式启动流水线**

```nf-core pipelines launch [pipeline-name]```

**显示流水线信息**

```nf-core pipelines info [pipeline-name]```

**从模板创建新流水线**

```nf-core pipelines create```

**按最佳实践检查流水线**

```nf-core pipelines lint```

**列出可用的流水线 schema**

```nf-core pipelines schema lint```

# SYNOPSIS

**nf-core** [_options_] _command_ [_subcommand_] [_args_]

# COMMANDS

**pipelines list**
> 列出可用的 nf-core 流水线及其星标数、发布版本和描述。

**pipelines download**
> 下载流水线及其容器镜像，供离线使用。

**pipelines launch**
> 以交互方式配置并启动流水线运行。

**pipelines create**
> 基于 nf-core 模板创建新流水线。

**pipelines lint**
> 按照 nf-core 最佳实践检查流水线代码。

**pipelines info**
> 显示流水线的详细信息。

**pipelines schema**
> 管理流水线参数的 schema 文件。

# PARAMETERS

**--help**
> 显示帮助信息。

**--version**
> 显示版本。

**--verbose**
> 增加输出详细程度。

**--hide-progress**
> 不显示进度条。

**--log-file** _FILE_
> 将日志输出保存到文件。

# DESCRIPTION

**nf-core** 是 nf-core 社区的命令行界面。该社区维护着一组用 Nextflow 构建的高质量生物信息学流水线。该工具帮助用户按照社区最佳实践查找、下载、启动和开发流水线。

**download** 命令会连同 Singularity 或 Docker 容器镜像一起获取流水线，用于离线或物理隔离（air-gapped）环境。**launch** 命令提供交互式界面来设置流水线参数、生成 params 文件并启动运行。

对于流水线开发者，**create** 会基于 nf-core 模板搭建新流水线骨架，内置 CI、文档和测试。**lint** 命令验证流水线是否遵循 nf-core 在代码质量、文档和可复现性方面的规范。

# CAVEATS

需要 Python 3.8 或更高版本。实际运行流水线必须另行安装 Nextflow。包含容器镜像时下载量可能很大。列出和下载流水线需要联网。

# HISTORY

nf-core 成立于 **2018 年**，是一项社区协作项目，旨在打造一组遵循可复现性和可移植性最佳实践的精选 Nextflow 流水线。该项目于 2020 年发表在 **Nature Biotechnology** 上。如今它已发展到包含 100 多条流水线，覆盖基因组学、蛋白质组学、成像等生物信息学领域。

# SEE ALSO

[nextflow](/man/nextflow)(1), [conda](/man/conda)(1), [docker](/man/docker)(1)
