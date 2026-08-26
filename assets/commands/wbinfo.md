# TAGLINE

向 Winbind 查询域信息

# TLDR

**列出域用户**

```wbinfo -u```

**列出域组**

```wbinfo -g```

**检查 winbind 连接**

```wbinfo -p```

**ping 域控制器**

```wbinfo -P```

**显示域信息**

```wbinfo -D [DOMAIN]```

**列出受信任的域**

```wbinfo -m```

**将用户名转换为 SID**

```wbinfo -n [DOMAIN/username]```

**将 SID 转换为名称**

```wbinfo -s [S-1-5-21-...]```

**按 UID 获取用户信息**

```wbinfo --uid-info [1000]```

**检查信任账户**

```wbinfo -t```

# SYNOPSIS

**wbinfo** [_options_]

# PARAMETERS

**-u**, **--domain-users**
> 列出所有域用户。

**-g**, **--domain-groups**
> 列出所有域组。

**-p**, **--ping**
> 检查 winbindd 是否正在运行。

**-P**, **--ping-dc**
> ping 域控制器。

**-t**, **--check-secret**
> 验证信任账户。

**-m**, **--trusted-domains**
> 列出受信任的域。

**-D**, **--domain-info** _domain_
> 显示域信息。

**--all-domains**
> 列出所有域。

**--own-domain**
> 显示自身所属的域。

**-n**, **--name-to-sid** _name_
> 将名称转换为 SID。

**-s**, **--sid-to-name** _SID_
> 将 SID 转换为名称。

**-U**, **--uid-to-sid** _UID_
> 将 UNIX UID 转换为 SID。

**-G**, **--gid-to-sid** _GID_
> 将 UNIX GID 转换为 SID。

**-r**, **--user-groups** _user_
> 获取用户的组成员身份。

**--uid-info** _UID_
> 获取指定 UID 的用户信息。

**--domain** _name_
> 为操作指定域名。

**-a** _user%pass_
> 对用户进行身份验证（仅用于测试）。

# DESCRIPTION

**wbinfo** 从 winbindd 守护进程查询信息，该守护进程为 Samba 和 Linux 系统提供 Windows 域集成。它从 Active Directory 或 NT 域检索用户、组和域信息。

该工具是排查 Winbind 配置和验证域连接性的必备工具。它可以依据已配置的 ID 映射在 Windows SID 与 UNIX UID/GID 之间进行转换。

winbindd 必须正在运行且配置正确，wbinfo 才能正常工作。该工具常用于验证 Samba 的域成员资格。

# CAVEATS

需要 winbindd 守护进程正在运行。通过 -a 进行的身份验证仅用于测试；应用程序请使用 ntlm_auth。某些操作在大型域上可能耗时较长。退出状态 0 表示成功，1 表示失败。

# HISTORY

**wbinfo** 是 Samba 套件的一部分，Samba 为 Unix 系统提供 Windows 互操作性。Winbind 使 Unix 系统能够作为 Windows 域成员出现，允许域用户在 Unix 系统上进行身份验证。

# INSTALL

```apt: sudo apt install winbind```

```dnf: sudo dnf install samba-winbind-clients```

```apk: sudo apk add samba-winbind-clients```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[samba](/man/samba)(7), [net](/man/net)(8)
