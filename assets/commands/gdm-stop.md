# TAGLINE

停止 GNOME 显示管理器服务

# TLDR

**停止 GNOME 显示管理器**

```sudo gdm-stop```

# SYNOPSIS

**gdm-stop**

# DESCRIPTION

**gdm-stop** 完全停止 GNOME 显示管理器服务，终止所有图形会话并关闭图形登录界面。系统返回文本控制台模式（TTY），这对于排查图形问题、执行系统维护或切换到其他显示管理器非常有用。

GDM 停止时，所有已登录的用户都会被强制注销。在基于 systemd 的系统上，这通常是 `systemctl stop gdm` 的包装。停止 GDM 后，可以用 `systemctl start gdm` 再次启动它，或直接访问文本控制台。

# CAVEATS

停止 GDM 会终止所有图形会话。运行此命令前请保存工作。

# INSTALL

```dnf: sudo dnf install gdm```

```pacman: sudo pacman -S gdm```

```apk: sudo apk add gdm```

```zypper: sudo zypper install gdm```

```nix: nix profile install nixpkgs#gdm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdm-restart](/man/gdm-restart)(1), [gdm](/man/gdm)(8), [systemctl](/man/systemctl)(1)
