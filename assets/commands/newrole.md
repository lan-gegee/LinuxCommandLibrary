# TAGLINE

以不同的 SELinux 安全上下文启动新的 shell

# TLDR

以指定的 **SELinux 角色**启动新 shell

```newrole -r [role_name]```

以指定的 **SELinux 类型**启动新 shell

```newrole -t [type_name]```

以指定的 **SELinux 级别**启动新 shell

```newrole -l [s0-s0:c0.c1023]```

以**角色和类型同时指定**的方式启动新 shell

```newrole -r [role_name] -t [type_name]```

# SYNOPSIS

**newrole** [_options_]

# PARAMETERS

**-r, --role _role_**
> 指定新的 SELinux 角色

**-t, --type _type_**
> 指定新的 SELinux 类型（域）

**-l, --level _level_**
> 指定新的 SELinux 敏感度级别

**-p, --preserve-environment**
> 切换时保留环境变量

**-V, --version**
> 显示版本信息

# DESCRIPTION

**newrole** 以不同的 SELinux 安全上下文启动一个新的 shell。它允许用户在其被授权使用的角色之间切换，从而在 SELinux 中实现基于角色的访问控制（RBAC）。

SELinux 上下文的格式为 **user:role:type:level**。newrole 命令更改其中的角色和/或类型部分，从而影响用户可以执行的操作。常见的切换包括从受限的用户角色切换到管理角色。

SELinux 策略中必须将用户映射到目标角色（参见 **semanage user**）。根据策略配置，可能需要进行身份验证。

# CAVEATS

仅在启用 SELinux 的系统上有效。SELinux 策略中必须授权用户使用目标角色。切换失败可能导致访问被拒绝。可使用 **id -Z** 在切换前后验证当前上下文。

# INSTALL

```apt: sudo apt install newrole```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[runcon](/man/runcon)(1), [semanage-user](/man/semanage-user)(8), [id](/man/id)(1), [seinfo](/man/seinfo)(1)
