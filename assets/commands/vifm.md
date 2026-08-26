# TAGLINE

类 vim 的双栏文件管理器

# TLDR

**启动 vifm**

```vifm```

**在指定目录中启动**

```vifm [/path/to/dir]```

**以两个不同目录的窗格启动**

```vifm [/left/path] [/right/path]```

**启动时执行命令**

```vifm -c "[command]"```

**选择文件并将选中项写入文件**

```vifm --choose-files [output_file]```

**打开并高亮指定文件**

```vifm --select [/path/to/file]```

**从 stdin 读取文件列表以创建自定义视图**

```find . -name "[*.txt]" | vifm -```

# SYNOPSIS

**vifm** [_options_] [_lwinpath_] [_rwinpath_]

# PARAMETERS

**-c** _CMD_
> 启动时执行命令行模式命令。

**+**_CMD_
> 启动时执行命令行模式命令（另一种语法）。

**--choose-files** _FILE_
> 退出时将所选文件路径写入 FILE（使用 **-** 表示 stdout）。

**--choose-dir** _FILE_
> 退出时将最后访问的目录写入 FILE（使用 **-** 表示 stdout）。

**--delimiter** _DELIM_
> 设置文件路径列表的分隔符（默认为换行符）。

**--select** _PATH_
> 打开父目录并高亮指定的文件。

**--on-choose** _CMD_
> 对选中的文件执行命令，而不是打开它们。

**-f**
> 将选中项写入 $VIFM/vimfiles（供 vifm.vim 插件使用）。

**--remote**
> 将其余参数发送给已在运行的 vifm 实例。

**--remote-expr** _EXPR_
> 将表达式传递给 vifm 服务器并打印结果。

**--server-name** _NAME_
> 设置或指向一个具名的 vifm 服务器实例。

**--server-list**
> 列出可用的 vifm 服务器名称并退出。

**--plugins-dir** _PATH_
> 添加插件目录（可多次指定）。

**--no-configs**
> 跳过读取 vifmrc 和 vifminfo 文件。

**--logging**[=_PATH_]
> 启用日志记录到 $VIFM/log 或指定路径。

**-h**, **--help**
> 显示帮助。

**-v**, **--version**
> 显示版本。

# KEY BINDINGS

**j/k**
> 向下/向上移动。

**h/l**
> 返回上级目录/进入目录。

**yy**
> 复制（yank）。

**dd**
> 删除。

**p**
> 粘贴。

**cw**
> 重命名。

**/**
> 搜索。

**:q**
> 退出。

**Tab**
> 切换窗格。

**Space**
> 选中文件。

**za**
> 切换隐藏文件显示。

# DESCRIPTION

**vifm** 是一个基于 curses 的文件管理器，采用类 vim 键绑定。它提供双栏导航和熟悉的模态编辑方式。

Vi 键绑定使导航非常快速。j/k 移动，h 返回上级，l 进入目录。标记、寄存器和宏的工作方式与 vim 类似。

双栏布局让跨目录的文件操作变得轻松。Tab 切换焦点。操作可以针对另一个窗格进行。

文件操作使用熟悉的模式。yy 复制，p 粘贴，dd 删除。Visual 模式可选择多个文件。

通过 **vifmrc** 可自定义键绑定、配色和行为。文件预览、图标和脚本可以扩展功能。**--choose-dir** 和 **--choose-files** 选项支持与 shell 脚本及其他程序集成。

**--remote** 选项允许向运行中的实例发送命令，**--server-name** 支持管理多个具名实例。

# CAVEATS

非 vim 用户需要学习曲线。某些操作与 vim 不同。需要配置才能获得最佳体验。

# HISTORY

**vifm** 创建于 **2001 年**前后，是一个采用类 vim 键绑定的基于 curses 的文件管理器。它持续活跃开发并加入现代特性，包括近期版本新增的插件支持。

# INSTALL

```apt: sudo apt install vifm```

```dnf: sudo dnf install vifm```

```pacman: sudo pacman -S vifm```

```apk: sudo apk add vifm```

```zypper: sudo zypper install vifm```

```brew: brew install vifm```

```nix: nix profile install nixpkgs#vifm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ranger](/man/ranger)(1), [nnn](/man/nnn)(1), [mc](/man/mc)(1), [lf](/man/lf)(1), [vim](/man/vim)(1)
