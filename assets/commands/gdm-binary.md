# TAGLINE

GNOME 显示管理器守护进程

# TLDR

**启动 GNOME 显示管理器**

```gdm-binary```

**带调试信息启动**

```gdm-binary --debug```

# SYNOPSIS

**gdm-binary** [_options_]

# PARAMETERS

**--debug**
> 启用调试输出。

**--nodaemon**
> 不转为守护进程。

**--preserve-ld-vars**
> 保留 LD_* 环境变量。

# DESCRIPTION

**gdm-binary** 是 GNOME 显示管理器（GDM）的实际守护进程可执行文件。它负责管理图形登录界面、验证用户身份以及启动桌面会话等底层操作。该二进制文件是 GDM 的核心进程，以提升后的权限运行，用于管理显示服务器和创建用户会话。

在现代系统中，gdm-binary 通常由 systemd 启动和管理，而非由用户或管理员直接调用。gdm 服务包装器负责进程管理，而 gdm-binary 则执行实际的显示管理器功能。

用户很少需要直接操作 gdm-binary，因为 systemctl 等系统管理命令或 gdm 包装脚本才是控制显示管理器的首选接口。

# INSTALL

```dnf: sudo dnf install gdm```

```pacman: sudo pacman -S gdm```

```apk: sudo apk add gdm```

```zypper: sudo zypper install gdm```

```nix: nix profile install nixpkgs#gdm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdm](/man/gdm)(8), [gdm-restart](/man/gdm-restart)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/gdm)```

<!-- verified: 2026-07-15 -->
