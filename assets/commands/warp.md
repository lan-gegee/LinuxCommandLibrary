# TAGLINE

安全而简单的终端共享

# TLDR

**共享你的终端**

```warp open [session-name]```

**连接到已共享的终端**

```warp connect [session-name]```

**授予已连接用户写权限**

```warp authorize [username]```

# SYNOPSIS

**warp** _command_ [_options_]

# DESCRIPTION

**warp** 用一条简单的命令实现安全的终端共享。一个用户打开会话，其他人即可连接并实时查看该终端。连接经 TLS 加密，默认只读，写权限需要显式授权。无需 SSH 或共享服务器。

# HISTORY

**warp** 由 **spolu** 创建，使用 **Go** 编写。

# INSTALL

```apt: sudo apt install libghc-wai-app-static-dev```

```pacman: sudo pacman -S warp```

```apk: sudo apk add warp```

```zypper: sudo zypper install warp```

```nix: nix profile install nixpkgs#warp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [screen](/man/screen)(1)
