# TAGLINE

F5 BIG-IP SSL VPN 客户端

# TLDR

**建立**新的 VPN 连接（跳过 CA 检查）

```sudo f5fpc -s -x -t [https://host.example.com]```

**显示当前 VPN 状态**

```sudo f5fpc -i```

**关闭** VPN 连接

```sudo f5fpc -o```

**使用用户名和密码连接**

```sudo f5fpc -s -t [https://host.example.com] -u [username] -p [password]```

**使用指定证书连接**

```sudo f5fpc --start --host [https://host.example.com] --cert [/path/to/cert.pem] --key [/path/to/key.pem]```

# SYNOPSIS

**f5fpc** [_options_]

# PARAMETERS

**-s**, **--start**
> 启动 VPN 连接（立即返回 shell）

**-o**, **--stop**
> 停止 VPN 连接

**-i**, **--info**
> 显示连接状态

**-t**, **--host** _url_
> VPN 服务器 URL [https://]hostname[:port]（--start 必需）

**-u**, **--user** _username_
> 用于身份验证的用户名

**-p**, **--password** _password_
> 用于身份验证的密码

**-r**, **--cert** _file_
> 客户端证书文件

**-k**, **--key** _file_
> 客户端证书密钥文件

**-a**, **--cacert** _file_
> 受信任的 CA 证书

**-x**, **--nocheck**
> 跳过受信任 CA 证书验证

**-b**, **--nonblock**
> 非阻塞模式

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**f5fpc** 是用于 SSL VPN 连接的 F5 BIG-IP Edge Client。它建立到 F5 网络访问服务器的安全 VPN 隧道。

这是面向企业网络的专有商业 VPN 客户端。

# CAVEATS

F5 Networks 的专有软件。需要 root 权限。可能需要先通过浏览器完成初始身份验证。标准软件仓库中没有提供。

# INSTALL

```aur: yay -S f5fpc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openconnect](/man/openconnect)(8), [openvpn](/man/openvpn)(8)
