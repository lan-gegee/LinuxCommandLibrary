# TAGLINE

实时网络流量 ASCII 图表

# TLDR

显示网卡的**网络流量**图表

```speedometer -r [eth0] -t [eth0]```

仅监控**接收**字节数

```speedometer -r [eth0]```

仅监控**发送**字节数

```speedometer -t [eth0]```

跟踪**文件下载**进度

```speedometer -f [path/to/file] [expected_size]```

用**多列**展示不同数据源

```speedometer -r [eth0] -c -t [eth0]```

设置**刷新间隔**

```speedometer -i [seconds] -r [eth0]```

# SYNOPSIS

**speedometer** [_OPTIONS_] _tap_ [_tap_...]

# PARAMETERS

**-r** _interface_
> 监控网卡上接收的字节数

**-t** _interface_
> 监控网卡上发送的字节数

**-f** _filename_ [_size_]
> 跟踪文件下载，可选进度条

**-c**
> 开启新的显示列

**-i** _seconds_
> 设置刷新间隔（默认：1）

**-b**
> 使用方块字符而非平滑字符显示

**-l**
> 使用线性刻度而非对数刻度

**-s**
> 以比特/秒而非字节/秒显示速度

**-m** _max_
> 设置图表的最大字节/秒值

**-n** _min_
> 设置图表的最小字节/秒值

**-k** _colors_
> 终端颜色支持（1, 16, 88 或 256）

**-p**
> 纯文本显示模式

**-x**
> 文件达到预期大小时退出

**-z**
> 对不存在的文件报告零值

# DESCRIPTION

**speedometer** 在终端中以 ASCII 图表形式显示实时网络流量或文件传输速度。它从网络接口读取数据或监控文件增长，以可自定义的刻度和刷新率将信息可视化呈现。

多个数据源（tap）可以同时在多列中显示，便于对比上传/下载速度或监控多个网卡。该工具适用于监控传输进度、排查网络问题以及可视化带宽使用情况。

# CAVEATS

需要访问 /proc 或 /sys 中的网络接口统计信息。接口名称因系统而异（eth0, enp0s3, wlan0 等）。较大的刷新间隔可能错过流量峰值。终端必须支持所使用的显示字符。

# HISTORY

**speedometer** 是一个用于可视化网络带宽的 Python 脚本。它提供了图形化网络监控器的轻量替代方案，适合远程 SSH 会话和无头服务器使用。自 **2000 年代中期**起，它就已被收录进各 Linux 发行版的软件仓库。

# INSTALL

```aur: yay -S speedometer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iftop](/man/iftop)(8), [nethogs](/man/nethogs)(8), [bmon](/man/bmon)(1), [vnstat](/man/vnstat)(1)
