# TAGLINE

浏览本地网络中的 VNC 服务器

# TLDR

**浏览本地网络中的 VNC 服务器**

```bvnc```

**在特定域中浏览**

```bvnc --domain [.local]```

**强制只浏览 VNC 服务器**

```bvnc --vnc```

**同时浏览 SSH 和 VNC 服务器**

```bvnc --shell```

# SYNOPSIS

**bvnc** [_options_]

# DESCRIPTION

**bvnc** 是一个 Avahi 服务浏览器，使用 mDNS/DNS-SD（Zeroconf）发现本地网络中的 VNC 服务器。它以 GUI 显示找到的服务器，选中某个服务器时会启动 vncviewer。

该工具是用于服务发现的 Avahi Zeroconf 套件的一部分。

# PARAMETERS

**-v, --vnc**
> 只浏览 VNC 服务器

**-s, --ssh**
> 只浏览 SSH 服务器

**-S, --shell**
> 同时浏览 SSH 和 VNC 服务器

**-d, --domain** _domain_
> 在指定域中浏览（默认：.local）

**-h, --help**
> 显示帮助

# RELATED BINARIES

**bvnc**
> 浏览 VNC 服务器（默认行为）

**bssh**
> 浏览 SSH 服务器

**bshell**
> 同时浏览 VNC 和 SSH 服务器

# REQUIREMENTS

需要 Avahi 守护进程正在运行，并依赖 gtk3、python-dbus 和 python-gobject。UDP 端口 5353 必须开放以支持 mDNS。

# PUBLISHING VNC SERVICE

要通告你的 VNC 服务器，请在 /etc/avahi/services/ 中创建一个服务文件，指定服务类型 **_rfb._tcp** 和你的 VNC 端口号。

# CAVEATS

只能发现本地网络上通过 mDNS 通告的服务。需要 GUI 环境和已安装的 vncviewer。

# INSTALL

```apt: sudo apt install avahi-ui-utils```

```dnf: sudo dnf install avahi-ui-tools```

```apk: sudo apk add avahi-ui-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[avahi-browse](/man/avahi-browse)(1), [bssh](/man/bssh)(1), [vncviewer](/man/vncviewer)(1), [avahi-daemon](/man/avahi-daemon)(8)

# RESOURCES

```[Source code](https://github.com/avahi/avahi)```

```[Homepage](https://www.avahi.org)```

<!-- verified: 2026-06-22 -->
