# TAGLINE

从 Windows 组信息生成 /etc/group（Cygwin）

# TLDR

**将本地组写入 /etc/group**

```mkgroup -l > /etc/group```

**输出当前域中的组**

```mkgroup -d```

**输出指定域中的组**

```mkgroup -d [DOMAIN]```

**输出另一台机器上的本地组**

```mkgroup -l [MACHINE]```

**排除 Windows BUILTIN 组**

```mkgroup -l -b```

**仅查询单个组**

```mkgroup -g [GROUPNAME]```

# SYNOPSIS

**mkgroup** [_options_] [_machine_ | _domain_]

# PARAMETERS

**-l**, **--local** [_machine_]
> 输出本地组账户（当前机器的或指定机器的）。

**-L**, **--Local** [_machine_]
> 类似 **-l**，但在每个组名前加上机器名前缀。

**-d**, **--domain** [_domain_]
> 输出域组（当前域或指定的域）。

**-c**, **--current**
> 输出用户的当前（主）组。

**-S**, **--separator** _CHAR_
> 用 _CHAR_ 替代 '+' 作为组名中 domain\group 的分隔符。

**-o**, **--id-offset** _OFFSET_
> 更改加到非本地域 GID 上的默认偏移量（0x10000）。

**-g**, **--group** _GROUPNAME_
> 只返回指定组的信息。

**-b**, **--no-builtin**
> 不输出 BUILTIN 组。

**-U**, **--unix** _GROUPLIST_
> 在 UNIX Samba 服务器上使用 **-l** 时输出 UNIX 组。

**-h**, **--help**
> 显示帮助。

**-v**, **--version**
> 打印版本信息。

# DESCRIPTION

**mkgroup** 是 Cygwin 的辅助工具，以 Unix `/etc/group` 的格式（name:passwd:gid:members）输出组信息，数据来源于 Windows 用户/组数据库（本地账户用 SAM，域账户用 Active Directory）。

现代 Cygwin 通过 `nsswitch.conf` 机制直接从 Windows 读取组信息，因此通常不再需要静态的 `/etc/group` 文件。在以下情况下用 **mkgroup** 生成一份仍然有用：机器经常与域控制器断开连接、需要确定性的 GID，或者要与 Samba 集成。

# CAVEATS

仅限 Cygwin 使用；对原生 Linux 系统无效（在 Linux 上请使用 `getent group` 或直接编辑 `/etc/group`）。自 Cygwin 1.7.34 起，静态 `/etc/group` 是可选项，多数情况下不建议使用。非本地账户生成的 GID 默认偏移 0x10000 以避免冲突。

# HISTORY

**mkgroup** 属于 **Cygwin** 的 base-files 软件包，与 **mkpasswd** 同属一套。它起源于 Cygwin 早期，当时 `/etc/passwd` 和 `/etc/group` 是在 Windows 上实现 POSIX 兼容所必需的。从 Cygwin 1.7.34（2014 年）开始，通过 Windows API 直接查询成为默认方式，该工具随之变为可选。

# SEE ALSO

[mkpasswd](/man/mkpasswd)(1), [groupadd](/man/groupadd)(8)
