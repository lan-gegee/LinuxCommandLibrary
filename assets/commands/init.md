# TAGLINE

系统中所有进程的父进程，负责启动和停止服务

# TLDR

将系统切换到**图形**环境（运行级别 5）

```sudo init 5```

将系统切换到**多用户终端**（运行级别 3）

```sudo init 3```

将系统切换到**单用户**模式（运行级别 1）

```sudo init 1```

**关闭**系统

```init 0```

**重启**系统

```init 6```

# SYNOPSIS

**init** [_runlevel_]

# PARAMETERS

**0**
> 停机（halt）系统

**1** 或 **S**
> 单用户模式（维护模式）

**2**
> 无 NFS 的多用户模式（Debian 上默认为带 GUI 的多用户模式）

**3**
> 带网络的多用户模式，仅文本控制台

**4**
> 未使用/自定义（可用于用户自定义用途）

**5**
> 带网络和图形桌面的多用户模式（Red Hat 默认的图形模式）

**6**
> 重启系统

# DESCRIPTION

**init** 是系统中所有进程的父进程，负责在不同运行级别启动和停止服务。它是管理传统 System V init 守护进程的系统状态。

运行级别定义了不同的系统状态，从单用户维护模式到完整的图形桌面。改变运行级别会让 init 按照 /etc/rc.d 或 /etc/init.d 脚本中的定义启动或停止服务。

在现代基于 systemd 的系统上，init 可能是一个兼容层包装器，将运行级别命令转换为 systemd target。

# CAVEATS

行为因发行版而异。在基于 systemd 的系统上，**init** 是指向 systemd 的符号链接，运行级别命令会被转换为 systemd target（例如运行级别 3 映射到 multi-user.target，运行级别 5 映射到 graphical.target）。直接切换运行级别可能干扰正在运行的服务。现代系统请使用 **systemctl**。

# HISTORY

System V init 源于 AT&T UNIX System V（**1983 年**）。在大约 **2011 年** systemd 开始取代它之前，它一直是大多数 Linux 发行版的标准 init 系统。

# INSTALL

```apt: sudo apt install runit-init```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [telinit](/man/telinit)(8), [runlevel](/man/runlevel)(8), [halt](/man/halt)(8), [reboot](/man/reboot)(8), [shutdown](/man/shutdown)(8), [service](/man/service)(8)
