# TAGLINE

MongoDB 数据库服务器守护进程

# TLDR

**启动 MongoDB 服务器**

```mongod```

**指定数据目录**

```mongod --dbpath [/data/db]```

**指定端口**

```mongod --port [27017]```

**绑定所有网络接口**

```mongod --bind_ip_all```

**启用认证**

```mongod --auth```

**使用配置文件**

```mongod --config [/etc/mongod.conf]```

**以副本集模式运行**

```mongod --replSet [rs0]```

**以守护进程方式运行并记录日志**

```mongod --fork --logpath [/var/log/mongod.log]```

# SYNOPSIS

**mongod** [_options_]

# PARAMETERS

**-f**, **--config** _FILE_
> 配置文件路径。

**--dbpath** _PATH_
> 数据库目录路径（默认：/data/db）。

**--port** _PORT_
> 监听端口号（默认：27017）。

**--bind_ip** _IP_
> 要绑定的 IP 地址列表（逗号分隔）。

**--bind_ip_all**
> 绑定所有 IP 地址。

**--auth**
> 启用认证。

**--replSet** _NAME_
> 副本集名称。

**--logpath** _FILE_
> 日志文件路径。使用 --fork 时必填。

**--fork**
> 将服务器作为后台守护进程运行。

**--keyFile** _FILE_
> 用于副本集/分片集群认证的共享密钥文件路径。隐含启用 --auth。

**--wiredTigerCacheSizeGB** _SIZE_
> WiredTiger 内部缓存的最大容量（GB）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mongod** 是 MongoDB 数据库服务器守护进程。它处理数据请求、管理数据存储，并执行后台管理操作。

该工具是核心数据库进程，支持复制、分片和认证。默认使用 WiredTiger 存储引擎。

# CAVEATS

需要合理的存储配置。资源占用较高。需要谨慎的安全设置。使用 --fork 时必须同时指定 --logpath。

# HISTORY

mongod 是 **MongoDB** 的服务器进程，是 MongoDB 自 2009 年首次发布以来的核心组件。

# SEE ALSO

[mongosh](/man/mongosh)(1), [mongo](/man/mongo)(1), [mongoimport](/man/mongoimport)(1), [mongodump](/man/mongodump)(1), [mongorestore](/man/mongorestore)(1)
