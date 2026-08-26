# TAGLINE

管理 Azure DevOps CI/CD 管道

# TLDR

**列出项目中的所有管道**

```az pipelines list --project [MyProject]```

**显示**某条管道的**详情**

```az pipelines show --name [MyPipeline] --project [MyProject]```

**创建新的 YAML 管道**

```az pipelines create --name [MyPipeline] --repository [MyRepo] --branch [main] --yml-path [azure-pipelines.yml]```

**运行管道**（排队一次运行）

```az pipelines run --name [MyPipeline] --project [MyProject]```

带参数和变量**运行管道**

```az pipelines run --name [MyPipeline] --parameters [env=prod] --variables [tag=v1]```

**删除管道**

```az pipelines delete --id [pipeline_id] --project [MyProject]```

**列出管道运行记录**

```az pipelines runs list --project [MyProject]```

**显示**某次管道运行的**详情**

```az pipelines runs show --id [run_id] --project [MyProject]```

# SYNOPSIS

**az** **pipelines** _subcommand_ [_options_]

# SUBCOMMANDS

**list**
> 列出管道。

**show**
> 显示管道详情。

**create**
> 创建管道。

**delete**
> 删除管道。

**run**
> 排队（运行）一条管道。

**update**
> 更新管道。

**runs**
> 管理管道运行（list、show、artifact、tag）。

**build**
> 管理构建和构建定义。

**release**
> 管理发布和发布定义。

**variable**
> 管理管道变量。

**variable-group**
> 管理变量组。

**folder**
> 管理用于组织管道的文件夹。

**agent**
> 管理代理。

**pool**
> 管理代理池。

**queue**
> 管理代理队列。

# PARAMETERS

**--org**, **--organization**
> Azure DevOps 组织 URL，例如 `https://dev.azure.com/MyOrg/`。除非已通过 **az devops configure -d organization=URL** 设为默认值，或可从本地 git 配置中检测到，否则必填。

**--project**, **-p**
> 项目名称或 ID。除非已通过 **az devops configure -d project=NAME** 设为默认值，否则必填。

**--detect**
> 从本地 git 上下文自动检测组织。接受 **true** 或 **false**。

# DESCRIPTION

**az pipelines** 管理 Azure Pipelines，即 Azure DevOps 中的 CI/CD 服务。它提供创建、运行和管理 YAML 管道、构建与发布的命令，也管理代理、代理池、队列、变量和变量组。

此命令组是 **azure-devops** 扩展的一部分，适用于 Azure DevOps Services。

# CAVEATS

属于 **azure-devops** 扩展（需要 Azure CLI 2.30.0 或更高版本）。首次运行 **az pipelines** 命令时会自动安装该扩展，也可以用 **az extension add --name azure-devops** 手动安装。使用 **az devops configure -d organization=URL project=NAME** 设置持久默认值，避免重复输入 **--org** 和 **--project**。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[azure-cli](/man/azure-cli)(1), [az-devops](/man/az-devops)(1), [az-repos](/man/az-repos)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-devops-cli-extension)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/pipelines)```

```[Homepage](https://learn.microsoft.com/en-us/cli/azure/)```

<!-- verified: 2026-06-19 -->
