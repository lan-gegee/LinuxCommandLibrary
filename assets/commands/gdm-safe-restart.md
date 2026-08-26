# TAGLINE

仅在没有活动会话时安全重启 GDM

# TLDR

**安全重启 GDM**

```sudo gdm-safe-restart```

# SYNOPSIS

**gdm-safe-restart**

# DESCRIPTION

**gdm-safe-restart** 提供比 gdm-restart 更安全的替代方案，只在没有用户处于活动图形会话时才重启 GNOME 显示管理器。这可以防止意外终止用户的工作，并确保只在系统处于登录界面时才执行重启。

如果当前有用户已登录，该命令会检查活动会话并拒绝重启 GDM，保护用户不丢失未保存的工作。因此它适合自动维护脚本，或希望在安全前提下重启显示管理器的场景。

# SEE ALSO

[gdm-restart](/man/gdm-restart)(1), [gdm-stop](/man/gdm-stop)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/gdm)```

<!-- verified: 2026-07-15 -->
