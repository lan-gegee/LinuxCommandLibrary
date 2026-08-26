# TAGLINE

在 Linux 中加载 Windows NDIS 驱动

# TLDR

**加载 Windows 驱动**

```loadndisdriver [driver.inf] [driver.sys]```

**安装驱动**

```loadndisdriver -i [driver.inf]```

**带设备 ID 加载**

```loadndisdriver [driver.sys] [device_id]```

**列出已加载的驱动**

```loadndisdriver -l```

# SYNOPSIS

**loadndisdriver** [_options_] _driver_

# PARAMETERS

_DRIVER_
> Windows 驱动文件（.sys）。

**-i** _INF_
> 从 INF 文件安装。

**-l**
> 列出已加载的驱动。

**-d**
> 调试模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**loadndisdriver** 在 Linux 中加载 Windows NDIS 驱动。它通过 ndiswrapper 启用 Windows 无线驱动。

当没有可用的 Linux 原生驱动时可以使用该工具。它会转换 Windows 驱动的调用。

# CAVEATS

已弃用的方案。优先使用原生驱动。需要 32/64 位匹配。属于 ndiswrapper 的一部分。

# HISTORY

loadndisdriver 作为 **ndiswrapper** 的一部分被创建，用于在 Linux 系统上启用 Windows 无线驱动。

# SEE ALSO

[ndiswrapper](/man/ndiswrapper)(8), [modprobe](/man/modprobe)(8)
