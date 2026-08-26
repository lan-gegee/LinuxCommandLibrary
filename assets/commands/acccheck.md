# TAGLINE

Windows SMB 密码字典攻击工具

# TLDR

**检查**目标是否存在空密码

```acccheck -t [192.168.1.1]```

对单个用户使用**密码列表**

```acccheck -t [192.168.1.1] -u [administrator] -P [passwords.txt]```

使用**用户名和密码列表**

```acccheck -t [192.168.1.1] -U [users.txt] -P [passwords.txt]```

从文件攻击**多个目标**

```acccheck -T [targets.txt] -U [users.txt] -P [passwords.txt]```

以**详细输出**模式检查

```acccheck -t [192.168.1.1] -U [users.txt] -P [passwords.txt] -v```

# SYNOPSIS

**acccheck** [_-t target_ | _-T targetfile_] [_-u user_ | _-U userfile_] [_-p pass_ | _-P passfile_] [_-v_]

# DESCRIPTION

**acccheck** 是一款专为 Windows SMB 身份验证设计的密码字典攻击工具。它使用提供的凭据尝试连接 Windows 的 IPC$ 和 ADMIN$ 共享，以识别有效的用户名/密码组合。

该工具在渗透测试中可用于发现 Windows 系统上的弱口令或默认密码。它既可以测试单一凭据，也可以遍历用户名和密码字典列表。

# PARAMETERS

**-t** _target_
> 单个目标 IP 地址。

**-T** _file_
> 包含目标 IP 列表的文件。

**-u** _username_
> 要测试的单个用户名。

**-U** _file_
> 包含用户名列表的文件。

**-p** _password_
> 要测试的单个密码。

**-P** _file_
> 包含密码列表的文件。

**-v**
> 详细模式（显示所有尝试过程）。

# CAVEATS

仅限用于获得授权的安全测试。未经授权的访问尝试属于违法行为。**acccheck** 是围绕 **smbclient** 的 Perl 封装，因此依赖可正常工作的 Samba 客户端。成功登录的用户名/密码组合会被追加写入当前工作目录下名为 **cracked** 的文件。多次失败尝试可能触发账户锁定策略；该工具依赖 SMB 连通性（端口 139/445）。

# HISTORY

**acccheck** 由 Faisal Dean（Faiz）编写，作为多种渗透测试工具合集的一部分发布。后来被收录进 Kali Linux 及其他注重安全的发行版，用于 Windows 网络安全评估。

# SEE ALSO

[smbclient](/man/smbclient)(1), [hydra](/man/hydra)(1), [medusa](/man/medusa)(1), [nmap](/man/nmap)(1), [enum4linux](/man/enum4linux)(1), [crackmapexec](/man/crackmapexec)(1)
