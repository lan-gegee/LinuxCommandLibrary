# TAGLINE

访问 Azure 虚拟机的串行控制台

# TLDR

**连接到 VM 的串行控制台**

```az serial-console connect --name [MyVM] --resource-group [MyResourceGroup]```

**连接到 VMSS 实例**

```az serial-console connect --name [MyVMSS] --resource-group [MyResourceGroup] --instance-id [2]```

**为整个订阅启用串行控制台**

```az serial-console enable```

**为整个订阅禁用串行控制台**

```az serial-console disable```

**向 VM 发送 NMI**（不可屏蔽中断）

```az serial-console send nmi --name [MyVM] --resource-group [MyResourceGroup]```

**向 VM 发送 SysRq 序列**

```az serial-console send sysrq --input [b] --name [MyVM] --resource-group [MyResourceGroup]```

**硬重置 VM**

```az serial-console send reset --name [MyVM] --resource-group [MyResourceGroup]```

# SYNOPSIS

**az** **serial-console** _subcommand_ [_options_]

# SUBCOMMANDS

**connect**
> 连接到 VM 或 VMSS 实例的串行控制台。

**enable**
> 为整个订阅启用串行控制台服务。

**disable**
> 为整个订阅禁用串行控制台服务。

**send nmi**
> 向 VM 或 VMSS 实例发送不可屏蔽中断（NMI）。

**send sysrq**
> 向 VM 或 VMSS 实例发送 SysRq 序列。

**send reset**
> 对 VM 或 VMSS 实例执行"硬"重启。

# PARAMETERS

**--name** **-n**
> 虚拟机或虚拟机规模集的名称。

**--resource-group** **-g**
> 资源组的名称。

**--instance-id**
> VMSS 实例的 ID。连接单个虚拟机时不需要。

# DESCRIPTION

**az serial-console** 提供对 Azure Linux 和 Windows VM 以及 VMSS 实例基于文本的串行控制台访问，用于故障排查。连接会附加到 ttyS0 串行端口，不依赖网络连通性和操作系统状态即可工作。

这在调试启动问题、网络配置错误，或 VM 无法通过 SSH 或 RDP 访问时非常有用。连接期间，先输入 **Ctrl + ]** 再输入 **q** 即可退出；输入 **n**、**s** 或 **r** 可分别发送 NMI、SysRq 或执行重置。

# CAVEATS

属于 **serial-console** 扩展（要求 Azure CLI 2.15.0 或更高版本）；首次运行 **az serial-console** 命令时会自动安装，也可用 **az extension add --name serial-console** 手动安装。串行控制台访问要求 VM 已启用启动诊断，并且你具备相应的 RBAC 权限。**enable** 和 **disable** 命令作用于整个订阅的服务，而非单个 VM。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[azure-cli](/man/azure-cli)(1), [az-vm](/man/az-vm)(1), [ssh](/man/ssh)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/serial-console)```

```[Homepage](https://learn.microsoft.com/en-us/cli/azure/)```

<!-- verified: 2026-06-19 -->
