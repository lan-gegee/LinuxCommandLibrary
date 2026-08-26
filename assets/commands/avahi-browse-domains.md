# TAGLINE

发现网络上的 mDNS 浏览域

# TLDR

在本地网络上**浏览**浏览域

```avahi-browse-domains```

以详细输出**浏览**

```avahi-browse-domains --verbose```

输出完整列表后即**终止**

```avahi-browse-domains --terminate```

在特定域中**浏览**

```avahi-browse-domains --domain=[domain_name]```

供脚本使用的**可解析输出**（分号分隔）

```avahi-browse-domains --parsable```

**忽略本地**服务，只显示远程服务

```avahi-browse-domains --ignore-local```

# SYNOPSIS

**avahi-browse-domains** [_options_]

# PARAMETERS

**-d, --domain=**_DOMAIN_
> 指定搜索域（默认为 local）

**-v, --verbose**
> 启用包含详细信息的详细输出

**-t, --terminate**
> 显示完整的域列表后退出

**-c, --cache**
> 输出所有缓存条目后退出

**-l, --ignore-local**
> 只显示远程服务，排除本地服务

**-r, --resolve**
> 自动解析发现的服务

**-a, --all**
> 浏览局域网上注册的所有服务类型，而不只是指定的那一种

**-f, --no-fail**
> 守护进程不可用时等待；断开时重连

**-p, --parsable**
> 以便于脚本处理的格式输出（字段以分号分隔，服务名转义）

**-k, --no-db-lookup**
> 跳过服务类型数据库查询

**-h, --help**
> 显示帮助信息

**-V, --version**
> 显示版本详情

# DESCRIPTION

**avahi-browse-domains** 通过 Avahi 守护进程浏览本地网络上的 mDNS/DNS-SD 浏览域。此命令等同于 **avahi-browse --browse-domains**，为发现可用的浏览域提供了便捷入口。

该工具连接到 Avahi 守护进程并显示网络中出现的浏览域。新出现的网络条目带 **"+"** 前缀，消失的条目用 **"-"** 表示，启用 resolve 标志时已解析的条目显示为 **"="**。

默认情况下，**avahi-browse-domains** 在 **local** 域中搜索，但可通过 **--domain** 选项配置为在其他域中搜索。使用 **--parsable** 选项可将输出格式化为易于脚本解析的形式，各字段以分号分隔。

该工具默认持续运行并监控域的变化。使用 **--terminate** 可在显示初始完整列表后退出，或使用 **--cache** 仅转储缓存的条目并立即退出。

# CAVEATS

需要 **avahi-daemon** 正在运行。如果守护进程不可用，除非指定 **--no-fail**（使命令等待守护进程变为可用），否则命令会失败。

# HISTORY

属于 **Avahi** 工具套件，该项目是对 Apple 的 Bonjour/Zeroconf 协议的自由软件实现。Avahi 无需配置即可在本地网络上实现服务发现，其 mDNS 和 DNS-SD 协议由 **IETF** 标准化。

# INSTALL

```apt: sudo apt install avahi-utils```

```dnf: sudo dnf install avahi-tools```

```apk: sudo apk add avahi-tools```

```zypper: sudo zypper install avahi-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[avahi-browse](/man/avahi-browse)(1), [avahi-publish](/man/avahi-publish)(1), [avahi-resolve](/man/avahi-resolve)(1), [avahi-daemon](/man/avahi-daemon)(8)

# RESOURCES

```[Homepage](https://avahi.org/)```

```[Source code](https://github.com/avahi/avahi)```

<!-- verified: 2026-06-17 -->
