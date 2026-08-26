# TAGLINE

显示当前打印服务的状态信息

# TLDR

**显示所有打印机**

```lpstat -p```

**显示默认打印机**

```lpstat -d```

**显示打印任务**

```lpstat```

**显示指定打印机的任务**

```lpstat -P [printer]```

**显示打印机详细信息**

```lpstat -l -p [printer]```

**显示全部状态信息**

```lpstat -t```

**显示接受任务的打印机**

```lpstat -a```

# SYNOPSIS

**lpstat** [_options_]

# DESCRIPTION

**lpstat** 显示当前打印服务的状态信息，包括 CUPS 的打印机、打印任务和系统配置。

该工具有助于排查打印问题和监控任务队列。

# PARAMETERS

**-a** [_printers_]
> 显示是否接受任务的状态。

**-d**
> 显示默认目的地。

**-o** [_dest_]
> 显示任务。

**-p** [_printers_]
> 显示打印机状态。

**-r**
> 显示调度器是否在运行。

**-s**
> 显示摘要。

**-t**
> 显示所有状态。

**-u** [_users_]
> 显示用户的任务。

**-l**
> 长（详细）输出。

**-W** _which_
> 显示已完成/未完成的任务。

# CAVEATS

信息取决于 CUPS 配置。部分细节需要相应的访问权限。网络打印机的状态可能延迟。

# HISTORY

**lpstat** 遵循 POSIX 打印接口，在各种 Unix 系统上都有实现。由 **Apple** 和 **Michael Sweet** 开发的 CUPS 实现已成为 macOS 和 Linux 上的标准。

# INSTALL

```apt: sudo apt install lprng```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lp](/man/lp)(1), [lpr](/man/lpr)(1), [lpq](/man/lpq)(1), [cancel](/man/cancel)(1), [cupsd](/man/cupsd)(8)
