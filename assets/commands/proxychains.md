# TAGLINE

通过代理服务器转发 TCP 连接

# TLDR

**通过代理运行命令**

```proxychains [command]```

**通过代理运行 curl**

```proxychains curl [url]```

**使用指定的配置**文件

```proxychains -f [path/to/config.conf] [command]```

**静默模式**（不显示代理信息输出）

```proxychains -q [command]```

**通过代理进行 SSH 连接**

```proxychains ssh [user]@[host]```

**将 proxychains 与浏览器结合使用**

```proxychains firefox```

# SYNOPSIS

**proxychains** [**-q**] [**-f** _config_file_] _program_ [_args_]

# PARAMETERS

**-q**
> 静默模式。不显示代理连接信息。

**-f** _config_file_
> 使用指定的配置文件代替默认配置。不带此标志时，proxychains 按以下顺序搜索：**PROXYCHAINS_CONF_FILE** 环境变量中的路径、**./proxychains.conf**、**~/.proxychains/proxychains.conf**，以及 **/etc/proxychains.conf**。

# DESCRIPTION

**proxychains** 强制指定应用建立的 TCP 连接经由 SOCKS4、SOCKS5 或 HTTP 等代理服务器转发。它利用 **LD_PRELOAD** 钩取与网络相关的 libc 函数，在不修改目标应用的情况下透明地重定向流量。

适用于匿名化、通过 Tor 路由流量以及绕过网络限制。支持的认证类型包括 SOCKS4/5 的用户名/密码认证和 HTTP 的基本认证。

目前维护的现代化版本是 **rofl0r** 编写的 **proxychains-ng**（proxychains4），是原项目的延续。

# CONFIGURATION

```
# /etc/proxychains.conf
strict_chain
proxy_dns

[ProxyList]
socks5 127.0.0.1 9050
http   192.168.1.1 8080
```

# CHAIN TYPES

```
strict_chain  - All proxies in order, fail if any is down
dynamic_chain - Skip dead proxies, at least one must respond
random_chain  - Random proxy order each connection
round_robin   - Cycle through proxies in order
```

# CAVEATS

仅支持 TCP 连接。UDP 和 ICMP 流量不经代理转发。静态链接的程序会绕过 LD_PRELOAD 钩子。在配置文件中启用 **proxy_dns** 可以代理 DNS 请求。

# HISTORY

proxychains 最初由 **haad** 编写，后来由 **rofl0r** 分叉为 **proxychains-ng**（proxychains4），在稳定性和功能上均有改进。

# INSTALL

```dnf: sudo dnf install proxychains-ng```

```pacman: sudo pacman -S proxychains-ng```

```apk: sudo apk add proxychains-ng```

```zypper: sudo zypper install proxychains-ng```

```brew: brew install proxychains-ng```

```nix: nix profile install nixpkgs#proxychains-ng```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tor](/man/tor)(1), [torsocks](/man/torsocks)(1), [socat](/man/socat)(1), [ssh](/man/ssh)(1), [curl](/man/curl)(1)
