# TAGLINE

显示 X 服务器信息

# TLDR

**显示全部 X 服务器信息**

```xdpyinfo```

**查询指定的 display**

```xdpyinfo -display [localhost:0.0]```

**列出扩展及其操作码和事件编号**

```xdpyinfo -queryExtensions```

**显示某个扩展的详细信息**

```xdpyinfo -ext [RENDER]```

**显示所有扩展的详细信息**

```xdpyinfo -ext all```

**显示版本并退出**

```xdpyinfo -version```

# SYNOPSIS

**xdpyinfo** [_options_]

# PARAMETERS

**-display** _name_
> 要查询的 X display（默认：$DISPLAY）。

**-queryExtensions**
> 包含扩展的操作码、事件基址和错误基址编号。

**-ext** _name_
> 显示指定扩展的详细信息（用 "all" 表示所有扩展）。

**-version**
> 显示程序版本并退出。

# DESCRIPTION

**xdpyinfo** 显示关于 X 服务器的信息，包括其能力、协议版本、厂商、可用的屏幕和视觉类型以及已加载的扩展。

输出内容包括屏幕尺寸、颜色深度、支持的视觉类型和默认设置。扩展信息显示哪些 X11 扩展可用，对调试图形和输入问题很有帮助。

该工具有助于验证 X 服务器配置、检查所需的扩展以及排查显示问题。它常被用来确认 X11 是否正常工作。

# CAVEATS

需要运行中的 X 服务器并正确设置 DISPLAY。使用 -queryExtensions 可能加载所有扩展，消耗资源。仅支持 X11；在纯 Wayland 下无法使用。

# HISTORY

**xdpyinfo** 是 X.Org 项目实用工具集的一部分。X11 自 1987 年以来一直是 Unix 系统的标准显示协议。该工具为 X 服务器管理和故障排查提供重要的诊断信息。

# INSTALL

```apt: sudo apt install x11-utils```

```dnf: sudo dnf install xdpyinfo```

```apk: sudo apk add xdpyinfo```

```zypper: sudo zypper install xdpyinfo```

```brew: brew install xdpyinfo```

```nix: nix profile install nixpkgs#xdpyinfo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xwininfo](/man/xwininfo)(1), [xprop](/man/xprop)(1), [xrandr](/man/xrandr)(1), [glxinfo](/man/glxinfo)(1), [xset](/man/xset)(1), [xlsclients](/man/xlsclients)(1)
