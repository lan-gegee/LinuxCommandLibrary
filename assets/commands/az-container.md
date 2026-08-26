# TAGLINE

管理 Azure 容器实例

# TLDR

**创建容器实例**

```az container create -g [resource-group] --name [container-name] --image [image:tag] --cpu [1] --memory [1]```

使用公共 IP 和 DNS 名称**创建**

```az container create -g [resource-group] --name [container-name] --image [image:tag] --ports [80] --dns-name-label [myapp]```

**列出资源组中的容器组**

```az container list -g [resource-group]```

**查看容器日志**

```az container logs -g [resource-group] --name [container-name]```

在运行中的容器内**执行命令**

```az container exec -g [resource-group] --name [container-name] --exec-command "[/bin/bash]"```

**显示容器详情**

```az container show -g [resource-group] --name [container-name]```

**停止容器组**

```az container stop -g [resource-group] --name [container-name]```

**删除容器组**

```az container delete -g [resource-group] --name [container-name]```

# SYNOPSIS

**az container** _subcommand_ [_options_]

# DESCRIPTION

**az container** 管理 Azure 容器实例（ACI），它是在 Azure 中运行容器的最快方式，无需管理虚拟机或引入编排服务。

ACI 适用于隔离容器、简单应用、任务自动化和构建作业。需要完整容器编排的场景请使用 Azure Kubernetes Service（AKS）。

# SUBCOMMANDS

**Lifecycle**
> create, delete, start, stop, restart

**Information**
> show, list, logs

**Interaction**
> attach, exec, export

**Profiles**
> container-group-profile create, container-group-profile delete, container-group-profile list

# PARAMETERS

**-g, --resource-group** _value_
> 资源组的名称

**--name** _value_
> 容器组的名称

**--image** _value_
> 容器镜像（例如 nginx:latest）

**--cpu** _value_
> CPU 核心数（默认：1）

**--memory** _value_
> 内存大小，以 GB 为单位（默认：1.5）

**--ports** _value_
> 要打开的端口列表，空格分隔

**--dns-name-label** _value_
> 公共 IP 的 DNS 名称标签

**--os-type** _value_
> 操作系统类型：Linux 或 Windows（默认：Linux）

**--ip-address** _value_
> IP 地址类型：Public 或 Private

**--restart-policy** _value_
> 重启策略：Always、OnFailure 或 Never（默认：Always）

**-e**, **--environment-variables** _key=value_
> 环境变量（空格分隔的 key=value 对）

**--secure-environment-variables** _key=value_
> 安全环境变量（不会显示在日志或门户中）

**--registry-login-server** _value_
> 私有容器注册表的登录服务器

# CAVEATS

带公共 IP 的容器组即使停止也会计费；请删除以免产生费用。Windows 容器支持的镜像有限且资源需求更高。包含机密信息的环境变量应使用安全值。每个区域和订阅都有最大资源限制。

# HISTORY

Azure 容器实例于 **2017** 年 **7 月**推出，是所有公有云中首个无服务器容器服务。它让运行容器无需管理基础设施，填补了虚拟机与完整编排平台之间的空白。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-aks](/man/az-aks)(1), [docker](/man/docker)(1)
