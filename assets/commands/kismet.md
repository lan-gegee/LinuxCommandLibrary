# TAGLINE

无线网络探测器、嗅探器和入侵检测系统

# TLDR

以默认设置**启动 Kismet**

```kismet```

使用指定捕获源**启动 Kismet**

```kismet -c [wlan0]```

**以多个捕获源启动**

```kismet -c [wlan0] -c [wlan1]```

**不使用 ncurses 包装器运行**（用于脚本或服务模式）

```kismet --no-ncurses```

**指定备用配置文件**

```kismet -f [path/to/kismet.conf]```

**禁用所有日志记录**

```kismet -n```

**指定日志类型**

```kismet -T [kismet,pcapng]```

**使用备用的日志目录**

```kismet -p [path/to/logs]```

**启用调试模式**（用于在 GDB 下运行）

```kismet --debug```

# SYNOPSIS

**kismet** [_options_]

# PARAMETERS

**-c** _SOURCE_
> 定义数据源（例如接口名）。可多次指定；优先于配置文件中的数据源。

**-f** _FILE_
> 使用备用配置文件。

**-n**, **--no-logging**
> 禁用所有日志记录。

**-T** _TYPES_, **--log-types** _TYPES_
> 覆盖要生成的日志类型（例如 kismet、pcapng）。

**-t** _TITLE_, **--log-title** _TITLE_
> 设置用于日志文件名的日志标题字段。

**-p** _DIR_, **--log-prefix** _DIR_
> 写入日志的目录。

**--homedir** _PATH_
> 为设置和日志使用备用主目录。

**--confdir** _PATH_
> 使用自定义配置目录。

**--override** _FLAVOR_
> 应用命名的覆盖配置（例如 wardrive）。

**--no-ncurses**
> 禁用 ncurses 包装器，输出纯文本。对脚本和服务很有用。

**--no-line-wrap**
> 禁用终端消息的自动换行。

**--no-plugins**
> 不加载插件。调试导致崩溃的插件时很有用。

**--debug**
> 启用调试模式：禁用崩溃/回溯处理程序和 ncurses 包装器，供在 GDB 下使用。

**--silent**
> 启动后不向控制台打印状态消息。

**--daemonize**
> 转入后台并作为守护进程运行。

**-v**, **--version**
> 打印版本信息。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**kismet** 是一款 802.11 无线网络探测器、嗅探器和入侵检测系统。它支持任何提供原始监控（rfmon）模式的无线网卡，能够探测 802.11a/b/g/n/ac 网络，还可以通过捕获插件探测蓝牙、Zigbee 及其他无线电信号。

Kismet 以被动方式工作——只收集数据包而不发送，因此很难被发现。它通过信标帧识别网络，随时间推移揭示隐藏网络，并根据数据流量推断出不发信标的网络。

现代版 Kismet（2016+）作为单一进程运行，提供基于 Web 的界面（默认位于 **http://localhost:2501**）和 REST API。旧的 **kismet_server**/**kismet_client**/**gpsmap** 分离架构已不再使用。Kismet 默认以其自有的 SQLite **.kismet** 格式记录日志，同时支持 pcap/pcapng 格式以便配合 Wireshark 等工具使用。

# CONFIGURATION

配置主要从系统配置目录（通常为 **/etc/kismet/** 或 **/usr/local/etc/**）中的 **kismet.conf** 和覆盖文件（如 **kismet_logging.conf**、**kismet_httpd.conf**）读取。用户级设置位于 **~/.kismet/** 下。

# CAVEATS

需要支持监控模式的无线网卡。将接口置于监控模式通常需要 root 权限（或 CAP_NET_ADMIN/CAP_NET_RAW）。未经授权捕获无线流量可能违反许多司法管辖区的法律。跳频轮询期间可能错过其他信道上的流量。

# HISTORY

Kismet 由 **Mike Kershaw**（dragorn）创建，第一个版本于 **2001 年**发布。它是最早被广泛使用的开源无线网络探测器之一。其名字来源于土耳其语中"命运"一词。2016 至 2018 年间架构经过大幅重写，将服务器/客户端/drone 组件合并为带有 Web UI 和 REST API 的单进程。

# INSTALL

```dnf: sudo dnf install kismet```

```pacman: sudo pacman -S kismet```

```zypper: sudo zypper install kismet```

```nix: nix profile install nixpkgs#kismet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aircrack-ng](/man/aircrack-ng)(1), [wireshark](/man/wireshark)(1), [tcpdump](/man/tcpdump)(1)
