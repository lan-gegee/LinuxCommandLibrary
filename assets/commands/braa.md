# TAGLINE

用于查询多台主机的批量 SNMP 扫描器

# TLDR

**遍历**某台主机的 **SNMP 树**

```braa public@[ip_address]:[.1.3.6.*]```

在**子网中查询**特定 OID

```braa public@[ip_range]:[.1.3.6.1.2.1.1.6.0]```

使用 SNMP 写操作**设置值**

```braa private@[ip_address]:[.1.3.6.1.2.1.1.6.0]=s'[workgroup]'```

# SYNOPSIS

**braa** [**-2**] [**-v**] [**-t** _secs_] [**-a** _secs_] [**-r** _retries_] [**-d** _usecs_] [**-f** _file_] _community@host:oid_...

# PARAMETERS

**-2**
> 使用 SNMPv2C（支持 Counter64）。

**-t** _SECS_
> 等待响应的时间，单位为秒（默认：2）。

**-a** _SECS_
> 截止时间/总超时。

**-r** _N_
> 放弃前的重试次数（默认：3）。

**-d** _USECS_
> 数据包之间的微秒级延迟。

**-f** _FILE_
> 从文件加载查询。

**-v**
> 详细输出。

# DESCRIPTION

**braa** 是一款超快的批量 SNMP 扫描器，可以同时查询多台主机。与按顺序逐个处理主机的传统 SNMP 工具不同，braa 以异步方式发送查询，大幅提升大型网络的扫描速度。它实现了自己的 SNMP 协议栈，只接受数字 OID 而不支持符号名称。

该工具支持在单条命令中对多台主机执行 SNMP GET、SET 和 WALK 操作。

# SYNTAX

查询采用如下格式：**[community@]host[-host2][:port]:OID[/id][,OID2...]**

- **community**：SNMP 团体字符串（如 public、private）
- **host**：IP 地址或主机名（支持范围写法，如 10.0.0.1-10.0.0.50）
- **OID**：对象标识符；加 * 后缀表示执行 walk 操作

SET 操作需追加 **=type'value'**，其中 type 为：
- **s**：字符串
- **i**：整数
- **a**：IP 地址
- **o**：OID

# CAVEATS

SNMP v1/v2c 的团体字符串以明文传输。批量扫描可能触发安全告警或速率限制。扫描网络前请确保已获得授权。不适用于 SNMPv3。

# INSTALL

```apt: sudo apt install braa```

```nix: nix profile install nixpkgs#braa```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snmpwalk](/man/snmpwalk)(1), [snmpget](/man/snmpget)(1), [snmpset](/man/snmpset)(1)
