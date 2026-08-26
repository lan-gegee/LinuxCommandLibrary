# TAGLINE

停止打印机处理任务

# TLDR

**禁用打印机**

```cupsdisable [printer_name]```

**附带原因禁用**

```cupsdisable -r "[maintenance]" [printer_name]```

**禁用并取消所有任务**

```cupsdisable -c [printer_name]```

# SYNOPSIS

**cupsdisable** [**-E**] [**-U** _user_] [**-c**] [**-h** _server_[:_port_]] [**-r** _reason_] [**--hold**] _destination_...

# PARAMETERS

**-c**
> 禁用目标后，取消其队列中的所有任务。

**-r** _reason_
> 附加到停止状态的原因信息，会由 **lpstat** 报告。

**-E**
> 强制加密与 CUPS 服务器的连接。

**-U** _user_
> 以 _user_ 而非当前登录用户进行身份验证。

**-h** _server_[:_port_]
> 连接到指定的 CUPS 服务器（默认：$CUPS_SERVER，其次 localhost:631）。

**--hold**
> 当前任务完成后保留所有剩余的排队任务——适合在执行中的任务完成后进行维护。

# DESCRIPTION

**cupsdisable** 让 CUPS 打印机或类停止处理后续任务。默认情况下，正在打印的任务继续完成，但新任务会排队等待，直到用 **cupsenable** 重新启用该目标。使用 **-c** 会取消所有任务；使用 **--hold** 则让当前任务完成后将其余任务置于保留状态（之后可用 **cupsenable --release** 释放）。

需要 CUPS 管理员权限（属于 **lpadmin** 组或 root）。

# CAVEATS

在 CUPS 1.5+ 中，同一二进制文件也以 **cupsdisable** 名称安装，以兼容历史上的 Berkeley **disable** 命令——实际上规范名称就是 **cupsdisable**。某些发行版仅以该名称提供。

# INSTALL

```apt: sudo apt install cups-client```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cupsenable](/man/cupsenable)(1), [cupsaccept](/man/cupsaccept)(1), [cupsreject](/man/cupsreject)(1)
