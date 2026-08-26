# TAGLINE

创建用于共享文件的 SMB 服务器

# TLDR

**启动共享当前目录的 SMB 服务器**

```impacket-smbserver [sharename] .```

**共享指定目录**

```impacket-smbserver [sharename] [/path/to/share]```

**使用 SMB2 协议**

```impacket-smbserver -smb2support [sharename] [path]```

**要求身份验证**

```impacket-smbserver -username [user] -password [pass] [sharename] [path]```

**指定绑定的 IP**

```impacket-smbserver -ip [0.0.0.0] [sharename] [path]```

# SYNOPSIS

**impacket-smbserver** [_options_] _sharename_ _path_

# PARAMETERS

**-smb2support**
> 启用 SMB2 协议支持。

**-username** _user_
> 要求用户名进行身份验证。

**-password** _pass_
> 要求密码进行身份验证。

**-ip** _address_
> 要绑定的 IP 地址。

**-port** _port_
> 监听端口（默认 445）。

# DESCRIPTION

**impacket-smbserver** 创建一个用于共享文件的 SMB 服务器。属于 Impacket 工具集。适用于渗透测试期间与 Windows 系统互传文件。支持 SMB1 和 SMB2 协议以及可选的身份验证。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[samba](/man/samba)(1), [impacket-smbclient](/man/impacket-smbclient)(1)
