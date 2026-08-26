# TAGLINE

与 i3 兼容的平铺式 Wayland 合成器

# TLDR

从 TTY **启动 sway**

```sway```

**使用自定义配置文件启动**

```sway --config [path/to/config]```

**校验配置文件**而不启动

```sway --validate```

**以详细日志启动**

```sway --verbose```

**以调试日志启动**

```sway --debug```

**获取 IPC 套接字路径**

```sway --get-socketpath```

# SYNOPSIS

**sway** [_options_] [_command_]

# PARAMETERS

**-c**, **--config** _file_
> 使用替代配置文件而不是默认值（~/.config/sway/config）。

**-C**, **--validate**
> 检查配置文件是否有语法错误，不启动合成器。

**-d**, **--debug**
> 启用完整日志，包括调试信息。

**-V**, **--verbose**
> 启用更详细的日志。

**--get-socketpath**
> 获取 IPC 套接字路径并打印后退出。

**--unsupported-gpu**
> 允许在不受支持的 GPU 上运行（NVIDIA 495 及以上驱动需要）。

**-v**, **--version**
> 显示版本号后退出。

**-h**, **--help**
> 显示帮助信息后退出。

# DESCRIPTION

**sway** 是一个平铺式 Wayland 合成器，是 X11 下 i3 窗口管理器的直接替代品。它可以兼容现有的 i3 配置文件，在原生 Wayland 上运行的同时支持大多数 i3 特性。

Sway 可以直接从 TTY 启动，也可以通过兼容 Wayland 的显示管理器启动。配置文件通常位于 **~/.config/sway/config**，默认模板位于 **/etc/sway/config**。Sway 通过 **SWAYSOCK** 环境变量指定的 IPC 套接字与客户端通信。

该合成器使用 wlroots 作为其 Wayland 库，支持多输出、工作区、浮动与平铺布局、键盘和鼠标绑定等特性，并能与 waybar、swaybar 等状态栏集成。

# CONFIGURATION

**~/.config/sway/config**
> 用户主配置文件，定义快捷键绑定、输出、输入、窗口规则和启动命令。

**/etc/sway/config**
> 全系统默认配置模板。

**SWAYSOCK**
> 指向 IPC 套接字的环境变量，用于与正在运行的 Sway 实例通信。

# CAVEATS

专有 NVIDIA 驱动不受官方支持。对于 NVIDIA 495 及以上版本的驱动，启用内核模式设置（kernel mode setting）后，sway 或许可以配合 **--unsupported-gpu** 参数运行，但这属于未受支持的情形。推荐使用开源驱动（Intel、AMD、nouveau）。

# HISTORY

Sway 由 **Drew DeVault**（SirCmpwn）创建，于 **2016 年**首次发布，目标是将 i3 的工作流带到 Wayland 上。名字代表 "SirCmpwn's Wayland compositor"。Sway 于 **2019 年 3 月**达到 1.0 稳定版，实现了与 i3 的功能对齐。它构建在 **wlroots** 库之上——该库同样由 Drew DeVault 创建，用于提供模块化的 Wayland 合成器库。

# INSTALL

```apt: sudo apt install sway```

```dnf: sudo dnf install sway```

```pacman: sudo pacman -S sway```

```apk: sudo apk add sway```

```zypper: sudo zypper install sway```

```nix: nix profile install nixpkgs#sway```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[swaymsg](/man/swaymsg)(1), [swaybar](/man/swaybar)(5), [i3](/man/i3)(1), [waybar](/man/waybar)(5)
