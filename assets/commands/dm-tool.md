# TAGLINE

LightDM 显示管理器控制工具

# TLDR

显示**登录界面**（greeter）

```dm-tool switch-to-greeter```

**锁定**当前会话

```dm-tool lock```

**切换**到指定用户

```dm-tool switch-to-user [username] [session]```

**添加**动态 seat

```dm-tool add-seat [xlocal] [name]=[value]```

# SYNOPSIS

**dm-tool** _command_ [_arguments_]

# DESCRIPTION

**dm-tool** 是一款用于与 LightDM 显示管理器交互的命令行工具。它提供会话管理功能，包括锁定当前会话、切换用户，以及在不注销的情况下显示登录界面。

该工具通过快速切换用户并保留所有打开的会话来支持多用户工作流。它还能管理显示 seat，即由显示器、键盘和鼠标组成的独立工作站。

dm-tool 通过 D-Bus 与 LightDM 通信，发送控制显示管理器行为的命令。这使其适合在使用 LightDM 的系统上进行脚本编写和自定义会话管理。

# PARAMETERS

**switch-to-greeter**
> 显示登录界面，保留当前会话

**lock**
> 锁定当前会话

**switch-to-user** _user_ [_session_]
> 切换到指定用户

**add-seat** _type_ _options_
> 添加动态 seat

**list-seats**
> 列出可用的 seat

# CAVEATS

只能配合 LightDM 显示管理器使用。其他显示管理器（GDM、SDDM）有不同的工具。会话类型必须有效。

# INSTALL

```apt: sudo apt install lightdm```

```dnf: sudo dnf install lightdm```

```pacman: sudo pacman -S lightdm```

```apk: sudo apk add lightdm```

```zypper: sudo zypper install lightdm```

```nix: nix profile install nixpkgs#lightdm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[loginctl](/man/loginctl)(1)
