# TAGLINE

用于设置默认 SELinux 安全上下文的 PAM 模块

# TLDR

为会话**设置 SELinux 上下文**

```session required pam_selinux.so```

在其他 session 模块之前**关闭会话**上下文

```session required pam_selinux.so close```

在其他 session 模块之后**打开会话**上下文

```session required pam_selinux.so open```

**提示用户选择**安全上下文角色

```session required pam_selinux.so select_context```

**从 PAM 环境**变量获取上下文

```session required pam_selinux.so env_params```

启用详细输出，**在设置上下文时告知用户**

```session required pam_selinux.so open verbose```

# SYNOPSIS

**pam_selinux.so** [**open**] [**close**] [**restore**] [**nottys**] [**debug**] [**verbose**] [**select_context**] [**env_params**] [**use_current_range**]

# PARAMETERS

**open**
> 只执行模块的 open_session 部分，即设置执行和终端安全上下文。

**close**
> 只执行模块的 close_session 部分，即恢复先前的安全上下文。

**restore**
> 在 open_session 中临时恢复到上一次模块调用之前的安全上下文。当 open 和 close 无法包住其他 session 模块时有用。

**nottys**
> 不设置控制终端的安全上下文。

**debug**
> 通过 syslog(3) 开启调试消息。

**verbose**
> 在安全上下文被设置时尝试通知用户。

**select_context**
> 提示用户为安全上下文选择自定义角色。与 **env_params** 互斥。

**env_params**
> 从 PAM 环境变量（SELINUX_ROLE_REQUESTED、SELINUX_LEVEL_REQUESTED、SELINUX_USE_CURRENT_RANGE）获取自定义的安全上下文角色。与 **select_context** 互斥。

**use_current_range**
> 使用当前进程的 MLS 敏感度级别而不是默认值。

# DESCRIPTION

**pam_selinux** 是一个 PAM 模块，为通过认证的用户会话设置默认的 SELinux 安全上下文。它分两个阶段工作：**open_session** 设置执行和控制终端的安全上下文；**close_session** 在会话结束时恢复先前保存的上下文。

在典型的 PAM 配置中，该模块被调用两次——一次带 **close** 放在其他 session 模块之前，一次带 **open** 放在其后。这样可确保其他模块以调用者的上下文运行，而用户会话则获得适当的 SELinux 上下文。

# RETURN VALUES

**PAM_SUCCESS**
> 安全上下文设置成功。

**PAM_SESSION_ERR**
> 无法获取或设置有效的上下文。

**PAM_USER_UNKNOWN**
> 系统无法识别该用户。

**PAM_BUF_ERR**
> 内存分配失败。

# CAVEATS

仅适用于启用了 SELinux 的系统。该模块只提供 **session** 模块类型。**select_context** 和 **env_params** 选项互斥。

# SEE ALSO

[pam](/man/pam)(8), [pam.d](/man/pam.d)(5), [chcon](/man/chcon)(1), [semanage](/man/semanage)(8), [sestatus](/man/sestatus)(8), [getenforce](/man/getenforce)(8)
