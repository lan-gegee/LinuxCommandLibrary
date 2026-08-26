# TAGLINE

PuTTY 命令行 SSH 连接工具

# TLDR

**连接到 SSH 服务器**

```plink [user]@[host]```

**执行远程命令**

```plink [user]@[host] [command]```

**使用指定端口**

```plink -P [port] [user]@[host]```

**使用私钥**

```plink -i [key.ppk] [user]@[host]```

**SSH 隧道**

```plink -L [local_port]:[remote_host]:[remote_port] [user]@[host]```

# SYNOPSIS

**plink** [_options_] [_user_@]_host_ [_command_]

# PARAMETERS

_HOST_
> 远程主机（可在前面加上 _user_@）。

**-ssh**, **-telnet**, **-rlogin**, **-raw**, **-serial**
> 强制使用指定的协议。

**-P** _PORT_
> 连接到指定端口。

**-l** _USER_
> 登录用户名。

**-pw** _PASSWORD_
> 使用给定密码登录（不安全；建议改用 -pwfile）。

**-pwfile** _FILE_
> 从文件读取密码。

**-i** _KEY_
> 用于身份验证的私钥文件（.ppk 格式）。

**-load** _SESSION_
> 从保存的 PuTTY 会话加载设置。

**-L** [_bindaddr_:]_port_:_host_:_hostport_
> 将本地端口转发到远程目标。

**-R** [_bindaddr_:]_port_:_host_:_hostport_
> 将远程端口转发到本地目标。

**-D** [_bindaddr_:]_port_
> 基于 SOCKS 的动态本地端口转发。

**-N**
> 不启动 Shell 或命令（仅限 SSH-2）。

**-T**, **-t**
> 禁用/启用伪终端分配。

**-A**, **-a**
> 启用/禁用代理转发。

**-X**, **-x**
> 启用/禁用 X11 转发。

**-m** _FILE_
> 从文件读取远程命令。

**-batch**
> 禁用所有交互式提示。

**-v**
> 详细输出。

**--help**
> 显示帮助。

# DESCRIPTION

**plink** 是 PuTTY 套件中的命令行 SSH 连接工具。它提供非交互式的 SSH 访问，用于执行远程命令、端口转发和脚本化的 SSH 操作。

与交互式的 PuTTY 终端不同，plink 专为自动化和批处理操作设计。它支持使用 PuTTY 的 .ppk 密钥格式进行 SSH 密钥认证。**-batch** 标志会禁用所有交互式提示，因此适合脚本和 cron 任务。

# CAVEATS

属于 PuTTY 的一部分。使用 PPK 密钥格式。有 Windows/Unix 版本。

# HISTORY

Plink 是 **PuTTY** 中负责命令行 SSH 操作的部分。

# INSTALL

```apt: sudo apt install putty-tools```

```dnf: sudo dnf install putty```

```pacman: sudo pacman -S putty```

```apk: sudo apk add putty```

```zypper: sudo zypper install putty```

```brew: brew install putty```

```nix: nix profile install nixpkgs#putty```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [putty](/man/putty)(1), [pscp](/man/pscp)(1)
