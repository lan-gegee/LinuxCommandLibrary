# TAGLINE

通过 SNMP 显示远程网络状态

# TLDR

**显示网络连接**

```snmpnetstat -v [2c] -c [public] [host]```

**显示路由表**

```snmpnetstat -v [2c] -c [public] -Cr [host]```

**显示接口统计信息**

```snmpnetstat -v [2c] -c [public] -Ci [host]```

# SYNOPSIS

**snmpnetstat** [_options_] _agent_

# PARAMETERS

**-v** _version_
> SNMP 版本（1、2c、3）。

**-c** _community_
> 社区字符串。

**-Ci**
> 接口统计信息。

**-Cr**
> 路由表。

**-Cs**
> 协议统计信息。

# DESCRIPTION

**snmpnetstat** 通过 SNMP 显示远程主机的网络状态。类似于 netstat，但使用 SNMP 协议通过网络获取数据。Net-SNMP 套件的一部分。

# INSTALL

```apt: sudo apt install snmp```

```apk: sudo apk add net-snmp-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snmpget](/man/snmpget)(1), [netstat](/man/netstat)(1)
