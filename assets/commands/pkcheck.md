# TAGLINE

检查操作的 PolicyKit 授权状态

# TLDR

**检查授权**

```pkcheck --action-id [org.freedesktop.action] --process [pid]```

**针对指定用户检查**

```pkcheck --action-id [action] --user [username]```

**允许与用户交互**

```pkcheck --action-id [action] --process [pid] --allow-user-interaction```

# SYNOPSIS

**pkcheck** [_options_]

# PARAMETERS

**-a**, **--action-id** _ACTION_
> 要进行授权判定的 polkit 操作标识符（例如 _org.freedesktop.systemd1.manage-units_）。

**-p**, **--process** _PID_[,_START-TIME_,_UID_]
> 对指定进程进行授权判定。提供 _start-time_ 和 _uid_ 可消除 PID 被复用带来的 TOCTOU 风险窗口。

**-u**, **--user** _USER_
> 以特定用户身份进行授权判定（仅可由 **root** 调用）。

**-s**, **--system-bus-name** _NAME_
> 对由 _NAME_ 标识的 D-Bus 连接进行授权判定。

**--allow-user-interaction**
> 允许 polkit 通过已注册的身份验证代理提示用户。

**--enable-internal-agent**
> 在没有注册图形代理时使用内置的文本模式代理（在 TTY 脚本中很有用）。

**--detail** _KEY_ _VALUE_
> 向 polkit 策略传递额外的键/值对（某些操作规则会用到）。

**--help**
> 显示帮助。

# DESCRIPTION

**pkcheck** 查询 polkit 守护进程，判断特定进程、用户或 D-Bus 连接是否有权执行给定操作。它是非图形化授权检查的标准编程入口。

# EXIT STATUS

| 代码 | 含义 |
| --- | --- |
| **0** | 已获得授权。 |
| **1** | 未获授权。 |
| **2** | 显示了帮助 / 调用错误。 |
| **3** | 需要身份验证但未给出 **--allow-user-interaction**。 |

脚本可以根据这些代码决定是通过 **pkexec** 提权还是跳过操作。

# CAVEATS

属于 PolicyKit 的组成部分。需要 polkitd 正在运行。

# HISTORY

pkcheck 是 **PolicyKit** 中用于检查授权策略的部分。

# INSTALL

```apt: sudo apt install polkitd```

```apk: sudo apk add polkit-common```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pkaction](/man/pkaction)(1), [pkexec](/man/pkexec)(1), [polkit](/man/polkit)(8)
