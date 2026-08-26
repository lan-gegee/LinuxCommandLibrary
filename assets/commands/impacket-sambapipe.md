# TAGLINE

通过 SMB 连接远程 Windows 系统上的命名管道

# TLDR

**访问远程 SMB 共享上的命名管道**

```impacket-sambapipe '[domain]/[user]:[password]@[192.168.1.100]' '[pipename]'```

**使用 NTLM 哈希连接管道**

```impacket-sambapipe -hashes ':[nthash]' '[domain]/[user]@[192.168.1.100]' '[pipename]'```

**通过 Kerberos 身份验证访问管道**

```impacket-sambapipe -k -no-pass '[domain]/[user]@[target]' '[pipename]'```

# SYNOPSIS

**impacket-sambapipe** [_-h_] [_-hashes LMHASH:NTHASH_] [_-no-pass_] [_-k_] [_-aesKey KEY_] [_-dc-ip IP_] _target_ _pipe_

# PARAMETERS

**-hashes** _LMHASH:NTHASH_
> 使用 NTLM 哈希而非密码进行身份验证

**-no-pass**
> 不询问密码（与 -k 搭配时有用）

**-k**
> 使用 ccache 文件中的 Kerberos 身份验证

**-aesKey** _KEY_
> 用于 Kerberos 身份验证的 AES 密钥

**-dc-ip** _IP_
> 域控制器的 IP 地址（用于 Kerberos）

# DESCRIPTION

**impacket-sambapipe** 通过 SMB 连接远程 Windows 系统上的命名管道。命名管道是 Windows 中进程间通信的方式，许多服务都通过管道暴露功能。

该工具适用于与通过命名管道通信的服务交互、测试管道的可访问性，或作为涉及管道通信的更复杂攻击链的一环。

# CAVEATS

需要拥有访问命名管道的相应权限。某些管道需要管理员权限。管道必须存在于目标系统上且可访问。

# HISTORY

属于 SecureAuth 的 **Impacket** 库。命名管道访问是许多 Windows 协议和服务的基础，使该工具在多种测试场景中都很有用。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[impacket-smbclient](/man/impacket-smbclient)(1), [smbclient](/man/smbclient)(1), [rpcclient](/man/rpcclient)(1)
