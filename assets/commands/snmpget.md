# TAGLINE

从代理检索 SNMP 对象值

# TLDR

使用 SNMPv2c **获取单个 OID 值**

```snmpget -v 2c -c [community] [host] [OID]```

从设备**获取系统描述**

```snmpget -v 2c -c [public] [192.168.1.1] sysDescr.0```

在单个请求中**获取多个 OID 值**

```snmpget -v 2c -c [community] [host] [OID1] [OID2] [OID3]```

使用带身份验证的 **SNMPv3 查询**

```snmpget -v 3 -u [username] -l authNoPriv -a MD5 -A [password] [host] [OID]```

使用带身份验证和加密的 **SNMPv3 查询**

```snmpget -v 3 -u [username] -l authPriv -a SHA -A [authpass] -x AES -X [privpass] [host] [OID]```

**设置超时和重试次数**

```snmpget -v 2c -c [community] -t [5] -r [3] [host] [OID]```

# SYNOPSIS

**snmpget** [_options_] _agent_ _OID_ [_OID_...]

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
> 重传前的超时时间，单位秒。默认：1。

**-r** _retries_
> 放弃前的重试次数。默认：5。

**-p** _port_
> SNMP 代理的 UDP 端口。默认：161。

**-m** _MIBLIST_
> 要加载的 MIB 模块列表，以冒号分隔。使用 **ALL** 表示所有 MIB。

**-M** _PATHLIST_
> 搜索 MIB 的目录列表，以冒号分隔。

**-O** _options_
> 输出格式选项（例如 **n** 表示数字 OID，**q** 表示快速打印）。

# DESCRIPTION

**snmpget** 使用 SNMP GET 请求与网络实体通信，检索特定的管理信息。它查询一个或多个对象标识符（OID），并从 SNMP 代理返回其当前值。

该工具支持 SNMPv1、SNMPv2c 和 SNMPv3。SNMPv1 和 v2c 使用社区字符串进行简单身份验证，而 SNMPv3 提供健壮的安全性，支持身份验证（MD5/SHA）和加密（DES/AES）选项。

OID 可以用数字形式指定（如 **.1.3.6.1.2.1.1.1.0**），也可以使用 MIB 名称（如 **sysDescr.0**）。标量值需要 **.0** 索引后缀，否则 snmpget 会返回错误。

# CONFIGURATION

**/etc/snmp/snmp.conf**
> 系统级 SNMP 客户端配置，包括默认版本、社区字符串和 MIB 搜索路径。

**~/.snmp/snmp.conf**
> 每用户 SNMP 客户端配置，覆盖系统默认值。

**MIBS**
> 指定要加载哪些 MIB 模块的环境变量（冒号分隔列表，或 ALL）。

**MIBDIRS**
> 指定搜索 MIB 文件目录的环境变量。

# CAVEATS

标量 OID 需要 **.0** 索引后缀；遗漏它是常见错误。SNMPv1/v2c 社区字符串以明文传输，只应在受信任的网络中使用。在要求安全的环境中，请使用带身份验证和加密的 SNMPv3。必须安装 MIB 文件才能使用符号 OID 名称。

# HISTORY

**snmpget** 是 **Net-SNMP** 项目的一部分，这是一个开源的 SNMP 工具和库套件。Net-SNMP 由 20 世纪 90 年代的 CMU SNMP 实现演化而来，其后是 UCD-SNMP 项目。该项目全面支持 SNMP v1、v2c 和 v3，广泛用于类 Unix 系统上的网络监控与管理。

# INSTALL

```apt: sudo apt install snmp```

```apk: sudo apk add net-snmp-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snmpwalk](/man/snmpwalk)(1), [snmpset](/man/snmpset)(1), [snmptranslate](/man/snmptranslate)(1)
