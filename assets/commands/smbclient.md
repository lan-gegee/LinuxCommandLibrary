# TAGLINE

访问 SMB/CIFS 共享的类 FTP 客户端

# TLDR

**连接**到共享

```smbclient //[server]/[share]```

使用**用户名**连接

```smbclient //[server]/[share] --user [username]```

使用**工作组**和用户名连接

```smbclient //[server]/[share] --workgroup [domain] --user [username]```

使用用户名和**密码**连接

```smbclient //[server]/[share] --user [username%password]```

**下载**文件

```smbclient //[server]/[share] --directory [path] --command "get [file.txt]"```

**上传**文件

```smbclient //[server]/[share] --directory [path] --command "put [file.txt]"```

匿名**列出共享**

```smbclient --list=[server] --no-pass```

# SYNOPSIS

**smbclient** _//server/share_ [_OPTIONS_]

# PARAMETERS

**-U, --user** _username[%password]_
> 指定用户名和可选的密码

**-W, --workgroup** _domain_
> 设置 SMB 工作组/域

**-N, --no-pass**
> 不提示输入密码，用于匿名访问

**-L, --list** _host_
> 列出服务器上可用的共享

**-D, --directory** _path_
> 连接后切换到初始目录

**-c, --command** _commands_
> 执行以分号分隔的命令

**-I, --ip-address** _ip_
> 直接指定服务器 IP

**-p, --port** _port_
> TCP 端口（默认：139 或 445）

**-m, --max-protocol** _level_
> 最大 SMB 协议版本（NT1、SMB2、SMB3）

**-A, --authentication-file** _file_
> 从文件读取凭据

**-T, --tar** _options_
> 带选项的 tar 备份模式

**-d, --debuglevel** _level_
> 调试详细程度（0-10）

**-n, --netbiosname** _name_
> 覆盖客户端 NetBIOS 名称

# INTERACTIVE COMMANDS

**get** _remote_ [_local_]
> 从共享下载文件

**put** _local_ [_remote_]
> 向共享上传文件

**ls** [_pattern_]
> 列出目录内容

**cd** _directory_
> 更改远程目录

**lcd** _directory_
> 更改本地目录

**mkdir** _directory_
> 创建远程目录

**rm** _file_
> 删除远程文件

**exit**
> 关闭连接

# DESCRIPTION

**smbclient** 是一个用于访问 SMB/CIFS 网络共享的类 FTP 客户端。它连接 Windows 文件服务器和 Samba 共享，支持在命令行中进行文件传输、目录操作和共享浏览。

该工具既支持带 FTP 风格命令的交互式会话，也支持通过 **-c** 标志进行批量操作。它可以创建共享的 tar 备份并浏览可用的网络资源。

# CAVEATS

命令行上的密码会在进程列表中可见；请使用 **-A** 指定凭据文件。某些功能需要特定的 SMB 协议版本。防火墙规则可能阻止 SMB 端口（139、445）。NTLM 身份验证正被 Kerberos 取代。

# HISTORY

**smbclient** 是 **Samba** 的一部分，由 **Andrew Tridgell** 于 **1992 年**在对 SMB 协议进行逆向工程后创建。Samba 已演进到支持现代 SMB2 和 SMB3 协议。对于跨平台文件共享以及从 Linux 访问 Windows 共享，该工具依然不可或缺。

# INSTALL

```apt: sudo apt install smbclient```

```dnf: sudo dnf install samba-client```

```pacman: sudo pacman -S smbclient```

```apk: sudo apk add samba-client```

```zypper: sudo zypper install samba-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount.cifs](/man/mount.cifs)(8), [smbcacls](/man/smbcacls)(1), [smbget](/man/smbget)(1), [nmblookup](/man/nmblookup)(1)
