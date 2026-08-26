# TAGLINE

管理 SELinux 用户定义和角色

# TLDR

**列出**所有 SELinux 用户

```sudo semanage user -l```

**添加**新的 SELinux 用户

```sudo semanage user -a -R "staff_r sysadm_r" newuser_u```

**删除** SELinux 用户

```sudo semanage user -d myuser_u```

**修改** SELinux 用户角色

```sudo semanage user -m -R "staff_r" myuser_u```

添加用户并指定**默认级别**

```sudo semanage user -a -R "staff_r" -L s0 newuser_u```

添加用户并指定 **MLS 范围**

```sudo semanage user -a -R "staff_r" -r s0-s0:c0.c1023 newuser_u```

仅列出**自定义的**用户

```sudo semanage user -l -C```

# SYNOPSIS

**semanage user** [_options_] [_selinux_user_]

# DESCRIPTION

**semanage user** 管理 SELinux 用户映射，控制一个用户可以承担哪些角色。SELinux 用户通过 semanage login 映射到 Linux 用户。

# PARAMETERS

**-l, --list**
> 列出所有 SELinux 用户

**-a, --add**
> 添加新的 SELinux 用户

**-d, --delete**
> 删除 SELinux 用户

**-m, --modify**
> 修改现有的 SELinux 用户

**-R, --roles ROLES**
> 为该用户指定 MLS/MCS 角色

**-L, --level LEVEL**
> 指定默认 MLS/MCS 级别（默认 s0）

**-r, --range RANGE**
> 为该用户指定 MLS/MCS 范围

**-C, --locallist**
> 仅列出自定义项

**-n, --noheading**
> 输出中不显示列标题

# CAVEATS

需要 root 权限。SELinux 用户定义的更改会影响用户可以切换到哪些角色。必须启用 SELinux 更改才能生效。

# HISTORY

**semanage user** 属于 **policycoreutils**，提供用于管理用户上下文和角色分配的 SELinux 策略管理工具。

# SEE ALSO

[semanage](/man/semanage)(8), [semanage-login](/man/semanage-login)(8), [seinfo](/man/seinfo)(1)
