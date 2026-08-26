# TAGLINE

带 GTK 密码对话框的 su 图形前端

# TLDR

以**特定用户**身份运行命令

```gksu -u [userid] [command]```

在**保留**当前环境的同时运行命令

```gksu -u [userid] -k [command]```

强制 gksu 使用 **su** 运行命令

```gksu -u [userid] -w [command]```

强制 gksu 使用 **sudo** 运行命令

```gksu -u [userid] -S [command]```

为给定命令输出**调试**信息

```gksu -u [userid] -d [command]```

让 gksu 将密码**打印到 stdout**

```gksu -p [command]```

# SYNOPSIS

**gksu** [_options_] _command_

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
> 强制使用 sudo 进行认证

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

**gksu** 是 `su` 的图形前端，通过 GTK 对话框提示输入密码。它允许从命令行或菜单项以提升的权限运行图形应用程序，而无需终端。

该工具可以以 su 模式（认证为目标用户，通常是 root）或 sudo 模式（使用当前用户的 sudo 权限）运行，并根据系统配置自动检测。

> **已弃用**：gksu 不再维护且存在安全问题。请改用 PolicyKit 的 **pkexec** 进行图形化权限提升。

# CAVEATS

已弃用且无人维护。以 root 身份运行图形应用程序可能导致用户文件（.Xauthority、配置文件）出现权限问题。现代桌面环境完全不鼓励以 root 身份运行 GUI 应用。

# HISTORY

gksu 创建于 2000 年代初期，为 GNOME 提供特权操作的图形密码提示。它在大约 **2012 年**被弃用，由提供更细粒度授权控制的 PolicyKit（pkexec）取代。

# INSTALL

```aur: yay -S gksu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pkexec](/man/pkexec)(1), [sudo](/man/sudo)(8), [su](/man/su)(1), [gksudo](/man/gksudo)(1)

# RESOURCES

```[Debian manual page (archived)](https://manpages.debian.org/testing/gksu/gksu.1.en.html)```

<!-- verified: 2026-07-17 -->
