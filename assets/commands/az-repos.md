# TAGLINE

管理 Azure DevOps Git 仓库和拉取请求

# TLDR

**列出项目中的所有仓库**

```az repos list --project [MyProject]```

**显示**某个仓库的**详情**

```az repos show --repository [MyRepo] --project [MyProject]```

**创建新仓库**

```az repos create --name [MyRepo] --project [MyProject]```

**获取仓库的克隆 URL**

```az repos show --repository [MyRepo] --project [MyProject] --query remoteUrl```

**删除仓库**

```az repos delete --id [repo_id] --project [MyProject]```

**列出拉取请求**

```az repos pr list --project [MyProject]```

**创建拉取请求**

```az repos pr create --repository [MyRepo] --source-branch [feature] --target-branch [main] --title [My PR]```

**显示拉取请求详情**

```az repos pr show --id [pr_id]```

**完成（合并）拉取请求**

```az repos pr update --id [pr_id] --status completed```

# SYNOPSIS

**az** **repos** _subcommand_ [_options_]

# SUBCOMMANDS

**list**
> 列出仓库。

**show**
> 显示仓库详情。

**create**
> 创建仓库。

**delete**
> 删除仓库。

**update**
> 更新仓库。

**pr list**
> 列出拉取请求。

**pr create**
> 创建拉取请求。

**pr show**
> 获取拉取请求的详情。

**pr update**
> 更新拉取请求（设置标题、描述、状态；通过 --status completed 完成）。

**pr checkout**
> 在本地检出 PR 的源分支。

**pr set-vote**
> 对拉取请求投票（approve、reject 等）。

**pr reviewer**
> 添加、列出或移除拉取请求的评审者。

**pr work-item**
> 将工作项与拉取请求关联或取消关联。

**policy**
> 管理分支策略（approver-count、build、comment-required 等）。

**ref**
> 管理 Git 引用（create、delete、list、lock、unlock）。

**import create**
> 创建 Git 导入请求。

# PARAMETERS

**--org**, **--organization**
> Azure DevOps 组织 URL，例如 `https://dev.azure.com/MyOrg/`。除非已通过 **az devops configure -d organization=URL** 设为默认值，或可从本地 git 配置中检测到，否则必填。

**--project**, **-p**
> 项目名称或 ID。除非已通过 **az devops configure -d project=NAME** 设为默认值，否则必填。

**--repository**, **-r**
> 仓库名称或 ID。

**--detect**
> 从本地 git 上下文自动检测组织。接受 **true** 或 **false**。

# DESCRIPTION

**az repos** 管理 Azure Repos，即 Azure DevOps 中的 Git 仓库托管服务。它提供管理仓库、拉取请求、引用、分支策略和仓库导入的命令。

此命令组是 **azure-devops** 扩展的一部分，适用于 Azure DevOps Services。

# CAVEATS

属于 **azure-devops** 扩展（需要 Azure CLI 2.30.0 或更高版本）。首次运行 **az repos** 命令时会自动安装该扩展，也可以用 **az extension add --name azure-devops** 手动安装。使用 **az devops configure -d organization=URL project=NAME** 设置持久默认值，避免重复输入 **--org** 和 **--project**。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[azure-cli](/man/azure-cli)(1), [az-devops](/man/az-devops)(1), [az-pipelines](/man/az-pipelines)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-devops-cli-extension)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/repos)```

```[Homepage](https://learn.microsoft.com/en-us/cli/azure/)```

<!-- verified: 2026-06-19 -->
