# TAGLINE

面向 traceroute 与探测的互联网测量工具

# TLDR

**Traceroute**

```scamper -c "trace" -i [target]```

**Ping**

```scamper -c "ping" -i [target]```

**从文件读取多个目标**

```scamper -c "trace" -f [targets.txt]```

**输出到文件**

```scamper -c "trace" -o [output.warts] -i [target]```

**设置探测速率**

```scamper -c "trace" -p [100] -i [target]```

**DNS 查询**

```scamper -c "host" -i [example.com]```

**别名解析（dealias）**

```scamper -c "dealias" -i [ip1],[ip2]```

# SYNOPSIS

**scamper** [_-c command_] [_-i target_] [_-f file_] [_-o output_] [_options_]

# PARAMETERS

**-c** _COMMAND_
> 测量命令。

**-i** _TARGET_
> 目标地址。

**-f** _FILE_
> 目标文件。

**-o** _FILE_
> 输出文件。

**-p** _RATE_
> 每秒数据包数。

**-M** _MONITORNAME_
> 监视器名称。

**-l** _LISTID_
> 列表 ID。

# COMMANDS

**trace** - Traceroute
**ping** - ICMP ping
**host** - DNS 查询
**dealias** - 别名解析
**tracelb** - 负载均衡的 traceroute
**sting** - NAT 检测

# DESCRIPTION

**scamper** 是一款为大规模互联网研究设计的网络测量工具。它支持多种探测技术，包括 traceroute、ping、DNS 查询、别名解析和负载均衡路径检测，并可通过可配置的并行度和速率限制高效地对大量目标执行这些测量。

结果以 warts 二进制格式存储，其中包含丰富的元数据，如精确的时间信息、ICMP 响应和测量参数。配套工具（sc_warts2json、sc_warts2csv 等）可将 warts 数据转换为常见格式以便分析。速率限制机制在保持测量吞吐量的同时避免压垮目标网络。

# CAVEATS

需要原始套接字访问权限。高速率探测可能引发问题。这是一款研究导向的工具。

# HISTORY

**scamper** 由 **Matthew Luckie** 为互联网测量研究而开发。它被研究网络拓扑与性能的研究人员广泛使用。

# INSTALL

```apt: sudo apt install scamper```

```zypper: sudo zypper install scamper```

```brew: brew install scamper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[traceroute](/man/traceroute)(1), [ping](/man/ping)(1), [mtr](/man/mtr)(1)
