# TAGLINE

用于系统时钟同步的 NTP 守护进程

# TLDR

**启动 chronyd** 守护进程

```chronyd```

**在前台启动**并输出调试信息

```chronyd -d```

**使用指定的配置文件启动**

```chronyd -f [/etc/chrony.conf]```

**检查配置文件语法**

```chronyd -p```

**运行一次**以进行初始时间同步

```chronyd -q```

# SYNOPSIS

**chronyd** [_options_]

# DESCRIPTION

**chronyd** 是 chrony 的守护进程组件，chrony 是网络时间协议（NTP）的一个功能丰富的实现。它将系统时钟与 NTP 服务器、参考时钟或手动输入同步，还可以向其他计算机提供时间服务。

chronyd 能够在广泛的环境条件下良好工作，包括间歇性网络连接、虚拟化环境以及时钟不稳定的系统。在许多场景下，它可以比传统的 ntpd 更快、更精确地完成同步。

该守护进程维护一个漂移文件来跟踪系统时钟的频率误差，即使失去网络连接也能准确校正时间。

# PARAMETERS

**-d**
> 不脱离终端（前台运行）。

**-f** _file_
> 使用指定的配置文件。

**-n**
> 不 fork 到后台。

**-p**
> 打印配置后退出。

**-q**
> 设置一次时间后退出。

**-Q**
> 类似 -q，但不跳变时钟。

**-r**
> 重启时重新加载样本历史记录。

**-R**
> 不恢复已保存的状态。

**-s**
> 启动时从 RTC 设置系统时间。

**-u** _user_
> 以指定用户身份运行。

**-x**
> 不控制系统时钟。

**-4**
> 仅使用 IPv4。

**-6**
> 仅使用 IPv6。

# CONFIGURATION

**/etc/chrony.conf**
> 主配置文件，指定 NTP 服务器、访问控制、漂移文件路径和日志选项。

**/var/lib/chrony/drift**
> 漂移文件，记录系统时钟的频率误差。

**/var/run/chrony/chronyd.pid**
> 正在运行的守护进程的 PID 文件。

# CAVEATS

调整系统时间需要 root 权限。不能与其他 NTP 守护进程（ntpd）同时运行。硬件时间戳需要内核和驱动支持。某些功能可能需要在 /etc/chrony.conf 中配置。实时时钟（RTC）同步需要硬件支持。

# HISTORY

**chrony** 由 **Richard Curnow** 于 **1997** 年开始编写，作为参考版 NTP 实现的替代品。它专为不保持持续网络连接的系统而设计。该项目现在由 Red Hat 的 **Miroslav Lichvar** 维护。chrony 已成为包括 Fedora、RHEL 和 CentOS 在内的许多 Linux 发行版的默认 NTP 实现。

# INSTALL

```apt: sudo apt install chrony```

```dnf: sudo dnf install chrony```

```pacman: sudo pacman -S chrony```

```apk: sudo apk add chrony```

```zypper: sudo zypper install chrony```

```brew: brew install chrony```

```nix: nix profile install nixpkgs#chrony```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chronyc](/man/chronyc)(1), [ntpd](/man/ntpd)(8), [timedatectl](/man/timedatectl)(1)
