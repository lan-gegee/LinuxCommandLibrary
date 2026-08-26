# TAGLINE

透明地将流量经 Tor 路由

# TLDR

使用 Tor **运行**命令

```torsocks [command]```

在 Shell 中**切换** Tor

```. torsocks [on|off]```

生成启用 Tor 的 **Shell**

```torsocks --shell```

**检查** Tor 是否已启用

```torsocks show```

通过不同链路**隔离**流量

```torsocks -i [curl https://check.torproject.org/api/ip]```

连接到指定的**代理**

```torsocks -a [ip_address] -P [port] [command]```

# SYNOPSIS

**torsocks** [_OPTIONS_] [_COMMAND_ [_ARGS_...]]

# PARAMETERS

**--shell**
> 生成一个新的启用 Tor 的 Shell

**-i, --isolate**
> 通过不同的 Tor 链路隔离流量

**-a, --address** _IP_
> 连接到指定地址的 Tor 代理

**-P, --port** _PORT_
> 连接到指定端口的 Tor 代理

**show**
> 检查当前 Shell 是否已启用 Tor

**on|off**
> 在当前 Shell 中切换 Tor 路由

# DESCRIPTION

**torsocks** 通过拦截网络调用并将其重定向到 Tor 的 SOCKS 代理，使应用程序的网络流量经 Tor 网络路由。默认情况下，它连接运行在 127.0.0.1:9050 的 Tor 守护进程。

该工具使用 LD_PRELOAD 拦截网络系统调用，为原生不支持 SOCKS 代理的应用程序提供透明的 Tor 路由。

# CAVEATS

需要有正在运行的 Tor 守护进程。某些应用程序可能泄露 DNS 或使用与 Tor 不兼容的协议。不支持 UDP 流量。使用原始套接字（raw socket）的应用程序会绕过 torsocks。

# HISTORY

**torsocks** 是作为 **torify** 的改进替代品而开发的，为经 Tor 匿名网络路由流量提供了更好的安全性和功能性。

# INSTALL

```dnf: sudo dnf install torsocks```

```pacman: sudo pacman -S torsocks```

```apk: sudo apk add torsocks```

```brew: brew install torsocks```

```nix: nix profile install nixpkgs#torsocks```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tor](/man/tor)(1), [torify](/man/torify)(1)
