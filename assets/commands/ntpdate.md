# TAGLINE

通过查询 NTP 服务器设置系统日期和时间

# TLDR

**查询**时间服务器而不更改时钟

```ntpdate -q [host]```

从服务器设置时钟（**同步**）

```sudo ntpdate [host]```

使用**非特权**源端口（应对防火墙）

```sudo ntpdate -u [host]```

立即**跳变**设置时钟而不是逐渐微调

```sudo ntpdate -b [host]```

# SYNOPSIS

**ntpdate** [_options_] _server_...

# PARAMETERS

**-q**
> 仅查询；不设置时钟

**-u**
> 出站数据包使用非特权端口（在防火墙环境下有用）

**-b**
> 强制跳变设置时间（突变）而非逐渐微调

**-s**
> 记录到 syslog 而不是 stdout

**-v**
> 详细输出

**-d**
> 调试模式；不更改时间，显示将要执行的操作

**-t _timeout_**
> 服务器响应超时时间（秒）

# DESCRIPTION

**ntpdate** 通过查询 NTP（网络时间协议）服务器来设置系统日期和时间。它执行一次性同步，这与持续运行的 **ntpd** 不同。

默认情况下，如果时间偏移较小，ntpdate 会逐渐调整（微调）时钟以避免干扰正在运行的程序。对于较大的偏移，它会立即跳变设置时钟。**-b** 标志无论偏移大小都强制跳变。

可以指定多个服务器；ntpdate 会查询所有服务器并采用最佳响应。

# CAVEATS

**已被弃用**，建议改用 **ntpd -q** 或 **sntp**。突然的时间变更（**-b**）可能让期望单调时间的应用出错。设置系统时钟需要 root 权限。不适合持续同步；请改用 ntpd 或 chronyd。

# HISTORY

ntpdate 属于最初的 NTP 发行版，但自 NTP 4.2.8 起已被弃用。现代系统通常使用 **systemd-timesyncd**、**chrony** 或 **ntpd** 进行时间同步。

# INSTALL

```apt: sudo apt install ntpsec-ntpdate```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ntpd](/man/ntpd)(8), [chronyc](/man/chronyc)(1), [timedatectl](/man/timedatectl)(1), [sntp](/man/sntp)(8)
