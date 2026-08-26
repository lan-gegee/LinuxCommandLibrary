# TAGLINE

简易网络时间协议客户端

# TLDR

**从 NTP 服务器查询时间**

```sntp [pool.ntp.org]```

从服务器**步进（直接设置）系统时钟**

```sudo sntp -S [pool.ntp.org]```

**缓调（逐步调整）**系统时钟

```sudo sntp -s [pool.ntp.org]```

**仅使用 IPv4 查询**

```sntp -4 [pool.ntp.org]```

**仅使用 IPv6 查询**

```sntp -6 [pool.ntp.org]```

**使用保留的 NTP 端口 123**

```sudo sntp -r [pool.ntp.org]```

# SYNOPSIS

**sntp** [_-46dhKoSs_] [_-a keyid_] [_-b bcaddress_] [_-c filename_] [_-M threshold_] [_-r_] [_server..._]

# PARAMETERS

**-S**, **--step**
> 使用 settimeofday() 步进（直接设置）系统时钟

**-s**, **--slew**
> 使用 adjtime() 缓调（逐步调整）时钟

**-4**, **--ipv4**
> 强制使用 IPv4 DNS 解析

**-6**, **--ipv6**
> 强制使用 IPv6 DNS 解析

**-r**, **--usereservedport**
> 使用保留的 NTP 端口 123 进行通信

**-M** _threshold_
> 偏移量小于阈值毫秒时缓调，否则步进

**-t** _seconds_
> 等待响应的超时时间（默认：5）

**-d**, **--debug-level**
> 提高调试详细程度（可多次指定）

**-K** _file_, **--kod**=_file_
> KoD（Kiss-of-Death）历史文件

**-a** _keyid_, **--authentication**=_keyid_
> 使用指定的密钥编号启用身份验证

**-b** _address_
> 监听指定地址以接收广播时间同步

**-l** _file_, **--logfile**=_file_
> 将状态消息记录到指定文件

**-c**, **--concurrent**
> 向解析出的 IP 并发发送查询（用于解析到不同机器上多个地址的主机名）

# DESCRIPTION

**sntp** 是一个简单网络时间协议客户端，它查询 NTP 服务器并显示本地系统时钟与服务器之间的时间偏移。在具有相应权限的情况下，它还可以校正系统时钟。

与完整的 ntpd 守护进程不同，sntp 执行一次性同步，因此适合无需持续同步的 cron 任务或脚本。它可以步进（立即设置）或缓调（逐步调整）时钟。

输出以秒为单位显示时间偏移和误差范围，表明本地时钟与服务器偏差多少。

# CAVEATS

步进时钟可能干扰依赖单调时间的应用程序。缓调更安全，但只限于小幅调整。现代发行版通常改用 **chronyd** 或 **systemd-timesyncd**。

# HISTORY

sntp 实现了 RFC 4330（Simple Network Time Protocol Version 4）。它是 NTP 参考实现的一部分，但在很大程度上已被 chrony 和 systemd-timesyncd 等更健壮的替代方案取代。

# SEE ALSO

[ntpd](/man/ntpd)(8), [ntpdate](/man/ntpdate)(1), [chronyc](/man/chronyc)(1), [timedatectl](/man/timedatectl)(1), [date](/man/date)(1)
