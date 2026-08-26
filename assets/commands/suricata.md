# TAGLINE

网络入侵检测与防御引擎

# TLDR

在网卡上**以 IDS 模式启动**

```suricata -c /etc/suricata/suricata.yaml -i [eth0]```

**分析 pcap 文件**

```suricata -c /etc/suricata/suricata.yaml -r [capture.pcap]```

配合 NFQUEUE **以 IPS 模式运行**

```suricata -c /etc/suricata/suricata.yaml -q [0]```

**测试配置文件**

```suricata -c /etc/suricata/suricata.yaml -T```

**以守护进程方式运行**

```suricata -c /etc/suricata/suricata.yaml -i [eth0] -D```

**设置自定义日志目录**

```suricata -c /etc/suricata/suricata.yaml -i [eth0] -l [/var/log/suricata]```

使用 suricata-update **更新规则**

```suricata-update```

**显示版本**

```suricata -V```

# SYNOPSIS

**suricata** [_options_]

# PARAMETERS

**-c** _file_
> 配置文件路径。

**-T**
> 测试配置后退出。

**-i** _interface_
> 用于抓包的网络接口。

**-r** _file_
> 从 pcap 文件读取数据包（离线模式）。

**-q** _queue_
> 使用 NFQUEUE 队列 ID 以内联方式运行。

**-D**
> 以后台守护进程方式运行。

**-l** _dir_
> 设置默认日志目录。

**-s** _file_
> 加载额外的签名文件。

**-S** _file_
> 仅从该文件加载签名。

**-v**
> 提高输出详细程度（可多次使用）。

**-V**
> 显示版本信息。

**--user** _user_
> 初始化完成后以指定用户身份运行。

**--group** _group_
> 初始化完成后以指定组身份运行。

**--pidfile** _file_
> 将进程 ID 写入文件。

**--runmode** _mode_
> 设置运行模式：workers、autofp 或 single。

**--af-packet** _interface_
> 启用 AF_PACKET 抓包。

**--netmap** _interface_
> 启用 NETMAP 抓包。

**--pfring** _interface_
> 启用 PF_RING 抓包。

**-F** _file_
> 使用文件中的 BPF 过滤器。

**-k** _mode_
> 校验和检查：all、none 或 auto。

**--set** _name=value_
> 覆盖某个配置值（如 --set default-log-dir=/tmp）。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**suricata** 是高性能的网络 IDS、IPS 与网络安全监测引擎。它通过基于签名的检测、协议分析和异常检测来检查网络流量，识别威胁和安全事件。

Suricata 可以在三种模式下工作：IDS（被动监控）、IPS（借助 NFQUEUE 或 netfilter 内联阻断）以及网络安全监测（日志记录与元数据提取）。它支持多种抓包方式，包括 AF_PACKET、PF_RING、NETMAP 和标准 pcap。

该引擎利用多线程实现高性能数据包处理，并支持用 Lua 脚本编写自定义检测逻辑。它与 Snort 规则兼容，可以处理 Emerging Threats 规则集。

输出格式包括用于 SIEM 集成的 EVE JSON、fast 日志、unified2 以及各种协议专属日志。

# CONFIGURATION

**/etc/suricata/suricata.yaml**
> 定义网络接口、规则路径、日志和检测设置的主配置文件。

**/etc/suricata/rules/**
> 存放 Snort 兼容格式检测规则文件的目录。

**/var/log/suricata/**
> EVE JSON、fast 日志和告警输出的默认日志目录。

# CAVEATS

实时抓包需要 root 权限或 CAP_NET_RAW 能力。高流量环境需要调优配置才能达到最佳性能。IPS 模式需要正确配置 netfilter/iptables。规则更新应在生产部署前先行测试。

# HISTORY

**Suricata** 由开放信息安全基金会（OISF）于 2009 年开始开发，2010 年发布首个稳定版本。它被打造为 Snort 的现代多线程替代品，旨在充分利用现代多核处理器。该项目由美国国土安全部及其他赞助方资助。

# INSTALL

```apt: sudo apt install suricata```

```dnf: sudo dnf install suricata```

```apk: sudo apk add suricata```

```zypper: sudo zypper install suricata```

```brew: brew install suricata```

```nix: nix profile install nixpkgs#suricata```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snort](/man/snort)(1), [tcpdump](/man/tcpdump)(1), [zeek](/man/zeek)(1), [tshark](/man/tshark)(1), [iptables](/man/iptables)(8), [nftables](/man/nftables)(8)
