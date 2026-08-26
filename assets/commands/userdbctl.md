# TAGLINE

查询 systemd 用户与组数据库

# TLDR

列出所有**用户**

```userdbctl user```

显示**特定**用户

```userdbctl user [username]```

列出所有**组**

```userdbctl group```

显示**特定**组

```userdbctl group [groupname]```

列出提供定义的**服务**

```userdbctl services```

# SYNOPSIS

**userdbctl** [_OPTIONS_] _COMMAND_ [_NAME_]

# COMMANDS

**user** [_NAME_]
> 列出用户或显示某个特定用户

**group** [_NAME_]
> 列出组或显示某个特定的组

**services**
> 列出提供用户/组定义的服务

# DESCRIPTION

**userdbctl** 用于检查系统中的用户、组和组成员关系。它提供统一的接口，可从 /etc/passwd、LDAP、systemd-homed 等多种来源查询用户和组信息。

该工具会汇总所有已向 systemd-userdbd 注册的服务所提供的信息。

# CAVEATS

仅适用于基于 systemd 的系统。输出格式与传统 getent 不同。某些数据源需要额外服务处于运行状态。

# INSTALL

```apt: sudo apt install systemd-userdbd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[getent](/man/getent)(1), [id](/man/id)(1), [homectl](/man/homectl)(1)
