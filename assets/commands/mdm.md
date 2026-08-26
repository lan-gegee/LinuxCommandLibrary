# TAGLINE

显示管理器

# TLDR

**启动 MDM**

```mdm```

**配置 MDM**

```mdm-config```

**重启 MDM**

```systemctl restart mdm```

**检查状态**

```systemctl status mdm```

**查看日志**

```journalctl -u mdm```

# SYNOPSIS

**mdm** [_options_]

# PARAMETERS

**--help**
> 显示帮助信息。

**--version**
> 显示版本。

# DESCRIPTION

**mdm** 是 MDM 显示管理器。它为 Linux Mint 提供图形化登录界面。

该工具处理用户身份验证和会话选择。是面向 Cinnamon/MATE 的 GDM 分支。

# CAVEATS

Linux Mint 专属。已被 LightDM 取代而弃用。属于旧式显示管理器。

# HISTORY

MDM 是 **Linux Mint 的**显示管理器，GDM 的一个分支，现已在很大程度上被 LightDM 取代。

# SEE ALSO

[gdm](/man/gdm)(1)
