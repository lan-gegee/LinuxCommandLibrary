# TAGLINE

具有合理默认值的快速可配置端口扫描器

# TLDR

**扫描主机的默认端口**

```havn [host]```

**扫描指定端口范围**

```havn -p [1-1024] [host]```

**扫描指定端口**

```havn -p [80,443,8080] [host]```

**以更多重试次数扫描**

```havn -r [3] [host]```

**以自定义超时时间扫描**（毫秒）

```havn -t [2000] [host]```

**扫描所有端口**

```havn -p [1-65535] [host]```

# SYNOPSIS

**havn** [**-p** _ports_] [**-r** _retries_] [**-t** _timeout_] _host_

# PARAMETERS

**-p** _PORTS_
> 要扫描的端口或端口范围（例如 80、1-1024、80,443,8080）

**-r** _RETRIES_
> 每个端口的重试次数

**-t** _TIMEOUT_
> 每个端口的超时时间（毫秒）

**-h**, **--help**
> 打印帮助信息

**-V**, **--version**
> 打印版本号

# DESCRIPTION

**havn** 是一个用 **Rust** 编写的轻量级、自包含的端口扫描应用。它借助异步 **Tokio** 多线程实现快速可靠的扫描结果，二进制体积不足 1MB。它支持 **IPv4** 与 **IPv6** 扫描，可运行于 Linux（含 ARM）、macOS 和 Windows。

havn 自带合理的默认值，适合快速扫描，同时允许自定义端口范围、超时时间和重试次数，以满足更彻底的扫描需求。

# CAVEATS

对你不拥有或未获授权测试的系统进行端口扫描可能是违法行为。防火墙和入侵检测系统可能会拦截或限制扫描尝试。超大端口范围搭配过短的超时时间可能导致漏报。

# HISTORY

**havn** 由 **Jack Wills**（mrjackwills）创建，使用 **Rust** 编写。其名称是丹麦语中的“港口”（harbor 的 port）。它的设计目标是成为比复杂扫描工具更精简、更快速的选择。

# INSTALL

```pacman: sudo pacman -S havn```

```apk: sudo apk add havn```

```brew: brew install havn```

```nix: nix profile install nixpkgs#havn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [ss](/man/ss)(8), [netcat](/man/netcat)(1), [rustscan](/man/rustscan)(1), [masscan](/man/masscan)(1)
