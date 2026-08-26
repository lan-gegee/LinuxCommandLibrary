# TAGLINE

SSH 和 Telnet 终端模拟器

# TLDR

**连接到 SSH 服务器**

```putty -ssh [user@host]```

**使用指定端口连接**

```putty -ssh -P [2222] [user@host]```

**加载已保存的会话**

```putty -load "[session_name]"```

**通过串口连接**

```putty -serial [/dev/ttyUSB0]```

**使用私钥**

```putty -ssh -i [key.ppk] [user@host]```

# SYNOPSIS

**putty** [_options_] [_host_]

# PARAMETERS

_HOST_
> 目标主机名。

**-ssh**
> 使用 SSH 协议。

**-telnet**
> 使用 Telnet 协议。

**-serial**
> 打开串口连接。

**-raw**
> 使用原始 TCP（不做协议层处理）。

**-rlogin**
> 使用 Rlogin 协议。

**-l** _USER_
> 指定登录用户名。

**-pw** _PASSWORD_
> 在命令行提供密码（不安全；建议使用 **-pwfile**）。

**-pwfile** _FILE_
> 从 _FILE_ 的第一行读取密码。

**-P** _PORT_
> 端口号。

**-i** _KEY_
> 私钥文件（PPK 格式）。

**-load** _SESSION_
> 按名称加载已保存的会话。

**-X** / **-x**
> 启用 / 禁用 X11 转发。

**-A** / **-a**
> 启用 / 禁用代理转发。

**-C**
> 启用压缩。

**-L** _local:host:port_
> 将本地端口转发到远程目标。

**-R** _remote:host:port_
> 将远程端口转发回本地机器。

**-D** _port_
> 打开 SOCKS 动态端口转发监听器。

**-m** _FILE_
> 在远程主机上执行 _FILE_ 的内容，而不是交互式 shell。

**-N**
> 不启动 shell 或命令（仅用于端口转发）。

**-nc** _host:port_
> 通过 SSH 服务器建立 TCP 连接而不是 shell。

**-t** / **-T**
> 强制 / 阻止伪终端分配。

**-agent** / **-noagent**
> 启用 / 禁用 Pageant 身份验证。

# DESCRIPTION

**PuTTY** 是一个免费的终端模拟器和网络文件传输应用程序，支持 SSH、Telnet、SCP 和串口连接。它最初为没有内置 SSH 客户端的 Windows 开发，如今已成为使用最广泛的远程访问工具之一，也可在 Linux 和 macOS 上使用。

PuTTY 将连接配置保存为会话（saved sessions），可以借助预先配置好的端口、协议、密钥认证和终端外观等设置快速访问常用服务器。它使用自己的 **PPK** 密钥格式，不过可以使用配套的 **puttygen** 工具在 PPK 与 OpenSSH 格式之间转换密钥。PuTTY 套件包括用于命令行连接的 **plink**、用于文件传输的 **pscp** 和 **psftp**，以及用于 SSH agent 密钥管理的 **pageant**。

# CONFIGURATION

**~/.putty/sessions/**
> 已保存的会话配置，包含连接设置、端口、协议、密钥文件路径和终端配置。

**~/.putty/sshhostkeys**
> 已知服务器的 SSH 主机密钥缓存，用于检测中间人攻击。

**~/.putty/sshkeys/**
> 存放 PPK 格式私钥文件的目录，用于公钥认证。

# CAVEATS

使用 PPK 密钥格式；可用 **puttygen** 转换 OpenSSH 密钥。**-pw** 选项会将密码暴露给任何能读取进程列表的人——建议改用 **-pwfile** 或基于密钥的身份验证。PuTTY 也可在 Linux 和 macOS 上使用。

# HISTORY

PuTTY 由 **Simon Tatham** 创建，于 **1999 年**首次发布。它曾是 Windows 上的标准 SSH 客户端——在 Windows 10（2018 年）之前 Windows 并无内置 SSH 客户端。

# INSTALL

```apt: sudo apt install putty```

```dnf: sudo dnf install putty```

```pacman: sudo pacman -S putty```

```apk: sudo apk add putty```

```zypper: sudo zypper install putty```

```brew: brew install putty```

```nix: nix profile install nixpkgs#putty```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [plink](/man/plink)(1), [pscp](/man/pscp)(1)
