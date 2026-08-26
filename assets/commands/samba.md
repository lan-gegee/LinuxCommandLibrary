# TAGLINE

SMB/CIFS 文件共享与 Active Directory 服务器

# TLDR

在前台**启动 Samba AD DC 守护进程**

```samba -i```

**使用指定的配置文件启动**

```samba -s [/etc/samba/smb.conf]```

**以 debug 日志级别启动**

```samba -d [3]```

**检查 Samba 版本**

```samba --version```

**作为经典 NT4 风格的域控制器启动**

```samba --option="server role=classic primary domain controller"```

# SYNOPSIS

**samba** [_-D_] [_-i_] [_-M model_] [_--no-process-group_] [_-d debuglevel_] [_-s configfile_]

# PARAMETERS

**-D**, **--daemon**
> 以守护进程（后台进程）方式运行

**-i**, **--interactive**
> 在前台交互式运行

**-M** _model_, **--model**=_model_
> 选择进程模型：single、standard、prefork、thread

**-d** _level_, **--debuglevel**=_level_
> 设置 debug 日志级别（0-10）

**-s** _file_, **--configfile**=_file_
> 使用替代的配置文件

**--no-process-group**
> 不创建新的进程组

**-V**, **--version**
> 打印版本信息

# DESCRIPTION

**Samba** 是一套实现 SMB/CIFS 协议的软件，让 Unix 系统能够与 Windows 客户端共享文件和打印机。samba 守护进程提供 Active Directory 域控制器服务。

该套件由多个组件构成：**smbd** 处理文件和打印服务，**nmbd** 提供 NetBIOS 名称解析和浏览，**winbindd** 处理用户和组查询，而 **samba** 本身在配置后可充当 AD 域控制器。

配置通过 **/etc/samba/smb.conf** 管理，其中定义了共享、身份验证和网络设置。Samba 可以集成到现有的 Windows 域中，也可以完全取代 Windows Server AD 基础设施。

# CONFIGURATION

**/etc/samba/smb.conf**
> Samba 主配置文件，定义共享、身份验证方法、网络设置和域控制器参数。

**/var/lib/samba/**
> Samba 状态目录，存放用户账户、组映射和域数据的数据库。

# CAVEATS

将 Samba 作为 AD DC 运行需要仔细配置 DNS 和 Kerberos。samba 守护进程（AD DC 模式）与 smbd/nmbd（文件服务器模式）是互斥的配置。防火墙规则必须放行 SMB 所需的端口 139 和 445，以及 AD 服务所需的端口 88、389 和 636。

# HISTORY

Samba 由 **Andrew Tridgell** 于 **1992 年**创建，是一个对 SMB 进行逆向工程实现的成果。它最初名为 "smbserver"，出于商标方面的考虑更名为 Samba。4.0 版本（**2012 年**）加入了对 Active Directory 的支持，实现了完整的域控制器功能。

# INSTALL

```apt: sudo apt install samba-ad-dc```

```dnf: sudo dnf install samba-dc```

```pacman: sudo pacman -S samba```

```apk: sudo apk add samba-dc```

```zypper: sudo zypper install samba-ad-dc```

```brew: brew install samba```

```nix: nix profile install nixpkgs#samba```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smbclient](/man/smbclient)(1)
