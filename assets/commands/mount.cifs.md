# TAGLINE

在 Linux 上挂载 CIFS 或 SMB 网络共享

# TLDR

**挂载 SMB 共享**并指定用户名（会提示输入密码）

```sudo mount.cifs -o user=[username] //[server]/[share] [mountpoint]```

以**访客身份**挂载（无需密码）

```sudo mount.cifs -o guest //[server]/[share] [mountpoint]```

为挂载的文件设置**属主**

```sudo mount.cifs -o uid=[user],gid=[group] //[server]/[share] [mountpoint]```

使用**凭据文件**挂载

```sudo mount.cifs -o credentials=[path/to/credentials] //[server]/[share] [mountpoint]```

指定 **SMB 协议版本**

```sudo mount.cifs -o vers=3.0 //[server]/[share] [mountpoint]```

以**只读方式**挂载

```sudo mount.cifs -o ro //[server]/[share] [mountpoint]```

# SYNOPSIS

**mount.cifs** _//server/share_ _mount-point_ [**-o** _options_]

# PARAMETERS

**user=_username_**
> 登录用户名；默认取 USER 环境变量

**password=_pass_**
> 登录密码；未设置时使用 PASSWD 变量

**credentials=_file_**
> 包含用户名、密码和域名的凭据文件

**guest**
> 不提示密码直接连接

**domain=_name_**
> Windows 域或工作组名称

**uid=_id_**
> 当服务器未提供属主时，为文件设置的 UID

**gid=_id_**
> 当服务器未提供属主时，为文件设置的 GID

**file_mode=_mode_**
> 覆盖默认的文件权限（如 0644）

**dir_mode=_mode_**
> 覆盖默认的目录权限（如 0755）

**vers=_version_**
> SMB 协议版本：1.0、2.0、2.1、3.0、3.02、3.1.1

**sec=_mode_**
> 安全模式：none、krb5、ntlm、ntlmv2、ntlmssp

**seal**
> 请求 SMB 层加密（需要 SMB3 及以上）

**cache=_mode_**
> 缓存模式：none、strict、loose

**ro**
> 以只读方式挂载

**rw**
> 以读写方式挂载（默认）

**noperm**
> 禁用客户端侧权限检查

**cifsacl**
> 将 CIFS/NTFS ACL 映射到 Linux 权限

# DESCRIPTION

**mount.cifs** 用于在 Linux 上挂载 CIFS（Common Internet File System）或 SMB（Server Message Block）网络共享。它使用 //server/share UNC 语法连接 Windows 文件共享、Samba 服务器和 NAS 设备。

该工具通常通过 mount 命令配合 -t cifs 选项调用。它需要 Linux 内核的 CIFS 文件系统支持。身份验证可以使用用户名/密码、Kerberos 或访客访问。

# CREDENTIALS FILE FORMAT

```
username=myuser
password=mypassword
domain=WORKGROUP
```

# CAVEATS

包含逗号的密码无法在命令行上正确解析；请改用凭据文件或环境变量。cache=loose 选项在多个客户端同时访问时可能导致数据损坏；共享访问请使用 cache=strict。除非已在 /etc/fstab 中配置 user 选项，否则需要 root 权限。

# HISTORY

Linux CIFS 文件系统是作为旧式 smbfs 的替代品而开发的。它为微软的 SMB/CIFS 协议提供了内核级原生支持，使其能够与 Windows 网络和 Samba 服务器无缝集成。

# INSTALL

```apt: sudo apt install cifs-utils```

```dnf: sudo dnf install cifs-utils```

```pacman: sudo pacman -S cifs-utils```

```apk: sudo apk add cifs-utils```

```zypper: sudo zypper install cifs-utils```

```nix: nix profile install nixpkgs#cifs-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount](/man/mount)(8), [smbclient](/man/smbclient)(1), [umount](/man/umount)(8), [fstab](/man/fstab)(5)
