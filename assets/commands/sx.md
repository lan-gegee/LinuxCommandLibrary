# TAGLINE

xinit 和 startx 的简单替代品

# TLDR

**启动一个 X 会话**，运行 _$XDG_CONFIG_HOME/sx/sxrc_ 中的命令

```sx```

**启动一个 X 会话**，直接运行指定的窗口管理器

```sx [dwm]```

**启动一个 X 会话**，使用显式命令行

```sx [exec] [i3]```

启动服务器后**运行**一个一次性的 X 程序

```sx [xterm]```

# SYNOPSIS

**sx** [_command_ [_args_...]]

# DESCRIPTION

**sx** 是一个小型 POSIX shell 脚本：它启动 **Xorg** 服务器，设置授权 cookie，然后以用户提供的命令（或 _sxrc_）作为 X 会话运行。它的定位是 **xinit** 和 **startx** 的极简、透明替代品，暴露相同的基本机制，但去掉两者众多可选行为。

X 服务器在调用 **sx** 的同一 TTY 上启动，显示编号由 TTY 编号推导而来（因此 VT1 变成 _:1_）。服务器以 **-keeptty -noreset** 启动之前，会先从 _/dev/urandom_ 生成新的 MIT-MAGIC-COOKIE-1 并注册到 **xauth**。

如果不带参数，**sx** 运行 _$XDG_CONFIG_HOME/sx/sxrc_ 处的可执行文件（默认为 _~/.config/sx/sxrc_）。否则，所给的命令及其参数成为会话主导进程：当它退出时，**sx** 关闭服务器。

# CONFIGURATION

**$XDG_CONFIG_HOME/sx/sxrc**
> 不带参数调用 **sx** 时作为 X 会话运行的可执行脚本。必须具有可执行位。典型的 _sxrc_ 以窗口管理器作为最后一条（前台）命令启动，例如：

```
#!/bin/sh
xrdb -merge ~/.Xresources &
xsetroot -cursor_name left_ptr &
exec dwm
```

**$XAUTHORITY**
> X 授权文件的路径。**sx** 在 _$XDG_DATA_HOME/sx/_ 下生成此文件，并为子进程导出该变量。

# PARAMETERS

**sx** 自身不解析任何标志。所有参数都被视为会话命令及其参数。如果命令开头可能被误认为选项，请在命令前使用 **--**。

# CAVEATS

Xorg 命令行是**硬编码的**：服务器标志无法通过 **sx** 本身自定义。只配置了 **Unix 域**套接字；未启用 TCP 监听。显示编号与 TTY 编号绑定，因此在 _tty1_ 上启动 **sx** 总是产生 _:1_，这与 **startx** 不同（其默认为 _:0_）。**sx** 需要 **Xorg**、**xauth** 和可读的 _/dev/urandom_；错误检查刻意保持最少，大部分报错交给底层工具。

# HISTORY

**sx** 由 **Earnest Wieczorek**（Earnestly）编写，是对 **xinit(1)** 中敦促"站点管理员"编写更好封装脚本这一评论的概念验证。它于 **2015 年**前后首次发布在 GitHub 上，始终保持为一个微型 shell 脚本（约 70 行），并被多个发行版打包，其中最著名的是 **Arch Linux**，作为不使用 **startx** 启动 X 会话的轻量方式。

# INSTALL

```apt: sudo apt install lrzsz```

```dnf: sudo dnf install lrzsz```

```pacman: sudo pacman -S lrzsz```

```apk: sudo apk add sx```

```brew: brew install lrzsz```

```nix: nix profile install nixpkgs#lrzsz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xinit](/man/xinit)(1), [startx](/man/startx)(1), [Xorg](/man/Xorg)(1), [xauth](/man/xauth)(1)
