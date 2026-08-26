# TAGLINE

通用 UNIX 打印系统

# TLDR

**列出可用的打印机**

```lpstat -p```

**将文件打印到默认打印机**

```lp [file.pdf]```

**打印到指定打印机**

```lp -d [printer-name] [file.pdf]```

**打印多份**

```lp -n [3] [file.pdf]```

**查看打印队列**

```lpq```

**取消打印任务**

```cancel [job-id]```

**添加打印机**

```lpadmin -p [printer-name] -E -v [ipp://printer/ipp/print] -m everywhere```

# SYNOPSIS

**lp** [_options_] [_file_...]

**lpr** [_options_] [_file_...]

**lpstat** [_options_]

# DESCRIPTION

**CUPS**（Common UNIX Printing System）管理 Linux 上的打印。它使用 IPP 协议进行网络打印，提供 lp、lpr、lpstat 等命令。Web 界面位于 http://localhost:631。

# PRINT COMMANDS

**lp**, **lpr**
> 打印文件

**lpstat**
> 显示打印机状态

**lpq**
> 显示打印队列

**lprm**, **cancel**
> 删除打印任务

**lpadmin**
> 管理打印机

**lpoptions**
> 设置打印机选项

**lpinfo**
> 列出驱动和设备

# PRINT OPTIONS

**-d** _printer_
> 目标打印机

**-n** _copies_
> 打印份数

**-o media=** _size_
> 纸张尺寸（Letter、A4 等）

**-o sides=** _mode_
> two-sided-long-edge、two-sided-short-edge

**-o number-up=** _N_
> 每张纸打印 N 页（1,2,4,6,9,16）

**-o job-hold-until=** _time_
> 将任务保留至指定时间（indefinite、night、weekend）

**-o job-priority=** _N_
> 优先级 1-100

# WEB INTERFACE

管理界面：http://localhost:631/admin

需要用户属于 lpadmin 组。

# CONFIGURATION

**/etc/cups/cupsd.conf**
> CUPS 守护进程的主配置文件，控制服务器行为、访问控制和日志记录。

**/etc/cups/printers.conf**
> 打印机定义与设置（由 cupsd 自动管理）。

**~/.cups/lpoptions**
> 用户专属的默认打印机选项和偏好设置。

# CAVEATS

用 lpstat -p -d 可查看打印机及默认打印机。通过 Web 界面配置最简单。cups-browsed 可自动发现网络打印机。

# INSTALL

```dnf: sudo dnf install cups```

```pacman: sudo pacman -S cups```

```zypper: sudo zypper install cups```

```brew: brew install cups```

```nix: nix profile install nixpkgs#cups```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lp](/man/lp)(1), [lpr](/man/lpr)(1), [lpstat](/man/lpstat)(1), [lpq](/man/lpq)(1), [lprm](/man/lprm)(1), [lpadmin](/man/lpadmin)(8), [lpoptions](/man/lpoptions)(1), [cupsctl](/man/cupsctl)(8)
