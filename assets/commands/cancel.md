# TAGLINE

取消 CUPS 打印任务

# TLDR

**取消默认打印机上当前正在打印的任务**

```cancel```

**按 ID 取消指定打印任务**

```cancel [job_id]```

**取消指定打印机上的打印任务**

```cancel [printer_name]-[job_id]```

**取消指定打印机上的所有打印任务**

```cancel -a [printer_name]```

**取消所有打印机上的所有打印任务**

```cancel -a```

**取消指定用户拥有的所有任务**

```cancel -u [username]```

# SYNOPSIS

**cancel** [**-E**] [**-U** _username_] [**-a**] [**-h** _hostname_[**:**_port_]] [**-u** _username_] [**-x**] [_id_] [_destination_] [_destination-id_]

# DESCRIPTION

**cancel** 是一个用于取消打印任务的 CUPS 命令。不带参数时，它会取消默认目标上当前正在打印的任务。可以通过任务 ID、目标打印机或两者同时指定要取消的任务。

任务 ID 由打印系统分配，可用 **lpstat** 查看。destination-id 格式由打印机名和任务 ID 组合而成（如 "myprinter-42"）。

# PARAMETERS

**-a**
> 取消指定目标上的所有任务；未指定目标时取消所有目标上的任务

**-E**
> 连接服务器时强制加密

**-h** _hostname_[**:**_port_]
> 指定备用服务器

**-u** _username_
> 取消指定用户拥有的任务

**-U** _username_
> 指定用于身份验证的用户名

**-x**
> 除取消外还删除任务数据文件

# CONFIGURATION

**/etc/cups/cupsd.conf**
> CUPS 服务器配置，包括控制 Cancel-Jobs 和 Cancel-My-Jobs 权限的操作策略。

**/etc/cups/printers.conf**
> 打印机定义和队列设置。

# CAVEATS

**-a** 和 **-u** 选项需要管理员权限。这些限制由 **cupsd.conf** 中针对 "Cancel-Jobs" 和 "Cancel-My-Jobs" 操作的操作策略控制。

CUPS 打印机名可包含除空格、制表符、"/" 或 "#" 以外的任意可打印字符，且不区分大小写。

# INSTALL

```apt: sudo apt install lprng```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lp](/man/lp)(1), [lpq](/man/lpq)(1), [lpr](/man/lpr)(1), [lprm](/man/lprm)(1), [lpstat](/man/lpstat)(1)
