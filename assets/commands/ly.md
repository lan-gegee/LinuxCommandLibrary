# TAGLINE

面向 Linux 和 BSD 的轻量级 TUI 显示管理器

# TLDR

**启动显示管理器**

```ly```

在**指定的 tty 上启动**

```ly -c [tty2]```

# SYNOPSIS

**ly** [_options_]

# PARAMETERS

**-c**, **--config-tty** _TTY_
> 设置要操作的 tty。

# DESCRIPTION

**ly** 是一款面向 Linux 和 BSD 的轻量级 TUI 显示管理器，它驻留在 framebuffer 控制台中，呈现交互式的文本登录界面。它同时支持 X11 和 Wayland 会话，并使用 PAM 进行身份验证，运行不依赖 systemd。

用户使用方向键切换字段和选择桌面环境，输入凭据后即可启动会话。界面设计极简，避免了图形显示管理器的开销。

# CONFIGURATION

**/etc/ly/config.ini**
> 配置文件，包含用于自定义登录界面外观和行为的默认值，包括动画、颜色和会话路径等。

# CAVEATS

运行于 framebuffer 控制台——登录界面本身不会启动图形环境。部分终端特性可能因 framebuffer 驱动而异。通常作为 systemd 服务（**ly.service**）或通过 init 系统管理。

# HISTORY

**ly** 由 **fairyglade** 项目开发，使用 **Zig** 编写。它的定位是 GDM 和 SDDM 等图形显示管理器的极简替代品。

# INSTALL

```dnf: sudo dnf install ly```

```pacman: sudo pacman -S ly```

```brew: brew install ly```

```nix: nix profile install nixpkgs#ly```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lemurs](/man/lemurs)(1), [gdm](/man/gdm)(1), [startx](/man/startx)(1), [xinit](/man/xinit)(1)
