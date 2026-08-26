# TAGLINE

控制 ATI Radeon 硬件设置

# TLDR

**关闭笔记本背光**

```radeontool light off```

**打开笔记本背光**

```radeontool light on```

**禁用外部视频输出**（DAC）

```radeontool dac off```

**启用外部视频输出**（DAC）

```radeontool dac on```

**显示寄存器值采样**

```radeontool regs```

**显示匹配模式的寄存器**

```radeontool regmatch [pattern]```

**将匹配模式的寄存器**设为特定值

```radeontool regset [pattern] [value]```

# SYNOPSIS

**radeontool** [_options_] [_command_]

# PARAMETERS

**light** [**on**|**off**]
> 控制笔记本屏幕背光的电源状态

**dac** [**on**|**off**]
> 控制外部视频输出（VGA/DVI）的电源状态

**stretch** [**on**|**off**|**vert**|**horiz**|**auto**|**manual**]
> 在运行非原生分辨率时控制 LCD 拉伸

**regs**
> 显示重要寄存器值的采样

**regmatch** _pattern_
> 显示名称与通配符模式匹配的寄存器

**regset** _pattern_ _value_
> 将名称与通配符模式匹配的寄存器设置为指定值

**--debug**
> 启用详细的调试输出。

**--skip=**_n_
> 跳过前 n 块 Radeon 显卡，操作第 n+1 块。

**--instance=**_n_
> 按编号使用特定的 Radeon 显卡实例。

# DESCRIPTION

**radeontool** 是一个用于控制基于 ATI Radeon 图形卡硬件功能的实用工具，主要用在笔记本电脑上。它提供对背光控制、外部显示输出和底层寄存器操作的直接访问。

该工具通过内存映射 I/O 直接与图形硬件通信，可以控制标准显示驱动未暴露的功能。常见用途包括通过脚本控制背光以进行电源管理，以及调试显示问题。

# CAVEATS

由于需要通过 /dev/mem 直接访问硬件，大多数操作**需要 root 权限**。

**寄存器操作很危险**：错误使用 regset 可能导致系统不稳定或永久性硬件损坏。只有在理解后果的情况下才应修改寄存器。

**并非所有功能在所有显卡上都可用**：兼容性因 Radeon 各代产品而异。请在你自己的硬件上谨慎测试各命令。

# HISTORY

radeontool 由 **David Airlie** 创建，是 Linux 开源图形工作的一部分。它诞生于 2000 年代初，当时 ATI Radeon 显卡需要用户空间工具来控制内核驱动尚不支持的功能。

# INSTALL

```apt: sudo apt install radeontool```

```dnf: sudo dnf install radeontool```

```pacman: sudo pacman -S radeontool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xrandr](/man/xrandr)(1), [xbacklight](/man/xbacklight)(1), [aticonfig](/man/aticonfig)(1), [lspci](/man/lspci)(1)
