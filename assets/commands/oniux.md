# TAGLINE

Tor Project 出品的实验性工具，用于隔离任意应用程序

# TLDR

**隔离**应用并让流量经由 Tor 路由

```oniux [command]```

**通过 Tor 查询**网站

```oniux curl [https://example.com]```

查询 **onion 站点**

```oniux curl [http://example.onion]```

在 tor 化隔离环境中运行整个 **shell**

```oniux bash```

隔离**图形应用程序**

```oniux hexchat```

# SYNOPSIS

**oniux** [_options_] _command_ [_args_...]

# DESCRIPTION

**oniux** 是 Tor Project 的一个实验性工具，用于隔离任意应用程序并将其网络流量路由到 Tor 网络。它利用 Linux 命名空间创建网络隔离，确保应用程序无法把流量泄漏到 Tor 之外。

与传统的 tor 化方法（如 torsocks）不同，oniux 通过将应用程序放入一个只允许 Tor 流量的独立网络命名空间来提供更强的隔离。这使它适合那些原本可能绕过 SOCKS 代理设置的应用程序。

该工具既能访问普通网站，也能访问 .onion 隐藏服务，因此对注重隐私的工作流和访问仅限 Tor 的资源很有用。

# CAVEATS

这是 Tor Project 的**实验性软件**，可能存在缺陷或安全问题。网络命名空间隔离需要相应的 Linux 内核支持和权限。某些被隔离的应用程序可能无法正常运行，尤其是那些依赖特定网络配置或本地服务访问的应用程序。它不会匿名化应用层的数据泄漏（主机名、用户名等）。

# HISTORY

由 **Tor Project** 开发，是其改进 Linux 上应用级 Tor 集成的努力的一部分。它使用 Linux 命名空间技术（类似容器），比 torsocks 等基于 LD_PRELOAD 的传统 tor 化方案提供更强的隔离保障。

# INSTALL

```nix: nix profile install nixpkgs#oniux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tor](/man/tor)(1), [torsocks](/man/torsocks)(1), [torify](/man/torify)(1)
