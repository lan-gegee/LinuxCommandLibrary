# TAGLINE

从网络流量中捕获图像

# TLDR

从网络中**捕获图像**

```driftnet -i [eth0]```

**将图像保存到**目录

```driftnet -i [eth0] -d [/tmp/images]```

**无界面捕获**

```driftnet -i [eth0] -a -d [/tmp/images]```

从 pcap **文件读取**

```driftnet -f [capture.pcap]```

**详细输出**

```driftnet -v -i [eth0]```

# SYNOPSIS

**driftnet** [_options_]

# PARAMETERS

**-i** _INTERFACE_
> 要在其上捕获的网络接口。

**-d** _DIR_
> 保存图像的目录。

**-a**
> 附属模式（无显示窗口）。

**-f** _FILE_
> 从 pcap 文件读取。

**-p**
> 不将接口置于混杂模式。

**-v**
> 详细模式。

**-b**
> 捕获到图像时发出蜂鸣。

**--help**
> 显示帮助信息。

# DESCRIPTION

**driftnet** 实时捕获并显示网络流量中的图像。它提取经过受监控网络接口的未加密 HTTP 连接所传输的 JPEG、GIF 和 PNG 图像。

该工具适用于网络监控、安全演示和取证。在显示模式下，捕获的图像会显示在窗口中；在附属模式下，它们会被保存到磁盘。

driftnet 还能从网络流中提取音频数据，实时播放或保存为文件。

# CAVEATS

只能捕获未加密流量（HTTP）。需要 root/混杂模式访问权限。无法看到 HTTPS 流量。仅用于经授权的监控。

# HISTORY

driftnet 由 **Chris Lightfoot** 创建，作为网络流量可见性的一个演示。它揭示了未加密通信对隐私的影响，常被用于安全意识培训。

# INSTALL

```apt: sudo apt install driftnet```

```nix: nix profile install nixpkgs#driftnet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(8), [wireshark](/man/wireshark)(1), [ettercap](/man/ettercap)(8)
