# TAGLINE

通过 SNMP 显示远程磁盘使用情况

# TLDR

**通过 SNMP 显示磁盘使用情况**

```snmpdf -v [2c] -c [public] [host]```

**人类可读的输出**

```snmpdf -v [2c] -c [public] -Ch [host]```

**SI 格式的人类可读输出**

```snmpdf -v [2c] -c [public] -CH [host]```

**使用 UCD-SNMP-MIB dskTable 代替默认表**

```snmpdf -v [2c] -c [public] -Cu [host]```

# SYNOPSIS

**snmpdf** [_options_] _agent_

# PARAMETERS

**-v** _version_
> SNMP 版本（1、2c、3）。

**-c** _community_
> 社区字符串。

**-Ch**
> 人类可读的大小（MiB、GiB、TiB）。

**-CH**
> SI 格式的人类可读大小（MB、GB、TB）。

**-Cu**
> 使用 UCD-SNMP-MIB dskTable 而不是默认的 HOST-RESOURCES-MIB hrStorageTable。

# DESCRIPTION

**snmpdf** 通过查询 SNMP 代理显示远程主机的磁盘空间和存储使用情况，功能类似 **df** 命令，但通过网络完成。它读取 Host Resources MIB（hrStorageTable）来报告文件系统大小、已用空间和可用空间。

该工具查询的存储条目包括物理磁盘、RAM、虚拟内存以及 SNMP 代理报告的其他存储类型。**-Ch** 标志以人类可读的大小格式化输出，**-Cu** 强制使用 UCD-SNMP-MIB dskTable 而非默认的 hrStorageTable。

snmpdf 是 **Net-SNMP** 套件的一部分，适合从中心位置监控多台主机的磁盘用量，无需 SSH 访问，也不需要标准 SNMP 守护进程之外的代理。

# CAVEATS

要求远程主机上运行着 SNMP 代理。默认的 hrStorageTable 可能会报告虚拟内存和其他非磁盘存储类型。社区字符串和 SNMP 凭据必须与代理配置匹配。SNMPv3 身份验证会增加复杂度，但出于安全考虑推荐使用。

# HISTORY

**snmpdf** 是 **Net-SNMP** 套件的一部分，该套件由加州大学戴维斯分校最初开发的 UCD-SNMP 项目演化而来。

# INSTALL

```apt: sudo apt install snmp```

```apk: sudo apk add net-snmp-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snmpget](/man/snmpget)(1), [snmpwalk](/man/snmpwalk)(1), [snmpset](/man/snmpset)(1), [df](/man/df)(1)
