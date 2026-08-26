# TAGLINE

Manjaro Linux 上专门用于配置显卡设置的工具

# TLDR

显示当前 **Xorg 配置路径**

```mhwd-gpu --status```

**检查** Xorg 配置是否具有有效的符号链接

```mhwd-gpu --check```

为 Nvidia GPU 设置**自定义 Xorg 配置**

```sudo mhwd-gpu --setmod nvidia --setxorg [/path/to/nvidia.conf]```

为 **AMD GPU** 设置自定义 Xorg 配置

```sudo mhwd-gpu --setmod [catalyst|ati] --setxorg [/path/to/amdgpu.conf]```

显示**帮助**

```mhwd-gpu --help```

# SYNOPSIS

**mhwd-gpu** [_options_]

# PARAMETERS

**--status**
> 显示当前 Xorg 配置路径

**--check**
> 验证 Xorg 配置的符号链接是否有效

**--setmod _driver_**
> 设置 GPU 驱动模块（nvidia、catalyst、ati、intel）

**--setxorg _path_**
> 设置 Xorg 配置文件的路径

**--help**
> 显示帮助信息

# DESCRIPTION

**mhwd-gpu** 是 Manjaro Linux 上用于配置显卡设置的工具，专门管理不同 GPU 驱动的 Xorg 配置文件。它负责处理指向当前活动 GPU 配置的符号链接，位于 **/etc/X11/xorg.conf.d/**。

该工具简化了在不同 GPU 配置之间的切换，对于配备多块显卡的系统或在开源驱动与专有驱动之间切换的场景尤为有用。

它是 Manjaro 硬件检测（MHWD）工具集的一部分，与负责驱动安装的 **mhwd** 以及负责内核管理的 **mhwd-kernel** 协同工作。

# CAVEATS

修改配置需要 root 权限。错误的 Xorg 配置可能导致显示无法工作；请始终准备好备份配置或恢复手段。仅适用于 Manjaro Linux，在其他发行版上可能无法使用。

# SEE ALSO

[mhwd](/man/mhwd)(1), [mhwd-kernel](/man/mhwd-kernel)(1), [nvidia-settings](/man/nvidia-settings)(1)
