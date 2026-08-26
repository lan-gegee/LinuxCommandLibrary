# TAGLINE

管理 PlatformIO Registry 软件包的访问权限

# TLDR

**授予软件包访问权限**

```pio access grant [maintainer] [user] [package]```

**撤销访问权限**

```pio access revoke [maintainer] [user] [package]```

**列出访问权限**

```pio access list [package]```

# SYNOPSIS

**pio access** _command_ [_options_]

# PARAMETERS

**grant** _level_ _user_ _package_
> 授予权限（guest、maintainer、admin）。

**revoke** _level_ _user_ _package_
> 撤销访问级别。

**list** _package_
> 列出软件包权限。

**private** _package_
> 将软件包设为私有。

**public** _package_
> 将软件包设为公开。

# DESCRIPTION

**pio access** 管理 PlatformIO Registry 软件包的访问权限。控制谁可以查看、下载和修改已发布的软件包。需要 PlatformIO 账户。

# SEE ALSO

[pio-account](/man/pio-account)(1), [pio-pkg](/man/pio-pkg)(1)
