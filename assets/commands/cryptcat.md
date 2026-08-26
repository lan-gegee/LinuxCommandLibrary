# TAGLINE

带 twofish 加密的 netcat

# TLDR

在端口上带加密**监听**

```cryptcat -k password -l -p 1234```

带加密**连接**到端口

```cryptcat -k password host 1234```

带**超时**连接

```cryptcat -k password -w 10 host 1234```

对主机进行**端口扫描**

```cryptcat -v -z host 1-1024```

在本地与远程之间**转发**数据

```cryptcat -k password -l -p 8080 | cryptcat -k password host 80```

**传输**文件

```cryptcat -k password -l -p 1234 < file.txt```

# SYNOPSIS

**cryptcat** [_options_] [_hostname_] [_port_]

# DESCRIPTION

**cryptcat** 是具备 twofish 加密能力的 netcat。它提供与 netcat 相同的功能，但会对数据传输进行加密，从而在不安全的网络上实现安全通信。

# PARAMETERS

**-k PASSWORD**
> 指定加密密码

**-l**
> 监听模式（充当服务器）

**-p PORT**
> 指定本地端口号

**-w SECONDS**
> 连接及最后一次读取网络的超时时间

**-z**
> 零 I/O 模式（用于扫描）

**-v**
> 详细输出模式

**-n**
> 仅使用数字 IP 地址，不做 DNS 解析

**-u**
> UDP 模式而非 TCP

# CAVEATS

两端必须使用相同的加密密码。如果未用 **-k** 指定密码，cryptcat 会使用硬编码的默认密码 "metallica"，此时连接实际上等于未加密。本工具仅用于经授权的安全测试和正当的加密通信。

# HISTORY

**cryptcat** 作为 netcat 的安全版本开发而成，通过加入 twofish 加密防止网络通信被窃听。

# SEE ALSO

[nc](/man/nc)(1), [netcat](/man/netcat)(1), [ncat](/man/ncat)(1), [socat](/man/socat)(1)
