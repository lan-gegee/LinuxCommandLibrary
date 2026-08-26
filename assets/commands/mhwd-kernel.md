# TAGLINE

管理 Manjaro Linux 上的 Linux 内核安装与卸载

# TLDR

列出所有**可用内核**

```mhwd-kernel -l```

列出所有**已安装内核**

```mhwd-kernel -li```

**安装**内核

```sudo mhwd-kernel -i [kernel]```

**卸载**内核

```sudo mhwd-kernel -r [kernel]```

安装内核并**替换当前正在运行的内核**

```sudo mhwd-kernel -i [kernel] rmc```

# SYNOPSIS

**mhwd-kernel** [_options_] [_kernel_] [_rmc_]

# PARAMETERS

**-l, --list**
> 列出软件仓库中所有可用的内核

**-li, --listinstalled**
> 列出当前已安装的所有内核

**-i, --install _kernel_**
> 安装指定的内核

**-r, --remove _kernel_**
> 卸载指定的内核

**rmc**
> 在安装新内核后移除当前内核

# DESCRIPTION

**mhwd-kernel** 管理 Manjaro Linux 上的 Linux 内核安装与卸载。它简化了安装多个内核以及在 LTS（长期支持）和主线内核版本之间切换的过程。

内核名称遵循 **linux** 加版本号的形式（例如 linux515、linux61、linux66）。该工具会自动处理与内核配套的内核模块和头文件。

**rmc**（remove current，移除当前）选项在替换有问题的内核时很有用——它会在成功安装新内核并在重启之后移除当前正在运行的内核。

# CAVEATS

请始终保持至少一个已知可用的内核处于安装状态。卸载唯一已安装的内核可能导致系统无法启动。安装新内核后需重启才能启用。内核更新可能需要重新构建第三方模块（如 NVIDIA 驱动）。

# SEE ALSO

[mhwd](/man/mhwd)(1), [mhwd-gpu](/man/mhwd-gpu)(1), [uname](/man/uname)(1), [dkms](/man/dkms)(8)
