# TAGLINE

FileZilla 的 SFTP 连接处理模块

# TLDR

**显示版本信息**

```fzsftp -V```

**连接到服务器**

```fzsftp [user@host]```

**在指定端口连接**

```fzsftp -P [2222] [user@host]```

**使用指定的私钥文件**

```fzsftp -i [key.ppk] [user@host]```

**从批处理文件运行命令**

```fzsftp -b [commands.txt] [user@host]```

**以详细输出模式连接**

```fzsftp -v [user@host]```

# SYNOPSIS

**fzsftp** [_options_] [_user@host_]

# PARAMETERS

**-V**
> 打印版本信息并退出。

**-P** _port_
> 连接到指定端口。

**-l** _user_
> 以指定用户名连接。

**-pw** _password_
> 用指定密码登录（不安全）。

**-i** _keyfile_
> 用于用户身份验证的私钥文件。

**-b** _file_
> 使用指定的批处理文件。

**-bc**
> 回显批处理文件中的命令。

**-be**
> 出错时不停止批处理文件的执行。

**-batch**
> 禁用所有交互式提示。

**-v**
> 显示详细消息。

**-C**
> 启用压缩。

**-1**, **-2**
> 强制使用 SSH 协议版本 1 或 2。

**-4**, **-6**
> 强制使用 IPv4 或 IPv6。

**-load** _session_
> 从已保存的会话加载设置。

**-noagent**
> 禁用 Pageant。

**-agent**
> 启用 Pageant。

**-hostkey** _fingerprint_
> 手动指定主机密钥（可重复使用）。

**-proxycmd** _command_
> 将命令用作本地代理。

**-sshlog** _file_
> 将协议细节记录到文件。

# DESCRIPTION

**fzsftp** 是 FileZilla 的 SFTP 后端模块，基于 PuTTY 的 **psftp** 组件。它由 FileZilla 图形界面内部调用，负责处理 SSH 文件传输协议连接，并非为直接交互使用而设计。

该工具通过 stdin/stdout 与 FileZilla 进程通信。它原生支持 PuTTY 格式（.ppk）密钥、批处理文件处理，以及从 PuTTY 继承的多种 SSH 连接选项。

# CAVEATS

不应直接使用；它由 FileZilla 内部调用。命令行上的密码不安全，会在进程列表中可见。PPK 密钥需要转换后才能在其他 SSH 客户端中使用。

# INSTALL

```apt: sudo apt install filezilla```

```dnf: sudo dnf install filezilla```

```pacman: sudo pacman -S filezilla```

```apk: sudo apk add filezilla```

```zypper: sudo zypper install filezilla```

```nix: nix profile install nixpkgs#filezilla```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sftp](/man/sftp)(1), [filezilla](/man/filezilla)(1), [scp](/man/scp)(1), [ssh](/man/ssh)(1)
