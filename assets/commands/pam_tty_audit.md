# TAGLINE

记录 TTY 击键

# TLDR

**启用 TTY 审计**

```session required pam_tty_audit.so enable=*```

**审计特定用户**

```session required pam_tty_audit.so enable=admin,root```

**对某些用户禁用**

```session required pam_tty_audit.so disable=service_account```

# SYNOPSIS

**pam_tty_audit.so** [_options_]

# PARAMETERS

**enable=**_PATTERN_
> 为匹配以逗号分隔模式的用户启用 TTY 审计（使用 `*` 表示所有用户）。

**disable=**_PATTERN_
> 为匹配的用户禁用 TTY 审计；与 `enable=` 一并处理，因此顺序很重要。

**open_only**
> 只在会话打开时设置审计标志，而不是在整个登录会话期间。

**log_passwd**
> 同时记录 TTY 处于非回显（密码）模式时输入的击键。出于隐私考虑默认禁用。

**debug**
> 通过 `syslog(3)` 记录额外的调试信息。

# DESCRIPTION

**pam_tty_audit** 是一个 PAM session 模块，在会话打开时切换每进程的 TTY 输入审计标志（`task->signal->audit_tty`），并在会话关闭时恢复它。启用后，受影响进程从控制 TTY 读取的每一次击键都会被内核记录，并以 `TTY` 记录的形式转发给 **auditd**。

它通常作为 `session` 规则放在 `/etc/pam.d/system-auth`（或各发行版的对应文件）中，用于满足要求记录管理员 Shell 活动的合规性要求（PCI-DSS、STIG）。

# CAVEATS

需要内核的 `CONFIG_AUDIT_TTY` 特性以及正在运行的 **auditd**。记录击键涉及严重的隐私问题，如果设置了 `log_passwd`，可能会捕获非回显模式下输入的密码。审计记录写入 `/var/log/audit/audit.log`；可用 **aureport --tty** 或 **ausearch -m TTY** 查看。

# HISTORY

pam_tty_audit 提供满足合规性要求的**击键审计**功能。

# SEE ALSO

[pam](/man/pam)(8), [auditd](/man/auditd)(8), [aureport](/man/aureport)(8)
