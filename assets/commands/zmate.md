# TAGLINE

基于 Zellij 会话的即时终端共享

# TLDR

**开始共享当前 Zellij 会话**

```zmate```

**在自定义端口上共享**

```zmate -p [3333]```

# SYNOPSIS

**zmate** [_options_]

# DESCRIPTION

**zmate** 让你能在不受信任的网络或 NAT 网关之后，即时与他人共享 Zellij 终端会话。它借助一台公共 SSH 服务器建立 SSH 远程端口转发隧道。灵感来自 tmate，但面向 Zellij 而非 tmux 设计。

# HISTORY

**zmate** 由 **ziinaio** 创建，使用 **Go** 编写。

# INSTALL

```nix: nix profile install nixpkgs#zmate```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zellij](/man/zellij)(1), [tmux](/man/tmux)(1)
