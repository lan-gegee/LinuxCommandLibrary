# TAGLINE

ACPI 事件守护进程

# TLDR

**启动** ACPI 守护进程

```sudo acpid```

以前台模式启动以便调试

```sudo acpid -f```

以自定义**配置目录**启动

```sudo acpid -c [/etc/acpi/events]```

以增强的**调试**输出启动

```sudo acpid -d```

# SYNOPSIS

**acpid** [_-c confdir_] [_-d_] [_-e eventfile_] [_-f_] [_-g group_] [_-l logfile_] [_options_]

# DESCRIPTION

**acpid**（ACPI Event Daemon）监视来自内核的 ACPI 事件并执行相应的 shell 脚本或程序。它处理电源键按下、合上笔记本盖、交流适配器变化、电池状态变化等硬件事件。

守护进程从 /etc/acpi/events/ 读取事件配置文件，并在匹配的事件发生时运行关联的脚本。由此可以自动响应硬件事件，例如合盖时挂起、按下电源键时关机。

# PARAMETERS

**-c** _dir_
> 事件文件的配置目录（默认：/etc/acpi/events）

**-d**
> 启用详细输出的调试模式

**-e** _file_
> 事件源文件（默认：/proc/acpi/event 或 /dev/input/event*）

**-f**
> 前台运行（不守护进程化）

**-g** _group_
> 设置套接字的属组

**-l** _file_
> 日志文件位置（默认：/var/log/acpid）

**-p** _file_
> PID 文件位置

**-s** _file_
> 用于客户端连接的套接字文件

# CONFIGURATION

**/etc/acpi/events/**
> 存放事件规则文件的目录。每个文件定义一个事件模式和事件发生时执行的动作（脚本）。

**/etc/acpi/handler.sh**
> 事件匹配时由 acpid 调用的默认事件处理脚本。它以参数形式接收事件类型和相关参数。

# CAVEATS

访问 ACPI 事件需要 root 权限或相应权限。事件脚本必须可执行。使用 systemd 的现代系统可能改为通过 logind 处理 ACPI 事件。配置不当的脚本可能干扰电源管理。

# HISTORY

**acpid** 开发于 **21 世纪初**，正值 Linux 从 APM（Advanced Power Management）向 ACPI 过渡之际。Tim Hockin 是早期维护者之一。此后该守护进程成为 Linux 系统上笔记本电脑电源管理的标准组件。

# INSTALL

```apt: sudo apt install acpid```

```dnf: sudo dnf install acpid```

```pacman: sudo pacman -S acpid```

```apk: sudo apk add acpid```

```zypper: sudo zypper install acpid```

```nix: nix profile install nixpkgs#acpid```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[acpi](/man/acpi)(1), [acpi_listen](/man/acpi_listen)(8), [systemctl](/man/systemctl)(1), [loginctl](/man/loginctl)(1)

# RESOURCES

```[Source code](https://sourceforge.net/projects/acpid2/)```

<!-- verified: 2026-06-10 -->
