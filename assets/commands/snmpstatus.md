# TAGLINE

检索 SNMP 代理的状态摘要

# TLDR

**显示主机状态**

```snmpstatus -v [2c] -c [public] [host]```

**用 SNMPv3 显示状态**

```snmpstatus -v [3] -u [user] -l authPriv -a SHA -A [authpass] [host]```

# SYNOPSIS

**snmpstatus** [_options_] _agent_

# PARAMETERS

**-v** _version_
> SNMP 版本（1、2c、3）。

**-c** _community_
> 社区字符串。

**-u** _user_
> SNMPv3 用户名。

**-l** _level_
> 安全级别。

# DESCRIPTION

**snmpstatus** 从 SNMP 代理检索状态信息。显示系统描述、运行时间和接口摘要。是网络设备的快速健康检查工具。Net-SNMP 套件的一部分。

# INSTALL

```apt: sudo apt install snmp```

```apk: sudo apk add net-snmp-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snmpget](/man/snmpget)(1), [snmpwalk](/man/snmpwalk)(1)
