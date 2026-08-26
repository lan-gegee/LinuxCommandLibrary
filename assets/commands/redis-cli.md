# TAGLINE

Redis 服务器的命令行界面

# TLDR

**连接本地 Redis 服务器**

```redis-cli```

**连接远程 Redis 服务器**

```redis-cli -h [hostname] -p [port]```

**使用密码认证连接**

```redis-cli -a [password]```

**以 TLS 加密**并认证的方式连接

```redis-cli --tls -h [hostname] -p [port] -a [password]```

**执行单条命令**

```redis-cli [command] [arguments]```

**获取键值**

```redis-cli GET [key]```

**设置键值**

```redis-cli SET [key] "[value]"```

**列出匹配模式的所有键**

```redis-cli KEYS "*"```

**实时监视所有命令**

```redis-cli MONITOR```

**获取服务器统计信息**

```redis-cli INFO```

# SYNOPSIS

**redis-cli** [**-h** _host_] [**-p** _port_] [**-a** _password_] [**-n** _db_] [_command_ [_args_...]]

# PARAMETERS

**-h** _host_
> 服务器主机名（默认：127.0.0.1）

**-p** _port_
> 服务器端口（默认：6379）

**-a** _password_
> AUTH 命令使用的密码

**-n** _db_
> 要选择的数据库编号

**-u** _uri_
> 使用 Redis URI 连接（redis://...）

**-r** _count_
> 将命令重复执行 count 次

**-i** _interval_
> 重复执行之间的间隔（秒）

**--scan**
> 使用 SCAN 而不是 KEYS 来列出键

**--pipe**
> 从标准输入传输原始 Redis 协议

**--rdb** _file_
> 将 RDB 转储从服务器传输到文件

**-c**
> 启用集群模式（跟随 -ASK 和 -MOVED 重定向）

**-s** _socket_
> 服务器套接字路径（覆盖主机名和端口）

**--tls**
> 建立安全的 TLS 连接

**--user** _username_
> AUTH 使用的 ACL 用户名

**--pass** _password_
> **-a** 的别名

**--csv**
> 以 CSV 格式输出

**--bigkeys**
> 采样键，寻找元素数量多的键

**--memkeys**
> 采样键，寻找内存占用最大的键

**--cluster** _command_
> 执行集群命令

**--latency**
> 持续监视延迟

**--stat**
> 打印滚动统计信息

# DESCRIPTION

**redis-cli** 是 Redis 的命令行界面。Redis 是一个内存数据结构存储，可用作数据库、缓存和消息代理。它提供对 Redis 服务器的交互式和脚本化访问。

在交互模式下（未指定命令），redis-cli 会显示提示符供输入命令。命令遵循 Redis 协议：命令名后跟参数，响应立即显示。

常见操作包括键值存储（GET、SET、DEL）、列表（LPUSH、RPOP）、集合（SADD、SMEMBERS）、哈希（HSET、HGET）以及发布/订阅消息（PUBLISH、SUBSCRIBE）。

该工具支持集群模式、哨兵连接以及各种用于 Redis 管理的调试和监控功能。

# COMMON COMMANDS

**SET** key value: 存储一个值
**GET** key: 取回一个值
**DEL** key: 删除一个键
**KEYS** pattern: 查找匹配模式的键
**EXPIRE** key seconds: 设置键的过期时间
**TTL** key: 获取剩余生存时间
**FLUSHDB**: 删除当前数据库中的所有键
**INFO**: 服务器信息和统计数据
**PING**: 测试连接

# CAVEATS

在数据量大的生产服务器上使用 **KEYS \*** 可能阻塞服务器。生产环境中请改用 **SCAN** 迭代键。

通过 **-a** 传入的密码会出现在进程列表和 shell 历史记录中。敏感环境请使用 **REDISCLI_AUTH** 环境变量或交互式 AUTH。

Redis 数据库默认编号为 0-15。使用 **-n** 选择数据库，或在交互模式中使用 **SELECT** 命令。

# INSTALL

```apt: sudo apt install redis-tools```

```apk: sudo apk add valkey-compat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[redis-server](/man/redis-server)(1), [redis-benchmark](/man/redis-benchmark)(1), [memcached](/man/memcached)(1)
