# TAGLINE

netExec WMI 模块

# TLDR

**检查 WMI 凭据**

```nxc wmi [target] -u [user] -p [password]```

**通过 WMI 执行命令**

```nxc wmi [target] -u [user] -p [password] -x "[command]"```

**查询 WMI**

```nxc wmi [target] -u [user] -p [password] --wmi "[query]"```

**使用哈希身份验证**

```nxc wmi [target] -u [user] -H [hash]```

# SYNOPSIS

**nxc** **wmi** [_target_] [_options_]

# PARAMETERS

_TARGET_
> Windows 主机地址。

**-u** _USER_
> 用户名。

**-p** _PASSWORD_
> 密码。

**-x** _COMMAND_
> 执行命令。

**--wmi** _QUERY_
> WMI 查询字符串。

**-H** _HASH_
> 用于哈希传递的 NT 哈希。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nxc wmi** 是 NetExec 的 WMI 模块，通过 Windows Management Instrumentation 执行操作。

该工具利用 WMI 进行远程执行，是 NetExec 套件的一部分。

# CAVEATS

安全工具。仅限授权使用。NetExec 的组成部分。

# HISTORY

nxc wmi 在 NetExec 中提供**基于 WMI 的执行**功能。

# SEE ALSO

[nxc](/man/nxc)(1), [impacket](/man/impacket)(1)
