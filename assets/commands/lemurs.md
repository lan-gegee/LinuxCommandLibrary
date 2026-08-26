# TAGLINE

可定制的 TUI 显示与登录管理器

# TLDR

**启动显示管理器**

```lemurs```

# SYNOPSIS

**lemurs** [_options_]

# DESCRIPTION

**lemurs** 是一个面向 Linux 与 BSD 系统的基于终端的显示和登录管理器。它使用 PAM（Pluggable Authentication Modules）进行认证，可以作为 TTY、X11 或 Wayland 会话的前端。无论是否使用 systemd 都能正常运行。

会话环境通过脚本配置：X11 的 xinitrc 脚本放入 **/etc/lemurs/wms**，Wayland 合成器脚本放入 **/etc/lemurs/wayland**。

# CONFIGURATION

**/etc/lemurs/config.toml**
> 用于自定义登录界面外观和行为的主配置文件。

**/etc/lemurs/wms/**
> 存放 X11 会话脚本的目录。

**/etc/lemurs/wayland/**
> 存放 Wayland 会话脚本的目录。

# CAVEATS

认证需要 PAM。会话脚本必须具有可执行权限。某些桌面环境可能需要额外的配置才能与基于 TUI 的显示管理器协同工作。

# HISTORY

**lemurs** 由 **coastalwhite** 创建，采用 **Rust** 编写。它已收录于 Arch Linux extra 软件仓库。

# INSTALL

```pacman: sudo pacman -S lemurs```

```nix: nix profile install nixpkgs#lemurs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ly](/man/ly)(1), [gdm](/man/gdm)(1), [startx](/man/startx)(1)
