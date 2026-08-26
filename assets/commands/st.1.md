# TAGLINE

Suckless 简约终端模拟器

# TLDR

**打开**终端

```st```

以指定**标题**打开

```st -T [title]```

**执行命令**并将输出写入文件

```st -o [path/to/file] -e [command] [args]```

在终端中**执行命令**

```st -e [command] [args]```

设置**几何尺寸**

```st -g [columns]x[rows]```

# KEYBOARD SHORTCUTS

**Ctrl+Shift+PageUp/PageDown**
> 增大/减小字号

**Ctrl+Shift+c**
> 复制到剪贴板

**Ctrl+Shift+v**
> 从剪贴板粘贴

**Ctrl+Shift+y**
> 从选择区粘贴

# SYNOPSIS

**st** [_OPTIONS_] [**-e** _command_ [_args_...]]

# PARAMETERS

**-T** _title_
> 设置窗口标题

**-t** _title_
> 设置窗口标题（-T 的别名）

**-e** _command_ [_args_]
> 执行命令而非 Shell

**-o** _file_
> 将终端输出写入文件

**-g** _geometry_
> 设置窗口几何尺寸（WxH+X+Y）

**-f** _font_
> 设置字体（X11 字体字符串）

**-c** _class_
> 设置窗口类

**-n** _name_
> 设置窗口名

**-w** _windowid_
> 嵌入到给定的窗口 ID 中

**-a**
> 禁用备用屏幕缓冲区

**-i**
> 在插入模式下固定屏幕

**-v**
> 打印版本号

# DESCRIPTION

**st** 是来自 suckless 项目的 X11 简约终端模拟器。它追求轻量级并遵循 suckless 的极简哲学，提供一个只包含核心功能的精简终端，配置需通过修改源代码完成。

特性包括 UTF-8 支持、真彩色、剪贴板处理和可配置的快捷键。与功能丰富的终端不同，st 的定制方式是打补丁后重新编译，而不是通过配置文件。

# CAVEATS

配置需要编辑 config.h 并重新编译。默认不支持回滚（scrollback）；需要补丁或 **scroll**、**tmux** 等外部工具。没有标签页或分屏；请使用多路复用器。需要 X11；没有 XWayland 时无法在 Wayland 上运行。

# HISTORY

**st** 由 **suckless.org** 社区创建，该社区以 **dwm** 窗口管理器等极简软件闻名。项目遵循 suckless 哲学，强调软件设计中的简洁、清晰与节俭。st 自 **2012 年**起持续开发，作为臃肿终端模拟器的替代品。

# SEE ALSO

[xterm](/man/xterm)(1), [urxvt](/man/urxvt)(1), [alacritty](/man/alacritty)(1), [tmux](/man/tmux)(1)
