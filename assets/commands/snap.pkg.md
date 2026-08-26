# TAGLINE

管理沙箱化的 snap 软件包

# TLDR

**搜索**软件包

```snap find [query]```

**安装**软件包

```snap install [package]```

**更新**软件包

```snap refresh [package]```

更新到特定**通道**

```snap refresh [package] --channel=[channel]```

更新**所有软件包**

```snap refresh```

**列出**已安装的 snap

```snap list```

**移除**软件包

```snap remove [package]```

查看最近的**变更**

```snap changes```

# SYNOPSIS

**snap** _command_ [_OPTIONS_]

# PARAMETERS

**find** _query_
> 在商店中搜索 snap

**install** _package_
> 安装一个 snap 软件包

**remove** _package_
> 卸载一个 snap 软件包

**refresh** [_package_]
> 将 snap 更新到最新版本

**list**
> 显示已安装的 snap

**info** _package_
> 显示 snap 的详细信息

**changes**
> 列出最近的系统变更

**revert** _package_
> 将 snap 回退到之前的版本

**enable** _package_
> 启用被禁用的 snap

**disable** _package_
> 禁用一个 snap

**services**
> 查询服务状态

**start/stop/restart** _service_
> 控制 snap 服务

**connect** _plug_ _slot_
> 连接接口

**disconnect** _plug_ _slot_
> 断开接口连接

**--channel** _channel_
> 指定通道（stable、candidate、beta、edge）

**--classic**
> 允许 classic 沙箱模式

**--devmode**
> 启用开发模式

# DESCRIPTION

**snap** 是 Snap 软件包的包管理器。Snap 是自包含的应用程序，可跨 Linux 发行版使用。Snap 包含全部依赖，并在沙箱环境中运行以实现安全隔离。

Snap 商店提供数千个应用程序，包括浏览器、开发工具和服务器软件。Snap 在后台自动更新，必要时可以回滚到之前的版本。

# CAVEATS

需要 snapd 守护进程处于运行状态。由于捆绑依赖，Snap 可能比原生软件包占用更多磁盘空间。Classic 沙箱模式会绕过沙箱限制。部分发行版已移除或禁用了 snap 支持。

# HISTORY

**Snap** 由 **Canonical** 开发，随 **2016 年**的 Ubuntu 16.04 一同推出。其设计目标是提供具备自动更新、安全沙箱和跨发行版兼容性的通用 Linux 打包方案。该技术建立在 Ubuntu Touch click 软件包的早期工作之上。

# SEE ALSO

[snapd](/man/snapd)(8), [flatpak](/man/flatpak)(1), [apt](/man/apt)(8)
