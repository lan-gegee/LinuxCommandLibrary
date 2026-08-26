# TAGLINE

自定义桌面小组件系统

# TLDR

启动**守护进程**

```eww daemon```

**打开**一个小组件

```eww [-c|--config] [path/to/source_code_directory] open [window_name]```

**关闭**一个小组件

```eww [-c|--config] [path/to/source_code_directory] close [window_name]```

**重新加载**配置

```eww reload```

**终止**守护进程

```eww kill```

**获取**变量的值

```eww get [variable_name]```

**更新**变量

```eww update [variable_name]="[value]"```

打印并**监视日志**

```eww logs```

# SYNOPSIS

**eww** [_options_] _command_ [_arguments_]

# PARAMETERS

**daemon**
> 启动守护进程。

**open** _window_
> 打开一个小组件窗口。

**open-many** _windows..._
> 同时打开多个小组件窗口。

**close** _window_
> 关闭一个小组件窗口。

**close-all**
> 关闭所有已打开的小组件窗口。

**reload**
> 重新加载配置文件。

**kill**
> 停止守护进程。

**logs**
> 显示并跟踪日志。

**get** _variable_
> 打印变量的当前值。

**update** _var=value_
> 更新变量的值。

**state**
> 显示所有变量的当前状态。

**inspect**
> 打开 GTK 调试器。

**shell-completions** _shell_
> 生成 Shell 补全脚本（bash、fish、zsh）。

**-c**, **--config** _path_
> 指定配置目录。

**--no-daemonize**
> 不将守护进程派生到后台。

# DESCRIPTION

**eww**（ElKowar's Wacky Widgets）为任意窗口管理器创建自定义桌面小组件。它使用一套配置语言来定义具有动态内容和样式的小组件。

它常用于创建状态栏、侧边栏和其他桌面元素。

# CONFIGURATION

**~/.config/eww/eww.yuck**
> 用 eww 配置语言编写的小组件定义与结构。

**~/.config/eww/eww.scss**
> 使用 CSS/SCSS 语法的组件样式。

# CAVEATS

需要 eww 格式的配置文件。小组件要显示出来必须有守护进程运行。支持 X11 和 Wayland。

# INSTALL

```zypper: sudo zypper install eww```

```nix: nix profile install nixpkgs#eww```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[polybar](/man/polybar)(1), [conky](/man/conky)(1), [waybar](/man/waybar)(1)
