# TAGLINE

控制 systemd 的机器管理器

# TLDR

**列出**运行中的机器

```machinectl list```

**启动**一台机器

```sudo machinectl start machine_name```

**停止**运行中的机器

```sudo machinectl stop machine_name```

在机器中打开**交互式 shell**

```sudo machinectl shell machine_name```

**登录**到一台机器

```sudo machinectl login machine_name```

查看机器**状态**

```machinectl status machine_name```

在机器中**执行**命令

```sudo machinectl shell machine_name /bin/command```

# SYNOPSIS

**machinectl** [_OPTIONS_] _COMMAND_ [_NAME_...]

# DESCRIPTION

**machinectl** 控制 systemd 的机器管理器。它通过 systemd-machined 管理本地容器和虚拟机，包括启动、停止以及与它们交互。

# COMMANDS

**list**
> 列出运行中的机器

**status NAME**
> 显示机器的运行状态

**show NAME**
> 显示机器属性

**start NAME**
> 以 systemd 服务方式启动一台机器

**stop NAME**
> 停止运行中的机器

**poweroff NAME**
> 关闭一台机器的电源

**reboot NAME**
> 重启一台机器

**terminate NAME**
> 立即终止一台机器

**kill NAME**
> 向机器的进程发送信号

**login NAME**
> 打开到机器的登录提示符

**shell [[USER@]NAME [COMMAND...]]**
> 在机器中打开 shell 或运行命令

**copy-to NAME PATH [PATH]**
> 将文件复制到机器中

**copy-from NAME PATH [PATH]**
> 从机器复制文件出来

**bind NAME PATH [PATH]**
> 将目录绑定挂载进机器

**list-images**
> 列出可用的机器镜像

**image-status NAME**
> 显示镜像状态

**pull-raw URL [NAME]**
> 下载 raw 磁盘镜像

**pull-tar URL [NAME]**
> 下载 tar 镜像

**import-raw FILE [NAME]**
> 导入 raw 磁盘镜像

**import-tar FILE [NAME]**
> 导入 tar 归档

**remove NAME**
> 移除机器镜像

**enable NAME**
> 启用机器随系统启动

**disable NAME**
> 禁止机器随系统启动

**clean**
> 移除隐藏或只读的机器镜像

# PARAMETERS

**-p, --property**
> 显示特定属性

**-a, --all**
> 显示所有属性

**-q, --quiet**
> 抑制输出

**--uid USER**
> 运行 shell 命令所用的用户

**-E, --setenv VAR=VALUE**
> 在 shell 中设置环境变量

**-H**, **--host** _USER@HOST_
> 通过 SSH 在远程主机上执行。

**-M**, **--machine** _NAME_
> 在本地容器中执行。

**-h**, **--help**
> 打印简短帮助文本并退出。

**--version**
> 打印简短版本字符串并退出。

**--no-pager**
> 不将输出送入分页器。

**--no-legend**
> 不打印图例（列标题和提示）。

# CAVEATS

机器通常使用 systemd-nspawn 启动。shell 命令要求 systemd-machined 正在运行。容器镜像存储在 /var/lib/machines/ 中。

# HISTORY

**machinectl** 是 **systemd** 的一部分，通过 systemd-machined 和 systemd-nspawn 提供容器和虚拟机管理。

# INSTALL

```apt: sudo apt install systemd-container```

```dnf: sudo dnf install systemd-container```

```zypper: sudo zypper install systemd-container```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-nspawn](/man/systemd-nspawn)(1), [systemctl](/man/systemctl)(1)
