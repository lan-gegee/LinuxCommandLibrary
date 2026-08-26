# TAGLINE

GDM 的图形化配置工具

# TLDR

**打开 GDM 配置**

```gdmsetup```

# SYNOPSIS

**gdmsetup** [_options_]

# PARAMETERS

**--help**
> 显示帮助信息。

# DESCRIPTION

**gdmsetup** 是 GDM（GNOME 显示管理器）的传统图形配置工具，提供用户友好的界面来管理登录界面设置，无需手动编辑配置文件。管理员可以通过它配置特定用户的自动登录、控制哪些用户出现在登录列表中、自定义登录界面主题以及调整会话超时行为等选项。

该工具以直观的 GUI 呈现 GDM 的配置选项，让偏好图形工具而非命令行配置的管理员也能轻松使用。通过 gdmsetup 修改的设置会影响系统上所有用户的登录界面外观和行为。

在现代 GNOME 系统（GNOME 3 及更高版本）上，gdmsetup 已基本被弃用，GDM 配置被直接整合进主 GNOME 设置应用程序。许多发行版不再附带 gdmsetup，而是通过 dconf-editor 或系统设置面板提供 GDM 配置。对于仍在使用它的系统，gdmsetup 需要管理员权限才能修改系统级的登录设置。

# CAVEATS

需要管理员权限。已被 GNOME 设置取代。可能并非在所有发行版上都可用。

# HISTORY

gdmsetup 曾是传统的 GDM 配置工具。现代 GNOME 系统将 GDM 设置整合进主设置应用程序，使这个独立工具变得少见。

# SEE ALSO

[gdm](/man/gdm)(8), [dconf](/man/dconf)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/gdm)```

<!-- verified: 2026-07-15 -->
