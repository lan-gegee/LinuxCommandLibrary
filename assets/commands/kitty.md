# TAGLINE

GPU 加速的终端模拟器

# TLDR

**启动 kitty**

```kitty```

**以特定命令启动**

```kitty [command]```

**在指定目录中启动**

```kitty -d [/path/to/directory]```

**使用会话布局启动**

```kitty --session [session.conf]```

**覆盖某项配置**

```kitty -o [font_size=14]```

通过远程控制**打开新窗口**

```kitty @ new-window```

通过远程控制**打开新标签页**

```kitty @ new-tab```

**以 JSON 列出所有窗口**

```kitty @ ls```

# SYNOPSIS

**kitty** [_options_] [_command_]

# PARAMETERS

_COMMAND_
> 要在终端中运行的命令。

**@**
> 远程控制前缀，用于向正在运行的 kitty 实例发送命令。

**--config** _FILE_, **-c** _FILE_
> 要使用的配置文件路径。

**--override** _OPTION=VALUE_, **-o** _OPTION=VALUE_
> 覆盖单个配置选项。

**--start-as** _MODE_
> 窗口模式：normal、fullscreen、maximized、minimized。

**--directory** _DIR_, **-d** _DIR_
> 启动时切换到指定目录。

**--session** _FILE_
> 包含启动会话（标签页、窗口、布局、程序）的文件路径。

**--single-instance**, **-1**
> 若已有 kitty 实例在运行，则在其中打开新窗口。

**--listen-on** _ADDRESS_
> 在指定地址上监听远程控制消息。

**--title** _TITLE_, **-T** _TITLE_
> 设置 OS 窗口标题。

**--class** _CLS_
> 设置 WM_CLASS 窗口属性（或 Wayland app id）。

**--detach**
> 与控制终端分离。

# DESCRIPTION

**kitty** 是一款快速、功能丰富的 GPU 加速终端模拟器，使用 OpenGL 渲染以获得流畅的性能。它支持内联图片显示、字体连字、Unicode、多种布局、标签页和窗口，以及用于专门任务的可扩展 kitten 程序。它可以通过 kitty.conf 高度配置，并能通过远程控制协议进行脚本化操作。

# CAVEATS

需要支持 OpenGL 3.3+ 的 GPU。它使用自己的 terminfo 条目（xterm-kitty），SSH 到远程服务器时可能需要在该服务器上安装。远程控制需要在 kitty.conf 中配置 --listen-on 或 allow_remote_control。

# HISTORY

kitty 由 **Kovid Goyal** 创建，是一款利用现代 GPU 能力的快速且功能丰富的终端模拟器。

# INSTALL

```apt: sudo apt install kitty```

```dnf: sudo dnf install kitty```

```pacman: sudo pacman -S kitty```

```apk: sudo apk add kitty```

```zypper: sudo zypper install kitty```

```nix: nix profile install nixpkgs#kitty```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[alacritty](/man/alacritty)(1), [wezterm](/man/wezterm)(1), [tmux](/man/tmux)(1)
