# TAGLINE

从 Zabbix 代理检索数据

# TLDR

从代理获取 CPU 负载

```zabbix_get -s [192.168.1.10] -k "system.cpu.load[all,avg1]"```

从指定端口获取数据

```zabbix_get -s [host] -p [10050] -k "[agent.version]"```

获取磁盘剩余空间

```zabbix_get -s [host] -k "vfs.fs.size[/,free]"```

带超时地获取数据

```zabbix_get -s [host] -t [60] -k "[key]"```

使用 TLS PSK 获取数据

```zabbix_get -s [host] --tls-connect psk --tls-psk-identity [id] --tls-psk-file [psk.txt] -k "[key]"```

# SYNOPSIS

**zabbix_get** -s _host_ -k _key_ [_options_]

# PARAMETERS

**-s**, **--host** _host_
> Zabbix 代理的主机名或 IP 地址。

**-p**, **--port** _port_
> 端口号（默认：10050）。

**-k**, **--key** _key_
> 要检索的监控项键。

**-I**, **--source-address** _ip_
> 连接使用的源 IP 地址。

**-t**, **--timeout** _seconds_
> 超时时间（1-600，默认：30）。

**--tls-connect** _mode_
> 连接类型：unencrypted、psk 或 cert。

**--tls-psk-identity** _id_
> PSK 身份字符串。

**--tls-psk-file** _file_
> 包含预共享密钥的文件。

**-P**, **--protocol** _value_
> 通信协议：auto（默认，JSON 并在失败时回退到明文）、json 或 plaintext（用于 6.4.x 及更早版本的代理）。

**--tls-ca-file** _file_
> 包含顶级 CA 证书的文件的完整路径，用于对端证书验证。

**--tls-cert-file** _file_
> 包含客户端证书的文件的完整路径。

**--tls-key-file** _file_
> 包含私钥的文件的完整路径。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本。

# DESCRIPTION

**zabbix_get** 用于从 Zabbix 代理检索数据，以便测试和排障。它执行被动检查，使用与 Zabbix 服务器相同的协议向代理查询特定监控项的值。

该工具有助于在将主机加入监控之前验证代理配置和连通性。发起请求的主机必须列入代理配置中的 Server 参数。

常见用例包括测试新的监控项键、验证代理响应，以及在不访问 Zabbix 前端的情况下调试采集问题。

# EXIT STATUS

成功返回 0，出错或取值失败返回 1。

# CAVEATS

发起请求的主机必须在代理的 Server 参数中。只适用于 Zabbix 代理，不支持其他监控协议。TLS 要求两端配置匹配。

# HISTORY

**zabbix_get** 是 Zabbix 监控系统的一部分，该系统由 Alexei Vladishev 于 2001 年创建。Zabbix 已成长为最受欢迎的企业监控解决方案之一，而 zabbix_get 始终是代理排障的重要工具。

# INSTALL

```apt: sudo apt install zabbix-proxy-mysql```

```dnf: sudo dnf install zabbix-proxy-mysql```

```apk: sudo apk add zabbix-utils```

```zypper: sudo zypper install zabbix-proxy-mysql```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zabbix_agentd](/man/zabbix_agentd)(8), [zabbix_server](/man/zabbix_server)(8), [zabbix_proxy](/man/zabbix_proxy)(8)
