# TAGLINE

基于 mDNS 的单播 DNS 服务器配置守护进程

# TLDR

**启动 DNS 配置守护进程**

```avahi-dnsconfd```

**作为后台守护进程启动**

```avahi-dnsconfd --daemonize```

**以 syslog 记录日志**启动

```avahi-dnsconfd --syslog```

**终止正在运行的实例**

```avahi-dnsconfd --kill```

**刷新 DNS 服务器数据**（发送 SIGHUP）

```killall -HUP avahi-dnsconfd```

# SYNOPSIS

**avahi-dnsconfd** [_options_]

# PARAMETERS

**-D**, **--daemonize**
> 作为后台守护进程运行并记录到 syslog

**-s**, **--syslog**
> 记录到 syslog 而非 stderr

**-k**, **--kill**
> 终止已在运行的 avahi-dnsconfd 实例

**--refresh**
> 刷新 DNS 服务器信息

**--check**
> 检查守护进程是否正在运行

**-h**, **--help**
> 显示帮助消息

**-v**, **--version**
> 显示版本信息

# DESCRIPTION

**avahi-dnsconfd** 是一个根据本地网络上的 mDNS/DNS-SD 通告来配置单播 DNS 服务器的守护进程。它连接到正在运行的 **avahi-daemon**，并监控 DNS 服务器的通告。

当网络上有单播 DNS 服务器被通告或被移除时，avahi-dnsconfd 会执行动作脚本 **/etc/avahi/avahi-dnsconfd.action** 来更新系统的 DNS 配置。这相当于用 mDNS 实现了类似 DHCP 的 DNS 服务器发现。

该守护进程要求 avahi-daemon 先行运行。它适用于通过 Zeroconf/Bonjour 协议动态通告 DNS 服务器、而非通过传统 DHCP 配置的环境。

# SIGNALS

**SIGINT**, **SIGTERM**
> 关闭守护进程

**SIGHUP**
> 刷新 DNS 服务器数据

# CONFIGURATION

**/etc/avahi/avahi-dnsconfd.action**
> 在网络上发现或移除 DNS 服务器时执行的 Shell 脚本。以动作类型和 DNS 服务器地址作为参数。

# CAVEATS

需要先运行 avahi-daemon。必须正确配置动作脚本才能更新 DNS 解析器设置。若未妥善集成，可能与 NetworkManager 或 systemd-resolved 等其他 DNS 管理工具冲突。

# HISTORY

**Avahi** 由 **Lennart Poettering** 和 **Trent Lloyd** 自 **2005 年**起创建，是 Linux 上 Zeroconf/mDNS/DNS-SD 的自由实现。avahi-dnsconfd 组件的设计目标是将零配置的 DNS 服务器发现与传统的单播 DNS 解析集成起来，让网络无需手动配置 DNS 即可运作。

# INSTALL

```apt: sudo apt install avahi-dnsconfd```

```dnf: sudo dnf install avahi-dnsconfd```

```pacman: sudo pacman -S avahi```

```apk: sudo apk add avahi```

```zypper: sudo zypper install avahi```

```brew: brew install avahi```

```nix: nix profile install nixpkgs#avahi```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[avahi-daemon](/man/avahi-daemon)(8), [avahi-browse](/man/avahi-browse)(1)
