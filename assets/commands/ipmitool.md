# TAGLINE

提供智能平台管理接口（IPMI）的命令行界面

# TLDR

显示机箱**电源状态**

```sudo ipmitool chassis status```

远程对服务器执行**开机 / 关机 / 电源循环**

```ipmitool -I lanplus -H [ip] -U [user] -P [pass] chassis power on```

读取全部**传感器**

```sudo ipmitool sensor list```

显示**系统事件日志**（SEL）

```sudo ipmitool sel list```

配置通道 1 上的 **IPMI LAN**

```sudo ipmitool lan print 1```

激活 **Serial-over-LAN** 控制台

```ipmitool -I lanplus -H [ip] -U [user] sol activate```

# SYNOPSIS

**ipmitool** [_options_] _command_

# PARAMETERS

**-H** _HOST_
> 远程主机的 IP 地址或主机名

**-U** _USER_
> 远程用户名

**-P** _PASSWORD_
> 远程密码（或用 -E 从环境变量读取）

**-I** _INTERFACE_
> 接口类型：open、lan、lanplus

**shell**
> 交互式 IPMI shell

**sensor**
> 显示传感器信息

**chassis**
> 机箱相关命令（电源、状态、定位灯）

**lan**
> 配置 LAN 设置

**user**
> 用户管理命令

**sol**
> Serial-over-LAN 命令

# DESCRIPTION

**ipmitool** 为智能平台管理接口（IPMI）提供命令行界面。IPMI 支持服务器的带外管理，包括电源控制、硬件监控和远程控制台访问。

常见操作包括查看传感器读数（温度、电压、风扇转速）、控制电源状态，以及通过网络访问串行控制台。IPMI 独立于主操作系统工作。

# CAVEATS

访问 IPMI 需要正确配置 BMC。网络访问使用 UDP 端口 623（IPMI），可能需要防火墙规则放行。lanplus 接口提供加密通信。本地访问需要加载 ipmi 内核模块。

# HISTORY

IPMI 由 Intel、HP、NEC 和 Dell 自 **1998 年**起联合开发。ipmitool 成为 Linux 系统上进行 IPMI 管理的标准开源工具，同时支持本地和远程操作。

# INSTALL

```apt: sudo apt install ipmitool```

```dnf: sudo dnf install ipmitool```

```pacman: sudo pacman -S ipmitool```

```apk: sudo apk add ipmitool```

```zypper: sudo zypper install ipmitool```

```brew: brew install ipmitool```

```nix: nix profile install nixpkgs#ipmitool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [dmidecode](/man/dmidecode)(8)
