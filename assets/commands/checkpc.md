# TAGLINE

校验 printcap 数据库与假脱机目录

# TLDR

**检查 printcap 数据库中的错误**

```checkpc```

**修复权限并创建缺失文件**

```sudo checkpc -f```

**输出详细的 printcap 信息**

```checkpc -p```

**报告早于指定时间的任务文件**

```checkpc -A [7D]```

**删除早于指定时间的垃圾文件**

```checkpc -r -A [7D]```

**将日志文件截断到指定大小**

```checkpc -t [10M]```

# SYNOPSIS

**checkpc** [**-aflprsV**] [**-A** _age_] [**-D** _debugflags_] [**-t** _size_]

# DESCRIPTION

**checkpc** 为 LPRng 打印系统校验 printcap 数据库和打印机假脱机目录。它会检查文件权限、所有权和目录结构，报告问题并可选择修复。

该命令在安装新的 printcap 配置或清理现有打印机假脱机程序时很有用。它可以识别并删除过期的任务文件，以及截断过大的日志文件。

# PARAMETERS

**-a**
> 不创建记账文件

**-f**
> 修复模式：创建缺失文件并修复权限。可能需要运行多次

**-l**
> 不创建日志文件

**-p**
> 输出详细的 printcap 信息

**-r**
> 删除早于指定时间的垃圾或任务文件（需要配合 -A）

**-s**
> 不创建过滤器状态文件

**-A** _age_
> 报告早于指定时间的文件。时间后缀：D（天）、H（小时）、M（分钟）、S（秒）。默认：天

**-D** _debugflags_
> 启用调试标志

**-t** _size_
> 将日志文件截断到指定大小，单位 K（千字节）或 M（兆字节，默认）

**-V**
> 输出版本信息

# CONFIGURATION

**/etc/printcap**
> 打印机能力数据库，checkpc 对其进行校验并检查错误。

# CAVEATS

**-f** 选项应以 root 身份运行。以非 root 用户运行会报告大量权限错误。它属于 **LPRng**，而非 CUPS。同时安装两者的系统可能出现冲突。

# HISTORY

**checkpc** 是 **LPRng**（LPR Next Generation）的一部分。LPRng 是一个增强型打印机假脱机系统，功能类似于最初的 Berkeley LPR 软件，但具有更多特性并改进了安全性。

# INSTALL

```apt: sudo apt install lprng```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lpr](/man/lpr)(1), [lpq](/man/lpq)(1), [lprm](/man/lprm)(1), [lpc](/man/lpc)(8)

# RESOURCES

```[Source code](https://sourceforge.net/projects/lprng/)```

<!-- verified: 2026-06-22 -->
