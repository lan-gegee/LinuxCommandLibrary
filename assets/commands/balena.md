# TAGLINE

管理 IoT 设备机群

# TLDR

**登录** Balena Cloud

```balena login```

**列出**设备

```balena devices```

向设备**推送**代码

```balena push [myApp]```

通过 **SSH** 连接设备

```balena ssh [device-uuid]```

**查看**日志

```balena logs [device-uuid]```

创建**新应用**

```balena app create [myApp]```

# SYNOPSIS

**balena** _command_ [_options_]

# DESCRIPTION

**balena** 是 Balena（原 Resin.io）的命令行界面；Balena 是一个用于部署和管理 IoT 设备机群的平台。它支持在边缘设备上构建、部署和监控容器化应用。

该 CLI 提供设备配置、应用部署、远程访问和机群管理等工具。

# PARAMETERS

**login**
> 向 Balena Cloud 认证

**push** _application_
> 将代码部署到应用

**devices**
> 列出设备

**ssh** _device_
> 通过 SSH 连接设备

**logs** _device_
> 查看设备日志

**scan**
> 扫描本地网络中的 Balena 设备

**os**
> 操作系统镜像管理命令

**env**
> 环境变量管理

**--application**, **-a** _name_
> 应用名称

**--device**, **-d** _uuid_
> 设备 UUID

# FEATURES

- 基于容器的部署
- 空中（OTA）更新
- 远程设备访问
- 环境变量管理
- 多架构支持
- 设备机群管理

# WORKFLOW

```bash
# Login
balena login

# Create app
balena app create myApp

# Push code
cd my-project
balena push myApp

# Monitor
balena logs <device>
```

# CAVEATS

需要 Balena 账户。设备必须运行 BalenaOS。云端功能需要联网。部分操作需要付费方案。本地模式可用于离线开发。

# HISTORY

**Balena CLI** 由 Balena（原 Resin.io）自 **2013** 年前后开始开发，是一个面向 IoT 机群管理与边缘计算的平台。

# SEE ALSO

[docker](/man/docker)(1), [kubectl](/man/kubectl)(1)
