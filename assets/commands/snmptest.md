# TAGLINE

交互式 SNMP 请求测试工具

# TLDR

**启动交互式 SNMP 会话**

```snmptest -v [2c] -c [public] [host]```

**用 SNMPv3 测试**

```snmptest -v [3] -u [user] -l authPriv -a SHA -A [authpass] [host]```

# SYNOPSIS

**snmptest** [_options_] _agent_

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

**snmptest** 提供用于测试和调试的交互式 SNMP 会话，可以交互式发送任意 SNMP 请求。Net-SNMP 开发与故障排查套件的一部分。

# INSTALL

```apt: sudo apt install snmp```

```apk: sudo apk add net-snmp-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snmpget](/man/snmpget)(1), [snmpwalk](/man/snmpwalk)(1)
