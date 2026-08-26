# TAGLINE

WezTerm 终端控制 CLI

# TLDR

**启动新终端**

```wezterm start```

**连接 SSH**

```wezterm ssh [user@host]```

**连接串口**

```wezterm serial [/dev/ttyUSB0]```

**新建标签页**

```wezterm cli spawn```

**分割面板**

```wezterm cli split-pane --right```

**列出面板**

```wezterm cli list```

# SYNOPSIS

**wezterm** [_command_] [_options_]

# PARAMETERS

**start**
> 启动新终端。

**ssh** _destination_
> SSH 连接。

**serial** _port_
> 串口连接。

**cli spawn**
> 创建新标签页。

**cli split-pane**
> 分割当前面板。

**cli list**
> 列出窗口/标签页/面板。

**--config** _key=value_
> 覆盖配置。

# CONFIGURATION

**~/.wezterm.lua** 或 **~/.config/wezterm/wezterm.lua**
> 基于 Lua 的配置文件，用于按键绑定、字体、颜色、多路复用设置和 SSH 域。

# DESCRIPTION

**wezterm** 是一款 GPU 加速的终端模拟器和多路复用器。它支持标签页、分割面板、SSH 和串口连接以及图像显示（sixel、iTerm2 协议）。配置通过 Lua 脚本完成，可实现动态行为和复杂的按键映射。

`wezterm cli` 子命令用于控制正在运行的 wezterm 实例，可以像 tmux 一样通过脚本管理面板。

# CAVEATS

`cli` 子命令要求 wezterm 实例正在运行且启用了 mux 服务器。Lua 配置出错会阻止终端启动；可使用 `wezterm --config-file` 测试备用配置。

# INSTALL

```pacman: sudo pacman -S wezterm```

```apk: sudo apk add wezterm-common```

```zypper: sudo zypper install wezterm```

```nix: nix profile install nixpkgs#wezterm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[alacritty](/man/alacritty)(1), [kitty](/man/kitty)(1), [tmux](/man/tmux)(1)
