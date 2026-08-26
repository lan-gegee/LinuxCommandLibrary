# TAGLINE

识别网络端口上的应用层协议

# TLDR

**识别**端口上的服务（应用映射是默认模式）

```amap [192.168.1.1] [80]```

扫描**端口范围**

```amap [192.168.1.1] [1-1000]```

仅**抓取横幅信息**而不发送触发包

```amap -B [192.168.1.1] [80]```

通过 **UDP** 识别服务

```amap -u [192.168.1.1] [53]```

**安静地**扫描，只报告已识别的端口

```amap -q [192.168.1.1] [80]```

# SYNOPSIS

**amap** [_mode_] [_options_] _target_ _port_[_-port_] [_port_ ...]

# DESCRIPTION

**amap**（Application Mapper）是一款新一代扫描工具，通过发送触发包并分析响应来识别网络端口上运行的应用和服务。与简单的端口扫描器不同，它能够识别运行在非标准端口上的服务。

该工具将响应与签名数据库进行比对来识别应用指纹，可用于安全评估和网络审计。

# PARAMETERS

**-A**
> 应用映射：发送触发包并分析响应（这是默认模式）

**-B**
> 仅抓取横幅信息，不发送触发包

**-P**
> 不进行横幅或应用识别：作为全连接端口扫描器运行

**-b**
> 收到 ASCII 横幅信息时将其打印出来

**-u**
> 命令行给定的端口为 UDP（默认为 TCP）

**-6**
> 使用 IPv6 而不是 IPv4

**-1**
> 对每个端口只在首次识别成功前发送触发包

**-q**
> 安静模式：不将关闭或超时的端口报告为未识别

**-v**
> 详细输出

**-H**
> 跳过可能有害的触发包

**-R**
> 不识别 RPC 服务

**-p** _proto_
> 只发送指定单一协议的触发包

**-i** _file_
> 从 nmap 生成的机器可读文件中读取主机和端口

**-o** _file_
> 将 amap 的输出记录到文件

**-m**
> 使日志文件输出为机器可读格式（冒号分隔）

# CONFIGURATION

**/etc/amap/appdefs.trig**
> 触发定义文件，包含用于识别服务而发送的数据包。

**/etc/amap/appdefs.resp**
> 响应签名文件，用于匹配和识别应用层协议。

# CAVEATS

仅供授权的安全测试使用。可能触发入侵检测系统。某些服务可能不会响应触发包。签名数据库可能未收录较新的应用。

# HISTORY

**amap** 由 THC（The Hacker's Choice）开发，于 **2000** 年代初发布，作为端口扫描器的补充，专注于应用层识别。

# SEE ALSO

[nmap](/man/nmap)(1), [netcat](/man/netcat)(1), [masscan](/man/masscan)(1)

# RESOURCES

```[Source code](https://github.com/vanhauser-thc/THC-Archive)```

```[Homepage](https://www.thc.org/)```

<!-- verified: 2026-06-11 -->
