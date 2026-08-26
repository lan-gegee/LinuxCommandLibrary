# TAGLINE

让应用流量经 Tor 路由

# TLDR

经 Tor **路由**流量

```torify [command]```

在 Shell 中**切换** Tor

```torify [on|off]```

生成启用 Tor 的 **Shell**

```torify --shell```

**检查** Tor 是否已启用

```torify show```

使用**配置**文件

```torify -c [config-file] [command]```

使用指定的**代理**

```torify -P [proxy] [command]```

# SYNOPSIS

**torify** [_OPTIONS_] [_COMMAND_ [_ARGS_...]]

# PARAMETERS

**--shell**
> 生成一个新的启用 Tor 的 Shell

**on|off**
> 在当前 Shell 中切换 Tor 路由

**show**
> 检查当前 Shell 是否已启用 Tor

**-c** _FILE_
> 使用指定的 Tor 配置文件

**-P** _PROXY_
> 使用指定的 SOCKS 代理

# DESCRIPTION

**torify** 让应用程序的网络流量经 Tor 匿名网络路由。它通过包装命令，将其网络连接重定向到 Tor 的 SOCKS 代理。

注意：该命令已被弃用，现在是向后兼容 torsocks 的包装器。新脚本应直接使用 torsocks。

# CAVEATS

已弃用，建议改用 torsocks。需要有正在运行的 Tor 守护进程。某些应用程序可能出现 DNS 泄露。并非所有协议都能通过 Tor 工作。

# HISTORY

**torify** 是最早将应用流量经 Tor 路由的工具。它已被功能更完善、更安全的 **torsocks** 取代。

# INSTALL

```apt: sudo apt install tor```

```dnf: sudo dnf install tor```

```pacman: sudo pacman -S tor```

```apk: sudo apk add tor```

```zypper: sudo zypper install tor```

```brew: brew install tor```

```nix: nix profile install nixpkgs#tor```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[torsocks](/man/torsocks)(1), [tor](/man/tor)(1)
