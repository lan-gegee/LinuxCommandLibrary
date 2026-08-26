# TAGLINE

网络入侵检测与防御系统

# TLDR

**嗅探器模式**

```snort -v -i [eth0]```

**数据包记录器**

```snort -dev -l [/var/log/snort] -i [eth0]```

**IDS 模式**

```snort -c [/etc/snort/snort.conf] -i [eth0]```

**测试配置**

```snort -T -c [/etc/snort/snort.conf]```

**读取 pcap 文件**

```snort -r [capture.pcap] -c [snort.conf]```

**守护进程模式**

```snort -D -c [snort.conf] -i [eth0]```

**告警模式**

```snort -A [fast] -c [snort.conf] -i [eth0]```

# SYNOPSIS

**snort** [_-c config_] [_-l logdir_] [_-i interface_] [_options_]

# PARAMETERS

**-c** _FILE_
> 配置文件。

**-i** _INTERFACE_
> 网络接口。

**-l** _DIR_
> 日志目录。

**-A** _MODE_
> 告警模式（fast、full、console）。

**-D**
> 守护进程模式。

**-r** _FILE_
> 读取 pcap。

**-T**
> 测试配置。

**-v**
> 详细输出。

**-d**
> 转储数据包数据。

**-e**
> 显示链路层信息。

# DESCRIPTION

**snort** 是一个开源的网络入侵检测与防御系统（IDS/IPS），可执行实时流量分析和数据包记录。它根据一组用户自定义的规则检查网络流量，以检测攻击、探测和可疑活动。

该工具有三种运行模式：嗅探器模式在控制台上显示数据包；记录器模式将流量记录到 pcap 文件以便离线分析；IDS 模式应用检测规则并生成告警。规则使用一种灵活的语言，可按协议、内容模式、流方向和其他数据包特征进行匹配。

Snort 可以内联运行为 IPS 以主动阻断检测到的威胁，也可以被动运行为 IDS 仅进行监控和告警。其规则格式已成为行业标准，社区和商业规则数以千计，可用于检测已知漏洞、恶意软件和策略违规。

# CONFIGURATION

**/etc/snort/snort.conf**
> 主配置文件，定义网络变量、预处理器、输出插件和规则路径。

**/etc/snort/rules/**
> 存放配置所加载检测规则文件的目录。

# CAVEATS

抓包需要 root 权限。需要调优规则。高带宽场景具有挑战性。

# HISTORY

**Snort** 由 **Martin Roesch** 于 **1998 年**创建。它成为部署最广泛的 IDS，目前由 Cisco 维护。

# INSTALL

```apk: sudo apk add snort```

```brew: brew install snort```

```nix: nix profile install nixpkgs#snort```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[suricata](/man/suricata)(1), [tcpdump](/man/tcpdump)(1), [zeek](/man/zeek)(1)
