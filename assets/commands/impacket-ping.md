# TAGLINE

基于 Impacket 库、使用原始套接字的简单 ICMP ping 实现

# TLDR

从特定源 IP 向目标**发送 ICMP 回显请求**

```impacket-ping [192.168.1.50] [192.168.1.100]```

# SYNOPSIS

**impacket-ping** _source\_ip_ _destination\_ip_

# PARAMETERS

**source_ip**
> 用于发出 ICMP 回显请求数据包的源 IP 地址。

**destination_ip**
> 要 ping 的目标 IP 地址。

# DESCRIPTION

**impacket-ping** 是一个简单的 ICMP ping 实现，通过 Impacket 库使用原始套接字。它向指定的目标发送 ICMP 回显请求包，并报告收到的回显应答。源 IP 和目标 IP 都是必需的位置参数。

该脚本以一秒为间隔循环发送回显请求，并报告每个应答的序列号。与标准 ping 工具不同，此实现使用 Impacket 的原始套接字能力，适用于标准 ping 受限的环境，或需要与其他 Impacket 工具集成的场景。

注意，收到应答并不能确凿证明主机可用，因为远程主机可能在线但被配置为拒绝 ICMP 探测。

# CAVEATS

创建原始套接字需要 root/管理员权限。可能被过滤 ICMP 流量的防火墙拦截。必须同时指定源 IP 和目标 IP（没有自动检测源地址的功能）。对大多数场景而言，标准的 **ping** 命令功能更完善。

# HISTORY

属于 **Impacket** 库，最初由 SecureAuth 开发（现由 Fortra 维护）。作为演示 Impacket 的 ImpactPacket 和 ImpactDecoder 类进行原始套接字操作的基础示例收录。作者：Gerardo Richarte 和 Javier Kohen。

# SEE ALSO

[ping](/man/ping)(1), [impacket-ping6](/man/impacket-ping6)(1), [nmap](/man/nmap)(1)
