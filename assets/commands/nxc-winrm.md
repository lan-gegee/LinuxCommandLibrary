# TAGLINE

netExec WinRM 模块

# TLDR

**检查 WinRM 凭据**

```nxc winrm [target] -u [user] -p [password]```

**执行命令**

```nxc winrm [target] -u [user] -p [password] -x "[command]"```

**执行 PowerShell**

```nxc winrm [target] -u [user] -p [password] -X "[ps_command]"```

**使用哈希身份验证**

```nxc winrm [target] -u [user] -H [hash]```

# SYNOPSIS

**nxc** **winrm** [_target_] [_options_]

# PARAMETERS

_TARGET_
> WinRM 服务器地址。

**-u** _USER_
> 用户名。

**-p** _PASSWORD_
> 密码。

**-x** _COMMAND_
> 执行 cmd 命令。

**-X** _COMMAND_
> 执行 PowerShell 命令。

**-H** _HASH_
> 用于哈希传递的 NT 哈希。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nxc winrm** 是 NetExec 的 WinRM 模块，用于测试 Windows 远程管理。

该工具可验证 WinRM 访问权限并执行命令，是 NetExec 套件的一部分。

# CAVEATS

安全工具。仅限授权使用。NetExec 的组成部分。

# HISTORY

nxc winrm 在 NetExec 中提供 **WinRM 渗透测试**功能。

# SEE ALSO

[nxc](/man/nxc)(1), [evil-winrm](/man/evil-winrm)(1), [winrm](/man/winrm)(1)
