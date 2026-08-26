# TAGLINE

自动获取 IPv4 链路本地地址

# TLDR

在接口上**启动**守护进程以自动配置 IPv4LL 地址

```avahi-autoipd [interface]```

启动后在**后台运行**（守护进程化）

```avahi-autoipd -D [interface]```

**终止**接口上正在运行的守护进程

```avahi-autoipd --kill [interface]```

**刷新**并重新通告已获取的 IP 地址

```avahi-autoipd --refresh [interface]```

**检查**守护进程是否在接口上运行

```avahi-autoipd --check [interface]```

成功获取 IP 后再**脱离**终端

```avahi-autoipd --wait [interface]```

# SYNOPSIS

**avahi-autoipd** [_options_] _interface_

# PARAMETERS

**-D, --daemonize**
> 启动后转为守护进程；隐含启用 syslog 日志

**-k, --kill**
> 终止指定接口上正在运行的守护进程

**-r, --refresh**
> 重新通告已获取的 IP 地址（等效于 SIGHUP）

**-c, --check**
> 若守护进程正在接口上运行则返回 0

**-s, --syslog**
> 记录到 syslog 而非 STDERR

**--debug**
> 启用详细模式以输出详细日志

**--no-drop-root**
> 保留 root 权限（出于安全考虑不推荐）

**--no-chroot**
> 跳过 chroot 操作

**-S, --start=**_address_
> 获取指定的 IPv4LL 地址

**-w, --wait**
> 成功获取 IP 后再脱离终端

**--force-bind**
> 即使存在可路由地址也获取 IPv4LL 地址

**--no-proc-title**
> 运行期间不修改进程名

**-h, --help**
> 显示帮助信息

**-v, --version**
> 显示版本详情

# DESCRIPTION

**avahi-autoipd** 实现了 IPv4LL（_IPv4 链路本地地址的动态配置_），这是 **IETF RFC3927** 定义的协议，可在无需中央服务器的情况下，从链路本地 **169.254.0.0/16** 范围内自动配置 IP 地址。

它主要面向没有 DHCP 服务器的**自组网（ad-hoc 网络）**，是 **Zeroconf 协议栈**的核心组件。该守护进程既可独立运行，也可作为 DHCP 不可用时的回退机制与 DHCP 客户端集成。

启动后，**avahi-autoipd** 会探测网络中的地址冲突，获取一个可用的链路本地地址，并持续监控冲突。获取成功后，它会执行 **/etc/avahi/avahi-autoipd.action** 脚本来配置网络接口。

该守护进程响应信号：**SIGINT** 和 **SIGTERM** 触发关闭，**SIGHUP** 强制重新通告当前 IP 地址。

# CAVEATS

链路本地地址（**169.254.0.0/16**）只能在同一网段内通信，无法路由到其他网络。若已存在可路由的 IP 地址，则不会分配链路本地地址，除非使用 **--force-bind**。

# HISTORY

属于 **Avahi** 项目的一部分，该项目是对 Apple 的 Bonjour/Zeroconf 协议的自由软件实现。IPv4LL 支持于 **2005 年**在 **RFC3927** 中标准化，**avahi-autoipd** 则成为 Linux 系统上一个轻量的独立实现。

# INSTALL

```apt: sudo apt install avahi-autoipd```

```dnf: sudo dnf install avahi-autoipd```

```zypper: sudo zypper install avahi-autoipd```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[avahi-daemon](/man/avahi-daemon)(8), [dhclient](/man/dhclient)(8), [ip](/man/ip)(8), [ifconfig](/man/ifconfig)(8)

# RESOURCES

```[Homepage](https://avahi.org/)```

```[Source code](https://github.com/avahi/avahi)```

<!-- verified: 2026-06-17 -->
