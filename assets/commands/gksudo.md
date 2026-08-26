# TAGLINE

带 GTK 密码对话框的 sudo 图形前端

# TLDR

以**特定用户**身份运行命令

```gksudo -u [userid] [command]```

在**保留**当前环境的同时运行命令

```gksudo -u [userid] -k [command]```

强制 gksudo 使用 **su** 运行命令

```gksudo -u [userid] -w [command]```

强制 gksudo 使用 **sudo** 运行命令

```gksudo -u [userid] -S [command]```

为给定命令输出**调试**信息

```gksudo -u [userid] -d [command]```

让 gksudo 将密码**打印到 stdout**

```gksudo -p [command]```

# SYNOPSIS

**gksudo** [_options_] _command_

# PARAMETERS

**-u**, **--user** _USER_
> 以指定用户身份运行命令（默认：root）

**-k**, **--preserve-env**
> 保留当前环境变量，不设置 `$HOME` 或 `$PATH`

**-l**, **--login**
> 使其成为登录 shell（可能与 Xauthority 产生问题）

**-w**, **--su-mode**
> 强制使用 su 进行认证

**-S**, **--sudo-mode**
> 强制使用 sudo 进行认证（默认）

**-d**, **--debug**
> 输出调试信息

**-g**, **--disable-grab**
> 在询问密码时不锁定键盘、鼠标和焦点

**-P**, **--prompt**
> 抓取键盘和鼠标前先询问用户

**-m**, **--message** _MSG_
> 密码对话框中的自定义消息

**-D**, **--description** _DESC_|_FILE_
> 所运行命令的描述，用于默认消息中

**-p**, **--print-pass**
> 将密码打印到 stdout，类似 ssh-askpass

# DESCRIPTION

**gksudo** 是 `sudo` 的图形前端，通过 GTK 对话框提示输入密码。它本质上是默认使用 sudo 模式的 `gksu`，以当前用户的密码和 sudo 权限进行认证。

这样可以在利用 sudo 的配置进行权限控制的同时，以提升的权限运行图形应用程序。

> **已弃用**：gksudo 不再维护且存在安全问题。请改用 PolicyKit 的 **pkexec** 进行图形化权限提升。

# CAVEATS

已弃用且无人维护。以 root 身份运行图形应用程序可能导致用户配置文件和 X 授权出现权限问题。现代系统不鼓励以 root 身份运行 GUI 应用。

# HISTORY

gksudo 与 gksu 一同诞生，面向偏好用 sudo 而非 su 提升权限的 Ubuntu 及其他发行版。两者都在大约 **2012 年**被弃用，由 PolicyKit 的 pkexec 机制取代。

# SEE ALSO

[pkexec](/man/pkexec)(1), [sudo](/man/sudo)(8), [gksu](/man/gksu)(1)

# RESOURCES

```[Debian manual page (archived)](https://manpages.debian.org/testing/gksu/gksu.1.en.html)```

<!-- verified: 2026-07-17 -->
