# TAGLINE

可扩展、可定制的文本编辑器与计算环境

# TLDR

**打开 Emacs** 并载入一个文件

```emacs [path/to/file]```

**打开文件**并定位到指定行号

```emacs +[42] [path/to/file]```

**打开文件**并定位到指定行列

```emacs +[42]:[10] [path/to/file]```

**以终端模式运行 Emacs**（无 GUI）

```emacs -nw [path/to/file]```

**启动 Emacs 但不加载初始化文件**

```emacs -q```

**求值 Elisp 表达式**后退出

```emacs --batch --eval '(message "Hello")'```

**以守护进程方式运行 Emacs**，便于客户端快速连接

```emacs --daemon```

**连接到 Emacs 守护进程**

```emacsclient [path/to/file]```

# SYNOPSIS

**emacs** [_options_] [_file_...]

**emacs** [_+line_] [_+line:column_] [_file_...]

# PARAMETERS

**-nw**, **--no-window-system**
> 以终端模式运行，不使用 GUI（文本终端）

**-q**, **--no-init-file**
> 不加载用户初始化文件（~/.emacs）

**--no-site-file**
> 不加载全站范围的启动文件

**-u** _USER_, **--user** _USER_
> 加载指定用户的初始化文件

**-t** _FILE_, **--terminal** _FILE_
> 将指定文件用作终端

**--debug-init**
> 在处理初始化文件期间启用 Emacs Lisp 调试器

**--batch**
> 以批处理模式运行（非交互式）

**--script** _FILE_
> 将指定文件作为 Emacs Lisp 脚本运行

**--eval** _EXPRESSION_
> 求值 Emacs Lisp 表达式

**-l** _FILE_, **--load** _FILE_
> 加载指定的 Emacs Lisp 文件

**-f** _FUNCTION_, **--funcall** _FUNCTION_
> 执行指定的 Emacs Lisp 函数

**--daemon**
> 将 Emacs 作为后台守护进程启动

**-Q**, **--quick**
> 以最小配置启动（等价于 -q --no-site-file --no-splash）

**--geometry** _WIDTHxHEIGHT+X+Y_
> 设置窗口几何属性（X11）

**-fs**, **--fullscreen**
> 以全屏模式启动

**-fw**, **--fullwidth**
> 使窗口与屏幕同宽

**-fh**, **--fullheight**
> 使窗口与屏幕同高

**-fg** _COLOR_
> 设置前景色

**-bg** _COLOR_
> 设置背景色

**-d** _DISPLAY_, **--display** _DISPLAY_
> 使用指定的 X display

**--version**
> 显示版本信息

**--help**
> 显示帮助信息

# DESCRIPTION

**emacs** 是一个可扩展、可定制、自我文档化的文本编辑器与计算环境。它远不止一个简单的编辑器，还提供电子邮件、文件管理、终端模拟、网页浏览等功能，并通过扩展系统支持数千种其他功能。

Emacs 构建于 Emacs Lisp（Elisp）之上——这是一门完整的编程语言，用户可以用它定制和扩展编辑器的几乎所有方面。用户配置存储在 **~/.emacs** 或 **~/.emacs.d/init.el** 中。

编辑器会根据文件类型进入不同的模式，提供语法高亮、缩进以及模式专属命令。主模式（major mode）负责处理不同的文件类型，次模式（minor mode）则添加可选功能。内置的帮助系统通过 **C-h**（Ctrl+h）或 **F1** 访问。

# CONFIGURATION

**~/.emacs**
> 用于 Emacs 配置与定制的用户初始化文件。

**~/.emacs.d/init.el**
> 用户初始化文件的替代位置，更适合组织多个配置文件。

**~/.emacs.d/**
> 存放软件包、主题及其他 Elisp 文件的目录。

# CAVEATS

Emacs 的键盘快捷键体系庞大，学习曲线陡峭。其默认按键绑定与大多数现代应用程序不同（例如用 **C-x C-s** 保存、**C-x C-c** 退出）。使用 **-q** 运行有助于排查配置问题。未做适当配置时大文件可能加载缓慢。GUI 模式与终端模式的功能有所不同。

# HISTORY

最初的 EMACS 由 **David A. Moon**、**Guy L. Steele Jr.** 和 **Richard Stallman** 于 **1976 年**在 MIT 创建，由 TECO 编辑器的编辑宏演化而来。使用最广泛的实现 GNU Emacs 于 **1985 年**首次发布，成为 GNU 计划的旗舰项目。该名称最初是 "**E**ditor **MAC**ro**S**" 的缩写。Emacs 推动了自由软件运动，至今仍是最古老且持续活跃开发的软件项目之一。它的竞争对手 **vi** 曾在 Unix 用户中引发著名的"编辑器之战"。

# INSTALL

```dnf: sudo dnf install emacs```

```pacman: sudo pacman -S emacs```

```apk: sudo apk add emacs-gtk3```

```zypper: sudo zypper install emacs```

```brew: brew install emacs```

```nix: nix profile install nixpkgs#emacs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1), [nano](/man/nano)(1), [emacsclient](/man/emacsclient)(1), [vi](/man/vi)(1)
