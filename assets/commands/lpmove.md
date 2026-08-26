# TAGLINE

在打印队列之间移动打印任务

# TLDR

**将任务移动到另一台打印机**

```lpmove [job_id] [destination_printer]```

**移动某台打印机的所有任务**

```lpmove [source_printer] [destination_printer]```

**移动指定任务**

```lpmove [printer]-[job_id] [destination]```

# SYNOPSIS

**lpmove** [_options_] _job_ _destination_

**lpmove** [_options_] _source_ _destination_

# PARAMETERS

_JOB_
> 任务 ID 号，或旧目的地加任务 ID（如 oldprinter-123）。

_SOURCE_
> 源打印机名称（会移动该打印机的所有任务）。

_DESTINATION_
> 目标打印机名称。

**-E**
> 连接服务器时强制加密。

**-U _username_**
> 指定其他用户名。

**-h _server[:port]_**
> 指定其他服务器。

# DESCRIPTION

**lpmove** 在队列之间移动打印任务，将任务从一台打印机转移到另一台。

当某台打印机发生故障或需要维护时，该工具很有用。任务会在新队列中继续等待。

# CAVEATS

需要管理员权限。任务必须处于待处理状态。CUPS 必须处于运行状态。

# HISTORY

lpmove 属于 **CUPS**，用于在打印机队列之间转移打印任务。

# INSTALL

```apt: sudo apt install cups-client```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cancel](/man/cancel)(1), [lp](/man/lp)(1), [lpq](/man/lpq)(1), [lpr](/man/lpr)(1), [lprm](/man/lprm)(1), [lpadmin](/man/lpadmin)(8), [lpstat](/man/lpstat)(1)
