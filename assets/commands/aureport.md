# TAGLINE

根据审计日志生成汇总报告

# TLDR

显示事件**摘要**

```sudo aureport```

报告**登录**情况

```sudo aureport -l```

报告**系统调用**

```sudo aureport -s```

报告**可执行文件**

```sudo aureport -x```

按**时间范围**报告

```sudo aureport -ts start_time -te end_time```

仅报告**失败**事件

```sudo aureport -au --failed --summary```

# SYNOPSIS

**aureport** [_OPTIONS_]

# DESCRIPTION

**aureport** 根据 Linux 审计日志生成汇总报告。它提供多种事件类型的总览，包括登录、认证、文件、系统调用和异常情况。

# PARAMETERS

**-au, --auth**
> 报告认证尝试。

**-l, --login**
> 报告登录事件。

**-s, --syscall**
> 报告系统调用事件。

**-x, --executable**
> 报告可执行文件事件。

**-f, --file**
> 报告文件和 AF_UNIX 套接字事件。

**-u, --user**
> 报告用户事件。

**-c, --config**
> 报告配置变更。

**-ts, --start** _time_
> 报告的开始时间。接受 now、recent、today、yesterday、this-week、boot 等关键字。

**-te, --end** _time_
> 报告的结束时间。接受与 **-ts** 相同的关键字。

**-t, --log**
> 报告每个审计日志文件的起止时间。

**--success**
> 只处理成功的事件。

**--failed**
> 只处理失败的事件。

**--summary**
> 在所选报告中包含汇总统计。

**-i, --interpret**
> 将数字实体（UID、系统调用等）转换为人类可读的名称。

# CONFIGURATION

**/etc/audit/auditd.conf**
> 审计守护进程的主配置，控制日志文件位置、大小和轮转。

**/etc/audit/audit.rules**
> 定义审计系统记录哪些事件。决定了可用于报告的数据范围。

# CAVEATS

需要 root 权限。报告基于现有的审计日志生成，完整性取决于已记录的内容。处理大型日志文件时请使用时间过滤。

# HISTORY

**aureport** 是 **audit** 软件包的一部分，为 Linux 审计框架提供报告能力。

# INSTALL

```apt: sudo apt install auditd```

```dnf: sudo dnf install audit```

```pacman: sudo pacman -S audit```

```apk: sudo apk add audit```

```zypper: sudo zypper install audit```

```nix: nix profile install nixpkgs#audit```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ausearch](/man/ausearch)(8), [auditctl](/man/auditctl)(8), [auditd](/man/auditd)(8)

# RESOURCES

```[Source code](https://github.com/linux-audit/audit-userspace)```

<!-- verified: 2026-06-17 -->
