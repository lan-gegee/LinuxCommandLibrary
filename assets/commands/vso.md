# TAGLINE

Vanilla OS 系统运维工具

# TLDR

检查**更新**

```vso sys-upgrade check```

立即**升级**系统

```vso sys-upgrade upgrade --now```

初始化 **Pico** 子系统

```vso pico-init```

**安装**应用

```vso install [package1] [package2]```

**移除**应用

```vso remove [package1] [package2]```

进入子系统 **Shell**

```vso shell```

**运行**应用

```vso run [package]```

显示**配置**

```vso config show```

# SYNOPSIS

**vso** _COMMAND_ [_OPTIONS_]

# COMMANDS

**sys-upgrade check**
> 检查系统更新

**sys-upgrade upgrade**
> 升级系统

**pico-init**
> 初始化 Pico 子系统

**install**
> 在子系统中安装应用

**remove**
> 从子系统中移除应用

**shell**
> 进入子系统 Shell

**run**
> 运行子系统中的应用

**export**
> 将已安装的应用导出为桌面入口

**unexport**
> 移除已导出的桌面入口

**config show**
> 显示配置

**help**
> 显示某个命令的帮助

# PARAMETERS

**--now**
> 立即执行系统升级，不进行调度

**-h**, **--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**vso**（Vanilla System Operator）是 Vanilla OS 的软件包管理器、系统更新器和任务自动化工具。它管理不可变的宿主系统以及一个可变的 Pico 子系统用于软件包安装。

该子系统提供了一个类似容器的环境，可以在不改动基础系统的情况下安装传统软件包。

# CAVEATS

仅适用于 Vanilla OS。执行软件包操作前必须先初始化子系统。系统升级可能需要重启。

# SEE ALSO

[apx](/man/apx)(1), [flatpak](/man/flatpak)(1), [snap](/man/snap)(1)
