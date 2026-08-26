# TAGLINE

返回可配置结果的 PAM 模块，用于调试 PAM 栈

# TLDR

在 auth 栈中**强制返回成功**

```auth optional pam_debug.so auth=success```

**强制特定的失败**代码

```auth optional pam_debug.so auth=auth_err```

**将凭据标记为不可用**以测试回退路径

```auth optional pam_debug.so cred=cred_unavail```

**强制 account 阶段失败**

```account required pam_debug.so acct=acct_expired```

**桩替 session 回调**

```session optional pam_debug.so open_session=success close_session=success```

# SYNOPSIS

**pam_debug.so** [_arg=value_...]

# PARAMETERS

**auth=**_VALUE_
> **pam_sm_authenticate** 的返回码。

**cred=**_VALUE_
> **pam_sm_setcred** 的返回码。

**acct=**_VALUE_
> **pam_sm_acct_mgmt** 的返回码。

**prechauthtok=**_VALUE_
> **pam_sm_chauthtok** 的 **PAM_PRELIM_CHECK** 阶段的返回码。

**chauthtok=**_VALUE_
> **pam_sm_chauthtok** 的 **PAM_UPDATE_AUTHTOK** 阶段的返回码。

**open_session=**_VALUE_
> **pam_sm_open_session** 的返回码。

**close_session=**_VALUE_
> **pam_sm_close_session** 的返回码。

_VALUE_ 是任意 PAM 返回常量的小写形式（success、auth_err、perm_denied、user_unknown、ignore 等）。未指定的钩子默认为 **success**。

# DESCRIPTION

**pam_debug** 是一个 Linux-PAM 测试模块，允许管理员为每个 PAM 服务模块钩子指定返回值。它用于在受控的失败条件下演练 PAM 栈、验证 **required**、**requisite**、**sufficient** 和 **optional** 控制标志是否按预期工作，以及验证自定义栈中的回退路径。

该模块本身不执行任何认证：它只是返回所请求的代码（或默认返回 **PAM_SUCCESS**），并通过 syslog 记录每次调用，以便追踪模块的执行顺序。每个参数恰好对应四个 PAM 管理组之一（auth、account、password、session）。

# CAVEATS

严格来说是开发和测试专用模块。在 **/etc/pam.d/** 中将其加载到真实服务的栈里可能完全绕过认证（例如在 **system-auth** 栈中强制 **auth=success**）。相关改动只应出现在临时测试配置中，部署前必须移除。

# HISTORY

**pam_debug** 随 **Linux-PAM** 一同发布，是上游 PAM 源码树的一部分，与 **pam_warn** 和 **pam_deny** 等其他诊断模块并列。它面向模块作者和 PAM 栈维护者，作为开发辅助工具使用。

# SEE ALSO

[pam](/man/pam)(8), [pam.d](/man/pam.d)(5), [pam_deny](/man/pam_deny)(8), [pam_permit](/man/pam_permit)(8)
