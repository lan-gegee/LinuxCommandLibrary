# TAGLINE

连接正在运行的 Emacs 服务器，实现快速编辑

# TLDR

在已有的 Emacs frame 中**打开文件**

```emacsclient [file.txt]```

在终端中**打开文件**（无窗口）

```emacsclient -nw [file.txt]```

在新 frame 中**打开文件**

```emacsclient -c [file.txt]```

**打开文件**且不等待编辑完成

```emacsclient -n [file.txt]```

**求值 Emacs Lisp** 表达式

```emacsclient -e "(message \"Hello\")"```

在没有服务器时**启动备用编辑器**

```emacsclient -a "" [file.txt]```

**创建新 frame** 且不等待

```emacsclient -cn [file.txt]```

**连接到指定的套接字**

```emacsclient -s [server_name] [file.txt]```

# SYNOPSIS

**emacsclient** [_options_] [_files_...]

# DESCRIPTION

**emacsclient** 连接到已存在的 Emacs 服务器进程来打开文件或求值 Lisp 表达式。这样无需启动新的 Emacs 实例即可快速编辑文件，大幅缩短启动时间。

必须先用 M-x server-start 或在初始化文件中加入 (server-start) 来启动 Emacs 服务器。随后 emacsclient 与该服务器通信，在已有或新建的 frame 中打开文件。

这种工作流常用于把 Emacs 作为其他程序（git、crontab）的外部编辑器，或在保持持久 Emacs 会话的同时作为快捷的命令行编辑器。

# PARAMETERS

**-n**, **--no-wait**
> 立即返回，不等待编辑完成。

**-c**, **--create-frame**
> 创建一个新的图形 frame。

**-nw**, **-t**, **--tty**
> 在终端中打开，而非图形 frame。

**-e**, **--eval**
> 将参数作为 Emacs Lisp 求值。

**-a** _editor_, **--alternate-editor=** _editor_
> 在没有服务器时使用指定的编辑器（空字符串表示启动守护进程）。

**-s** _name_, **--socket-name=** _name_
> 连接到指定名称的服务器套接字。

**-f** _file_, **--server-file=** _file_
> 使用服务器文件进行 TCP 连接。

**-q**, **--quiet**
> 不显示消息。

**--version**
> 显示版本信息。

**--help**
> 显示帮助信息。

# CONFIGURATION

**~/.emacs.d/server/**
> Emacs 服务器连接所用的服务器套接字与认证文件。

# CAVEATS

需要 Emacs 服务器正在运行（或用 -a 启动守护进程）。终端模式（-nw）需要合适的终端。套接字权限可能阻止不同用户的访问。TCP 连接需要服务器文件。

# HISTORY

**emacsclient** 自早期版本起就是 **GNU Emacs** 的一部分，其服务器/客户端架构由 **Richard Stallman** 及贡献者设计。引入 Emacs 服务器模式的目的是让外部程序能够请求编辑，并减少反复启动 Emacs 的开销。该功能后来发展为同时支持 Unix 套接字和 TCP 连接。

# INSTALL

```dnf: sudo dnf install emacsclient```

```apk: sudo apk add emacs-gtk3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[emacs](/man/emacs)(1), [vim](/man/vim)(1), [nano](/man/nano)(1)

# RESOURCES

```[Source code](https://cgit.git.savannah.gnu.org/cgit/emacs.git)```

```[Homepage](https://www.gnu.org/software/emacs/)```

```[Documentation](https://www.gnu.org/software/emacs/manual/html_node/emacs/Emacs-Server.html)```

<!-- verified: 2026-07-14 -->
