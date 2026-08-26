# TAGLINE

基于时间的访问控制 PAM 模块

# TLDR

在 PAM 服务配置中**启用基于时间的访问控制**

```account required pam_time.so```

**仅允许在工作时间登录**（周一至周五 08:00-17:00）

```echo "login ; * ; * ; Wk0800-1700" >> /etc/security/time.conf```

**将特定用户的 SSH 访问限制**在工作日

```echo "sshd ; * ; john ; Wk0000-2400" >> /etc/security/time.conf```

**禁止所有用户在周末进行控制台登录**

```echo "login ; tty* ; !root ; !Wd0000-2400" >> /etc/security/time.conf```

# SYNOPSIS

**pam_time.so** [_debug_] [_noaudit_]

# PARAMETERS

**debug**
> 通过 syslog 记录详细的调试信息。

**noaudit**
> 不向审计子系统报告登录拒绝事件。

# CONFIGURATION

**/etc/security/time.conf** 中的规则采用如下格式：

_services_ ; _ttys_ ; _users_ ; _times_

**services**
> PAM 服务名称（例如 login、sshd、su）。使用 * 表示全部。

**ttys**
> 终端名称（例如 tty1、pts/*）。使用 * 表示全部。

**users**
> 用户名或组。加 ! 前缀表示取反。

**times**
> 日/时间段。日期代码：Mo Tu We Th Fr Sa Su Wk Wd Al。时间采用 HHMM-HHMM 格式。加 ! 前缀表示取反。

# DESCRIPTION

**pam_time** 是一个 PAM 模块，可在一天中的不同时段和一周中的特定日子限制对系统或特定应用程序的访问。它不对用户进行认证，而是根据 /etc/security/time.conf 中定义的时间规则来允许或拒绝访问。

规则按顺序求值。每条规则指定受影响的服务、终端和用户，以及允许的时间窗口。该模块通常作为 PAM 配置中的 **account** 类型使用。

# CAVEATS

该模块只在登录时执行限制；当允许的时间窗口结束后，它不会终止已经活动的会话。time.conf 中以 # 开头的行视为注释。空白字符会被忽略，行可以用反斜杠续行。

# HISTORY

**pam_time** 是 **Linux-PAM**（可插拔认证模块）的一部分，为系统登录和服务提供基于时间的访问控制。

# SEE ALSO

[pam](/man/pam)(8), [pam_limits](/man/pam_limits)(8)
