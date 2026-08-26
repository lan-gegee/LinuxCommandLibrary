# TAGLINE

etcd 键值存储的命令行客户端

# TLDR

**设置键**

```etcdctl put [mykey] "[myvalue]"```

**获取键**

```etcdctl get [mykey]```

**获取某前缀下的所有键**

```etcdctl get --prefix [/myapp/]```

**删除键**

```etcdctl del [mykey]```

**监视变更**

```etcdctl watch [mykey]```

**列出集群成员**

```etcdctl member list```

**检查集群健康状况**

```etcdctl endpoint health```

# SYNOPSIS

**etcdctl** [_global-options_] _command_ [_args_]

# PARAMETERS

**put** _key_ _value_
> 将键设置为指定的值。

**get** _key_
> 获取键的值。

**del** _key_
> 删除键。

**watch** _key_
> 监视键的变更。

**--prefix**
> 将操作应用于具有指定前缀的键。

**member list**
> 列出集群成员。

**member add** _name_ _urls_
> 添加集群成员。

**member remove** _id_
> 移除集群成员。

**endpoint health**
> 检查端点健康状况。

**snapshot save** _file_
> 保存集群快照。

**snapshot restore** _file_
> 从快照恢复。

**--endpoints** _urls_
> etcd 端点。

**--cacert** _file_
> CA 证书。

**--cert** _file_
> 客户端证书。

**--key** _file_
> 客户端密钥。

# DESCRIPTION

**etcdctl** 是 etcd 的命令行客户端。etcd 是一种分布式键值存储，用于共享配置和服务发现，也是 Kubernetes 存储集群状态的核心组件。

etcd 通过 Raft 共识算法提供强一致性。etcdctl 用于管理键、监视变更以及管理集群。

# CAVEATS

默认使用 API 版本 3（需设置 ETCDCTL_API=3）。可能需要进行身份验证。集群操作需要仔细规划。应定期制作快照。过大的值会影响性能。

# HISTORY

etcd 由 **CoreOS** 于 **2013 年**创建，最初是其 Container Linux 的分布式配置存储。它后来成为 CNCF 项目，现由 etcd 社区维护。Kubernetes 从一开始就采用 etcd 作为其底层存储。

# INSTALL

```apt: sudo apt install etcd-client```

```apk: sudo apk add etcd-ctl```

```zypper: sudo zypper install etcdctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [consul](/man/consul)(1)
