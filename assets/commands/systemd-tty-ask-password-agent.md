# TAGLINE

处理启动时的密码请求

# TLDR

**列出**待处理的密码请求

```systemd-tty-ask-password-agent --list```

持续**监视**并处理请求

```systemd-tty-ask-password-agent --watch```

就待处理的密码**询问**用户

```systemd-tty-ask-password-agent --query```

转发为 **wall** 消息

```systemd-tty-ask-password-agent --wall```

# SYNOPSIS

**systemd-tty-ask-password-agent** [_OPTIONS_]

# PARAMETERS

**--list**
> 列出待处理的密码请求

**--watch**
> 持续处理密码请求

**--query**
> 通过在当前 TTY 上询问用户来处理待处理的请求

**--wall**
> 将请求作为 wall 消息转发

**--console**
> 在控制台而非当前 TTY 上询问

# DESCRIPTION

**systemd-tty-ask-password-agent** 处理来自 systemd 服务的密码请求。在启动期间，磁盘加密等服务可能需要密码；该代理负责收集并转发这些密码。

代理会监视密码请求文件，并在合适的终端上向用户显示提示。

# CAVEATS

主要用于启动期间的磁盘加密密码输入。可以同时运行多个代理。--wall 选项会向所有终端广播。

# HISTORY

**systemd-tty-ask-password-agent** 提供 systemd 密码查询基础架构中面向用户的组件，使得在没有完整登录环境的情况下也能在早期启动阶段提示输入密码。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-ask-password](/man/systemd-ask-password)(1), [cryptsetup](/man/cryptsetup)(8)
