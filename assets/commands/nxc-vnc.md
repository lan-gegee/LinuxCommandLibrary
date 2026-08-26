# TAGLINE

netExec VNC 模块

# TLDR

**检查 VNC 访问**

```nxc vnc [target]```

**使用密码进行身份验证**

```nxc vnc [target] -p [password]```

**连接时截取屏幕截图**

```nxc vnc [target] --screenshot```

**扫描多台主机**

```nxc vnc [targets.txt]```

# SYNOPSIS

**nxc** **vnc** [_target_] [_options_]

# PARAMETERS

_TARGET_
> VNC 服务器地址。

**-p** _PASSWORD_
> VNC 密码。

**--screenshot**
> 截取屏幕截图。

**--port** _PORT_
> VNC 端口（默认：5900）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nxc vnc** 是 NetExec 的 VNC 模块，用于测试 VNC 服务器的安全性。

该工具可检查 VNC 身份验证，是 NetExec 套件的一部分。

# CAVEATS

安全工具。仅限授权使用。NetExec 的组成部分。

# HISTORY

nxc vnc 在 NetExec 中提供 **VNC 渗透测试**功能。

# SEE ALSO

[nxc](/man/nxc)(1), [vncviewer](/man/vncviewer)(1), [tigervnc](/man/tigervnc)(1)
