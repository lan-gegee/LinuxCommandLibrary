# TAGLINE

显示并监控 AppArmor 拒绝通知

# TLDR

**显示摘要**：自上次登录以来的 AppArmor 拒绝记录

```aa-notify --since-last```

**显示最近 N 天**的摘要

```aa-notify --since-days [7]```

**轮询日志**并显示桌面通知

```aa-notify --poll --user [username] --display $DISPLAY```

在**指定文件中搜索** AppArmor 消息

```aa-notify --file [/var/log/audit/audit.log]```

**显示详细消息**及摘要

```aa-notify --since-days [3] --verbose```

**延迟显示通知**（启动时有用）

```aa-notify --poll --wait [10]```

# SYNOPSIS

**aa-notify** [_options_]

# PARAMETERS

**-p**, **--poll**
> 持续轮询 AppArmor 日志，并为 DENIED 消息显示桌面通知

**-f** _FILE_, **--file=**_FILE_
> 在 FILE 中搜索 AppArmor 消息，而不是默认的日志位置

**-l**, **--since-last**
> 显示自上次登录以来消息的摘要

**-s** _NUM_, **--since-days=**_NUM_
> 显示最近 NUM 天消息的摘要

**-u** _USER_, **--user=**_USER_
> 以特权身份运行时降权为 USER；配合 --poll 发送桌面通知时必须指定

**-w** _NUM_, **--wait=**_NUM_
> 等待 NUM 秒后再显示通知（自动启动场景有用）

**--display** _$DISPLAY_
> 为桌面通知设置 DISPLAY 环境变量

**-v**, **--verbose**
> 在摘要之外同时显示完整消息

**-h**, **--help**
> 显示用法信息

# DESCRIPTION

**aa-notify** 显示已记录的 AppArmor 安全事件信息，特别是应用尝试执行被其 AppArmor 配置文件阻止的操作时产生的 DENIED 消息。

该工具有两种模式：摘要模式展示指定时间段内历史拒绝事件的报告；轮询模式持续监控日志并实时推送桌面通知。因此它既适合审计历史安全事件，也适合即时接收策略违规告警。

AppArmor 消息从 systemd journal、**/var/log/syslog**、**/var/log/kern.log** 读取；若安装了 auditd，则从 **/var/log/audit/audit.log** 读取。读取这些日志需要相应的权限，通常通过 sudo 运行。

# CAVEATS

桌面通知需要正在运行的显示服务器以及正确的 DISPLAY 环境变量配置。使用 sudo 时 DISPLAY 变量可能被重置，需要显式指定 **--display**。对于装有 auditd 的系统，必须用 **--file /var/log/audit/audit.log** 显式设置日志路径。

# HISTORY

**aa-notify** 是 AppArmor 工具套件的一部分。AppArmor 起源于上世纪 **90 年代末**的 Immunix，于 **2005 年**被 Novell 收购，并在 **2010 年**发布的 Linux 内核 **2.6.36** 版本中进入主线。这个通知守护进程的加入是为了帮助管理员在桌面环境中监控安全事件。

# INSTALL

```apk: sudo apk add apparmor-utils```

```zypper: sudo zypper install apparmor-utils```

```nix: nix profile install nixpkgs#apparmor-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aa-logprof](/man/aa-logprof)(8), [aa-decode](/man/aa-decode)(8), [aa-status](/man/aa-status)(8), [aa-complain](/man/aa-complain)(8), [journalctl](/man/journalctl)(1), [apparmor](/man/apparmor)(7)

# RESOURCES

```[Source code](https://gitlab.com/apparmor/apparmor)```

```[Homepage](https://apparmor.net/)```

```[Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/home)```

<!-- verified: 2026-06-10 -->
