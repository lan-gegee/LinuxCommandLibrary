# TAGLINE

实时捕获并显示 HTTP 流量

# TLDR

**在网卡上捕获 HTTP 流量**

```sudo httpflow -i [eth0]```

**按端口过滤**

```sudo httpflow -i [eth0] 'port 80'```

**保存到文件**

```sudo httpflow -i [eth0] -w [output]```

**从 pcap 读取**

```httpflow -r [capture.pcap]```

# SYNOPSIS

**httpflow** [_options_] [_filter_]

# PARAMETERS

_FILTER_
> BPF 过滤表达式。

**-i** _INTERFACE_
> 网络接口。

**-r** _FILE_
> 从 pcap 文件读取。

**-w** _DIR_
> 输出写入的目录。

**-u** _URL_
> 按 URL 模式过滤。

**-d**
> 打印调试信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**httpflow** 实时捕获并显示 HTTP 流量。它会从网络数据包中重建 HTTP 请求和响应。

该工具可用于调试、监视和分析 Web 流量。它能显示请求头、请求体以及请求/响应对。

# CAVEATS

实时捕获需要 root 权限。无法解码 HTTPS。使用时须注意隐私问题。

# HISTORY

**httpflow** 是一款基于 **libpcap** 的开源工具，它重组 TCP 流以重建 HTTP 请求和响应，用于实时的流量分析与调试。

# INSTALL

```brew: brew install httpflow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1), [mitmproxy](/man/mitmproxy)(1)

# RESOURCES

```[Source code](https://github.com/six-ddc/httpflow)```

<!-- verified: 2026-07-19 -->
