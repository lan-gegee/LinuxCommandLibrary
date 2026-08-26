# TAGLINE

显示打印队列状态

# TLDR

**显示打印队列**

```lpq```

**显示指定打印机的队列**

```lpq -P [printer]```

**显示所有打印机**

```lpq -a```

**以长格式显示**详细信息

```lpq -l```

**显示特定用户的队列**

```lpq -U [username]```

每 N 秒**持续刷新**

```lpq +[5]```

# SYNOPSIS

**lpq** [_-E_] [_-U username_] [_-h server[:port]_] [_-P destination[/instance]_] [_-a_] [_-l_] [_+interval_]

# PARAMETERS

**-E**
> 连接服务器时强制加密。

**-U** _USERNAME_
> 使用其他用户名。

**-h** _SERVER[:PORT]_
> 使用其他服务器。

**-P** _DESTINATION[/INSTANCE]_
> 指定其他打印机或类名。

**-a**
> 显示所有打印机上的任务。

**-l**
> 长（详细）列表格式。

**+** _INTERVAL_
> 每 _interval_ 秒持续报告队列状态，直到队列为空。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lpq** 显示当前打印队列的状态，列出待处理和正在处理的任务及其所有者、任务 ID、文件名和大小。不带参数时，显示默认打印机的队列。

该工具提供查看打印队列的 BSD 风格接口，现在通常由 CUPS 实现。它可用于检查任务状态、诊断卡住的队列以及监控打印活动。

# CAVEATS

需要 CUPS。输出格式因实现而异。属于旧式 BSD 接口。

# HISTORY

lpq 起源于 **BSD Unix** 的打印队列查看工具，现由 CUPS 实现。

# INSTALL

```apt: sudo apt install lpr```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lp](/man/lp)(1), [lpr](/man/lpr)(1), [lprm](/man/lprm)(1), [lpstat](/man/lpstat)(1), [cancel](/man/cancel)(1)
