# TAGLINE

在独立终端中运行的 Vim 文件浏览器

# TLDR

在当前目录**启动 vitree**（需要一个正在运行的 Vim 服务器）

```vitree```

**以服务器名启动 Vim**，让 vitree 能与其通信

```vim --servername vim```

**在指定目录打开 vitree**

```vitree [path/to/directory]```

在 vitree 内部**循环切换过滤模式**（默认 → 仅显示已变更 → 显示全部）

```f```

在 vitree 内部**显示快捷键帮助**

```?```

# SYNOPSIS

**vitree** [_path_]

# DESCRIPTION

**vitree** 是一个基于终端的文件浏览器，专为与 **Vim** 配合使用而设计。它不在编辑器内部运行文件树（也就不必再学一套关于调整大小、分屏和焦点切换的按键），而是在一个独立的终端窗口中运行，由你常用的窗口管理器或终端复用器管理。

它通过 Vim 的 **--servername** 机制连接到正在运行的 Vim 实例，因此在 vitree 中选中文件就会在所连接的 Vim 中打开。其界面是一个异步 TUI，具有自动刷新的目录树、类 Vim 的导航按键、鼠标支持和 ANSI 彩色输出。

默认情况下，被 **.gitignore** 匹配的文件会被隐藏，同时会为受 Git 跟踪的文件显示状态标记。按 **f** 可在过滤模式之间切换（默认 → 仅显示已变更 → 显示全部），按 **?** 则显示完整的快捷键参考。

# PARAMETERS

**_path_**
> 要打开的目录。默认为当前工作目录。

# CONFIGURATION

vitree 需要一个以服务器名启动的 Vim 实例，以便向其发送打开文件的命令：

```vim --servername vim```

Vim 运行后，在另一个终端中启动 **vitree** 即可自动连接。Git 集成使用所打开目录及其上层目录中的仓库；过滤时会遵循 **.gitignore** 规则。

# CAVEATS

要求 Vim 编译时带有 **+clientserver** 支持，并且有一个活动的 Vim 服务器（用 **--servername** 启动 Vim）。如果没有运行中的服务器，在 vitree 中选择文件时就没有可发送目标的编辑器。该项目是第三方软件（不属于标准 Linux 发行版），可通过 Homebrew、Go install 或 GitHub releases 页面上的预编译二进制分发。

# HISTORY

**vitree** 由 **hoffa** 编写，于 **2024** 年发布在 GitHub 上，采用 MIT 许可证。它使用 **Go** 编写，旨在作为 NERDTree 或 nvim-tree 等编辑器内文件树的轻量替代品。

# SEE ALSO

[vim](/man/vim)(1), [nnn](/man/nnn)(1), [ranger](/man/ranger)(1), [lf](/man/lf)(1), [broot](/man/broot)(1)
