# TAGLINE

用 Python 编写、可深度定制的平铺窗口管理器

# TLDR

**启动**窗口管理器

```qtile start```

**检查**配置文件是否有错误

```qtile check```

显示**资源占用**信息

```qtile top --force```

在特定分组上**运行命令**

```qtile run-cmd --group [groupname] --float xterm```

**重启**窗口管理器

```qtile cmd-obj --object cmd --function restart```

以 **Wayland** 后端启动

```qtile start --backend wayland```

# SYNOPSIS

**qtile** _command_ [_options_]

# DESCRIPTION

**qtile** 是一款功能齐全、可深度定制的平铺窗口管理器，使用 Python 编写并通过 Python 进行配置。它提供动态平铺布局系统，可通过 Python 配置实现高度定制。

# PARAMETERS

**start**
> 启动窗口管理器（从 .xsession 或类似文件运行）

**start --backend** _BACKEND_
> 以指定后端启动（x11 或 wayland）

**check**
> 检查配置文件是否有错误（默认：~/.config/qtile/config.py）

**top**
> 显示当前资源占用信息

**run-cmd**
> 以特定选项启动程序

**cmd-obj**
> 执行命令对象的方法

**shell**
> 打开交互式 Python Shell 以控制 qtile

**migrate**
> 将用户的 config.py 迁移到较新的 Qtile API 版本

**repl**
> 将 Python REPL 连接到正在运行的 Qtile 实例，进行实时内省

**--group** _GROUP_
> 为 run-cmd 指定分组（工作区）

**--float**
> 以浮动窗口方式启动

**--object** _OBJECT_
> 为 cmd-obj 指定对象

**--function** _FUNCTION_
> 为 cmd-obj 指定要调用的函数

# CAVEATS

配置通过 Python 完成，位于 ~/.config/qtile/config.py。修改配置后务必运行 qtile check 验证语法。Qtile 需要 X11 或 Wayland（通过 qtile start --backend wayland）。

# HISTORY

**qtile** 的设计目标是一款高度可配置的平铺窗口管理器，使用 Python 进行配置，从而支持复杂的定制与脚本能力。

# INSTALL

```dnf: sudo dnf install qtile```

```pacman: sudo pacman -S qtile```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[i3](/man/i3)(1), [bspwm](/man/bspwm)(1), [awesome](/man/awesome)(1)
