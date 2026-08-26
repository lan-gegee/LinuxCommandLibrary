# TAGLINE

遍历 SNMP MIB 树并获取所有值

# TLDR

**遍历整个 MIB**

```snmpwalk -v2c -c [community] [host]```

**遍历指定 OID**

```snmpwalk -v2c -c [public] [host] [1.3.6.1.2.1.1]```

带身份验证和加密的 **SNMPv3**

```snmpwalk -v3 -u [user] -l authPriv -a SHA -A [authpass] -x AES -X [privpass] [host]```

**显示数字 OID**

```snmpwalk -On -v2c -c [community] [host]```

**遍历 system 子树**

```snmpwalk -v2c -c [public] [host] system```

**仅输出值**

```snmpwalk -Oqv -v2c -c [public] [host] [oid]```

# SYNOPSIS

**snmpwalk** [_-v version_] [_-c community_] [_options_] _host_ [_oid_]

# PARAMETERS

**-v** _VERSION_
> SNMP 版本（1、2c、3）。

**-c** _COMMUNITY_
> 社区字符串。

**-u** _USER_
> SNMPv3 用户名。

**-l** _LEVEL_
> 安全级别。

**-A** _PASS_
> 身份验证口令。

**-X** _PASS_
> 隐私口令。

**-On**
> 以数字形式显示 OID。

**-Oq**
> 快速打印（去除类型信息）。

**-Ov**
> 仅显示值，不带 OID 前缀。

**-Cr**
> 不检查返回的 OID 是否递增（针对有缺陷的代理）。

**-Of**
> 显示完整 OID（不缩写）。

**-Cc**
> 不检查返回的 OID 是否属于正确的子树。

**-a** _PROTOCOL_
> SNMPv3 身份验证协议（MD5、SHA、SHA-224、SHA-256、SHA-384、SHA-512）。

**-x** _PROTOCOL_
> SNMPv3 隐私协议（DES、AES、AES-192、AES-256）。

**-t** _TIMEOUT_
> 每个请求的超时时间，单位秒（默认 1）。

**-r** _RETRIES_
> 重试次数（默认 5）。

# DESCRIPTION

**snmpwalk** 通过连续发出 GETNEXT 请求，从 SNMP 代理检索管理值的一个子树。它从指定的 OID 开始遍历 MIB 树并显示所有值，直到到达子树末尾，从而全面呈现设备的管理数据。

该工具支持 SNMPv1、v2c 和 v3。对于 v1 和 v2c，使用社区字符串进行身份验证，"public" 是常见的只读默认值。SNMPv3 通过基于用户的身份验证（MD5/SHA）和加密（DES/AES）提供健壮的安全性。

起始 OID 决定了遍历的范围。从根开始遍历会获取所有可用数据，而指定 **system** 或 **interfaces** 等子树则会限制结果范围。**-On**（数字 OID）和 **-Oq**（快速打印）等输出格式选项让输出更易于脚本解析。

# CAVEATS

社区字符串是明文的。出于安全考虑推荐 v3。大范围遍历可能较慢。

# HISTORY

**snmpwalk** 是 **Net-SNMP**（标准开源 SNMP 实现）的一部分。它是网络设备监控和发现的重要工具。

# INSTALL

```apt: sudo apt install snmp```

```apk: sudo apk add net-snmp-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snmpget](/man/snmpget)(1), [snmpset](/man/snmpset)(1), [snmptranslate](/man/snmptranslate)(1)
