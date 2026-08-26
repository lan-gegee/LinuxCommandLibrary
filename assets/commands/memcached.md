# TAGLINE

高性能分布式内存缓存系统

# TLDR

**启动 memcached**

```memcached```

**以指定内存启动**

```memcached -m [256]```

**监听指定端口**

```memcached -p [11211]```

**以守护进程方式运行**

```memcached -d -u [memcache]```

**详细输出**

```memcached -vv```

**限制连接数**

```memcached -c [1024]```

# SYNOPSIS

**memcached** [_options_]

# PARAMETERS

**-p** _port_
> TCP 端口（默认 11211）。

**-m** _MB_
> 内存上限（MB）。

**-c** _connections_
> 最大并发连接数。

**-d**
> 以守护进程方式运行。

**-u** _user_
> 以指定用户身份运行。

**-l** _ip_
> 监听地址。

**-v**, **-vv**
> 详细输出。

**-t** _threads_
> 线程数。

# DESCRIPTION

**memcached** 是一个高性能的分布式内存缓存系统。它将键值对存储在 RAM 中，以减轻数据库负载并加速动态 Web 应用。

memcached 使用简单的协议，被广泛用于缓存数据库查询、API 响应和会话数据。

# PROTOCOL COMMANDS

```
set key 0 3600 5\r\nvalue\r\n  # Store
get key\r\n                     # Retrieve
delete key\r\n                  # Remove
incr key 1\r\n                  # Increment
stats\r\n                       # Statistics
```

# CAVEATS

无持久化（仅存于 RAM）。默认无认证。写满时按 LRU 淘汰。不适合大值（上限 1MB）。

# HISTORY

memcached 由 **Brad Fitzpatrick** 于 **2003 年**在 **LiveJournal** 开发，用于降低数据库负载。此后成为 Web 规模化的基础设施之一。

# INSTALL

```apt: sudo apt install memcached```

```dnf: sudo dnf install memcached```

```pacman: sudo pacman -S memcached```

```apk: sudo apk add memcached```

```zypper: sudo zypper install memcached```

```brew: brew install memcached```

```nix: nix profile install nixpkgs#memcached```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[redis-cli](/man/redis-cli)(1)
