# TAGLINE

在 Linux 上运行 Android 应用程序

# TLDR

启动 Anbox 并进入**应用管理器**

```anbox launch --package=org.anbox.appmgr --component=org.anbox.appmgr.AppViewActivity```

# SYNOPSIS

**anbox** [_command_] [_options_]

# DESCRIPTION

**anbox** 可以在任何 Linux 操作系统上运行 Android 应用。它将 Android 操作系统放入容器中，抽象硬件访问，并将核心系统服务集成到 Linux 环境中。

# PARAMETERS

**launch**
> 启动一个 Android 应用

**session-manager**
> 启动会话管理器，负责运行 Android 容器和图形栈

**container-manager**
> 启动特权容器管理器（通常作为系统服务运行）

**system-info**
> 打印主机系统和 Anbox 配置的相关信息

**--package**
> 指定要启动的 Android 软件包名称

**--component**
> 指定要启动的组件/Activity

# CAVEATS

Anbox 需要内核模块（ashmem、binder）以及配置正确的容器环境。由于缺少 Google Play 服务，并非所有 Android 应用都兼容。上游项目已于 2024 年 2 月归档且不再维护；桌面 Linux 推荐使用继任者 Waydroid。

# HISTORY

Anbox（Android in a Box）是一个开源兼容层，让 Android 应用可以在 Linux 上运行。开发始于 **2017** 年前后，作为 Android 模拟器的替代方案。该项目于 **2024 年 2 月 13 日**归档为只读状态。

# SEE ALSO

[waydroid](/man/waydroid)(1), [lxc](/man/lxc)(1)

# RESOURCES

```[Source code](https://github.com/anbox/anbox)```

```[Homepage](https://anbox.io)```

<!-- verified: 2026-06-11 -->
