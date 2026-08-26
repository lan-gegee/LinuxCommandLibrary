# TAGLINE

通用 SMB 客户端，用于列出共享和文件、上传等操作

# TLDR

**连接 SMB 服务器**

```impacket-smbclient [domain]/[user]:[password]@[target]```

**使用 NTLM 哈希连接**

```impacket-smbclient -hashes :[hash] [domain]/[user]@[target]```

**使用 Kerberos 身份验证**

```impacket-smbclient -k [domain]/[user]@[target]```

# SYNOPSIS

**impacket-smbclient** [_options_] _target_

# PARAMETERS

**-hashes** _lm:nt_
> 使用 NTLM 哈希。

**-k**
> 使用 Kerberos 身份验证。

**-dc-ip** _ip_
> 域控制器 IP。

**-target-ip** _ip_
> 目标 IP（与主机名不同时）。

# DESCRIPTION

**impacket-smbclient** 是一个通用 SMB 客户端，可用于在 Windows 系统上列出共享和文件、上传、下载、重命名以及管理目录。属于 Impacket 工具集。支持密码、NTLM 哈希和 Kerberos 身份验证。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smbclient](/man/smbclient)(1), [impacket-psexec](/man/impacket-psexec)(1)
