# TAGLINE

Valkey 数据存储的命令行客户端

# TLDR

**连接服务器**

```valkey-cli```

**连接指定主机**

```valkey-cli -h [host] -p [6379]```

**执行命令**

```valkey-cli SET [key] [value]```

**使用密码连接**

```valkey-cli -a [password]```

**选择数据库**

```valkey-cli -n [2]```

**集群模式**

```valkey-cli -c```

**监控服务器实时延迟**

```valkey-cli --latency```

**扫描匹配模式的键**

```valkey-cli --scan --pattern '[user:*]'```

**找出数据集中较大的键**

```valkey-cli --bigkeys```

# SYNOPSIS

**valkey-cli** [_-h host_] [_-p port_] [_-a password_] [_options_] [_command_]

# PARAMETERS

**-h** _HOST_
> 服务器主机名（默认：127.0.0.1）。

**-p** _PORT_
> 服务器端口（默认：6379）。

**-s** _SOCKET_
> Unix 套接字路径（覆盖主机和端口设置）。

**-u** _URI_
> 连接 URI（valkey://user:password@host:port/db）。

**-a** _PASSWORD_
> 用于身份验证的密码。

**--user** _USERNAME_
> 用于 ACL 身份验证的用户名。

**--askpass**
> 以不回显方式提示输入密码。

**-n** _DB_
> 连接时要选择的数据库编号。

**-c**
> 启用集群模式并自动重定向。

**-r** _N_
> 将命令执行 _N_ 次（用 **-1** 表示无限次）。

**-i** _SECONDS_
> 使用 **-r** 时每次重复之间的间隔时间。

**-x**
> 从标准输入读取最后一个参数。

**--scan**
> 使用 SCAN 迭代键。

**--pattern** _PATTERN_
> 按模式过滤键（配合 --scan/--bigkeys/--hotkeys 使用）。

**--bigkeys**
> 对键空间采样并报告最大的键。

**--memkeys**
> 对键空间采样并报告占用内存最多的键。

**--hotkeys**
> 报告访问最频繁的键（需要 LFU 淘汰策略）。

**--latency**
> 实时测量服务器延迟。

**--stat**
> 显示持续的服务器统计信息。

**--rdb** _FILE_
> 将远程 RDB 转储传输到本地文件。

**--pipe**
> 从标准输入传输原始 RESP 协议数据以进行批量导入。

**--tls**
> 启用 TLS 加密连接。

**--cluster** _CMD_
> 运行集群管理子命令（create、check、reshard、rebalance、add-node、del-node）。

# DESCRIPTION

**valkey-cli** 是与 Valkey 服务器交互的命令行界面。它既提供用于探索数据的交互式 REPL 模式，也提供适用于脚本化和自动化的非交互模式。该客户端使用与 Redis 相同的协议，因此兼容现有的 Redis 工作流。

命令可以直接在命令行上传入，也可以从文件或其他程序通过管道传入。客户端支持连接分片部署的集群模式，还支持数据库选择、身份验证和 TLS 连接。

# CAVEATS

Redis 的分支版本。与 redis-cli 兼容。服务器必须处于运行状态。

# HISTORY

**valkey-cli** 是 **Valkey** 的 CLI 工具，Valkey 是由 Linux 基金会维护的 Redis 分支项目。

# INSTALL

```apt: sudo apt install valkey-tools```

```apk: sudo apk add valkey-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[redis-cli](/man/redis-cli)(1), [valkey-server](/man/valkey-server)(1)
