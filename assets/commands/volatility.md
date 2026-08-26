# TAGLINE

内存取证分析框架

# TLDR

**列出可用插件**和配置档案

```volatility --info```

从内存转储中**列出进程**

```volatility -f [memory.img] --profile=[LinuxProfile] linux_pslist```

**显示网络连接**

```volatility -f [memory.img] --profile=[Profile] linux_netstat```

**恢复 bash 历史**

```volatility -f [memory.img] --profile=[Profile] linux_bash```

**列出所有进程打开的文件**

```volatility -f [memory.img] --profile=[Profile] linux_lsof```

**显示进程命令行**

```volatility -f [memory.img] --profile=[Profile] linux_cmdline```

**用 Yara 规则扫描**

```volatility -f [memory.img] --profile=[Profile] linux_yarascan -y [rules.yar]```

# SYNOPSIS

**volatility** -f _memory_image_ [--profile=_PROFILE_] _plugin_ [_options_]

**vol.py** -f _memory_image_ _plugin_

# PARAMETERS

**-f** _FILE_, **--file** _FILE_
> 要分析的内存镜像文件

**--profile** _PROFILE_
> 操作系统配置档案（Volatility 2 必需）

**--info**
> 列出可用的插件和配置档案

**-d**, **--debug**
> 启用调试输出

**-h**, **--help**
> 显示帮助信息

**-p** _PID_
> 按进程 ID 过滤

**-o** _OFFSET_
> 内存中的物理偏移量

**--output** _FORMAT_
> 输出格式（text、json、html）

**--output-file** _FILE_
> 将输出写入文件

# LINUX PLUGINS

**linux_pslist**
> 列出正在运行的进程

**linux_pstree**
> 进程树视图

**linux_bash**
> 恢复 bash 命令历史

**linux_netstat**
> 显示网络连接

**linux_lsof**
> 列出已打开的文件描述符

**linux_cmdline**
> 显示进程的命令行参数

**linux_mount**
> 列出已挂载的文件系统

**linux_find_file**
> 在内存中查找文件

**linux_yarascan**
> 用 Yara 规则扫描内存

**linux_moddump**
> 转储已加载的内核模块

**linux_proc_maps**
> 显示进程内存映射

# DESCRIPTION

**volatility** 是一个开源的内存取证框架，用于从 RAM 转储中提取数字证据。它通过分析内存镜像来恢复正在运行的进程、网络连接、命令历史以及其他不存在于磁盘上的易失性数据。

该框架支持 Windows、Linux 和 macOS 的内存分析。Linux 插件以 **linux_** 为前缀，并且需要一个与生成转储的系统在发行版、内核版本和架构上完全匹配的配置档案。

Volatility 3 通过自动符号检测简化了配置档案的管理，而 Volatility 2 则需要手动构建或获取配置档案。内存转储可以使用 LiME（Linux Memory Extractor）或 VMware 快照等工具获取。

# CAVEATS

Linux 分析需要与内核版本和发行版完全匹配的配置档案。构建配置档案需要内核头文件和调试符号。内存镜像很大，分析可能消耗大量资源。反取证技术可能会干扰某些插件。并非所有插件都适用于所有内存格式。

# HISTORY

Volatility 框架由 **Aaron Walters** 创建，于 **2007 年**首次发布。它源自乔治梅森大学对内存取证的学术研究，后来成为数字取证与应急响应领域进行内存分析的标准工具。**2019 年**发布的 Volatility 3 引入了 Python 3 支持和自动符号表生成，简化了 Linux 和 macOS 的分析工作。

# SEE ALSO

[lime](/man/lime)(1), [strings](/man/strings)(1), [file](/man/file)(1), [dd](/man/dd)(1)
