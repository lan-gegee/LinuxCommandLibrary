# TAGLINE

Linux udev 设备管理器的管理工具

# TLDR

**监视**所有设备事件

```sudo udevadm monitor```

**打印**内核发送的 uevent

```sudo udevadm monitor -k```

**打印**经过 udev 处理后的设备事件

```sudo udevadm monitor -u```

**列出**设备的属性

```sudo udevadm info -a [/dev/sda]```

**重新加载**所有 udev 规则

```sudo udevadm control -R```

**触发**所有 udev 规则执行

```sudo udevadm trigger```

**通过模拟设备加载来测试**事件运行

```sudo udevadm test [/dev/sda]```

# SYNOPSIS

**udevadm** [_command_] [_options_]

# PARAMETERS

**monitor**
> 监视内核 uevent 和 udev 事件

**info**
> 查询设备信息

**control**
> 控制 udev 守护进程

**trigger**
> 向内核请求设备事件

**settle**
> 等待待处理的 udev 事件完成

**test**
> 模拟一次 udev 事件

**-k, --kernel**
> 打印内核 uevent

**-u, --udev**
> 打印 udev 事件

**-a, --attribute-walk**
> 显示设备的全部属性

**-R, --reload**
> 重新加载 udev 规则

# DESCRIPTION

**udevadm** 是 Linux 的 udev 管理工具，用于查询和控制 udev 设备管理器。它可以监视设备事件、查询设备属性、重载规则以及触发规则处理。

该工具对于调试 udev 规则、了解设备属性以及管理热插拔设备处理至关重要。

# CAVEATS

大多数操作需要 root 权限。**test** 命令只模拟事件而不真正执行。规则更改需要 **control --reload** 才能生效。属于 systemd/udev 套件。

# INSTALL

```apt: sudo apt install udev```

```apk: sudo apk add eudev```

```zypper: sudo zypper install udev```

```nix: nix profile install nixpkgs#udev```

<!-- packages: 2026-07-22 -->

# SEE ALSO
