# TAGLINE

管理 Azure 虚拟机

# TLDR

**创建**虚拟机

```az vm create --resource-group [MyRG] --name [MyVM] --image [Ubuntu2204]```

**列出**VM

```az vm list```

**启动**VM

```az vm start --resource-group [MyRG] --name [MyVM]```

**停止**VM

```az vm stop --resource-group [MyRG] --name [MyVM]```

**解除分配**VM（停止计算计费）

```az vm deallocate --resource-group [MyRG] --name [MyVM]```

**删除**VM

```az vm delete --resource-group [MyRG] --name [MyVM]```

**获取** VM 详情

```az vm show --resource-group [MyRG] --name [MyVM]```

# SYNOPSIS

**az vm** _command_ [_options_]

# DESCRIPTION

**az vm** 管理 Azure 虚拟机。它提供创建、启动、停止、配置和删除 VM 的命令，还可管理磁盘、网络接口和扩展。

该命令组支持对 Azure 计算资源进行全面的生命周期管理。

# PARAMETERS

**create**
> 创建新的虚拟机

**list**
> 列出虚拟机

**start**
> 启动 VM

**stop**
> 停止 VM（仍会产生计算费用）

**deallocate**
> 解除分配 VM（停止计算计费）

**restart**
> 重启 VM

**delete**
> 删除 VM

**show**
> 获取 VM 详情

**--resource-group**, **-g** _name_
> 资源组名称

**--name**, **-n** _name_
> VM 名称

**--image**
> 操作系统镜像（Ubuntu2204、Win2022Datacenter 等）

**--size**
> VM 大小（Standard_B2s、Standard_D2s_v3 等）

**--admin-username**
> 管理员用户名

**--admin-password**
> 管理员密码

**--ssh-key-values**
> SSH 公钥（一个或多个）

# COMMON OPERATIONS

```bash
# Create Ubuntu VM with SSH key
az vm create -g MyRG -n MyVM --image Ubuntu2204 --ssh-key-values ~/.ssh/id_rsa.pub

# Get VM IP address
az vm show -g MyRG -n MyVM -d --query publicIps -o tsv

# Resize VM
az vm resize -g MyRG -n MyVM --size Standard_D4s_v3

# Run command on VM
az vm run-command invoke -g MyRG -n MyVM --command-id RunShellScript --scripts "apt-get update"
```

# CAVEATS

创建 VM 会产生费用。**az vm stop** 并不会解除分配——请使用 **az vm deallocate** 停止计算计费。某些 VM 大小并非在所有区域都可用。默认情况下，删除 VM 不会删除关联的资源（磁盘、NIC）。**UbuntuLTS** 镜像别名已于 2023 年弃用；请改用 **Ubuntu2204** 或类似别名。

# HISTORY

**az vm** 自 **2017** 年的 Azure CLI 2.0 版本起就是其一部分，提供全面的 VM 管理能力。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-group](/man/az-group)(1), [az-network](/man/az-network)(1)
