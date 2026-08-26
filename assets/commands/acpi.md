# TAGLINE

显示电池、温度和电源信息

# TLDR

显示**电池**信息

```acpi```

显示**温度**信息

```acpi -t```

显示**散热设备**信息

```acpi -c```

以**华氏度**显示温度信息

```acpi -t -f```

显示**全部**信息

```acpi -V```

从 **/proc** 而非 /sys 提取信息

```acpi -p```

# SYNOPSIS

**acpi** [_-b_] [_-a_] [_-t_] [_-c_] [_-V_] [_-f_] [_-k_] [_-p_] [_-i_]

# DESCRIPTION

**acpi** 显示来自 /proc 或 /sys 文件系统的信息，例如电池状态、交流适配器状态、温区温度和散热设备状态。它主要用于笔记本电脑和便携设备上，在命令行监控电池电量、剩余时间和系统温度。

默认显示电池信息。附加标志可查看温区、交流适配器状态和散热设备活动。温度输出可以摄氏度、华氏度或开尔文显示。该工具读取内核暴露的 ACPI 数据，是图形化电源管理小程序的轻量替代方案。

# PARAMETERS

**-b, --battery**
> 显示电池状态信息

**-a, --ac-adapter**
> 显示交流适配器状态

**-t, --thermal**
> 显示温度相关信息

**-c, --cooling**
> 显示散热设备详情

**-V, --everything**
> 显示所有设备（覆盖其他选项）

**-r, --remaining-time**
> 显示剩余充/放电时间

**-e, --end-time**
> 显示充/放电完成的预计时间

**-i, --details**
> 提供电池容量和温度阈值信息

**-f, --fahrenheit**
> 使用华氏度而非摄氏度

**-k, --kelvin**
> 使用开尔文而非摄氏度

**-p, --proc**
> 使用旧的 /proc 接口（默认使用 /sys）

**-s, --show-empty**
> 在输出中包含非工作状态的设备

**-d, --directory dir**
> 指定自定义的 ACPI 信息路径

# CAVEATS

取决于 ACPI 支持情况和内核配置，某些选项可能并非在所有系统上都可用。旧式 /proc 接口在较新的内核上可能不可用。

# HISTORY

为在 Linux 笔记本和台式机上提供简单的 ACPI 信息命令行接口而创建。

# INSTALL

```apt: sudo apt install acpi```

```dnf: sudo dnf install acpi```

```pacman: sudo pacman -S acpi```

```apk: sudo apk add acpi```

```zypper: sudo zypper install acpi```

```nix: nix profile install nixpkgs#acpi```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[acpi_listen](/man/acpi_listen)(8), [acpid](/man/acpid)(8), [acpi_available](/man/acpi_available)(1)

# RESOURCES

```[Source code](https://sourceforge.net/projects/acpiclient/)```

<!-- verified: 2026-06-10 -->
