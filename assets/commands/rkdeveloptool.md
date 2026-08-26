# TAGLINE

通过 USB 为 Rockchip 设备刷写固件

# TLDR

**列出设备**

```rkdeveloptool ld```

**下载引导程序**

```rkdeveloptool db [loader.bin]```

**写入镜像**

```rkdeveloptool wl [0] [image.img]```

**读取闪存信息**

```rkdeveloptool rfi```

**重启设备**

```rkdeveloptool rd```

**读取分区**

```rkdeveloptool rl [0] [size] [output.img]```

# SYNOPSIS

**rkdeveloptool** _command_ [_options_]

# PARAMETERS

**ld**
> 列出设备。

**db** _FILE_
> 下载引导加载程序。

**wl** _OFFSET FILE_
> 在指定偏移处写入镜像。

**rl** _OFFSET SIZE FILE_
> 读取内容到文件。

**rfi**
> 读取闪存信息。

**rd**
> 重启设备。

**ef**
> 擦除整个闪存。

**ul** _FILE_
> 从打包的更新镜像升级固件。

**rid**
> 读取芯片 ID。

# DESCRIPTION

**rkdeveloptool** 是一款 Linux 实用工具，用于通过 USB 向 Rockchip ARM SoC 设备（RK3399、RK3328、RK3288 等）刷写固件。当设备进入 maskrom 模式——一种通过短接特定引脚或开机时按住某个按键进入的特殊恢复状态——它会与设备的 bootrom 通信。

刷写过程通常分两步：先用 **db** 命令载入引导加载程序，再用 **wl** 在合适的偏移位置写入系统镜像。该工具还可以读回闪存内容、查询闪存芯片信息以及擦除整个存储设备。它是 Rockchip 基于 Windows 的刷写工具的开源 Linux 替代方案。

与设备通信需要 root 权限或相应的 USB 权限。在执行写入操作之前，可用 **ld** 命令确认设备已被检测到且处于正确的模式。

# CAVEATS

需要 root 权限。设备必须处于 maskrom 模式。错误的镜像可能导致设备变砖。

# HISTORY

**rkdeveloptool** 由 **Rockchip** 开发，用于通过 USB 向其 ARM SoC 设备刷写固件。

# INSTALL

```apt: sudo apt install rkdeveloptool```

```dnf: sudo dnf install rkdeveloptool```

```apk: sudo apk add rkdeveloptool```

```zypper: sudo zypper install rkdeveloptool```

```nix: nix profile install nixpkgs#rkdeveloptool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dd](/man/dd)(1), [fastboot](/man/fastboot)(1)
