# TAGLINE

SteamOS 系统与硬件管理工具

# TLDR

**获取所有系统属性**

```steamosctl get-all-properties```

**获取当前的风扇控制状态**

```steamosctl get-fan-control-state```

**将风扇控制**设为操作系统管理

```steamosctl set-fan-control-state os```

**获取当前 TDP 限制**

```steamosctl get-tdp-limit```

**以瓦特为单位设置 TDP 限制**

```steamosctl set-tdp-limit [15]```

**设置 GPU 性能级别**

```steamosctl set-gpu-performance-level [auto|low|high|manual]```

**设置最大电池充电水平**

```steamosctl set-max-charge-level [80]```

**获取设备型号**

```steamosctl get-device-model```

# SYNOPSIS

**steamosctl** \<command\> [arguments]

# DESCRIPTION

**steamosctl** 是一个用于管理 SteamOS 系统硬件和软件设置的命令行工具。它通过 D-Bus 与 **steamos-manager** 守护进程通信，控制运行 SteamOS 的设备上的硬件功能，包括 Steam Deck 和其他支持的手持设备。

steamos-manager 系统由会话总线上的用户守护进程和系统总线上的 root 守护进程组成，后者负责特权操作。steamosctl 提供对所有公开功能的命令行访问，包括风扇控制、CPU 与 GPU 调节、TDP 限制、Wi-Fi 配置、电池管理和固件更新。

# COMMANDS

**get-fan-control-state** / **set-fan-control-state** _\<bios|os\>_
> 获取或设置风扇控制模式。

**get-cpu-scaling-governor** / **set-cpu-scaling-governor** _\<governor\>_
> 获取或设置 CPU 调频策略。

**get-cpu-boost-state** / **set-cpu-boost-state** _\<enabled|disabled\>_
> 获取或设置 CPU 加速。

**get-gpu-performance-level** / **set-gpu-performance-level** _\<auto|low|high|manual|profile_peak\>_
> 获取或设置 GPU 性能级别。

**get-gpu-power-profile** / **set-gpu-power-profile** _\<profile\>_
> 获取或设置 GPU 功耗配置。

**get-manual-gpu-clock** / **set-manual-gpu-clock** _\<freq\>_
> 获取或设置手动 GPU 频率（MHz）。

**get-tdp-limit** / **set-tdp-limit** _\<watts\>_
> 获取或设置 TDP 限制。

**get-tdp-limit-min** / **get-tdp-limit-max**
> 获取允许的最小或最大 TDP 值。

**get-performance-profile** / **set-performance-profile** _\<profile\>_
> 获取或设置性能配置。

**get-wifi-backend** / **set-wifi-backend** _\<iwd|wpa_supplicant\>_
> 获取或设置 Wi-Fi 后端。

**get-wifi-power-management-state** / **set-wifi-power-management-state** _\<enabled|disabled\>_
> 获取或设置 Wi-Fi 电源管理。

**get-hdmi-cec-state** / **set-hdmi-cec-state** _\<disabled|control-only|control-and-wake\>_
> 获取或设置 HDMI-CEC 状态。

**get-max-charge-level** / **set-max-charge-level** _\<1-100|-1\>_
> 获取或设置最大电池充电水平。-1 表示默认值。

**update-bios**
> 更新 BIOS 固件。

**update-dock**
> 更新扩展坞固件。

**trim-devices**
> 对适用的存储驱动器执行 TRIM。

**prepare-factory-reset** _\<user|os|all\>_
> 准备恢复出厂设置。

**reload-config**
> 从磁盘重新加载配置。

**get-all-properties**
> 获取管理器的所有属性。

**get-device-model**
> 获取设备的型号与变体。

# CAVEATS

仅在 SteamOS 上可用。需要 **steamos-manager** 守护进程正在运行。固件更新和恢复出厂设置等操作需要通过系统 D-Bus 守护进程获得提升的权限。该工具没有传统的 man page；文档位于源代码中。

# HISTORY

**steamosctl** 由 **Valve** 开发，**Collabora** 和 **Igalia** 参与贡献，是 **steamos-manager** 项目的一部分。它使用 **Rust** 编写，于 **2025 年 5 月**随 SteamOS 3.7 发布而开源。该工具提供标准化的 D-Bus 接口，使第三方手持设备能够支持 SteamOS 的硬件管理功能。

# SEE ALSO

[steamos-update](/man/steamos-update)(1), [cpupower](/man/cpupower)(1), [powerprofilesctl](/man/powerprofilesctl)(1)
