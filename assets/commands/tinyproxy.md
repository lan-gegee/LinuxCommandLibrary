# TAGLINE

轻量级 HTTP 与 HTTPS 代理守护进程

# TLDR

以默认配置**启动 tinyproxy**

```tinyproxy```

**使用自定义配置文件启动**

```tinyproxy -c [path/to/tinyproxy.conf]```

**前台运行**（不守护进程化）

```tinyproxy -d```

前台运行并加载自定义配置，用于调试

```tinyproxy -d -c [path/to/tinyproxy.conf]```

**显示版本信息**

```tinyproxy -v```

**显示帮助**

```tinyproxy -h```

# SYNOPSIS

**tinyproxy** [**-c** _config-file_] [**-d**] [**-h**] [**-l**] [**-v**]

# PARAMETERS

**-c** _config-file_
> 使用替代配置文件，而不是默认的 /etc/tinyproxy/tinyproxy.conf。

**-d**
> 不守护进程化，保持在前台运行，便于调试。

**-h**
> 显示简短的帮助界面后退出。

**-l**
> 显示许可协议后退出。

**-v**
> 显示版本信息后退出。

# DESCRIPTION

**Tinyproxy** 是一款轻量级 HTTP/HTTPS 代理守护进程，设计目标是极低的资源消耗。它在可配置的 TCP 端口上监听并处理 HTTP 代理请求，非常适合嵌入式系统、容器，或者完整功能代理显得过于消耗资源的场景。

该守护进程支持基本的 HTTP 代理、通过 CONNECT 方法的 HTTPS、上游代理配置、访问控制列表以及基于 URL 的过滤。它还可以充当反向代理，将请求转发给后端服务器。

配置通过配置文件完成（通常是 /etc/tinyproxy/tinyproxy.conf），其中指定监听端口、允许的客户端、日志设置和过滤规则。Tinyproxy 内置统计页面，通过请求 stathost（默认：tinyproxy.stats）即可访问。

信号可以控制运行中的守护进程：SIGHUP 触发连接的垃圾回收，标准信号用于优雅关机。

# CONFIGURATION

**/etc/tinyproxy/tinyproxy.conf**
> 主配置文件，指定监听端口、允许的客户端、日志设置、上游代理、过滤规则和访问控制列表。

**-c** _file_
> 运行时使用替代配置文件。

# CAVEATS

Tinyproxy 不支持缓存、basic 以外的身份验证方式以及 SOCKS 代理。对于高流量的生产环境，请考虑 Squid 等功能更全面的代理。默认配置可能允许来自任意主机的连接，因此应合理配置访问控制。

# HISTORY

**Tinyproxy** 由 **Steven Young** 于 **1999 年**编写，作为重量级代理服务器的轻量替代品。该项目由多位贡献者维护，目前在 GitHub 上持续开发。凭借小巧的占用和简洁性，它在嵌入式 Linux 系统、Docker 容器和注重隐私的环境中广受欢迎。

# INSTALL

```apt: sudo apt install tinyproxy-bin```

```dnf: sudo dnf install tinyproxy```

```pacman: sudo pacman -S tinyproxy```

```apk: sudo apk add tinyproxy```

```zypper: sudo zypper install tinyproxy```

```brew: brew install tinyproxy```

```nix: nix profile install nixpkgs#tinyproxy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[squid](/man/squid)(8), [privoxy](/man/privoxy)(1), [nginx](/man/nginx)(8), [curl](/man/curl)(1), [wget](/man/wget)(1)
