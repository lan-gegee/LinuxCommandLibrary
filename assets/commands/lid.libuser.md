# TAGLINE

显示 Linux 系统上的组成员身份信息

# TLDR

显示包含某**用户**的组（主组和附加组）

```sudo lid [username]```

显示某个**组**的成员

```sudo lid --group [group_name]```

# SYNOPSIS

**lid** [_OPTION_]... [_name_]

# PARAMETERS

**-g, --group**
> 列出属于某个组的用户，而不是包含某个用户的组

**-i, --interactive**
> 访问用户数据库时对所有配置问题进行提示询问

**-n, --onlynames**
> 只显示名称而不显示对应的数字 ID

# DESCRIPTION

**lid** 显示 Linux 系统上的组成员身份信息。默认情况下，它显示包含指定用户的所有组（未给出名称时则为调用者）。使用 **-g** 选项后行为相反，会显示指定组内的所有用户。

作为 **libuser** 库工具的一部分，lid 从系统的用户和组数据库中读取信息。查询其他用户或组的成员信息需要 root 权限。

# CAVEATS

查询除调用者之外的用户或组的信息需要 **root 权限**（sudo）。该命令依赖 libuser 库配置来访问数据库。

# HISTORY

lid 命令是 **libuser** 库项目的一部分，该项目于 21 世纪初开发，旨在为不同 Linux 发行版提供统一的用户和组账户操作接口。

# SEE ALSO

[groups](/man/groups)(1), [id](/man/id)(1), [getent](/man/getent)(1), [usermod](/man/usermod)(8)
