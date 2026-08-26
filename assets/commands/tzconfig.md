# TAGLINE

交互式系统时区配置

# TLDR

**配置时区**

```tzconfig```

# SYNOPSIS

**tzconfig** [_options_]

# PARAMETERS

**--help**
> 显示帮助。

# DESCRIPTION

**tzconfig** 是 Debian 的一个用于配置系统时区的交互式工具。它提供基于菜单的界面，引导用户依次选择地理区域和城市以确定正确的时区，然后通过修改 **/etc/localtime** 更新全系统范围的时区配置。

在基于 systemd 的系统上，该工具已被弃用，推荐使用 **timedatectl**，它除了时区管理外还提供更广泛的时间和日期配置能力。在没有 systemd 的较旧 Debian 系统上，首选的替代方案是 **dpkg-reconfigure tzdata**。

# CAVEATS

在许多系统上已弃用。请改用 timedatectl。需要 root 权限。

# HISTORY

**tzconfig** 曾是 Debian 传统的时区配置工具，如今在 systemd 系统上已被 **timedatectl** 取代。

# SEE ALSO

[timedatectl](/man/timedatectl)(1), [dpkg-reconfigure](/man/dpkg-reconfigure)(1), [tzselect](/man/tzselect)(1)
