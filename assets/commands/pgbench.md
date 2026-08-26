# TAGLINE

对 PostgreSQL 数据库运行类 TPC-B 基准测试

# TLDR

**初始化基准测试数据库**

```pgbench -i [database]```

**运行基准测试**

```pgbench -c [10] -t [100] [database]```

**按持续时间运行基准测试**

```pgbench -c [10] -T [60] [database]```

**使用自定义脚本运行**

```pgbench -f [script.sql] [database]```

**运行只读基准测试**

```pgbench -S -c [10] -T [30] [database]```

**以多线程运行**

```pgbench -c [20] -j [4] -T [60] [database]```

**以指定规模因子初始化**

```pgbench -i -s [10] [database]```

# SYNOPSIS

**pgbench** [_-i_] [_-c clients_] [_-t transactions_] [_-T seconds_] [_-f script_] [_options_] _database_

# PARAMETERS

**-i**
> 初始化基准测试表。

**-s** _SCALE_
> 初始化时的规模因子。

**-c** _CLIENTS_
> 并发客户端数量。

**-t** _TRANSACTIONS_
> 每个客户端的事务数（默认：10）。

**-T** _SECONDS_
> 持续时间（秒）。

**-j** _THREADS_
> 线程数量。

**-f** _FILE_
> 自定义 SQL 脚本。

**-S**
> 仅查询（只读）。是 -b select-only 的简写。

**-N**
> 跳过对 pgbench_tellers 和 branches 的更新。是 -b simple-update 的简写。

**-b** _scriptname[@weight]_
> 内置脚本：tpcb-like、simple-update、select-only。可用权重（可选）控制混合比例。

**-C**
> 为每个事务新建一个连接（用于测量连接开销）。

**-M** _protocol_
> 查询协议：simple、extended 或 prepared（默认：simple）。

**-R** _rate_
> 目标事务速率（TPS）。通过加入休眠来维持该速率。

**-L** _limit_
> 将超过 _limit_ 毫秒的事务报告为滞后。

**-r**
> 报告每条语句的延迟。

**-P** _SECONDS_
> 每 N 秒显示一次进度。

**-l**
> 将事务记录到文件。

**-n**
> 运行测试前跳过 vacuum。

**-I** _steps_
> 要执行的初始化步骤（默认：dtgvp）。字符含义：d=drop，t=tables，g=generate，v=vacuum，p=主键，f=外键。

**-h** _HOST_
> 数据库主机。

**-p** _PORT_
> 数据库端口。

**-U** _USER_
> 数据库用户。

# DESCRIPTION

**pgbench** 对 PostgreSQL 数据库运行类 TPC-B 基准测试，测量并发负载下的事务吞吐量。

初始化（-i）会创建基准测试表。规模因子决定数据量倍数：规模 10 会创建 100 万行。更大的规模可以测试不同的负载特征。

该基准测试模拟银行业务事务：对 accounts、tellers 和 branches 表的更新。它在并发客户端负载下测量每秒事务数（TPS）。

客户端数量影响并发程度。更多客户端可以测试并行执行和锁行为。线程数应与可用的 CPU 核心数匹配。

自定义脚本可用于测试特定负载。它们可以使用变量、条件判断和多个语句来模拟应用的行为。

进度输出会实时显示 TPS 和延迟。最终报告包括平均 TPS、延迟分布以及出现的错误。

# CAVEATS

并非完整的 TPC-B 实现。结果取决于硬件、配置和工作负载。请使用合适的规模进行初始化，测试才有意义。

# HISTORY

**pgbench** 自 **PostgreSQL** 7.0 版本起就是其组成部分，最初由 **Tatsuo Ishii** 编写。它为测试 PostgreSQL 性能和比较配置提供了标准方式。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[psql](/man/psql)(1), [pg_dump](/man/pg_dump)(1), [postgres](/man/postgres)(1)
