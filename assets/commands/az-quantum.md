# TAGLINE

管理 Azure Quantum 工作区和作业

# TLDR

在某个位置**列出可用的量子提供程序**

```az quantum offerings list --location [eastus]```

**创建量子工作区**

```az quantum workspace create --name [MyWorkspace] --resource-group [MyResourceGroup] --location [eastus] --storage-account [MyStorageAccount]```

**列出量子工作区**

```az quantum workspace list --resource-group [MyResourceGroup]```

为后续命令**设置默认工作区**

```az quantum workspace set --resource-group [MyResourceGroup] --workspace-name [MyWorkspace] --location [eastus]```

**提交量子作业**

```az quantum job submit --resource-group [MyResourceGroup] --workspace-name [MyWorkspace] --target-id [ionq.simulator] --job-name [MyJob] --job-input-file [circuit.json] --job-input-format [ionq.circuit.v1]```

**提交作业并等待**结果

```az quantum run --resource-group [MyResourceGroup] --workspace-name [MyWorkspace] --target-id [ionq.simulator] --job-input-file [circuit.json] --job-input-format [ionq.circuit.v1]```

**列出量子作业**

```az quantum job list```

**显示作业状态**

```az quantum job show --job-id [job_id]```

# SYNOPSIS

**az** **quantum** _subcommand_ [_options_]

# SUBCOMMANDS

**workspace create**
> 创建新的 Azure Quantum 工作区。

**workspace list**
> 列出可用的 Azure Quantum 工作区。

**workspace set**
> 为后续命令选择默认工作区。

**workspace show**
> 显示给定（或当前）工作区的详情。

**workspace delete**
> 删除量子工作区。

**workspace quotas**
> 列出工作区的配额。

**workspace keys**
> 列出或重新生成工作区的 API 密钥。

**offerings list**
> 列出某个位置所有可用的提供程序产品。

**offerings accept-terms**
> 在使用某个提供程序和 SKU 之前接受其条款。

**job submit**
> 提交要在 Azure Quantum 上运行的程序或线路。

**job list**
> 列出工作区中的作业。

**job show**
> 获取作业的状态和详情。

**job output**
> 获取已完成的作业的结果。

**job wait**
> 等待作业运行结束。

**run**, **execute**
> 提交作业并等待结果（等价命令）。

**target list**
> 列出工作区中的提供程序及其目标。

**target set**
> 选择用于提交作业的默认目标。

# PARAMETERS

**--resource-group**, **-g**
> 资源组的名称。可用 **az configure --defaults group=NAME** 配置默认值。

**--workspace-name**, **-w**
> Quantum 工作区的名称。可用 **az quantum workspace set** 配置默认值。

**--target-id**, **-t**
> 作业的执行引擎（目标），例如 `ionq.simulator`。可用 **az quantum target set** 配置默认值。

**--job-input-file**
> 要提交的程序或线路文件的路径。

**--job-input-format**
> 输入文件的格式，例如 `ionq.circuit.v1` 或 `qir.v1`。

# DESCRIPTION

**az quantum** 管理 Azure Quantum 资源，这些资源提供对来自多家提供商的量子计算硬件和模拟器的访问。Azure Quantum 支持多个提供商，包括 IonQ、Quantinuum、Rigetti 以及 Microsoft 的模拟器。

工作区是管理量子作业、目标和提供商访问的顶层资源。设置默认工作区和目标可以避免在每条命令上重复输入 **--workspace-name** 和 **--target-id**。

# CAVEATS

此命令组处于**预览**阶段。属于 **quantum** 扩展（需要 Azure CLI 2.73.0 或更高版本）；首次运行 **az quantum** 命令时会自动安装，也可以用 **az extension add --name quantum** 手动安装。量子服务存在区域可用性限制，且作业成本因提供商和目标而异，差异很大。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[azure-cli](/man/azure-cli)(1), [az](/man/az)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/quantum)```

```[Homepage](https://learn.microsoft.com/en-us/cli/azure/)```

<!-- verified: 2026-06-19 -->
