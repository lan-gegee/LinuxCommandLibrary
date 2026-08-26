# TAGLINE

用于工作流开发的 Databricks CLI 扩展

# TLDR

**在当前目录配置新的 dbx 项目**

```dbx configure --profile [DEFAULT]```

**将工作流部署**到工件存储

```dbx deploy [workflow_name]```

**启动已部署的工作流**

```dbx launch [workflow_name]```

**在交互式集群上执行工作流**（无需部署）

```dbx execute [workflow_name] --cluster-name=[cluster]```

**将本地文件同步到 DBFS**并监视变更

```dbx sync dbfs --source [path/to/directory] --dest [path/to/remote_directory]```

# SYNOPSIS

**dbx** _command_ [_options_]

# PARAMETERS

**configure**
> 配置当前目录中的项目。

**init**
> 从模板生成新的项目骨架。

**deploy** _workflow_
> 将工作流定义及其工件部署到 Databricks 工作区。

**launch** _workflow_
> 以作业运行的方式启动先前部署的工作流。

**execute** _workflow_
> 直接在交互式（通用）集群上运行工作流代码。

**sync**
> 将本地文件同步到 DBFS 或仓库，可选择监视变更。

**destroy**
> 删除已定义的工作流，并可选删除其资产。

**--profile** _PROFILE_
> 要使用的 Databricks CLI 连接配置文件。

**--environment** _ENV_
> 部署文件中定义的项目环境（默认：default）。

# DESCRIPTION

**dbx**（Databricks CLI eXtensions）是 Databricks Labs 的一个工具，它为 databricks CLI 扩展了快速开发和 CI/CD Databricks 工作流的功能。它管理作业、工作流及其工件在多个环境和工作区之间的部署。

项目由部署文件（deployment.yml）描述，其中定义了工作流、集群配置和依赖项。dbx 会对工件进行版本管理并上传，然后创建或更新对应的 Databricks 作业，因此适合自动化流水线。

身份验证复用 databricks CLI 的配置文件（~/.databrickscfg），因此 dbx 可以对该文件中配置的任何工作区进行操作。

# CAVEATS

dbx 已被 Databricks 停用；推荐改用 Databricks Asset Bundles（新版 Databricks CLI 中的 `databricks bundle` 命令）。通过 pip 安装（`pip install dbx`），需要 Python 以及已配置好的 Databricks 身份验证配置文件。

# HISTORY

dbx 由 Databricks Labs 开发，名称是 "Databricks CLI eXtensions" 的缩写，在 Databricks Asset Bundles 正式可用之前填补了 CI/CD 方面的空缺。后来随着第一方工具的推出，它被弃用。

# INSTALL

```nix: nix profile install nixpkgs#dbx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [python](/man/python)(1)

# RESOURCES

```[Source code](https://github.com/databrickslabs/dbx)```

```[Documentation](https://dbx.readthedocs.io)```

<!-- verified: 2026-07-11 -->
