# TLDR

**连接远程服务器**

```ssh [user]@[hostname]```

**在指定端口上连接**

```ssh -p [port] [user]@[hostname]```

**使用指定的身份文件**（私钥）连接

```ssh -i [~/.ssh/id_rsa] [user]@[hostname]```

**在远程服务器上运行命令**

```ssh [user]@[hostname] "[command]"```

**创建本地端口转发**（隧道）

```ssh -L [local_port]:[target_host]:[target_port] [user]@[hostname]```

**创建远程端口转发**

```ssh -R [remote_port]:localhost:[local_port] [user]@[hostname]```

**创建 SOCKS 代理**

```ssh -D [port] [user]@[hostname]```

**启用 X11 转发**

```ssh -X [user]@[hostname]```

**将 SSH 密钥复制到服务器**以实现免密登录

```ssh-copy-id [user]@[hostname]```

# SYNOPSIS

**ssh** [**-p** _port_] [**-i** _identity_file_] [**-L** _forward_] [_user_**@**]_hostname_ [_command_]

# PARAMETERS

**-p** _port_
> 连接指定端口（默认：22）

**-i** _identity_file_
> 使用指定的私钥文件

**-l** _login_name_
> 指定用户名（user@host 的替代写法）

**-L** [_bind_:]_port_:_host_:_port_
> 本地端口转发

**-R** [_bind_:]_port_:_host_:_port_
> 远程端口转发

**-D** [_bind_:]_port_
> 动态端口转发（SOCKS 代理）

**-N**
> 不执行远程命令（用于隧道）

**-f**
> 认证后转入后台

**-X**
> 启用 X11 转发

**-Y**
> 启用受信任的 X11 转发

**-A**
> 启用代理转发

**-C**
> 启用压缩

**-v**
> 详细模式（用 -vvv 可获得更多信息）

**-o** _option_
> 设置配置选项

**-J** _jump_host_
> 通过跳板机连接（ProxyJump）

**-t**
> 强制分配伪终端

# DESCRIPTION

**ssh**（Secure Shell）在不安全的网络上的主机之间提供安全加密的通信。它是远程服务器管理和安全文件传输的主要工具。

认证可以使用密码或公钥加密。基于密钥的认证更安全也更方便；使用 **ssh-keygen** 生成密钥，再用 **ssh-copy-id** 将公钥复制到服务器。

端口转发可为其他流量创建加密隧道。本地转发（**-L**）让远程服务在本地可用。远程转发（**-R**）把本地服务暴露在远程主机上。动态转发（**-D**）则创建 SOCKS 代理。

通过 **~/.ssh/config** 可以定义带自定义设置（端口、用户、身份文件、代理）的主机，让复杂的连接变得简单。

# CONFIGURATION

**~/.ssh/config**
> 每用户配置文件，定义主机别名、默认端口、用户名、身份文件、代理设置及其他连接选项。

**~/.ssh/known_hosts**
> 已验证主机密钥的数据库，用于检测服务器仿冒。

**/etc/ssh/ssh_config**
> 应用于所有用户的系统级 SSH 客户端配置。

# CAVEATS

首次连接新主机时会出现指纹警告。接受之前请通过可信渠道核实指纹。

代理转发（**-A**）虽然方便，但在不受信任的服务器上有风险。建议改用 **ProxyJump**。

私钥务必妥善保管，权限设为 600。为密钥设置口令保护，并配合 ssh-agent 避免重复输入口令。

防火墙规则可能封锁 SSH。22 端口常被过滤；在这类网络中可考虑让 SSH 使用其他端口运行。

# INSTALL

```apt: sudo apt install openssh-client```

```apk: sudo apk add dropbear-ssh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scp](/man/scp)(1), [sftp](/man/sftp)(1), [ssh-keygen](/man/ssh-keygen)(1), [ssh-copy-id](/man/ssh-copy-id)(1), [ssh-agent](/man/ssh-agent)(1)
