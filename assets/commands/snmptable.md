# TAGLINE

以表格形式显示 SNMP MIB 数据

# TLDR

**显示 SNMP 表**

```snmptable -v [2c] -c [public] [host] [TABLE_OID]```

**显示带列标题的表**

```snmptable -v [2c] -c [public] -Cb [host] [TABLE_OID]```

**显示接口表**

```snmptable -v [2c] -c [public] [host] ifTable```

# SYNOPSIS

**snmptable** [_options_] _agent_ _table_oid_

# PARAMETERS

**-v** _version_
> SNMP 版本（1、2c、3）。

**-c** _community_
> 社区字符串。

**-Cb**
> 简短的列名。

**-Cf** _sep_
> 字段分隔符。

**-Cw** _width_
> 列宽。

# DESCRIPTION

**snmptable** 以表格格式显示 SNMP 表数据。它检索并格式化 MIB 表，便于阅读。Net-SNMP 网络管理套件的一部分。

# INSTALL

```apt: sudo apt install snmp```

```apk: sudo apk add net-snmp-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snmpwalk](/man/snmpwalk)(1), [snmpget](/man/snmpget)(1)
