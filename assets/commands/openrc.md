# TAGLINE

基于 OpenRC 的系统的服务管理器，是 systemd 之外的另一种选择

# TLDR

切换到**特定 runlevel**

```sudo openrc [runlevel_name]```

切换 runlevel 但**不停止任何现有服务**

```sudo openrc -n [runlevel_name]```

# SYNOPSIS

**openrc** [_options_] [_runlevel_]

# PARAMETERS

**-n, --no-stop**
> 更改 runlevel 时不停止任何服务

**-o, --override**
> 覆盖离开单用户模式时要进入的下一个 runlevel

**-s, --service**
> 运行由其余参数指定的服务

**-S, --sys**
> 如同位于 /etc/init.d 中一样运行服务

# DESCRIPTION

**openrc** 是基于 OpenRC 的系统的服务管理器，为管理系统服务和 runlevel 提供了 systemd 之外的另一种选择。它是 Gentoo、Alpine Linux 及其他发行版的默认 init 系统。

OpenRC 使用 runlevel（运行级别）的概念（类似于 SysV init）来组织应当一起运行的服务。常见的 runlevel 包括 **default**（正常运行）、**boot**（必要服务）、**single**（单用户模式）和 **shutdown**。

服务通过 **/etc/init.d/** 中的脚本管理，并使用 **rc-update** 将其加入或移出 runlevel。

# CAVEATS

更改 runlevel 时可能会停止当前 runlevel 中不存在于目标 runlevel 的服务。使用 **-n** 可保留正在运行的服务。OpenRC 与 systemd 不兼容；发行版会在二者中选择其一。

# INSTALL

```apt: sudo apt install openrc```

```apk: sudo apk add openrc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rc-status](/man/rc-status)(8), [rc-update](/man/rc-update)(8), [rc-service](/man/rc-service)(8)
