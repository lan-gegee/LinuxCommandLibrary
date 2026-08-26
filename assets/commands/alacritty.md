# TAGLINE

GPU 加速的终端模拟器

# TLDR

**启动** Alacritty

```alacritty```

以**指定工作目录**打开

```alacritty --working-directory [/path/to/dir]```

执行一条**命令**

```alacritty -e [htop]```

以**自定义配置**打开

```alacritty --config-file [~/.config/alacritty/custom.toml]```

设置**窗口标题**

```alacritty --title "[My Terminal]"```

将旧的 YAML 配置**迁移**为 TOML

```alacritty migrate```

# SYNOPSIS

**alacritty** [_options_] [**-e** _command_ ...]

**alacritty** _subcommand_ [_options_]

# DESCRIPTION

**alacritty** 是一款注重简洁与性能的现代 GPU 加速终端模拟器。它利用 OpenGL 进行渲染，提供流畅的滚动和低延迟的输入处理。

配置通过 TOML 或 YAML 文件完成（取决于版本），支持自定义颜色、字体、按键绑定和行为。它力求在保持可配置性的同时提供合理的默认值。

# PARAMETERS

**-e**, **--command** _command_ _args_
> 执行命令及其参数而不是默认 shell（必须是最后一个参数）。

**--working-directory** _path_
> 在指定工作目录中启动 shell。

**--config-file** _file_
> 使用备用配置文件。

**-T**, **--title** _title_
> 设置窗口标题。

**--class** _class_
> 在 Linux/BSD 上设置窗口类提示（仅限 X11）。

**-o**, **--option** _key=value_
> 覆盖配置文件中的选项。

**--hold**
> 子进程退出后保持窗口打开。

**--daemon**
> 不生成初始窗口（在后台运行以支持 IPC）。

**--embed** _id_
> 用于嵌入 Alacritty 的 X11 窗口 ID。

**--socket** _path_
> 创建 IPC 套接字的路径。

**-V**, **--version**
> 显示版本信息。

**-q**, **-v**
> 降低（**-q**、**-qq**）或提高（**-v**、**-vv**、**-vvv**）详细程度。

**--print-events**
> 将所有事件打印到 stdout 以便调试。

**migrate**
> 将现有 YAML 配置文件转换为 TOML 的子命令。

**msg**
> 向正在运行的守护进程实例发送 IPC 消息（例如 **create-window**、**config**）的子命令。

# CONFIGURATION

**~/.config/alacritty/alacritty.toml**
> 主配置文件，用于颜色、字体、按键绑定、窗口设置和 shell 行为。

**~/.config/alacritty/alacritty.yml**
> 0.13 之前版本使用的旧版 YAML 配置文件。

# CAVEATS

需要支持 OpenGL 3.3+ 的 GPU。没有标签页或分屏功能（请使用 tmux/screen）。配置格式在 0.13 版本从 YAML 变更为 TOML。某些功能可能需要较新的显卡驱动。

# HISTORY

**alacritty** 由 Joe Wilm 创建，于 **2017** 年首次发布。它是第一款主要的 GPU 加速终端模拟器，启发了类似项目，并因性能和极简设计而流行。

# INSTALL

```apt: sudo apt install alacritty```

```dnf: sudo dnf install alacritty```

```pacman: sudo pacman -S alacritty```

```apk: sudo apk add alacritty```

```zypper: sudo zypper install alacritty```

```nix: nix profile install nixpkgs#alacritty```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[tmux](/man/tmux)(1), [screen](/man/screen)(1), [kitty](/man/kitty)(1)

# RESOURCES

```[Source code](https://github.com/alacritty/alacritty)```

```[Homepage](https://alacritty.org/)```

<!-- verified: 2026-06-11 -->
