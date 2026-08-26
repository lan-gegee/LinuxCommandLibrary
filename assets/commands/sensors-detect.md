# TAGLINE

检测硬件监控传感器芯片

# TLDR

**交互式运行**以检测硬件监控芯片

```sudo sensors-detect```

**以自动模式运行**并采用默认回答

```sudo sensors-detect --auto```

**显示 I2C 地址统计信息**

```sudo sensors-detect --stat```

# SYNOPSIS

**sensors-detect** [**--auto**] [**--stat**]

# PARAMETERS

**--auto**
> 以自动、非交互模式运行。对所有问题假定默认回答。请谨慎使用，因为可能触发具有潜在危险的硬件探测。

**--stat**
> 显示 I2C 地址统计信息。

# DESCRIPTION

**sensors-detect** 是一个交互式程序，扫描系统中 libsensors 和 lm_sensors 工具套件所支持的硬件监控芯片（传感器）。它会系统地搜索：

1. 内嵌于 CPU、南桥和内存控制器中的传感器
2. 内嵌于 Super I/O 芯片中的传感器
3. 通过 ISA I/O 端口访问的硬件监控芯片
4. 可通过 SMBus 或 I2C 总线访问的硬件监控芯片

检测完成后，sensors-detect 会建议需要加载哪些内核模块，并可选择将它们添加到 **/etc/modules** 以便在启动时自动加载。之后即可使用 **sensors** 命令读取检测到的传感器数据。

如果发现了具备完整硬件监控功能的 Super I/O 芯片，程序通常会跳过最后两个检测步骤，但用户也可以根据需要要求执行完整检测。

# CAVEATS

sensors-detect 在检测过程中必须直接访问硬件，这在极少数情况下可能导致从 SMBus 锁死到永久性硬件损坏等各种问题。作者已尽可能保证检测的安全性，但无法保证在所有系统上都安全。在不了解风险的情况下，请勿在生产系统上运行。**--auto** 模式可能触发具有潜在危险的探测，应谨慎使用。

# HISTORY

**sensors-detect** 是 **lm_sensors**（Linux monitoring sensors）项目的一部分，该项目始于 **1998** 年，旨在为 Linux 上的硬件监控提供工具和内核驱动。项目最初托管于 lm-sensors.org，后来迁移至 GitHub。它已成为 Linux 系统上检测和配置硬件传感器的标准工具，支持众多主板芯片组、CPU 温度传感器和专用监控芯片。

# INSTALL

```apt: sudo apt install lm-sensors```

```apk: sudo apk add lm-sensors-detect```

```brew: brew install lm-sensors```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sensors](/man/sensors)(1), [fancontrol](/man/fancontrol)(8), [modprobe](/man/modprobe)(8), [lshw](/man/lshw)(1)
