# TAGLINE

控制 systemd 登录管理器

# TLDR

打印所有**当前会话**

```loginctl```

显示某个会话的**全部属性**

```loginctl show-session session_id -a```

显示**特定用户**的属性

```loginctl show-user username```

显示用户的**特定属性**

```loginctl show-user username -p Property```

在**远程主机**上执行

```loginctl list-users -H hostname```

让用户从所有会话中**注销**

```loginctl terminate-user username```

**锁定**所有会话

```loginctl lock-sessions```

# SYNOPSIS

**loginctl** [_OPTIONS_] [_COMMAND_]

# DESCRIPTION

**loginctl** 控制 systemd 登录管理器（systemd-logind）。它可用于查看和控制用户会话、seat 以及登录管理器本身的状态。

# COMMANDS

**list-sessions**
> 列出当前会话

**session-status [ID]**
> 显示运行时会话状态

**show-session [ID]**
> 显示会话的属性

**activate ID**
> 激活一个会话

**lock-session [ID]**
> 锁定会话

**unlock-session [ID]**
> 解锁会话

**lock-sessions**
> 锁定所有会话

**unlock-sessions**
> 解锁所有会话

**terminate-session ID**
> 终止一个会话

**list-users**
> 列出已登录的用户

**user-status [USER]**
> 显示运行时用户状态

**show-user [USER]**
> 显示用户的属性

**enable-linger [USER]**
> 启用用户 linger（注销后保持服务运行）

**disable-linger [USER]**
> 禁用用户 linger

**terminate-user USER**
> 终止一个用户的所有会话

**list-seats**
> 列出可用的 seat

**seat-status [SEAT]**
> 显示 seat 状态

# PARAMETERS

**-a, --all**
> 显示所有属性

**-p, --property**
> 显示特定属性

**-H, --host**
> 在远程主机上执行

**-M, --machine**
> 在容器中执行

**--no-pager**
> 不将输出管道传给分页器

**--no-legend**
> 不打印页眉/页脚

# CAVEATS

启用 linger 允许用户服务在注销后继续运行。终止会话可能导致正在运行的应用程序丢失数据。

# HISTORY

**loginctl** 是 **systemd** 的组成部分，通过 systemd-logind 管理多 seat 配置、用户会话和用户 linger。

# INSTALL

```apt: sudo apt install elogind```

```apk: sudo apk add elogind```

```nix: nix profile install nixpkgs#elogind```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [lslogins](/man/lslogins)(1)
