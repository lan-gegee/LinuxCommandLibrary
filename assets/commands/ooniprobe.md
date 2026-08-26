# TAGLINE

检测互联网审查和网络干扰

# TLDR

**运行所有测试**

```ooniprobe run```

**运行特定测试**

```ooniprobe run [websites]```

**列出可用测试**

```ooniprobe list```

**查看结果**

```ooniprobe list results```

**上传待上传的结果**

```ooniprobe upload```

**显示版本**

```ooniprobe version```

# SYNOPSIS

**ooniprobe** [_options_] _command_ [_args_]

# PARAMETERS

**run**
> 运行网络测试。

**list**
> 列出测试或结果。

**upload**
> 上传待上传的结果。

**version**
> 显示版本。

**--config** _FILE_
> 配置文件。

**--batch**
> 非交互模式。

**-v**, **--verbose**
> 详细输出。

# TEST CATEGORIES

**websites**
> 测试网站封锁情况。

**im**
> 即时通讯应用。

**circumvention**
> 审查规避工具。

**performance**
> 网络性能。

**middlebox**
> 网络操纵检测。

# DESCRIPTION

**ooniprobe** 用于检测互联网审查和网络干扰，属于网络干扰开放观测台（OONI）项目的一部分。

网站测试检查网站是否被封锁或过滤。DNS、TCP 和 HTTP 层都会被检查是否存在干扰。

即时通讯测试检查 WhatsApp、Telegram、Facebook Messenger 和 Signal 的可达性。

性能测试测量网络速度和质量。中间盒检测用于发现代理和流量操纵。

结果可以上传到 OONI 的公开数据集，为全球范围内的审查研究做出贡献。

# CAVEATS

在某些国家运行这些测试可能违法。测试会向 OONI 服务器暴露你的网络。某些测试可能触发网络监控。

# HISTORY

**OONI**（Open Observatory of Network Interference，网络干扰开放观测台）创立于 **2012** 年，是 Tor 项目的一部分。**ooniprobe** 提供客户端测试工具，供世界各地的志愿者测量互联网审查状况。

# INSTALL

```brew: brew install ooniprobe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tor](/man/tor)(1), [nmap](/man/nmap)(1), [traceroute](/man/traceroute)(1)
