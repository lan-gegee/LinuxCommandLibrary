# TAGLINE

netExec RDP 模块

# TLDR

**检查 RDP 凭据**

```nxc rdp [target] -u [user] -p [password]```

**登录时截取屏幕截图**

```nxc rdp [target] -u [user] -p [password] --screenshot```

**检查 NLA 状态**

```nxc rdp [target] -u [user] -p [password] --nla```

**扫描多台主机**

```nxc rdp [targets.txt] -u [user] -p [password]```

# SYNOPSIS

**nxc** **rdp** [_target_] [_options_]

# PARAMETERS

_TARGET_
> RDP 服务器地址。

**-u** _USER_
> 用户名。

**-p** _PASSWORD_
> 密码。

**--screenshot**
> 登录时截取屏幕截图。

**--nla**
> 检查 NLA 状态。

**-H** _HASH_
> 用于哈希传递的 NT 哈希。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nxc rdp** 是 NetExec 的 RDP 模块，用于测试远程桌面凭据。

该工具可验证 RDP 访问权限，是 NetExec 套件的一部分。

# CAVEATS

安全工具。仅限授权使用。NetExec 的组成部分。

# HISTORY

nxc rdp 在 NetExec 中提供 **RDP 渗透测试**功能。

# SEE ALSO

[nxc](/man/nxc)(1), [rdesktop](/man/rdesktop)(1), [xfreerdp](/man/xfreerdp)(1)
