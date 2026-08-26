# TAGLINE

重启 GNOME 显示管理器服务

# TLDR

**重启 GNOME 显示管理器**

```sudo gdm-restart```

# SYNOPSIS

**gdm-restart**

# DESCRIPTION

**gdm-restart** 重启 GNOME 显示管理器服务，终止所有活动的图形用户会话并返回登录界面。该命令适用于应用配置更改、从显示问题中恢复，或在不完全重启系统的情况下重置图形环境。

执行时，所有已登录的用户都会被强制注销，任何未保存的工作都会丢失。随后显示管理器重新初始化，呈现全新的登录界面。在使用 systemd 的现代系统中，这通常是 "systemctl restart gdm" 的包装。

# CAVEATS

重启 GDM 会终止所有用户会话。运行此命令前请保存工作。

# INSTALL

```dnf: sudo dnf install gdm```

```pacman: sudo pacman -S gdm```

```apk: sudo apk add gdm```

```zypper: sudo zypper install gdm```

```nix: nix profile install nixpkgs#gdm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdm](/man/gdm)(8), [gdm-stop](/man/gdm-stop)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/gdm)```

<!-- verified: 2026-07-15 -->
