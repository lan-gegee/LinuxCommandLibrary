# TAGLINE

在 SNMP OID 格式之间转换

# TLDR

将**数字 OID 转换**为文本名称

```snmptranslate [.1.3.6.1.2.1.1.1.0]```

将**文本 OID 转换**为数字形式

```snmptranslate -On [sysDescr.0]```

**显示完整 OID 详情**（含描述）

```snmptranslate -Td [sysDescr]```

从某个节点开始**显示 MIB 树**

```snmptranslate -Tp [system]```

按正则表达式模式**搜索 OID**

```snmptranslate -TB [pattern]```

显示已加载 MIB 中的**所有 OID**

```snmptranslate -Ta```

**加载额外的 MIB** 进行转换

```snmptranslate -m [+MY-MIB] [OID]```

# SYNOPSIS

**snmptranslate** [_options_] _OID_

# PARAMETERS

**-On**
> 仅以数字形式打印 OID。

**-Of**
> 打印完整的 OID 路径。

**-OS**
> 只打印 OID 的最后一个符号元素。

**-Td**
> 打印详细信息，包括描述、类型和访问权限。

**-Tp**
> 打印以该 OID 为根的子树。

**-Ta**
> 打印已加载 MIB 中的所有 OID。

**-TB** _pattern_
> 搜索匹配正则表达式模式的 OID。

**-m** _MIBLIST_
> 要加载的 MIB 模块列表，以冒号分隔。使用 **+MIB** 表示追加到默认值之后。

**-M** _PATHLIST_
> 搜索 MIB 的目录列表，以冒号分隔。

**-IR**
> 使用随机访问查找以获得更好的性能。

**-h**
> 显示帮助信息。

# DESCRIPTION

**snmptranslate** 是一个在 SNMP 对象标识符（OID）的数字形式和文本形式之间转换的工具。它使用 MIB（管理信息库）文件执行转换，并可显示 OID 的详细信息，包括描述、语法和访问权限。

该工具适合用来理解 MIB 结构、浏览可用的 OID，以及在人类可读名称与 SNMP 操作中使用的数字点分表示法之间转换。它不与任何 SNMP 代理通信；所有转换都使用加载的 MIB 文件在本地完成。

MIB 定义了 OID 的结构和含义。常见的 MIB 如 SNMPv2-MIB 和 IF-MIB 默认会加载，但厂商专用的 MIB 可能需要显式加载。

# CAVEATS

转换的准确性取决于是否安装并加载了正确的 MIB。厂商专用 OID 需要相应的厂商 MIB。**-m** 选项带 **+** 前缀时追加到默认 MIB 之后；不带 **+** 时则会替换默认 MIB。MIB 文件应放在标准目录中，或通过 **-M** 指定。

# HISTORY

**snmptranslate** 是 **Net-SNMP** 项目的一部分，这是一个开源的 SNMP 工具和库套件。它无需网络通信即可处理 OID，非常适合 MIB 探索、文档编写和脚本处理。自早期版本起它就是 Net-SNMP 的组成部分。

# INSTALL

```apt: sudo apt install snmp```

```apk: sudo apk add net-snmp-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snmpget](/man/snmpget)(1), [snmpset](/man/snmpset)(1), [snmpwalk](/man/snmpwalk)(1)
