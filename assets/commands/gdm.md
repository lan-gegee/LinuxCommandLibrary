# TAGLINE

GNOME 的图形登录管理器

# TLDR

**启动 GDM**

```systemctl start gdm```

**停止 GDM**

```systemctl stop gdm```

**设置开机自启**

```systemctl enable gdm```

**重启 GDM**

```systemctl restart gdm```

**查看状态**

```systemctl status gdm```

# SYNOPSIS

**gdm** [_options_]

# PARAMETERS

**--version**
> 显示版本。

**--help**
> 显示帮助信息。

# CONFIGURATION

**/etc/gdm/custom.conf**
> GDM 主配置文件，控制登录行为、自动登录和会话设置。

**/etc/gdm3/custom.conf**
> 基于 Debian 系统上的另一配置路径。

# DESCRIPTION

**gdm**（GNOME Display Manager）是 GNOME 的图形登录管理器。它为桌面环境提供登录界面、用户身份验证和会话管理。

GDM 处理用户选择、密码验证和桌面会话的启动。它支持多会话、无障碍功能和用户切换。

gdm 通常由 systemd 启动，作为系统服务运行。

# CAVEATS

需要 X11 或 Wayland。通过 dconf 进行配置。在现代系统中由 systemd 管理。

# HISTORY

GDM 作为 **GNOME 项目**的一部分而创建，旨在提供与 GNOME 桌面环境集成的显示管理器。它为 GNOME 用户取代了 xdm。

# INSTALL

```dnf: sudo dnf install gdm```

```pacman: sudo pacman -S gdm```

```apk: sudo apk add gdm```

```zypper: sudo zypper install gdm```

```nix: nix profile install nixpkgs#gdm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ly](/man/ly)(1), [slim](/man/slim)(1), [xinit](/man/xinit)(1)
