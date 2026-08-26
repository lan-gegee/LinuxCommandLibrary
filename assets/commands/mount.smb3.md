# TAGLINE

挂载 SMB3 网络共享

# TLDR

此命令是 **mount.cifs** 的别名，仅限 SMB3 文件系统。

**挂载 SMB3 共享**并指定用户名

```sudo mount.smb3 -o username=[user] //[server]/[share] [/mnt/point]```

以**访客身份**挂载

```sudo mount.smb3 -o guest //[server]/[share] [/mnt/point]```

**使用凭据文件挂载**

```sudo mount.smb3 -o credentials=[/etc/samba/creds] //[server]/[share] [/mnt/point]```

**以指定权限挂载**

```sudo mount.smb3 -o username=[user],uid=[1000],gid=[1000],file_mode=[0644],dir_mode=[0755] //[server]/[share] [/mnt/point]```

**启用加密挂载**

```sudo mount.smb3 -o username=[user],seal //[server]/[share] [/mnt/point]```

# SYNOPSIS

**mount.smb3** _//server/share_ _mount-point_ [**-o** _options_]

# PARAMETERS

**username=**_arg_
> 用于身份验证的用户名。默认取 USER 环境变量。

**password=**_arg_
> 用于身份验证的密码。使用凭据文件更安全。

**credentials=**_filename_
> 包含用户名、密码以及可选域名的文件。

**domain=**_arg_
> 用于身份验证的工作组或域。

**guest**
> 不使用密码连接。

**sec=**_mode_
> 安全模式（krb5、krb5i、ntlmv2、ntlmv2i、ntlmssp、ntlmsspi、none）。

**uid=**_arg_
> 挂载共享中文件的属主 UID。

**gid=**_arg_
> 挂载共享中文件的属主 GID。

**file_mode=**_mode_
> 默认文件权限（八进制）。

**dir_mode=**_mode_
> 默认目录权限（八进制）。

**seal**
> 为所有数据启用 SMB3 加密。

**vers=**_version_
> SMB 协议版本（3.0、3.02、3.1.1）。

**cache=**_mode_
> 缓存模式（none、strict、loose）。

**ro**
> 以只读方式挂载。

**rw**
> 以读写方式挂载。

**multiuser**
> 允许不同用户使用各自的凭据访问该挂载。

**nounix**
> 禁用 Unix 扩展。

# DESCRIPTION

**mount.smb3** 将 SMB3 网络共享挂载到本地目录。它是指向 **mount.cifs** 的符号链接，仅限 SMB3 文件系统。也可以通过 **mount -t smb3** 调用。

对于较旧的 SMB 版本，请改用 mount.cifs 并配合 **vers=** 选项。

# CAVEATS

需要 cifs-utils 软件包。命令行上的密码会在进程列表中可见；请改用凭据文件。Kerberos 身份验证需要有效的 keytab 或票据。

# INSTALL

```apt: sudo apt install cifs-utils```

```dnf: sudo dnf install cifs-utils```

```pacman: sudo pacman -S cifs-utils```

```apk: sudo apk add cifs-utils```

```zypper: sudo zypper install cifs-utils```

```nix: nix profile install nixpkgs#cifs-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount.cifs](/man/mount.cifs)(8), [mount](/man/mount)(8), [umount](/man/umount)(8), [smbclient](/man/smbclient)(1), [fstab](/man/fstab)(5)
