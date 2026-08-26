# TAGLINE

管理 PlatformIO 组织中的团队和成员

# TLDR

**创建团队**

```pio team create [orgname:teamname]```

**列出团队**

```pio team list [orgname]```

**向团队添加成员**

```pio team add [orgname:teamname] [username]```

**移除成员**

```pio team remove [orgname:teamname] [username]```

# SYNOPSIS

**pio team** _command_ [_options_]

# PARAMETERS

**create** _name_
> 创建团队。

**destroy** _name_
> 删除团队。

**list** _org_
> 列出组织中的团队。

**add** _team_ _user_
> 添加团队成员。

**remove** _team_ _user_
> 移除团队成员。

# DESCRIPTION

**pio team** 用于管理 PlatformIO 组织内的团队。团队允许对软件包访问权限进行细粒度管理。命名遵循 org:team 约定。

# SEE ALSO

[pio-org](/man/pio-org)(1), [pio-access](/man/pio-access)(1)
