# TAGLINE

对 Redis 服务器性能进行基准测试

# TLDR

**运行默认基准测试**

```redis-benchmark```

**连接到主机**

```redis-benchmark -h [localhost] -p [6379]```

**设置客户端数量**

```redis-benchmark -c [100]```

**设置请求总数**

```redis-benchmark -n [10000]```

**测试特定命令**

```redis-benchmark -t [get,set]```

**以指定数据大小测试**

```redis-benchmark -d [256]```

**管道化请求**

```redis-benchmark -P [16]```

**安静模式**

```redis-benchmark -q```

# SYNOPSIS

**redis-benchmark** [_-h host_] [_-p port_] [_-c clients_] [_-n requests_] [_options_]

# PARAMETERS

**-h** _HOST_
> 服务器主机名。

**-p** _PORT_
> 服务器端口。

**-c** _N_
> 并发客户端数。

**-n** _N_
> 总请求数。

**-t** _TESTS_
> 要测试的命令。

**-d** _SIZE_
> 数据大小（字节）。

**-P** _N_
> 管道化 N 个请求。

**-q**
> 安静模式，仅显示每秒查询数。

**-a** _PASSWORD_
> 认证密码。

**--csv**
> CSV 输出。

# DESCRIPTION

**redis-benchmark** 通过模拟多个客户端并发执行各种命令来测量 Redis 服务器的性能。默认情况下，它测试一组标准操作（包括 SET、GET、INCR、LPUSH、LPOP 等），并报告每种命令类型的每秒请求数。

**-c** 标志控制并发客户端连接数，**-n** 设置总请求数。使用 **-P** 进行管道化可将多个请求合并到每个往返中，从而测试与网络延迟无关的原始吞吐量。**-d** 标志调整数据载荷大小以对不同的工作负载模式进行基准测试，**-t** 将测试限制为特定命令。

# CAVEATS

结果因硬件和网络而异。本地测试可消除网络开销。生产环境的访问模式有所不同。

# HISTORY

**redis-benchmark** 随 **Redis** 发布。Redis 由 **Salvatore Sanfilippo** 于 **2009 年**创建。该工具为 Redis 部署提供标准化的性能测试。

# INSTALL

```apt: sudo apt install redis-tools```

```apk: sudo apk add redict-compat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[redis-cli](/man/redis-cli)(1), [redis-server](/man/redis-server)(1), [memtier_benchmark](/man/memtier_benchmark)(1)
