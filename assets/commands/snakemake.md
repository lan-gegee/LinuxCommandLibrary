# TAGLINE

可重现的工作流管理系统

# TLDR

从 Snakefile **运行工作流**

```snakemake```

先**试运行**，只显示计划执行的内容而不实际运行

```snakemake -n```

以指定的核心数**运行**

```snakemake --cores [4]```

**构建特定目标**

```snakemake [target_file]```

连同 shell 命令一起**显示执行计划**

```snakemake -n -p```

**生成工作流的 DAG 可视化图**

```snakemake --dag | dot -Tpng > dag.png```

**使用指定的 Snakefile 运行**

```snakemake --snakefile [path/to/Snakefile]```

**强制重新执行**所有 rule

```snakemake --forceall```

# SYNOPSIS

**snakemake** [_options_] [_targets_]

# PARAMETERS

**-n**, **--dry-run**
> 显示执行计划而不实际运行任何作业。

**-p**, **--printshellcmds**
> 打印将要执行的 shell 命令。

**--cores**, **-c** _N_
> 最多并行使用 N 个 CPU 核心。省略 N 时使用所有可用核心。

**-s**, **--snakefile** _FILE_
> 指定 Snakefile。默认：当前目录下的 Snakefile。

**-d**, **--directory** _DIR_
> 在指定目录中执行工作流。

**--forceall**, **-F**
> 强制重新执行所有 rule。

**--forcerun**, **-R** _rules_
> 强制重新执行指定的 rule。

**--until**, **-U** _rules_
> 只执行到指定 rule 为止。

**--dag**
> 以 DOT 格式输出作业的有向无环图。

**--rulegraph**
> 以 DOT 格式输出 rule 的依赖图。

**--config** _key=value_
> 设置或覆盖配置值。

**--configfile** _FILE_
> 指定 YAML 或 JSON 格式的配置文件。

**--profile** _PROFILE_
> 使用工作流 profile 来设定执行参数。

**--cluster** _CMD_
> 使用给定的提交命令在集群上执行作业。

**--use-conda**
> 使用 rule 中定义的 conda 环境。

**--use-singularity**
> 使用 rule 中定义的 Singularity 容器。

**-q**, **--quiet**
> 抑制除警告和错误之外的输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Snakemake** 是一个工作流管理系统，用于创建可重现、可扩展的数据分析。工作流通过基于 Python 的领域专用语言定义在称为"Snakefile"的文件中，其中描述了将输入文件转换为输出文件的 rule。

Snakemake 根据文件依赖关系构建作业的有向无环图（DAG），自动确定执行顺序。只有在输入文件比输出文件新时才重新执行 rule，避免冗余计算。工作流无需修改即可从单台工作站无缝扩展到集群和云环境。

该工具能够处理包含大量相互依赖步骤的复杂流水线，因此在生物信息学和数据科学领域尤为流行。它支持 conda 环境、容器（Docker/Singularity）以及多种集群执行后端。

# CAVEATS

需要 Python 3.7+。Snakefile 必须是合法的 Python 语法。使用 **--cores** 且不带数字时会占用所有可用核心，可能影响系统响应速度。集群执行需要针对目标调度器进行相应配置。Conda 与容器集成需要单独安装相应工具。

# HISTORY

**Snakemake** 由 Johannes Köster 创建，于 **2012 年**首次发表在 Bioinformatics 期刊上。其名字是对"make"（构建自动化工具）和 Python（"snake"，蛇）的双关。它旨在解决计算生物学工作流中的可重现性难题。项目发展迅速，每年被引用数百次，并与主要生物信息学社区深度集成。目前仍在活跃开发并定期发布版本。

# INSTALL

```brew: brew install snakemake```

```nix: nix profile install nixpkgs#snakemake```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[make](/man/make)(1), [nextflow](/man/nextflow)(1), [dvc](/man/dvc)(1)
