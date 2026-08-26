# TAGLINE

在远程 Windows 主机上执行 MS-RPC 命令

# TLDR

**连接**到远程主机

```rpcclient -U domain\username%password ip_address```

以**无密码**方式连接

```rpcclient -U username -W domain -N ip_address```

使用**密码哈希**连接

```rpcclient -U domain\username --pw-nt-hash ip_address```

执行 **shell 命令**

```rpcclient -U domain\username%password -c "command1;command2" ip_address```

显示**域用户**（交互式）

```rpcclient $> enumdomusers```

显示**用户信息**（交互式）

```rpcclient $> queryuser username```

**枚举域组**（交互式）

```rpcclient $> enumdomgroups```

**按名称查找 SID**（交互式）

```rpcclient $> lookupnames username```

**获取服务器信息**（交互式）

```rpcclient $> srvinfo```

**创建**域用户（交互式）

```rpcclient $> createdomuser username```

# SYNOPSIS

**rpcclient** [_options_] _server_

# PARAMETERS

**-U**, **--user** _user_
> 用于身份验证的用户名（domain\user%password 格式）

**-W**, **--workgroup** _domain_
> 工作组或域名

**-N**, **--no-pass**
> 不使用密码连接

**--pw-nt-hash**
> 密码为 NT 哈希

**-c**, **--command** _commands_
> 执行以分号分隔的命令

**-A**, **--authentication-file** _file_
> 从文件读取凭据（用户名、密码、域名）

**-k**, **--kerberos**
> 使用 Kerberos 身份验证

**-I**, **--dest-ip** _ip_
> 指定目标 IP 地址

# DESCRIPTION

**rpcclient** 是 Samba 套件中的一个 MS-RPC 客户端工具。它可以对 Windows 系统和 Samba 服务器执行 RPC 命令，用于用户管理、信息枚举和管理操作。

交互模式提供了一个 shell，可用于执行 enumdomusers、queryuser、createdomuser 等 RPC 命令。

# CAVEATS

大多数操作需要有效的凭据。某些命令需要目标系统上的管理员权限。

# HISTORY

属于 **Samba** 套件，为 Unix 系统提供与 Windows 互操作的工具。

# INSTALL

```apt: sudo apt install smbclient```

```dnf: sudo dnf install samba-client```

```pacman: sudo pacman -S smbclient```

```apk: sudo apk add samba-client```

```zypper: sudo zypper install samba-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smbclient](/man/smbclient)(1), [net](/man/net)(8), [enum4linux](/man/enum4linux)(1), [nmap](/man/nmap)(1)
