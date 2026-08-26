# TAGLINE

GPU 加速的终端模拟器

# TLDR

**启动终端**

```wezterm```

**启动并执行命令**

```wezterm start -- [command]```

**打开新标签页**

```wezterm cli spawn```

**水平分割面板**

```wezterm cli split-pane --horizontal```

**垂直分割面板**

```wezterm cli split-pane```

**列出标签页**

```wezterm cli list```

**连接远程主机**

```wezterm connect [host]```

**显示配置**

```wezterm show-keys```

# SYNOPSIS

**wezterm** [_start_] [_cli_] [_connect_] [_options_] [_-- command_]

# PARAMETERS

**start** [_--_] _CMD_
> 启动终端并执行命令。

**cli spawn**
> 打开新标签页。

**cli split-pane**
> 分割当前面板。

**cli list**
> 列出面板/标签页。

**connect** _HOST_
> 连接到多路复用器。

**ssh** _DEST_
> SSH 连接。

**serial** _PORT_
> 串口连接。

**show-keys**
> 显示按键绑定。

**--config** _KEY=VALUE_
> 覆盖配置。

**--config-file** _FILE_
> 配置文件路径。

# DESCRIPTION

**wezterm** 是一款 GPU 加速的终端模拟器。它使用 Rust 编写，跨平台且高度可配置。

配置采用 Lua 脚本。按键绑定、外观和行为均可编程定制，具备完整的脚本能力。

内置多路复用功能。无需 tmux 即可使用标签页和面板。会话持久保存并可重新接入。

远程多路复用可以连接其他机器上运行的 wezterm。本地终端控制远程会话。

GPU 渲染带来流畅滚动和高效显示。连字、emoji 和 Nerd Fonts 都能正确工作。

超链接可点击。URL、文件路径和自定义模式都可以配置为可点击链接。

# CAVEATS

Lua 配置有一定学习曲线。某些功能仅跨平台可用。GPU 加速需要兼容的驱动。

# HISTORY

**WezTerm** 由 **Wez Furlong**（wez）于 **2018 年**前后创建。它将现代渲染与强大的多路复用相结合，定位于简单终端与完整终端复用器之间。

# INSTALL

```pacman: sudo pacman -S wezterm```

```apk: sudo apk add wezterm-common```

```zypper: sudo zypper install wezterm```

```nix: nix profile install nixpkgs#wezterm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[alacritty](/man/alacritty)(1), [kitty](/man/kitty)(1), [tmux](/man/tmux)(1), [foot](/man/foot)(1)
