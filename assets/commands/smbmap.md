# TAGLINE

枚举 SMB 共享权限与访问级别

# TLDR

**列出主机上的共享**

```smbmap -H [192.168.1.100]```

**使用凭据进行身份验证**

```smbmap -H [192.168.1.100] -u [user] -p [password]```

**列出共享内容**

```smbmap -H [192.168.1.100] -u [user] -p [password] -r [share]```

**下载文件**

```smbmap -H [192.168.1.100] -u [user] -p [password] --download '[share/file.txt]'```

**执行命令**

```smbmap -H [192.168.1.100] -u [admin] -p [password] -x '[whoami]'```

# SYNOPSIS

**smbmap** [_options_]

# PARAMETERS

**-H** _host_
> 目标主机。

**-u** _user_
> 用户名。

**-p** _pass_
> 密码。

**-d** _domain_
> 域。

**-r** _share_
> 递归列出共享。

**--download** _path_
> 下载文件。

**--upload** _src_ _dst_
> 上传文件。

**-x** _cmd_
> 执行命令。

**-L**
> 列出驱动器。

# DESCRIPTION

**smbmap** 枚举 SMB 共享的权限和内容。它是一款安全工具，用于经授权的渗透测试和共享审计。可显示读/写访问级别，并支持文件操作。

# CAVEATS

仅用于经授权的安全评估。使用前必须获得适当授权。

# INSTALL

```nix: nix profile install nixpkgs#smbmap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smbclient](/man/smbclient)(1), [enum4linux](/man/enum4linux)(1)
