# TAGLINE

管理用于团队协作的 PlatformIO 组织

# TLDR

**创建组织**

```pio org create [orgname]```

**列出组织**

```pio org list```

**添加成员**

```pio org add [orgname] [username]```

**移除成员**

```pio org remove [orgname] [username]```

# SYNOPSIS

**pio org** _command_ [_options_]

# PARAMETERS

**create** _name_
> 创建组织。

**destroy** _name_
> 删除组织。

**list**
> 列出组织。

**add** _org_ _user_
> 添加成员。

**remove** _org_ _user_
> 移除成员。

**update** _org_
> 更新组织。

# DESCRIPTION

**pio org** 用于管理面向团队协作的 PlatformIO 组织。组织可以共享软件包、库和访问权限。需要 PlatformIO 账户。

# SEE ALSO

[pio-account](/man/pio-account)(1), [pio-team](/man/pio-team)(1)
