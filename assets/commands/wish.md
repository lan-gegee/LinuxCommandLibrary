# TAGLINE

Tcl/Tk 图形化解释器

# TLDR

**启动交互式 Tk shell**

```wish```

**运行 Tk 脚本**

```wish [script.tcl]```

**带参数运行脚本**

```wish [script.tcl] [arg1] [arg2]```

**直接执行 Tk 命令**

```echo "[button .b -text Hello; pack .b]" | wish```

# SYNOPSIS

**wish** [_options_] [_script_] [_args_...]

# PARAMETERS

**-colormap** _new_
> 使用新的私有色彩映射表。

**-display** _display_
> 要使用的 X display。

**-geometry** _geometry_
> 初始窗口几何布局。

**-name** _name_
> 将 name 用作应用名称。

**-sync**
> 同步执行 X 服务器请求。

**-visual** _visual_
> 主窗口的 visual 类型。

**-use** _id_
> 嵌入到具有给定 id 的窗口中。

**--**
> 选项结束；其余参数传给脚本。

# DESCRIPTION

**wish** 是一个用 Tk 工具集命令扩展的 Tcl 解释器，用于创建图形界面。它从文件或标准输入读取 Tcl/Tk 命令并执行，创建 GUI 窗口和控件。

不带参数运行时，wish 以交互方式启动，显示一个空的主窗口和一个 "%" 提示符供输入命令。脚本可以在第一行加上 #!/usr/bin/wish 使其可直接执行。

Tk 提供的控件包括按钮、标签、输入框、列表框、画布、菜单等等。几何管理器命令（pack、grid、place）控制控件的布局。

# INTERACTIVE

在交互模式下，wish 显示 "%" 提示符。完整语句输入后才会执行。提示符可通过 tcl_prompt1 和 tcl_prompt2 变量自定义。

# CAVEATS

需要显示服务器（X11 或带 XWayland 的 Wayland）。没有主题时 Tk 应用外观较陈旧（ttk 主题控件可改善这一点）。某些发行版使用带版本号的名称，如 wish8.6。在 macOS 上，Tk 原生使用 Aqua。

# HISTORY

**wish** 由 John Ousterhout 于 20 世纪 80 年代末与 Tcl 一同创建。Tk 是最早的跨平台 GUI 工具集之一，影响了后来的许多框架。Wish 至今仍常用于快速 GUI 脚本编写，gitk 等工具就使用了它。

# INSTALL

```apt: sudo apt install tk```

```dnf: sudo dnf install tk```

```pacman: sudo pacman -S tk```

```apk: sudo apk add tk```

```zypper: sudo zypper install tk```

```nix: nix profile install nixpkgs#tk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gitk](/man/gitk)(1), [xdotool](/man/xdotool)(1)
