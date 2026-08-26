# TAGLINE

面向可扩展科学流水线的数据驱动工作流编排工具

# TLDR

**运行流水线**

```nextflow run [pipeline.nf]```

**带参数运行**

```nextflow run [pipeline.nf] --input [data.txt]```

**从 GitHub 运行流水线**

```nextflow run [user/repo]```

**从检查点恢复失败的运行**

```nextflow run [pipeline.nf] -resume```

**使用 Docker 容器运行**

```nextflow run [pipeline.nf] -with-docker```

**使用指定的配置 profile 运行**

```nextflow run [pipeline.nf] -profile [docker]```

**生成执行报告和时间线**

```nextflow run [pipeline.nf] -with-report -with-timeline```

**显示流水线信息**

```nextflow info [pipeline]```

**列出历史运行**

```nextflow log```

**清理缓存的工作目录**

```nextflow clean -f```

# SYNOPSIS

**nextflow** [_options_] _command_ [_arguments_]

# PARAMETERS

**run** _PIPELINE_
> 执行一个流水线项目（本地路径、脚本或 GitHub 仓库）。

**pull** _PROJECT_
> 下载或更新远程项目。

**info** [_PROJECT_]
> 显示系统或流水线信息。

**log**
> 显示执行历史。

**clean**
> 清理过去执行产生的工作目录。

**drop** _PROJECT_
> 删除本地项目缓存。

**list**
> 列出已下载的流水线项目。

**-resume** [_SESSION_]
> 从缓存结果恢复执行；可选指定会话 ID。

**-with-docker** [_IMAGE_]
> 启用 Docker 容器执行。

**-with-podman** [_IMAGE_]
> 启用 Podman 容器执行。

**-with-singularity** [_IMAGE_]
> 启用 Singularity 容器执行。

**-with-conda** [_ENV_]
> 启用 Conda 环境管理。

**-profile** _NAME_
> 选择 nextflow.config 中定义的配置 profile。

**-c** _FILE_, **-config** _FILE_
> 使用替代的配置文件。

**-params-file** _FILE_
> 从 JSON/YAML 文件加载流水线参数。

**-w** _DIR_, **-work-dir** _DIR_
> 存放中间任务文件的目录（默认：./work）。

**-with-report** [_FILE_]
> 生成 HTML 执行报告。

**-with-timeline** [_FILE_]
> 生成时间线 HTML 文件。

**-with-trace** [_FILE_]
> 生成执行跟踪文件。

**-with-dag** [_FILE_]
> 生成工作流 DAG 图。

**-bg**
> 在后台运行。

**-r** _REV_
> 使用指定的 Git 版本/分支/标签。

**-h**, **-help**
> 显示帮助信息。

# DESCRIPTION

**nextflow** 是一个响应式工作流框架和 DSL，用于编写数据密集型计算流水线。它通过由数据流通道连接的隔离进程，实现并行与分布式流水线的快速组装。

Nextflow 将执行方式与流水线逻辑解耦，使同一工作流可以在本地、HPC 集群（SLURM、SGE、PBS、LSF）或云平台（AWS Batch、Azure Batch、Google Cloud、Kubernetes）上运行。它内置对容器（Docker、Singularity、Podman）和包管理器（Conda）的支持，并利用内容寻址缓存安全地恢复失败的运行。

# CAVEATS

需要 Java 11 或更高版本。工作流脚本采用基于 Groovy 的 DSL（DSL2 是当前标准）。**work** 目录可能随多次运行不断增大；请使用 `nextflow clean` 回收空间。从 GitHub 拉取的流水线缓存在 `~/.nextflow/assets/` 中。

# HISTORY

Nextflow 由 **Paolo Di Tommaso** 在巴塞罗那 **基因组调控中心（CRG）** 创建，于 **2013 年**首次公开发布。它的设计目标是在生物信息学领域实现可复现、可扩展的科学工作流。该项目现由 **Seqera Labs** 维护，并支撑着 **nf-core** 社区的精选流水线体系。

# INSTALL

```brew: brew install nextflow```

```nix: nix profile install nixpkgs#nextflow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snakemake](/man/snakemake)(1), [cwl-runner](/man/cwl-runner)(1), [luigi](/man/luigi)(1)
