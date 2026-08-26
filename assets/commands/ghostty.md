# TAGLINE

具备现代特性的 GPU 加速终端模拟器

# TLDR

**启动 Ghostty** 终端模拟器

```ghostty```

**在新终端窗口中运行命令**

```ghostty -e [command]```

**以指定的工作目录启动**

```ghostty --working-directory=[/path/to/directory]```

**使用自定义配置文件**

```ghostty --config-file=[path/to/config]```

**以全屏模式启动**

```ghostty --fullscreen```

**设置自定义字体和字号**

```ghostty -o font-family=[Fira Code] -o font-size=[14]```

**覆盖某个配置选项**

```ghostty -o [font-size=14]```

**列出可用主题**

```ghostty +list-themes```

**列出系统上可用的字体**

```ghostty +list-fonts```

**显示当前配置及所有已解析的值**

```ghostty +show-config```

# SYNOPSIS

**ghostty** [_-e command_] [_-o option=value_] [_--config-file file_] [_--working-directory path_] [_options_]

**ghostty** **+**_action_ [_options_]

# PARAMETERS

**-e** _command_
> 执行指定命令而不是默认 Shell。

**-o** _option=value_
> 覆盖某个配置选项。

**--config-file** _path_
> 使用备用配置文件。

**--working-directory** _path_
> 设置初始工作目录。

**--fullscreen**
> 以全屏模式启动。

**--title** _string_
> 设置窗口标题。

**--class** _string_
> 设置窗口类（Wayland/X11）。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

**+list-actions**
> 列出可用于按键绑定的操作。

**+list-colors**
> 列出可用的颜色名称。

**+list-fonts**
> 列出可用的字体。

**+list-keybinds**
> 列出当前的按键绑定。

**+list-themes**
> 列出可用的主题。

**+show-config**
> 显示当前配置及所有已解析的值。

**+validate**
> 检查配置文件中的错误。

**+crash-report**
> 显示最近一次崩溃的详细信息。

# DESCRIPTION

**Ghostty** 是一个快速且功能丰富的终端模拟器，使用 GPU 加速进行渲染。它兼具极简终端的速度与高级特性，同时保持与原生平台的深度集成。

该终端支持真彩色（24 位）、带连字和表情符号的 Unicode、图片（Sixel、iTerm2、Kitty 协议）、超链接以及带字体回退的高级文本渲染。它提供标签页、分屏和多窗口支持，按键绑定完全可自定义。

# CONFIGURATION

**~/.config/ghostty/config**（Linux）
> 主配置文件，以键值对形式存放所有设置，包括字体、颜色、按键绑定和行为。

**~/Library/Application Support/com.mitchellh.ghostty/config**（macOS）
> macOS 系统上的主配置文件。

# CAVEATS

需要支持 OpenGL 3.3+ 或 Vulkan（Linux）或 Metal（macOS）的 GPU。配置采用简单的 key=value 格式（值不加引号）。目前仅支持 macOS 和 Linux。

# HISTORY

**Ghostty** 由 Mitchell Hashimoto（HashiCorp 创始人）创建，经过数年开发后于 **2024 年 12 月**公开发布。该项目开源，使用 Zig 编写。

# INSTALL

```pacman: sudo pacman -S ghostty```

```zypper: sudo zypper install ghostty```

```nix: nix profile install nixpkgs#ghostty```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kitty](/man/kitty)(1), [alacritty](/man/alacritty)(1), [wezterm](/man/wezterm)(1), [foot](/man/foot)(1), [tmux](/man/tmux)(1)
