# TAGLINE

功能丰富的 NTP 时间同步套件

# TLDR

**检查同步状态**

```chronyc tracking```

**显示 NTP 时间源**

```chronyc sources```

**显示详细的时间源统计信息**

```chronyc sourcestats```

**强制立即同步**

```sudo chronyc makestep```

**添加新的 NTP 服务器**

```chronyc add server [ntp.example.com]```

**显示所有客户端**

```chronyc clients```

**检查 chrony 是否已同步**

```chronyc waitsync```

# SYNOPSIS

**chronyc** [_options_] [_command_]

**chronyd** [_options_]

# PARAMETERS (chronyc)

**tracking**
> 显示系统时钟同步状态。

**sources** [**-v**]
> 显示 NTP 时间源（使用 -v 显示详细信息）。

**sourcestats**
> 显示时间源统计信息。

**makestep**
> 若偏差较大则立即跳变校正时钟。

**add server** _address_
> 添加一个 NTP 服务器。

**delete** _address_
> 移除一个 NTP 时间源。

**burst** _polls_/_good_
> 加快初始同步速度。

**activity**
> 显示在线/离线时间源的数量。

**ntpdata** _address_
> 显示某个时间源的详细 NTP 数据。

**waitsync** [_max-tries_]
> 等待直到同步完成。

# PARAMETERS (chronyd)

**-d**
> 在前台运行（调试模式）。

**-f** _file_
> 指定配置文件。

**-q**
> 设置一次时钟后退出。

**-Q**
> 类似 -q，但不设置时钟。

# DESCRIPTION

**chrony** 是一个功能丰富的 NTP（网络时间协议）实现，用于同步系统时钟。它由 **chronyd**（守护进程）和 **chronyc**（命令行界面）组成。

chrony 擅长应对复杂环境：间歇性网络连接、时钟不稳定的虚拟机，以及会睡眠或休眠的系统。它比 ntpd 同步更快，并且在多变的条件下保持更好的精度。

配置文件位于 **/etc/chrony.conf**（或 **/etc/chrony/chrony.conf**），用于指定 NTP 服务器、访问控制和时钟调整。该守护进程既可以作为 NTP 客户端，也可以作为服务器运行。

# CONFIGURATION

**/etc/chrony.conf**（或 **/etc/chrony/chrony.conf**）
> 主配置文件，指定 NTP 服务器、访问控制、时钟调整和日志选项。

**/var/lib/chrony/drift**
> 漂移文件，记录系统时钟的频率误差，以便在离线时进行精确校正。

**/var/log/chrony/**（或通过 syslog）
> 日志目录，存放跟踪与测量数据。

# CAVEATS

makestep 命令可能导致时间跳变，影响正在运行的应用程序。防火墙必须允许 UDP 端口 123 以进行 NTP 通信。chronyd 必须以 root 身份或具备 CAP_SYS_TIME 能力运行。如果时间变化显著，某些应用程序可能会出现异常。

# HISTORY

chrony 由 **Richard Curnow** 于 **1997** 年开始编写，旨在为间歇性网络连接的系统提供更好的精度。**Miroslav Lichvar** 于 **2007** 年接手维护和开发工作。chrony 已成为包括 Fedora 和 RHEL 在内的许多 Linux 发行版的默认 NTP 客户端，因其同步更快且能更好地应对现代计算环境而胜过 ntpd。

# INSTALL

```dnf: sudo dnf install chrony```

```pacman: sudo pacman -S chrony```

```zypper: sudo zypper install chrony```

```brew: brew install chrony```

```nix: nix profile install nixpkgs#chrony```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ntpd](/man/ntpd)(8), [timedatectl](/man/timedatectl)(1), [hwclock](/man/hwclock)(8)

# RESOURCES

```[Homepage](https://chrony-project.org/)```

```[Documentation](https://chrony-project.org/documentation.html)```

<!-- verified: 2026-06-22 -->
