# TAGLINE

简化 payload 生成

# TLDR

**生成 Windows payload**

```msfpc windows [192.168.1.10]```

**生成 Linux payload**

```msfpc linux [192.168.1.10]```

**使用特定端口生成**

```msfpc windows [192.168.1.10] [4444]```

**生成 Meterpreter payload**

```msfpc windows msf [192.168.1.10]```

**生成分段的反向连接 payload**

```msfpc windows staged reverse [192.168.1.10]```

**生成 Python payload**

```msfpc python [192.168.1.10]```

为某个 IP **生成所有类型的 payload**

```msfpc loop [192.168.1.10]```

# SYNOPSIS

**msfpc** _type_ [_domain/ip_] [_port_] [_cmd/msf_] [_bind/reverse_] [_staged/stageless_] [_tcp/http/https/find_port_] [_batch/loop_] [_verbose_]

# PARAMETERS

_TYPE_
> Payload 类型：APK、ASP、ASPX、Bash、Java、Linux、OSX、Perl、PHP、Powershell、Python、Tomcat 或 Windows。

_DOMAIN/IP_
> 目标 IP 地址、域名或接口名（如 eth0）。使用 "wan" 可自动检测外部 IP。

_PORT_
> 端口号（默认：443）。

**cmd**
> 使用标准的本地命令提示符/终端 Shell。

**msf**
> 使用 Meterpreter shell（可用时为默认）。

**bind**
> 在目标上打开端口供攻击者连接。

**reverse**
> 让目标反向连回攻击者（默认）。

**staged**
> 将 payload 拆分为多段（更小，需要 Metasploit）。

**stageless**
> 完整独立的 payload（更稳定）。

**tcp** / **http** / **https**
> 连接使用的协议。默认为 TCP。

**batch**
> 为给定类型生成所有可能的 payload。

**loop**
> 为每种类型各生成一个 payload。

**verbose**
> 启用详细输出。

# DESCRIPTION

**msfpc**（MSFvenom Payload Creator）简化了 payload 的生成。它封装了 msfvenom 的功能。

该工具可以快速创建常见 payload，并生成对应的 handler 和多种格式的输出。

# CAVEATS

仅限授权测试。需要 Metasploit。不做混淆编码的话很容易被检测。

# HISTORY

msfpc 的诞生是为了给渗透测试人员简化 **msfvenom payload** 的生成过程。

# INSTALL

```nix: nix profile install nixpkgs#msfpc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[msfvenom](/man/msfvenom)(1), [msfconsole](/man/msfconsole)(1), [nmap](/man/nmap)(1)
