# TAGLINE

更改在网络中通告的 mDNS 主机名

# TLDR

**设置 mDNS 主机名**

```avahi-set-host-name [newhost]```

**以详细输出模式设置主机名**

```avahi-set-host-name -v [newhost]```

# SYNOPSIS

**avahi-set-host-name** _hostname_

# DESCRIPTION

**avahi-set-host-name** 更改 Avahi 守护进程通告的 mDNS 主机名。这使你无需修改系统主机名文件即可改变系统在本地网络中的显示方式。

更改会立即生效，并影响本地网络上的服务发现。

# PARAMETERS

_hostname_
> 要通告的新 mDNS 主机名。将以 _hostname_.local 的形式发布到网络上。

**-v**, **--verbose**
> 启用详细输出模式。

**-V**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助。

# CAVEATS

需要 avahi-daemon 正在运行。此操作通常需要特权。不会更改系统主机名（如需更改请使用 **hostname** 或 **hostnamectl**）。更改在守护进程重启后不会保留。主机名必须是有效的 DNS 名称。

# HISTORY

**avahi-set-host-name** 是 Avahi 套件的一部分，Avahi 是由 Lennart Poettering 在 **2005** 年前后发起的免费 Zeroconf/Bonjour 实现。

# INSTALL

```apt: sudo apt install avahi-utils```

```dnf: sudo dnf install avahi-tools```

```apk: sudo apk add avahi-tools```

```zypper: sudo zypper install avahi-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[avahi-daemon](/man/avahi-daemon)(8), [avahi-resolve](/man/avahi-resolve)(1), [hostname](/man/hostname)(1), [hostnamectl](/man/hostnamectl)(1)
