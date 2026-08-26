# TAGLINE

多播 DNS/DNS-SD 服务发现守护进程

# TLDR

**启动** Avahi mDNS/DNS-SD 守护进程

```avahi-daemon```

**启动**并守护进程化（后台运行）

```avahi-daemon --daemonize```

**检查**守护进程是否正在运行

```avahi-daemon --check```

**重新加载**配置和服务定义

```avahi-daemon --reload```

**终止**正在运行的守护进程

```avahi-daemon --kill```

**启用调试**输出并记录详细日志

```avahi-daemon --debug```

# SYNOPSIS

**avahi-daemon** [_options_]

# PARAMETERS

**-f, --file=**_FILE_
> 指定配置文件（默认：/etc/avahi/avahi-daemon.conf）

**-D, --daemonize**
> 启动后转为守护进程；隐含 --syslog

**-s, --syslog**
> 记录到 syslog 而非 STDERR

**--debug**
> 将日志级别提高到调试级

**--no-rlimits**
> 不强制执行配置文件中的资源限制

**--no-drop-root**
> 不放弃 root 权限（出于安全考虑不推荐）

**--no-chroot**
> 禁用 chroot 操作（需要编译期支持）

**--no-proc-title**
> 执行期间不更改进程名

**-k, --kill**
> 通过发送 SIGTERM 终止正在运行的守护进程

**-r, --reload**
> 通过发送 SIGHUP 重新读取 resolv.conf 和服务定义

**-c, --check**
> 守护进程正在运行则返回 0，否则返回非零值

**-h, --help**
> 显示帮助信息

**-v, --version**
> 显示版本信息

# DESCRIPTION

**avahi-daemon** 在 Linux 及其他类 Unix 系统上实现了 Apple 的 Zeroconf 架构（也称 **Rendezvous** 或 **Bonjour**）。它使用 **mDNS**（多播 DNS）和 **DNS-SD**（DNS 服务发现）协议注册本地 IP 地址和静态服务。

该守护进程提供**服务发现**功能，让本地网络中的应用程序和设备无需手动配置或中央 DNS 服务器即可自动相互发现。它发布服务并响应来自其他主机的服务发现查询。

启动时，**avahi-daemon** 从 **/etc/avahi/avahi-daemon.conf** 读取配置，并从 **/etc/avahi/services/\*.service** 加载 XML 服务定义。启用相应功能后，它还会处理 **/etc/resolv.conf** 以获取单播 DNS 服务器信息。

该守护进程提供两个 IPC API：一个是由 **avahi-dnsconfd** 和 **nss-mdns** 使用的简单协议，另一个是用于应用集成的完整 **D-Bus** 接口。

**信号处理**：**SIGINT** 和 **SIGTERM** 触发关闭，**SIGHUP** 重新加载 DNS 服务器数据和服务定义，**SIGUSR1** 将缓存的资源记录转储到 syslog 以便调试。

# CONFIGURATION

**/etc/avahi/avahi-daemon.conf**
> 守护进程的主配置文件，控制服务器设置、网络接口、发布选项和资源限制。

**/etc/avahi/hosts**
> 通过 mDNS 发布的主机名到地址的静态映射。

**/etc/avahi/services/*.service**
> XML 服务定义文件，用于持久化的静态服务注册。

# CAVEATS

需要网络多播支持才能正常工作。必须能够访问 IPv4 链路本地地址（169.254.0.0/16）和多播地址。某些严格的防火墙可能阻止 UDP 端口 5353 上的 mDNS 流量。

# HISTORY

**Avahi** 作为 Apple 的 **Bonjour**（最初名为 Rendezvous）协议族的自由软件实现而开发。项目始于 **2004 年**，现已成为 Linux 系统上事实标准的 mDNS/DNS-SD 实现，并被各大发行版集成。

# INSTALL

```apt: sudo apt install avahi-daemon```

```dnf: sudo dnf install avahi```

```pacman: sudo pacman -S avahi```

```apk: sudo apk add avahi```

```zypper: sudo zypper install avahi```

```brew: brew install avahi```

```nix: nix profile install nixpkgs#avahi```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[avahi-browse](/man/avahi-browse)(1), [avahi-publish](/man/avahi-publish)(1), [avahi-dnsconfd](/man/avahi-dnsconfd)(8)
