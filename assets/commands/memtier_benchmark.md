# TAGLINE

面向 Redis 和 Memcached 的负载生成与基准测试工具

# TLDR

**基准测试 Redis**

```memtier_benchmark -s [localhost] -p [6379]```

**指定客户端数和线程数进行基准测试**

```memtier_benchmark -s [host] -c [50] -t [4]```

**自定义键模式**

```memtier_benchmark -s [host] --key-pattern=S:S```

**设置数据大小**

```memtier_benchmark -s [host] -d [128]```

**运行指定时长**

```memtier_benchmark -s [host] --test-time=[60]```

**基准测试 memcached**

```memtier_benchmark -s [host] -p [11211] --protocol=memcache_text```

# SYNOPSIS

**memtier_benchmark** [_options_]

# PARAMETERS

**-s** _host_
> 服务器主机名。

**-p** _port_
> 服务器端口。

**-c** _clients_
> 每线程客户端数。

**-t** _threads_
> 线程数。

**-d** _size_
> 数据大小（字节）。

**--protocol** _proto_
> redis、memcache_text、memcache_binary。

**--ratio** _get:set_
> GET:SET 比例。

**--test-time** _secs_
> 测试时长。

**--key-pattern** _pattern_
> 键访问模式。

# DESCRIPTION

**memtier_benchmark** 是面向 Redis 和 Memcached 的负载生成与基准测试工具。它测量各种负载条件下的吞吐量和延迟。

该工具支持多种协议，并提供包括百分位延迟在内的详细统计信息。

# KEY PATTERNS

```
S:S - Sequential
R:R - Random
G:G - Gaussian
```

# CAVEATS

仅做性能测试；不验证数据完整性。结果受网络影响。高吞吐量测试请使用多个实例。

# HISTORY

memtier_benchmark 由 **Redis Labs**（现为 Redis Inc.）开发，是针对内存数据存储的综合基准测试工具。

# INSTALL

```brew: brew install memtier_benchmark```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[redis-benchmark](/man/redis-benchmark)(1), [redis-cli](/man/redis-cli)(1), [memcached](/man/memcached)(1)
