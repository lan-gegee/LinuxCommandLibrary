# TAGLINE

枚举 Windows 和 Samba 系统的信息

# TLDR

使用**全部**方法枚举

```enum4linux -a [remote_host]```

使用给定的**凭据**枚举

```enum4linux -u [user_name] -p [password] [remote_host]```

列出主机的**用户名**

```enum4linux -U [remote_host]```

列出**共享**

```enum4linux -S [remote_host]```

获取 **OS** 信息

```enum4linux -o [remote_host]```

# SYNOPSIS

**enum4linux** [_options_] _target_

# DESCRIPTION

**enum4linux** 通过 SMB 枚举 Windows 和 Samba 系统的信息。它可以提取用户列表、共享信息、组成员关系、密码策略以及操作系统细节。

它是 smbclient、rpcclient 和 nmblookup 等工具的 Perl 封装，面向渗透测试。

# PARAMETERS

**-a**
> 执行所有简单枚举

**-U**
> 获取用户列表

**-S**
> 获取共享列表

**-o**
> 获取 OS 信息

**-u** _user_
> 用于认证的用户名

**-p** _password_
> 用于认证的密码

**-G**
> 获取组信息

**-P**
> 获取密码策略

**-r**
> 通过 RID 轮询枚举用户（即使 RestrictAnonymous 阻止直接列出也有效）

**-M**
> 获取机器列表

**-d**
> 输出详细信息，作用于 -U 和 -S

**-w** _workgroup_
> 手动指定工作组或域

# CAVEATS

安全测试工具。只在你获得授权的系统上使用。部分枚举需要有效凭据或空会话（null session），而现代 Windows 默认阻止空会话。可能触发安全告警。最初的 Perl 版 enum4linux 实际上已停止维护；Python 重写的 **enum4linux-ng** 是持续开发的继任者，输出更整洁且便于机器读取。

# INSTALL

```nix: nix profile install nixpkgs#enum4linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smbclient](/man/smbclient)(1), [rpcclient](/man/rpcclient)(1), [nmap](/man/nmap)(1), [nmblookup](/man/nmblookup)(1)

# RESOURCES

```[Source code](https://github.com/CiscoCXSecurity/enum4linux)```

<!-- verified: 2026-07-14 -->
