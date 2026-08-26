# TAGLINE

入侵防御控制接口

# TLDR

获取某个 jail 的当前**状态**

```fail2ban-client status [jail]```

从 jail 的封禁列表中**移除** IP

```fail2ban-client set [jail] unbanip [ip_address]```

验证服务器是否**存活**

```fail2ban-client ping```

# SYNOPSIS

**fail2ban-client** _command_ [_arguments_]

# DESCRIPTION

**fail2ban-client** 用于配置和控制 fail2ban 服务器。Fail2ban 监控日志文件，封禁表现出恶意行为（如反复登录失败）的 IP 地址。

用于管理 jail 状态、封禁/解封 IP 以及服务器控制。

# PARAMETERS

**status** [_jail_]
> 显示 jail 状态

**set** _jail_ _action_ _value_
> 配置 jail 设置

**unbanip** _ip_
> 从封禁列表移除 IP

**ping**
> 检查服务器是否存活

**start**
> 启动服务器

**stop**
> 停止服务器

**reload**
> 重载配置

# CONFIGURATION

**/etc/fail2ban/jail.conf**
> 默认 jail 配置（不要直接修改）。

**/etc/fail2ban/jail.local**
> jail 配置的本地覆盖。

**/etc/fail2ban/fail2ban.conf**
> fail2ban 服务器主配置。

**/etc/fail2ban/filter.d/**
> 用于日志解析的过滤器定义。

# CAVEATS

需要 fail2ban-server 正在运行。Jail 名称在配置文件中定义。大多数操作可能需要 root 权限。

# INSTALL

```dnf: sudo dnf install fail2ban```

```pacman: sudo pacman -S fail2ban```

```apk: sudo apk add fail2ban```

```zypper: sudo zypper install fail2ban```

```brew: brew install fail2ban```

```nix: nix profile install nixpkgs#fail2ban```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iptables](/man/iptables)(8)
