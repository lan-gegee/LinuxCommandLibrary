# TAGLINE

浏览 mDNS/DNS-SD 网络服务

# TLDR

**浏览全部**服务并解析地址

```avahi-browse -a -r```

浏览全部服务，转储后即**终止**（用于脚本）

```avahi-browse -a -t -p```

浏览**特定服务类型**

```avahi-browse _http._tcp```

列出**域**

```avahi-browse -D```

搜索特定**域**

```avahi-browse -a --domain=[example.local]```

浏览并忽略**本地**服务

```avahi-browse -a -r -l```

# SYNOPSIS

**avahi-browse** [_OPTIONS_] [_SERVICE-TYPE_]

# DESCRIPTION

**avahi-browse** 显示本地网络上通过 mDNS/DNS-SD（多播 DNS 服务发现）暴露的服务和主机。它与 Apple 的 Bonjour/Zeroconf 协议兼容。

默认情况下，该工具持续运行，并在服务出现或消失于网络时实时显示，新增条目以 **"+"** 为前缀，被移除的条目以 **"-"** 为前缀。配合 **--resolve** 使用时，还会查询所发现服务的主机名和端口号。**--terminate** 标志使其在转储当前所有已知服务后退出，便于脚本使用。

# PARAMETERS

**-a, --all**
> 显示所有服务

**-r, --resolve**
> 将发现的服务解析为地址和端口

**-l, --ignore-local**
> 忽略本机上的服务

**-t, --terminate**
> 转储列表后终止（不再继续等待）

**-p, --parsable**
> 以便于脚本处理的可解析格式输出

**-D, --browse-domains**
> 浏览域而不是服务

**--domain** _domain_
> 将搜索限制到特定域

**-f, --no-fail**
> 守护进程未运行时不失败；等待其出现

**-k, --no-db-lookup**
> 不在服务类型数据库中查找服务类型

**-b, --dump-db**
> 转储服务类型数据库

**-v, --verbose**
> 启用详细输出

# CAVEATS

需要 Avahi 守护进程正在运行。服务必须通过 mDNS 通告才能被发现。网络配置和防火墙设置可能影响发现效果。

# HISTORY

**avahi-browse** 是 **Avahi** 软件包的一部分，在 Linux 上提供与 Apple Bonjour 兼容的 mDNS/DNS-SD 服务发现功能。

# INSTALL

```apt: sudo apt install avahi-utils```

```dnf: sudo dnf install avahi-tools```

```apk: sudo apk add avahi-tools```

```zypper: sudo zypper install avahi-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[avahi-resolve](/man/avahi-resolve)(1), [avahi-publish](/man/avahi-publish)(1), [avahi-daemon](/man/avahi-daemon)(8)
