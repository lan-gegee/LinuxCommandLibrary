# TAGLINE

增强隐私的过滤型 Web 代理

# TLDR

**启动 privoxy**

```privoxy [/etc/privoxy/config]```

**在前台启动**

```privoxy --no-daemon [config]```

**检查配置**

```privoxy --config-test [config]```

**显示版本**

```privoxy --version```

# SYNOPSIS

**privoxy** [_options_] _config-file_

# DESCRIPTION

**privoxy** 是一个不带缓存、具备过滤能力的 Web 代理。它可以拦截广告、移除跟踪器、修改网页内容并增强隐私。

该工具工作在浏览器与互联网之间，根据可配置的规则检查和修改 HTTP 流量。

# PARAMETERS

**--no-daemon**
> 在前台运行。

**--pidfile** _file_
> PID 文件位置。

**--user** _user_
> 以指定用户身份运行。

**--chroot**
> Chroot 到主目录。

**--pre-chroot-nslookup** _host_
> 在 chroot 之前进行 DNS 查询。

**--config-test**
> 测试配置。

**--version**
> 显示版本。

**--help**
> 显示帮助。

# CONFIGURATION

**listen-address**: 代理监听地址
**forward**: 上游代理
**actionsfile**: 动作定义
**filterfile**: 内容过滤器
**logfile**: 日志文件路径

# CAVEATS

HTTPS 过滤需要配置浏览器。复杂规则需要调优。可能导致某些网站无法正常访问。过滤会带来性能开销。

# HISTORY

**Privoxy** 于 **2001 年**从 **Internet Junkbuster** 演化而来，是一个以隐私为核心的 Web 代理。它由志愿者团队开发，至今仍是最灵活的内容过滤代理之一。

# INSTALL

```apt: sudo apt install privoxy```

```dnf: sudo dnf install privoxy```

```pacman: sudo pacman -S privoxy```

```apk: sudo apk add privoxy```

```zypper: sudo zypper install privoxy```

```brew: brew install privoxy```

```nix: nix profile install nixpkgs#privoxy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[squid](/man/squid)(8), [tinyproxy](/man/tinyproxy)(1), [tor](/man/tor)(1), [dnsmasq](/man/dnsmasq)(1)
