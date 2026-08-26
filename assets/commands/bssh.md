# TAGLINE

在本地网络中浏览查找 SSH 和 VNC 服务器

# TLDR

**在本地网络中浏览查找 SSH 服务器**

```bssh```

**在指定域中浏览**

```bssh --domain [.local]```

**强制仅浏览 SSH 服务器**

```bssh --ssh```

**同时浏览 SSH 和 VNC 服务器**

```bssh --shell```

# SYNOPSIS

**bssh** [_options_]

# DESCRIPTION

**bssh** 是一个 Avahi 服务浏览器，使用 mDNS/DNS-SD（Zeroconf）在本地网络中发现 SSH 服务器。它以图形界面显示找到的服务器，并在选中某个服务器时启动 ssh。

该工具是用于服务发现的 Avahi Zeroconf 套件的一部分。

# PARAMETERS

**-s, --ssh**
> 仅浏览 SSH 服务器

**-v, --vnc**
> 仅浏览 VNC 服务器

**-S, --shell**
> 同时浏览 SSH 和 VNC 服务器

**-d, --domain** _domain_
> 在指定域中浏览（默认：.local）

**-h, --help**
> 显示帮助

**-V, --version**
> 显示版本

# RELATED BINARIES

**bssh**
> 浏览 SSH 服务器（默认行为）

**bvnc**
> 浏览 VNC 服务器

**bshell**
> 同时浏览 SSH 和 VNC 服务器

# REQUIREMENTS

需要 Avahi 守护进程正在运行，以及 gtk3、python-dbus、python-gobject 依赖。UDP 端口 5353 必须开放以供 mDNS 使用。

# PUBLISHING SSH SERVICE

要发布你的 SSH 服务器：

```cp /usr/share/doc/avahi/ssh.service /etc/avahi/services/```

# CAVEATS

只能发现在本地网络中通过 mDNS 发布的服务。需要图形界面环境。"B" 代表 "Browse"，而非 Bluetooth。

# INSTALL

```apt: sudo apt install avahi-ui-utils```

```dnf: sudo dnf install avahi-ui-tools```

```apk: sudo apk add avahi-ui-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[avahi-browse](/man/avahi-browse)(1), [avahi-daemon](/man/avahi-daemon)(8), [ssh](/man/ssh)(1), [bvnc](/man/bvnc)(1)

# RESOURCES

```[Source code](https://github.com/avahi/avahi)```

```[Homepage](https://www.avahi.org/)```

<!-- verified: 2026-06-22 -->
