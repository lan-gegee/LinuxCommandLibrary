# TAGLINE

Linux 系统启动流程文档

# TLDR

**查看启动流程文档**

```man 7 boot```

**查看 systemd 启动流程文档**

```man 7 bootup```

# SYNOPSIS

这是一个描述 Linux 启动过程的文档页，不是可执行命令。

# DESCRIPTION

**boot**(7) man page 基于UNIX System V Release 4 记录了 Linux 系统的启动过程。启动序列包括以下几个阶段：

**硬件启动（BIOS/UEFI）**
> POST（加电自检）运行，硬件初始化，固件定位引导加载程序。

**OS 加载器（GRUB/LILO）**
> 引导加载程序找到内核并将其载入内存。

**内核启动**
> 内核初始化设备，启动 swapper 进程（kswapd），并挂载根文件系统。

**Init 进程**
> 第一个用户态进程（PID 1）启动。现代系统使用 **systemd**，较旧的系统使用 **SysVinit**。

**启动脚本**
> 系统服务按照配置的运行级别或 systemd target 启动。

# CAVEATS

此文档主要描述传统的 SysV init 启动过程。大多数现代 Linux 发行版使用 **systemd**，其启动架构不同，记录在 **bootup**(7) 中。

确切的启动顺序因发行版、硬件平台和所用 init 系统而异。

# HISTORY

System V init 进程起源于 1983 年发布的 **AT&T Unix System V**。Linux 发行版历史上采用了这一模型，之后从 2010-2011 年前后开始向 **systemd** 过渡。到 2015 年，systemd 已成为大多数主流发行版的默认 init 系统。

# INSTALL

```nix: nix profile install nixpkgs#boot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [journalctl](/man/journalctl)(1), [init](/man/init)(1), [grub](/man/grub)(1)
