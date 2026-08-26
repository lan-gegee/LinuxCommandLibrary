# TAGLINE

管理 macOS 上的 launchd 服务

# TLDR

**列出已加载的服务**

```launchctl list```

**加载服务**

```launchctl load [/path/to/service.plist]```

**卸载服务**

```launchctl unload [/path/to/service.plist]```

**启动服务**

```launchctl start [com.example.service]```

**停止服务**

```launchctl stop [com.example.service]```

**引导注册服务**（bootstrap，load 的现代替代）

```sudo launchctl bootstrap gui/[uid] [/path/to/service.plist]```

**注销移除服务**（bootout，unload 的现代替代）

```sudo launchctl bootout gui/[uid]/[com.example.service]```

**打印服务信息**

```launchctl print gui/[uid]/[com.example.service]```

# SYNOPSIS

**launchctl** _subcommand_ [_options_]

# DESCRIPTION

**launchctl** 用于管理 macOS 上的 launchd 服务。它控制系统和用户的守护进程，负责处理服务的生命周期、调度和资源限制。

该工具在 macOS 上取代了传统的 init 脚本，通过属性列表（plist）文件来定义服务。

# PARAMETERS

**list**
> 列出已加载的服务。

**load** _plist_
> 加载服务（已弃用）。

**unload** _plist_
> 卸载服务（已弃用）。

**start** _label_
> 启动服务。

**stop** _label_
> 停止服务。

**bootstrap** _domain_ _plist_
> 加载服务（现代方式）。

**bootout** _domain_ _plist_
> 卸载服务（现代方式）。

**print** _target_
> 打印服务信息。

**kickstart** _target_
> 强制启动服务。

**enable** _service_
> 启用服务。

**disable** _service_
> 禁用服务。

**blame** _target_
> 打印服务被加载/启动的原因。

**dumpstate**
> 将 launchd 的状态转储到标准输出。

# CAVEATS

仅限 macOS。**load/unload** 子命令自 macOS 10.10 起已弃用；请改用 **bootstrap/bootout**。系统服务需要 root 权限。GUI 服务使用用户域（gui/UID）。

# HISTORY

**launchctl** 是 **launchd** 的组成部分，由 **Apple** 于 **Mac OS X 10.4 Tiger**（2005 年）引入。它取代了传统的 init、xinetd 和 cron 系统，统一了守护进程的管理。Dave Zarzycki 主导了它的开发。

# SEE ALSO

[systemctl](/man/systemctl)(1)
