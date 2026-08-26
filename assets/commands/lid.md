# TAGLINE

显示用户所属的组或组内的用户

# TLDR

列出某用户的**组**

```sudo lid [username]```

列出某**组内的用户**

```sudo lid -g [groupname]```

列出**当前**用户的组

```sudo lid```

# SYNOPSIS

**lid** [_options_] [_name_]

# DESCRIPTION

**lid** 显示用户所属的组或组内的用户。它从系统的用户和组数据库中读取成员身份信息。不带参数时，显示当前用户的组。

# PARAMETERS

**-g**, **--group**
> 将参数视为组名并列出其成员

**name**
> 要查询的用户或组名（默认为用户）

# CAVEATS

访问所有组成员身份信息需要 root 权限。是 **libuser** 库中用于用户和组账户管理的工具之一。

# INSTALL

```dnf: sudo dnf install libuser```

```apk: sudo apk add libuser```

```zypper: sudo zypper install libuser```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groups](/man/groups)(1), [id](/man/id)(1), [getent](/man/getent)(1), [gpasswd](/man/gpasswd)(1), [groupmems](/man/groupmems)(1)
