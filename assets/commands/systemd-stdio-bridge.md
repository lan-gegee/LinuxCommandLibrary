# TAGLINE

将 stdio 桥接到 D-Bus 连接

# TLDR

转发到**系统**总线

```systemd-stdio-bridge```

转发到**用户**总线

```systemd-stdio-bridge --user```

转发到**容器**总线

```systemd-stdio-bridge -M [container]```

转发到**自定义**总线地址

```systemd-stdio-bridge -p unix:path=[/path/to/socket]```

# SYNOPSIS

**systemd-stdio-bridge** [_OPTIONS_]

# PARAMETERS

**--user**
> 连接到用户 D-Bus 会话

**--system**
> 连接到系统 D-Bus（默认）

**-M, --machine=** _CONTAINER_
> 连接到指定容器中的 D-Bus

**-p, --bus-path=** _ADDRESS_
> 连接到自定义 D-Bus 地址

# DESCRIPTION

**systemd-stdio-bridge** 在 stdin/stdout 与一条 D-Bus 连接之间实现代理。它期待一个通过 stdin/stdout 打开的连接，并创建一个到指定总线的新连接。

这使得通过 SSH 或类似的传输机制远程访问 D-Bus 成为可能，将外部连接桥接到本地总线。

# CAVEATS

要求 stdin 上是格式正确的 D-Bus 连接。主要用于远程访问 D-Bus 的场景。需要对目标总线拥有相应的权限。

# HISTORY

**systemd-stdio-bridge** 支持远程 D-Bus 访问模式，让 `busctl` 和 `systemctl` 等工具可以通过 SSH 操作远程系统。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[busctl](/man/busctl)(1), [dbus-daemon](/man/dbus-daemon)(1)
