# TAGLINE

分布式键值存储管理

# TLDR

**获取键的值**

```consul kv get [key]```

**写入值**

```consul kv put [key] [value]```

**删除一个键**

```consul kv delete [key]```

按前缀**列出键**

```consul kv get -keys [prefix/]```

**递归获取**

```consul kv get -recurse [prefix/]```

**导出所有键**

```consul kv export [prefix/] > [backup.json]```

**导入键**

```consul kv import @[backup.json]```

# SYNOPSIS

**consul** **kv** _subcommand_ [_options_]

# SUBCOMMANDS

**get**
> 从 KV 存储中检索值。

**put**
> 在 KV 存储中设置值。

**delete**
> 从 KV 存储中移除键。

**export**
> 以 JSON 格式导出 KV 对。

**import**
> 从 JSON 导入 KV 对。

# PARAMETERS

**-keys**
> 只列出键，不列出值。

**-recurse**
> 检索具有该前缀的所有键。

**-base64**
> 以 base64 编码/解码值。

**-detailed**
> 提供关于该键的额外元数据。

**-separator** _STRING_
> 键列表使用的分隔符字符串（默认："/"）。

**-cas**
> 执行 Check-And-Set 操作（需要 -modify-index）。

**-modify-index** _N_
> **-cas** 用于原子更新的 ModifyIndex。

**-flags** _N_
> 与该 KV 对关联的无符号整数标志值。

**-acquire**
> 获取键上的锁（需要 **-session**）。

**-release**
> 释放键上的锁（需要 **-session**）。

**-session** _ID_
> 配合 **-acquire**/**-release** 使用的会话标识符。

**-token** _TOKEN_
> 用于 API 请求的 ACL 令牌。

**-datacenter** _DC_
> 请求的目标数据中心。

**-http-addr** _ADDRESS_
> Consul 代理的地址（默认："http://127.0.0.1:8500"）。

# DESCRIPTION

**consul kv** 管理 Consul 的键值存储——一种用于配置和服务发现的分布式数据存储。值可以是字符串、JSON 或二进制数据。

KV 存储是 HashiCorp Consul 的一部分，常用于动态配置、功能开关和服务协调。键以 `/` 为分隔符按层级组织，类似文件系统的路径结构。每个值最大可达 512 KB。

# CAVEATS

KV 存储并非为批量数据存储而设计；每个值有 512 KB 的上限。递归删除（`consul kv delete -recurse`）不可撤销。导出/导入使用 JSON 格式并包含元数据。视 Consul 配置而定，可能需要 ACL 令牌。

# INSTALL

```pacman: sudo pacman -S consul```

```nix: nix profile install nixpkgs#consul```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[consul](/man/consul)(1), [etcdctl](/man/etcdctl)(1)
