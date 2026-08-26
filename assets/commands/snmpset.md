# TAGLINE

修改代理上的 SNMP 对象值

# TLDR

使用 SNMPv2c **设置整数值**

```snmpset -v 2c -c [community] [host] [OID] i [value]```

**设置字符串值**

```snmpset -v 2c -c [community] [host] [OID] s "[string_value]"```

在单个请求中**设置多个值**

```snmpset -v 2c -c [community] [host] [OID1] i [value1] [OID2] s "[value2]"```

使用带身份验证的 **SNMPv3 设置**

```snmpset -v 3 -u [username] -l authNoPriv -a MD5 -A [password] [host] [OID] i [value]```

使用带身份验证和加密的 **SNMPv3 设置**

```snmpset -v 3 -u [username] -l authPriv -a SHA -A [authpass] -x AES -X [privpass] [host] [OID] i [value]```

# SYNOPSIS

**snmpset** [_options_] _agent_ _OID_ _type_ _value_ [_OID_ _type_ _value_...]

# PARAMETERS

**-v** _version_
> SNMP 版本：**1**、**2c** 或 **3**。

**-c** _community_
> 用于 SNMPv1/v2c 身份验证的社区字符串。

**-u** _username_
> SNMPv3 安全名（用户名）。

**-l** _level_
> SNMPv3 安全级别：**noAuthNoPriv**、**authNoPriv** 或 **authPriv**。

**-a** _protocol_
> SNMPv3 身份验证协议：**MD5** 或 **SHA**。

**-A** _passphrase_
> SNMPv3 身份验证口令。

**-x** _protocol_
> SNMPv3 隐私协议：**DES** 或 **AES**。

**-X** _passphrase_
> SNMPv3 隐私口令。

**-t** _timeout_
> 重传前的超时时间，单位秒。

**-r** _retries_
> 放弃前的重试次数。

# VALUE TYPES

**i**
> 整数

**u**
> 无符号整数

**s**
> 字符串

**x**
> 十六进制字符串

**d**
> 十进制字符串

**n**
> Null

**o**
> 对象标识符

**t**
> Timeticks

**a**
> IP 地址

**b**
> 位串

# DESCRIPTION

**snmpset** 使用 SNMP SET 请求与网络实体通信，修改设备上的管理信息。每个要设置的变量需要三个参数：OID、数据类型和值。

该工具支持 SNMPv1、SNMPv2c 和 SNMPv3。写入访问通常需要与只读访问不同的社区字符串，并且许多设备会限制可修改的 OID。出于安全考虑，建议使用带身份验证和加密的 SNMPv3。

常见用例包括更改设备配置、启用/禁用接口、修改系统联系人或位置信息，以及触发网络设备上的操作。

# CAVEATS

修改 SNMP 值可能影响设备运行和网络稳定性。使用 snmpset 前请确保已获得适当授权并了解其影响。写入社区字符串应严格保密。许多 OID 是只读的，无法修改。类型指定不正确会导致请求失败。

# HISTORY

**snmpset** 是 **Net-SNMP** 项目的一部分，这是一个开源的 SNMP 工具和库套件。Net-SNMP 由 CMU SNMP 实现演化而来，其后是 UCD-SNMP。它全面支持 SNMP v1、v2c 和 v3，是大多数类 Unix 系统上的标准 SNMP 工具包。

# INSTALL

```apt: sudo apt install snmp```

```apk: sudo apk add net-snmp-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snmpget](/man/snmpget)(1), [snmpwalk](/man/snmpwalk)(1), [snmptranslate](/man/snmptranslate)(1)
