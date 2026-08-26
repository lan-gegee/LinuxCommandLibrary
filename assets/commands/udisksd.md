# TAGLINE

存储设备管理 D-Bus 守护进程

# TLDR

**守护进程由 D-Bus 或 systemd 自动启动**

```udisksd```

**以调试输出运行**

```udisksd --debug```

**运行时不替换已有实例**

```udisksd --no-replace```

**在不支持 LUKS 的情况下运行**

```udisksd --no-cryptsetup```

# SYNOPSIS

**udisksd** [_options_]

# PARAMETERS

**--debug**
> 启用调试输出。

**--no-replace**
> 不替换已存在的守护进程实例。

**--no-cryptsetup**
> 禁用 LUKS 加密卷支持。

**--no-sigint**
> 收到 SIGINT 时退出（调试时禁用此行为）。

**--force-load-modules**
> 即使不需要也加载内核模块。

**-h**, **--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**udisksd** 是 udisks2 的系统守护进程，提供用于管理存储设备的 D-Bus 接口。它处理挂载、卸载、格式化、分区以及 LUKS 加密操作，无需为每个动作单独获取 root 权限。

该守护进程监视 udev 事件以跟踪设备变化，并通过 org.freedesktop.UDisks2 D-Bus 接口暴露设备信息。桌面环境和应用程序都使用该接口进行存储管理。

用户不应手动启动 udisksd；当应用程序访问其接口时，它会被 D-Bus 或 systemd 自动激活。访问控制使用 polkit，允许已登录的用户管理其会话所在 seat 上的设备。

# CAVEATS

访问控制依赖 polkit。自动挂载取决于桌面环境的集成程度。调试模式会产生大量输出。某些功能需要特定的内核模块。

# HISTORY

**udisksd** 由最初的 udisks 项目（DeviceKit-disks）演化而来，该项目为现代 Linux 桌面存储管理而创建。udisks2 重写版改进了 API 并增加了 LUKS 支持等特性。它如今作为 storaged 项目的一部分维护，是大多数 Linux 桌面环境的核心组件。

# SEE ALSO

[udisksctl](/man/udisksctl)(1), [polkit](/man/polkit)(8), [mount](/man/mount)(8), [udevadm](/man/udevadm)(8)
