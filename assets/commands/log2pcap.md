# TAGLINE

从 Samba 日志文件提取网络追踪数据

# TLDR

**将 Samba 日志转换为 pcap**

```log2pcap [samba.log] > [output.pcap]```

**输出到指定文件**

```log2pcap -o [output.pcap] [samba.log]```

**从 stdin 读取**

```log2pcap < [/var/log/samba/log.smbd] > [output.pcap]```

**输出为供 text2pcap 使用的十六进制转储**

```log2pcap -h [samba.log] | text2pcap -T 139,139 - [trace.pcap]```

**静默模式，抑制警告**

```log2pcap -q [samba.log] > [output.pcap]```

# SYNOPSIS

**log2pcap** [_options_] [_logfile_]

# PARAMETERS

_logfile_
> Samba 调试日志文件。未指定时从 stdin 读取。

**-h**
> 输出为 text2pcap 可读取的十六进制转储。

**-q**
> 静默模式。抑制关于数据缺失或不完整的警告。

**--help**
> 显示帮助信息。

# DESCRIPTION

**log2pcap** 读取 Samba 日志文件，并根据日志中的数据包转储生成 pcap 文件。生成的 pcap 文件随后可用 Wireshark 或 tcpdump 等网络嗅探工具进行分析。

Samba 日志级别必须至少为 5 才能正确捕获 SMB 头部/参数，为 10 时包含数据包数据的前 512 字节，为 50 时可获得完整的数据包。

# CAVEATS

只从日志中提取 SMB 数据；不包含 LDAP、NetBIOS 查询和其他协议。生成的 TCP 和 IP 头部不含有效的校验和。属于 Samba 套件的一部分。

# HISTORY

log2pcap 是 **Samba** 套件的组成部分，用于从调试日志分析 SMB 协议流量。

# SEE ALSO

[smbclient](/man/smbclient)(1), [wireshark](/man/wireshark)(1), [tcpdump](/man/tcpdump)(1), [tshark](/man/tshark)(1)
