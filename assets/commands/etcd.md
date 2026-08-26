# TAGLINE

基于 Raft 共识的分布式键值存储

# TLDR

**启动 etcd 服务器**

```etcd```

**以自定义数据目录启动**

```etcd --data-dir [/var/lib/etcd]```

**以指定监听地址启动**

```etcd --listen-client-urls [http://localhost:2379]```

**以通告 URL 启动**

```etcd --advertise-client-urls [http://localhost:2379]```

**启动一个集群成员**

```etcd --name [node1] --initial-cluster [node1=http://host1:2380,node2=http://host2:2380]```

**启用 TLS**

```etcd --cert-file [cert.pem] --key-file [key.pem]```

# SYNOPSIS

**etcd** [_options_]

# PARAMETERS

**--name** _name_
> 易读的节点名称。

**--data-dir** _path_
> 数据目录路径。

**--listen-client-urls** _urls_
> 客户端监听 URL。

**--advertise-client-urls** _urls_
> 对外通告的客户端 URL。

**--listen-peer-urls** _urls_
> 节点间监听 URL。

**--initial-cluster** _config_
> 初始集群配置。

**--initial-cluster-state** _state_
> 初始集群状态（new 或 existing）。

**--cert-file** _file_
> TLS 证书文件。

**--key-file** _file_
> TLS 密钥文件。

**--initial-cluster-token** _token_
> 唯一的集群令牌，用于防止跨集群交互。

**--initial-advertise-peer-urls** _urls_
> 向集群其余成员通告的节点间 URL。

**--snapshot-count** _count_
> 触发快照落盘的已提交事务数量（默认 100000）。

**--quota-backend-bytes** _bytes_
> 当后端大小超过给定配额时引发告警（0 表示使用较低的默认空间配额）。

**--max-request-bytes** _bytes_
> 服务器接受的最大客户端请求大小，单位字节（默认 1572864）。

# DESCRIPTION

**etcd** 是一个分布式键值存储，为分布式系统提供可靠、一致的数据存储。它实现了 Raft 共识算法以确保多个节点间的强一致性，适合保存关键的配置数据和服务协调信息。

该服务器是 Kubernetes 集群状态管理的支柱，在云原生架构中被广泛用于配置管理、服务发现和分布式锁。其简洁的 HTTP/gRPC API 和 watch 功能使应用能够实时响应配置变化。

etcd 优先保证一致性和可用性，是存储集群成员信息、功能开关及其他分布式系统元数据的理想选择。

# CONFIGURATION

**/etc/etcd/etcd.conf.yml**
> etcd 服务器设置的主配置文件，涵盖集群拓扑和安全选项。指定时将覆盖所有命令行标志和环境变量。

**ETCD_***
> 每个标志都有对应的环境变量，前缀为大写的 ETCD_ 并采用蛇形命名（例如 --data-dir 对应 ETCD_DATA_DIR）。命令行标志优先于环境变量。

# CAVEATS

生产使用需要细致的集群规划。网络分区会影响可用性。磁盘性能影响延迟。必须定期备份。Raft 共识需要多数派仲裁。

# HISTORY

etcd 由 **CoreOS** 于 **2013 年**创建，后成为云原生计算基金会（CNCF）项目。它已成为 Kubernetes 配置存储的事实标准，在生产云环境中广泛部署。

# INSTALL

```apt: sudo apt install etcd-server```

```pacman: sudo pacman -S etcd```

```apk: sudo apk add etcd```

```zypper: sudo zypper install etcd```

```brew: brew install etcd```

```nix: nix profile install nixpkgs#etcd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[etcdctl](/man/etcdctl)(1), [kubectl](/man/kubectl)(1), [consul](/man/consul)(1)
