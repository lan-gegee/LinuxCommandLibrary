# TAGLINE

chrony NTP 守护进程的命令行界面

# TLDR

**检查同步状态**

```chronyc tracking```

**列出时间源**

```chronyc sources```

**详细的时间源列表**

```chronyc sources -v```

**时间源统计信息**

```chronyc sourcestats```

**强制时间同步**

```chronyc makestep```

**添加 NTP 服务器**

```chronyc add server [pool.ntp.org]```

**显示在线/离线时间源的数量**

```chronyc activity```

**连接到远程 chrony 守护进程**

```chronyc -h [remote-host]```

**交互模式**

```chronyc```

# SYNOPSIS

**chronyc** [_options_] [_command_]

# DESCRIPTION

**chronyc** 是 chronyd（NTP 守护进程）的命令行界面。用于监控同步状态、管理时间源和配置守护进程。更改在重启后不会保留。

# COMMANDS

**tracking**
> 显示系统时钟状态与偏差

**sources**
> 列出 NTP 时间源

**sourcestats**
> 显示时间源统计信息

**makestep**
> 强制立即校正时钟

**activity**
> 显示在线/离线时间源数量

**add server** _host_
> 添加 NTP 服务器

**delete** _address_
> 移除 NTP 时间源

**burst** _good_/_max_
> 开始快速轮询

**offline** / **online**
> 将时间源设为离线/在线

**ntpdata**
> 显示时间源的 NTP 数据

# PARAMETERS

**-n**
> 不解析主机名

**-N**
> 按配置中指定的原始主机名输出，而非反向 DNS 结果

**-c**
> CSV 输出格式

**-m**
> 允许在一行输入多个命令

**-4**
> 仅将主机名解析为 IPv4 地址

**-6**
> 仅将主机名解析为 IPv6 地址

**-h** _host_
> 连接到远程 chronyd

**-p** _port_
> 指定连接远程 chronyd 的端口

# CONFIGURATION

**/etc/chrony.conf**
> chronyd 的持久配置。通过 chronyc 做的运行时更改会在重启后丢失。

# CAVEATS

需要 chronyd 正在运行。运行时更改在重启后丢失。借助硬件时间戳可实现亚微秒级精度。

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

[chronyd](/man/chronyd)(8), [timedatectl](/man/timedatectl)(1), [ntpq](/man/ntpq)(1), [ntpd](/man/ntpd)(8), [hwclock](/man/hwclock)(8), [date](/man/date)(1)
