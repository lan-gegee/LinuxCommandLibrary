# TAGLINE

Linux 的图形化系统信息与基准测试工具

# TLDR

**启动图形界面**

```hardinfo```

**生成文本报告输出到标准输出**

```hardinfo -r```

**生成 HTML 报告**

```hardinfo -r -f html > [report.html]```

**列出可用模块**

```hardinfo -l```

# SYNOPSIS

**hardinfo** [_options_]

# PARAMETERS

**-r**, **--generate-report**
> 生成报告到标准输出而不是打开 GUI

**-f**, **--report-format** _FORMAT_
> 报告格式：text、html 或 shell

**-m**, **--load-module** _MODULE_
> 加载指定模块

**-a**, **--autoload**
> 自动加载所有模块

**-l**, **--list-modules**
> 列出可用模块

# DESCRIPTION

**hardinfo**（Hardware Information）是一款面向 Linux 的图形化系统信息与基准测试工具。它显示关于硬件组件、软件配置和系统资源的详细信息。

GUI 将信息分为以下几个类别：
- **Computer** - 摘要、操作系统、内核模块、启动记录
- **Devices** - 处理器、内存、PCI 设备、USB 设备、存储
- **Network** - 接口、IP 连接、路由表
- **Benchmarks** - CPU、FPU 和内存性能测试

可以生成文本、HTML 或 shell 变量格式的报告，用于存档或寻求技术支持。

# CAVEATS

某些信息需要 root 权限。基准测试结果是相对值，不应跨不同的 hardinfo 版本进行比较。硬件检测依赖已加载的内核驱动。

# HISTORY

hardinfo 由 Leandro A. F. Pereira 创建，首次发布于 **2003 年**。它一直是 Linux 桌面上广受欢迎的系统信息工具，提供的功能与 Windows 的系统信息实用程序类似。

# INSTALL

```zypper: sudo zypper install hardinfo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lshw](/man/lshw)(1), [inxi](/man/inxi)(1), [hwinfo](/man/hwinfo)(8), [lscpu](/man/lscpu)(1)
