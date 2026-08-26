# TAGLINE

向 Berkeley DB 数据库导入数据的工具

# TLDR

**将数据载入 Berkeley DB 数据库**

```db_load -T -t hash [database.db] < [data.txt]```

**载入键值对**（每行一条：键、值、键、值……）

```db_load -T -t btree [database.db] < [pairs.txt]```

**以指定页大小创建数据库**

```db_load -T -t btree -c pagesize=[4096] [database.db] < [data.txt]```

**以支持重复键的方式载入**

```db_load -T -t btree -c duplicates=1 [database.db] < [data.txt]```

**从转储文件格式载入**

```db_load [database.db] < [dump.txt]```

# SYNOPSIS

**db_load** [_options_] _database.db_

# PARAMETERS

**-T**
> 输入为纯文本（键/值对逐行交替）。

**-t** _type_
> 数据库类型：btree、hash、queue、recno。

**-c** _name=value_
> 设置数据库配置选项。

**-f** _file_
> 输入文件（默认：stdin）。

**-n**
> 不覆盖已存在的数据库。

**-r** _lsn_
> 重置日志序列号。

**-V**
> 显示版本。

# INPUT FORMAT

**带 -T 标志**（纯文本）：
```
key1
value1
key2
value2
```

**不带 -T**（db_dump 格式）：
```
VERSION=3
format=bytevalue
type=btree
HEADER=END
 6b657931
 76616c756531
DATA=END
```

# DESCRIPTION

**db_load** 将数据导入 Berkeley DB 数据库。它从标准输入或文件读取键值对，创建或填充 BDB 数据库文件。

该工具支持多种数据库类型：**btree** 用于有序访问，**hash** 用于快速查找，**queue** 用于 FIFO 操作，**recno** 用于按记录号访问。配置选项可控制页大小、缓存和重复键处理。

输入可以是纯文本（配合 **-T**），其中交替的行分别是键和值；也可以是 **db_dump** 生成的二进制安全格式。转储格式能处理二进制数据并保留数据库元数据。

# CAVEATS

Berkeley DB 正在被更新的方案（SQLite、LMDB）逐步取代。6.x 版本许可证变更为 AGPL，影响商业使用。大量导入可能需要调整缓存大小。若不是新建数据库，数据库类型必须与现有数据库一致。

# HISTORY

Berkeley DB 由 **UC Berkeley** 自 **1991 年**起开发，用于取代更早的 Unix dbm 库。db_load 工具自早期版本起就是 BDB 的一部分。Oracle 于 **2006 年**收购了 Sleepycat Software（BDB 的商业维护方）。尽管已是遗留技术，BDB 仍被许多系统使用，包括 OpenLDAP 和旧版本的软件包管理器。

# INSTALL

```apk: sudo apk add db-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sqlite3](/man/sqlite3)(1)
