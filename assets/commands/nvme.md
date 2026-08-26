# TAGLINE

NVMe 存储命令行接口工具

# TLDR

**列出所有 NVMe 设备**

```sudo nvme list```

**显示控制器识别信息**

```sudo nvme id-ctrl [/dev/nvme0]```

**显示命名空间识别信息**

```sudo nvme id-ns [/dev/nvme0n1]```

**显示 SMART 健康信息**

```sudo nvme smart-log [/dev/nvme0]```

**显示错误日志条目**

```sudo nvme error-log [/dev/nvme0]```

**格式化命名空间（会销毁所有数据）**

```sudo nvme format [/dev/nvme0n1]```

**向设备下载固件**

```sudo nvme fw-download [/dev/nvme0] --fw=[firmware.bin]```

**运行设备自检**

```sudo nvme device-self-test [/dev/nvme0] --stc=[1]```

# SYNOPSIS

**nvme** _command_ [_device_] [_options_]

# PARAMETERS

**list**
> 列出所有 NVMe 设备和命名空间。

**id-ctrl** _DEVICE_
> 发送 identify controller 命令并显示结果。

**id-ns** _DEVICE_
> 发送 identify namespace 命令并显示结果。

**smart-log** _DEVICE_
> 获取 SMART / 健康信息日志。

**error-log** _DEVICE_
> 获取错误信息日志。

**fw-log** _DEVICE_
> 获取固件插槽信息日志。

**format** _DEVICE_
> 以指定的 LBA 格式格式化命名空间。

**fw-download** _DEVICE_
> 将固件镜像下载到设备。

**fw-activate** _DEVICE_
> 激活已下载的固件镜像。

**sanitize** _DEVICE_
> 执行清理操作（安全擦除）。

**device-self-test** _DEVICE_
> 运行设备自检（短测试或扩展测试）。

**get-feature** _DEVICE_
> 从控制器获取特性值。

**set-feature** _DEVICE_
> 在控制器上设置特性值。

**discover**
> 发现 NVMe-over-Fabrics 子系统。

**connect** _DEVICE_
> 连接到 NVMe-over-Fabrics 控制器。

**help** _COMMAND_
> 显示特定子命令的帮助。

# DESCRIPTION

**nvme** 是一款用户空间工具，为 Linux 上的 NVM-Express（NVMe）驱动器提供符合标准的工具集。它包含 NVMe 规范中定义的所有管理命令和 I/O 命令对应的子命令，还提供用于显示控制器寄存器和获取各类日志页的命令。

该工具支持 NVMe-over-Fabrics 操作，包括针对远程 NVMe 子系统的发现、连接和断开连接。它还可以通过 passthrough 提交完全任意的厂商特定命令。

所有命令成功时返回 0，失败时返回 1。

# CAVEATS

大多数操作需要 root 权限。**format** 和 **sanitize** 命令会销毁设备上的所有数据且不可逆。**sanitize** 命令一旦开始便无法中止。NVMe-over-Fabrics 命令需要相应的内核模块。

# HISTORY

**nvme-cli** 是 Linux NVMe 项目下的开源项目，位于 https://github.com/linux-nvme/nvme-cli。它依赖 Linux 内核的 NVMe IOCTL，仅适用于 Linux。

# INSTALL

```apt: sudo apt install nvme-cli```

```dnf: sudo dnf install nvme-cli```

```pacman: sudo pacman -S nvme-cli```

```apk: sudo apk add nvme-cli```

```zypper: sudo zypper install nvme-cli```

```nix: nix profile install nixpkgs#nvme-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smartctl](/man/smartctl)(1), [hdparm](/man/hdparm)(8), [lsblk](/man/lsblk)(1)
