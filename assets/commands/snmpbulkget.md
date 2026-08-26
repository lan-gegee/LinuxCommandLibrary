# TAGLINE

高效批量获取 SNMP MIB 值

# TLDR

**批量获取 MIB 值**

```snmpbulkget -v [2c] -c [public] [host] [OID]```

**带 non-repeaters 获取**

```snmpbulkget -Cn [1] -v [2c] -c [public] [host] [OID]```

**带最大重复次数获取**

```snmpbulkget -Cr [10] -v [2c] -c [public] [host] [OID]```

# SYNOPSIS

**snmpbulkget** [_options_] _agent_ _oid_...

# PARAMETERS

**-v** _version_
> SNMP 版本（2c、3）。

**-c** _community_
> 社区字符串。

**-Cn** _num_
> Non-repeaters 数量。

**-Cr** _num_
> 最大重复次数。

**-O** _opts_
> 输出选项。

# DESCRIPTION

**snmpbulkget** 使用 SNMPv2c 中引入的 GETBULK 操作，在单个请求中从 SNMP 代理检索多个 MIB 值。这比发出多个单独的 GET 或 GETNEXT 请求效率显著更高，尤其是在检索大表或连续 OID 区间时。

**-Cn**（non-repeaters）参数指定前多少个 OID 用简单的 GETNEXT 检索，而 **-Cr**（max-repetitions）控制其余 OID 各获取多少个连续值。这种组合允许在单个请求中混合检索标量和表数据。

该工具是 **Net-SNMP** 套件的一部分，要求 SNMPv2c 或 SNMPv3，因为 GETBULK 操作在 SNMPv1 中不可用。

# INSTALL

```apt: sudo apt install snmp```

```apk: sudo apk add net-snmp-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snmpget](/man/snmpget)(1), [snmpgetnext](/man/snmpgetnext)(1), [snmpwalk](/man/snmpwalk)(1)
