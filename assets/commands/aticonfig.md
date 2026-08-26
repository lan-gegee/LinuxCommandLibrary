# TAGLINE

配置 AMD/ATI 专有图形驱动程序

# TLDR

**显示当前 GPU 配置**

```aticonfig --query-monitor```

**初始化 X 配置**

```sudo aticonfig --initial```

**启用扩展模式的双显示器**

```sudo aticonfig --initial=dual-head --screen-layout=right```

**设置显示器分辨率**

```aticonfig --resolution=0,1920x1080```

**启用或禁用垂直同步**

```aticonfig --set-pcs-str="DDX,EnableVSync,1"```

**显示 GPU 温度和风扇转速**

```aticonfig --odgt```

**列出所有显卡适配器**

```aticonfig --list-adapters```

**设置 GPU 时钟频率**（超频）

```aticonfig --odsc=950,1200```

# SYNOPSIS

**aticonfig** [_options_]

# PARAMETERS

**--initial**
> 为 AMD GPU 生成基本的 X 配置。

**--initial=dual-head**
> 配置双显示器环境。

**--query-monitor**
> 显示已连接的显示器及其状态。

**--list-adapters**
> 列出所有检测到的显卡适配器。

**--resolution** _adapter,resolution_
> 为某个适配器设置屏幕分辨率。

**--screen-layout** _position_
> 设置双显示器布局（left、right、above、below）。

**--odgt**
> 显示 GPU 温度（OverDrive Get Temperature）。

**--odgc**
> 显示 GPU 时钟信息。

**--odsc** _core,memory_
> 设置 GPU 核心与显存时钟频率。

**--od-enable**
> 启用 OverDrive（超频功能）。

**--set-pcs-str** _path,value_
> 设置一条持久化的配置字符串。

**--lsa**
> 列出适配器及详细信息。

# DESCRIPTION

**aticonfig** 是 AMD/ATI 专有图形驱动（Catalyst/fglrx）的配置工具。它提供对 AMD Radeon 显卡的显示设置、GPU 参数和 X.org 配置的命令行控制。

该工具可生成并修改 X 配置文件，管理多显示器环境，并提供 OverDrive 功能入口以监控温度和调整时钟频率。它是 AMD Catalyst Control Center 图形工具的命令行对应版本。

X.org 的配置更改通常需要重启 X 服务器才能生效。而 OverDrive 的频率与风扇控制设置可以在运行时直接应用。

# CONFIGURATION

**/etc/X11/xorg.conf**
> 由 aticonfig 生成和修改的 X.org 服务器配置文件，涵盖显示设置、多显示器布局和 GPU 参数。

# CAVEATS

**aticonfig** 仅适用于已停止维护的旧版 fglrx/Catalyst 专有驱动，该驱动与新版 Linux 内核（4.2+）及 X.org 版本不兼容。现代 AMD GPU 应使用开源 amdgpu 驱动，并配合 radeon-profile 或 corectrl 实现类似功能。此处记录该工具仅供维护旧系统的用户参考。

# HISTORY

**aticonfig** 工具曾是 AMD 面向 Linux 的专有 Catalyst 驱动包的一部分，支持 Radeon HD 系列及更早的 GPU。AMD 于 **2015** 年放弃 Catalyst 驱动，转向为较新硬件开发开源 AMDGPU 驱动。如今该工具仅对仍在使用无法迁移到开源方案的老旧硬件的用户有意义。

# SEE ALSO

[xrandr](/man/xrandr)(1), [nvidia-settings](/man/nvidia-settings)(1)
