# TAGLINE

关闭系统并切断电源

# TLDR

**关闭**系统电源

```poweroff```

**挂起**系统

```poweroff --halt```

**重启**系统

```poweroff --reboot```

**立即**关机（强制）

```poweroff -f```

**只**写入 wtmp 记录

```poweroff -w```

# SYNOPSIS

**poweroff** [**-f**|**--force**] [**-w**|**--wtmp-only**] [**--halt**] [**--reboot**]

# PARAMETERS

**-f, --force**
> 不经由系统管理器强制立即关机

**-w, --wtmp-only**
> 只写入 wtmp 记录而不实际关机

**--halt**
> 挂起而不是断电

**--reboot**
> 重启而不是断电

**-n, --no-wtmp**
> 不写入 wtmp 记录

# DESCRIPTION

**poweroff** 关闭系统并切断电源。在支持 ACPI 或 APM 的系统上，它会在关机完成后通知硬件切断电源。

该命令通常是指向 systemctl 或 init 系统关机机制的符号链接。它确保以干净的方式关闭系统，正确终止各项服务。

# CAVEATS

强制选项可能导致数据丢失。需要 root 权限。具体行为因 init 系统而异。虚拟机可能不响应断电信号。

# HISTORY

**poweroff** 一直是 Unix 中标准的系统关机命令。现代实现与 systemd 或其他 init 系统集成，同时保留了传统接口。

# INSTALL

```apt: sudo apt install runit-init```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[shutdown](/man/shutdown)(8), [halt](/man/halt)(8), [reboot](/man/reboot)(8), [systemctl](/man/systemctl)(1)
