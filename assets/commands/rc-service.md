# TAGLINE

管理 OpenRC init 系统的服务

# TLDR

显示服务的**状态**

```rc-service [service] status```

**启动**服务

```sudo rc-service [service] start```

**停止**服务

```sudo rc-service [service] stop```

**重启**服务

```sudo rc-service [service] restart```

对命令进行**演练运行**

```sudo rc-service -Z [service] [command]```

**解析**服务位置

```sudo rc-service -r [service]```

# SYNOPSIS

**rc-service** [**-Z**|**--dry-run**] [**-r**|**--resolve**] _service_ _command_

# PARAMETERS

**-Z, --dry-run**
> 模拟执行命令而不实际运行

**-r, --resolve**
> 显示服务脚本的位置

**-l, --list**
> 列出所有服务

**-e, --exists**
> 检查服务是否存在

**service**
> 服务名称

**command**
> start、stop、restart、status 或自定义命令

# DESCRIPTION

**rc-service** 用于控制 OpenRC 服务。它会定位服务的 init 脚本并以指定命令运行它们。OpenRC 是 Gentoo、Alpine 以及其他一些发行版使用的 init 系统。

无论服务脚本位于系统中的哪个位置，该工具都提供一致的服务管理接口。

# CAVEATS

仅适用于 OpenRC，不适用于 systemd 系统。服务控制需要 root 权限。服务脚本位于 /etc/init.d/。自定义命令取决于服务自身的实现。

# HISTORY

**rc-service** 是 **OpenRC** 的一部分，后者是为 Gentoo Linux 创建的 init 系统。它提供基于依赖关系的服务管理，可作为 systemd 的替代方案。

# INSTALL

```apt: sudo apt install openrc```

```apk: sudo apk add openrc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rc-update](/man/rc-update)(8), [rc-status](/man/rc-status)(8), [openrc](/man/openrc)(8)
