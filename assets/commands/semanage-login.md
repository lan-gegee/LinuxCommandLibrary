# TAGLINE

将 Linux 用户映射到 SELinux 用户

# TLDR

**列出**所有登录映射

```sudo semanage login -l```

**添加**登录映射（Linux 用户到 SELinux 用户）

```sudo semanage login -a -s selinux_user linux_username```

**删除**登录映射

```sudo semanage login -d linux_username```

**修改**现有映射

```sudo semanage login -m -s selinux_user linux_username```

添加时指定 **MLS/MCS 范围**

```sudo semanage login -a -s user_u -r s0-s0:c0.c1023 linux_username```

仅列出**自定义的**映射

```sudo semanage login -l -C```

# SYNOPSIS

**semanage login** [_options_]

# PARAMETERS

**-l**, **--list**
> 列出登录映射。

**-a**, **--add**
> 添加新的登录映射。

**-d**, **--delete**
> 删除登录映射。

**-m**, **--modify**
> 修改现有的登录映射。

**-s**, **--seuser** _user_
> 要映射到的 SELinux 用户。

**-r**, **--range** _range_
> MLS/MCS 安全范围（例如 s0-s0:c0.c1023）。

**-C**, **--locallist**
> 仅显示本地自定义项。

**-n**, **--noheading**
> 列出时不打印标题。

**-N**, **--noreload**
> 提交后不重新加载策略。

**-S** _STORE_, **--store** _STORE_
> 选择要管理的备用 SELinux 策略存储。

**-D**, **--deleteall**
> 移除所有本地自定义项。

**-E**, **--extract**
> 提取可自定义的命令。

# DESCRIPTION

**semanage login** 管理 Linux 用户与 SELinux 用户之间的映射。Linux 用户登录时，此映射决定其获得的 SELinux 安全上下文。

不同的 SELinux 用户具有不同的角色和权限，可实现细粒度的访问控制。在 Linux 用户名前加 **%** 表示组映射（例如 **%wheel**）。

# CAVEATS

更改只影响新登录的会话。已有会话保持其原有上下文。

# HISTORY

属于 **policycoreutils**，提供 SELinux 策略管理工具。

# SEE ALSO

[semanage](/man/semanage)(8), [semanage-user](/man/semanage-user)(8), [semanage-fcontext](/man/semanage-fcontext)(8), [sestatus](/man/sestatus)(8)
