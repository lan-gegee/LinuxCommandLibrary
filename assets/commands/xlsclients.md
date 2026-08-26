# TAGLINE

列出已连接的 X11 客户端应用程序

# TLDR

**列出 X 客户端**

```xlsclients```

**显示所有窗口**

```xlsclients -a```

**长格式输出**

```xlsclients -l```

**指定显示器**

```xlsclients -display [:0]```

# SYNOPSIS

**xlsclients** [_-a_] [_-l_] [_-display dpy_] [_options_]

# PARAMETERS

**-a**
> 所有屏幕。

**-l**
> 长格式。

**-display** _DPY_
> X 显示器。

**-m** _MAXCMD_
> 命令的最大长度。

# DESCRIPTION

**xlsclients** 列出当前连接到 X 显示服务器的客户端应用程序。它会显示每个客户端的窗口名称和启动命令，让你快速了解哪些 X11 应用正在运行。

该工具适用于调试 X11 会话、识别哪些应用正在占用显示资源，以及确认预期的客户端已连接。**-a** 选项显示所有屏幕上的客户端，而 **-l** 提供长格式输出，包含每个客户端的主机名和命令行等额外细节。

# CAVEATS

仅支持 X11。不支持 Wayland。显示的信息有限。

# HISTORY

**xlsclients** 是用于列出连接到 X server 的客户端应用程序的标准 X11 工具。

# INSTALL

```apt: sudo apt install x11-utils```

```dnf: sudo dnf install xlsclients```

```zypper: sudo zypper install xlsclients```

```brew: brew install xlsclients```

```nix: nix profile install nixpkgs#xlsclients```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xwininfo](/man/xwininfo)(1), [xprop](/man/xprop)(1), [xdotool](/man/xdotool)(1)
