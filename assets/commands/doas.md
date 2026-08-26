# TAGLINE

极简的提权工具

# TLDR

**以 root 身份运行命令**

```doas [command]```

**以其他用户身份运行命令**

```doas -u [username] [command]```

**启动 root shell**

```doas -s```

**以其他用户身份启动 shell**

```doas -u [username] -s```

**无需密码运行**（若已配置）

```doas -n [command]```

**检查 doas.conf** 是否允许该命令

```doas -C [/etc/doas.conf] [command]```

**清除缓存的凭据**

```doas -L```

# SYNOPSIS

**doas** [_-nLs_] [_-a style_] [_-C config_] [_-u user_] _command_ [_args_]

# PARAMETERS

**-n**
> 非交互模式；需要密码时直接失败。

**-L**
> 清除所有持久化的身份验证凭据。

**-s**
> 执行 SHELL 环境变量或 /etc/passwd 中指定的 shell。

**-u** _user_
> 以指定用户身份运行命令（默认：root）。

**-a** _style_
> 使用指定的身份验证方式。

**-C** _config_
> 解析并检查指定的配置文件后退出。

_command_
> 要以提升后的权限执行的命令。

# DESCRIPTION

**doas**（dedicated openbsd application subexecutor）是一个用于以其他用户（通常是 root）身份运行命令的极简程序。它源自 OpenBSD，是比 sudo 更简单、更安全的替代品，代码库和攻击面都小得多。

配置通过 **/etc/doas.conf** 完成，使用简单的规则规定谁可以执行什么。一条基本规则例如 **permit persist :wheel**，允许 wheel 组成员以 root 身份执行命令并缓存凭据。

配置语法很直观：每行是一条规则，包含 **permit** 或 **deny**、可选的关键字如 **nopass**（免密码）、**persist**（缓存凭据）、**keepenv**（保留环境变量），以及用户、组和允许的命令的说明。

与 sudo 庞大的功能集不同，doas 专注于以最小的复杂度实现提权这一核心用例。这使得它更容易审计并减少了潜在的安全漏洞。许多 Linux 发行版现在都将 doas 作为 sudo 的替代品打包提供。

# CONFIGURATION

**/etc/doas.conf**
> 指定授权规则的主配置文件。每行包含一条 permit/deny 规则、可选关键字（nopass、persist、keepenv）以及用户/组/命令的限定条件。

# CAVEATS

配置语法与 sudo 不同；迁移时需要重写规则。功能少于 sudo（没有细粒度的命令日志记录，也没有复杂的按命令选项）。某些软件可能明确要求 sudo。使用前必须先完成配置（没有默认放行的配置）。

# HISTORY

**doas** 由 Ted Unangst 创建，于 **2015 年**随 **OpenBSD 5.8** 引入基础系统，作为 sudo 的替代品。其设计目标是用最少的代码（约 1000 行，而 sudo 超过 10 万行）提供必要的功能。它已被移植到 Linux 及其他系统，在注重安全的用户中颇受欢迎。

# INSTALL

```apt: sudo apt install opendoas```

```dnf: sudo dnf install opendoas```

```pacman: sudo pacman -S opendoas```

```apk: sudo apk add doas```

```nix: nix profile install nixpkgs#doas```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sudo](/man/sudo)(8), [su](/man/su)(1)
