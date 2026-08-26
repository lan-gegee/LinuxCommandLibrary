# TAGLINE

可滚动平铺的 Wayland 合成器

# TLDR

**启动**合成器

```niri```

**以桌面会话方式启动**（把环境导入 systemd 和 D-Bus）

```niri --session```

**使用备用配置**文件

```niri -c [path/to/config.kdl]```

**校验**配置文件

```niri validate```

向运行中的实例**查询已连接的输出**

```niri msg outputs```

在运行中的实例里**执行一个绑定的操作**

```niri msg action [action-name]```

以机器可读的 JSON **列出窗口**

```niri msg --json windows```

# SYNOPSIS

**niri** [_-c config_] [_--session_] [_subcommand_]

# DESCRIPTION

**niri** 是一款可滚动平铺（scrollable-tiling）的 Wayland 合成器。它不把窗口挤进固定的网格，而是把窗口排成一列列，放在一条无限宽的水平带上：打开新窗口绝不会改变其他窗口的大小，你只需滚动到那里即可。每台显示器都有自己独立的一条带，以及一组垂直堆叠的动态工作区。

在 TTY 上直接运行 **niri** 会立即启动合成器。在已有会话中通常以 **niri --session** 启动，这样会把 Wayland 和显示环境导出到 systemd 和 D-Bus，使 portal 和用户服务得以正常工作。对于运行中的实例，可通过 IPC 套接字用 **niri msg** 子命令进行检查和控制：它能报告输出、工作区和窗口信息，并能触发 niri 的任意内置操作。

# PARAMETERS

**-c** _PATH_, **--config** _PATH_
> 从 _PATH_ 加载配置，而不是默认位置。

**--session**
> 以会话方式启动：设置好环境，并与 systemd 和 D-Bus 集成。

**validate**
> 检查配置文件是否有错误，然后退出。

**msg** _SUBCOMMAND_
> 与运行中的 niri 实例通信（outputs、workspaces、windows、focused-window、focused-output、action、keyboard-layouts、version、event-stream）。

**msg --json** _SUBCOMMAND_
> 以 JSON 格式输出应答，便于脚本处理。

**panic**
> 故意触发一次 panic，用于测试崩溃处理流程。

# CONFIGURATION

niri 从 **$XDG_CONFIG_HOME/niri/config.kdl** 读取 KDL 配置文件（如果不存在则回退到 **~/.config/niri/config.kdl**）。该文件定义了按键绑定、输入设备、输出布局、窗口规则和动画；当它在磁盘上发生变化时会被实时重新加载。

# HISTORY

**niri** 由 **Ivan Molodetskikh**（YaLTeR）创建，于 **2023 年**首次发布。它在 Smithay 合成器工具包之上用 **Rust** 编写，以 **GPL-3.0** 许可证分发。其按列组织的"可滚动平铺"模型灵感来自 GNOME 的 PaperWM 扩展。

# INSTALL

```dnf: sudo dnf install niri```

```pacman: sudo pacman -S niri```

```apk: sudo apk add niri```

```zypper: sudo zypper install niri```

```nix: nix profile install nixpkgs#niri```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sway](/man/sway)(1), [hyprland](/man/hyprland)(1), [swaymsg](/man/swaymsg)(1), [weston](/man/weston)(1)

# RESOURCES

```[Source code](https://github.com/YaLTeR/niri)```

```[Documentation](https://niri-wm.github.io/niri/)```

<!-- verified: 2026-06-10 -->
