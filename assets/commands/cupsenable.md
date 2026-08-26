# TAGLINE

恢复打印机的任务处理

# TLDR

**启用打印机**

```cupsenable [printer_name]```

**启用并释放被保留的任务**

```cupsenable --release [printer_name]```

**启用远程服务器上的打印机**

```cupsenable -h [server:port] [printer_name]```

**以指定用户身份验证**

```cupsenable -U [username] [printer_name]```

**强制使用加密连接**

```cupsenable -E [printer_name]```

# SYNOPSIS

**cupsenable** [**-E**] [**-U** _username_] [**-c**] [**-h** _server[:port]_] [**--release**] _destination(s)_

# PARAMETERS

**-E**
> 强制加密与服务器的连接。

**-U** _username_
> 连接服务器时使用指定的用户名。

**-c**
> 取消指定目标上的所有任务。

**-h** _server[:port]_
> 连接到指定的服务器和端口。

**--release**
> 释放先前保留的任务以供打印。在 **cupsdisable --hold** 之后用于恢复打印。

# DESCRIPTION

**cupsenable** 启动指定的打印机或类，使其能够处理排队的任务。其效果与 **cupsdisable** 相反。

与 System V 版本（_enable_ / _disable_）不同，CUPS 命令已改名，以避免与 bash(1) 内建命令冲突。打印机和类的名称不区分大小写，可包含除空格、TAB、"/" 或 "#" 之外的任何可打印字符。

# CAVEATS

根据 CUPS 配置的不同，该命令可能提示输入管理员密码而不是要求 root 用户。**--release** 选项通常与 **cupsdisable --hold** 配合，用于计划性维护。

# INSTALL

```apt: sudo apt install cups-client```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cupsdisable](/man/cupsdisable)(1), [cupsaccept](/man/cupsaccept)(1), [cupsreject](/man/cupsreject)(1), [cancel](/man/cancel)(1), [lp](/man/lp)(1), [lpadmin](/man/lpadmin)(1), [lpstat](/man/lpstat)(1)
