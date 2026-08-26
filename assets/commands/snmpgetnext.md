# TAGLINE

按顺序检索下一个 SNMP OID 值

# TLDR

**获取下一个 OID 值**

```snmpgetnext -v [2c] -c [public] [host] [OID]```

**用 SNMPv3 获取下一个值**

```snmpgetnext -v [3] -u [user] -l authPriv -a SHA -A [authpass] -x AES -X [privpass] [host] [OID]```

# SYNOPSIS

**snmpgetnext** [_options_] _agent_ _oid_...

# PARAMETERS

**-v** _version_
> SNMP 版本（1、2c、3）。

**-c** _community_
> 社区字符串。

**-u** _user_
> SNMPv3 用户名。

**-l** _level_
> 安全级别（noAuthNoPriv、authNoPriv、authPriv）。

**-O** _opts_
> 输出格式选项。

# DESCRIPTION

**snmpgetnext** 从 SNMP 代理检索字典序上的下一个 OID 值。用于遍历 MIB 树并发现可用的 OID。Net-SNMP 套件的一部分。

# INSTALL

```apt: sudo apt install snmp```

```apk: sudo apk add net-snmp-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snmpget](/man/snmpget)(1), [snmpwalk](/man/snmpwalk)(1), [snmpbulkget](/man/snmpbulkget)(1)
