# TAGLINE

从队列中移除打印任务

# TLDR

**取消所有任务**

```lprm -```

**取消指定任务**

```lprm [job_id]```

**取消某台打印机上的任务**

```lprm -P [printer] -```

**取消用户的任务**

```lprm [username]```

**按 ID 取消打印机上的任务**

```lprm -P [printer] [job_id]```

# SYNOPSIS

**lprm** [_options_] [_job_]

# PARAMETERS

_JOB_
> 任务 ID 或 "-" 表示全部。

**-P** _PRINTER_
> 指定打印机。

**-E**
> 强制加密。

**-U** _USER_
> 指定用户名。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lprm** 从队列中移除打印任务，可取消待处理或正在处理的任务。

它是 BSD 风格的任务移除命令。非 root 用户只能移除自己的任务。

# CAVEATS

需要 CUPS。普通用户仅能删除自己的任务。可能无法停止已经开始的打印。

# HISTORY

lprm 起源于 **BSD Unix** 的打印任务移除工具，现由 CUPS 实现。

# INSTALL

```apt: sudo apt install lpr```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lp](/man/lp)(1), [lpr](/man/lpr)(1), [lpq](/man/lpq)(1), [cancel](/man/cancel)(1)
