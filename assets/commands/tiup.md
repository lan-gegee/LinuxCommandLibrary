# TAGLINE

TiDB 组件与集群管理器

# TLDR

**启动本地 TiDB playground**

```tiup playground```

**以指定版本启动**

```tiup playground v[7.1.0]```

**以多实例启动**

```tiup playground --db [3] --pd [3] --kv [3]```

**部署集群**

```tiup cluster deploy [cluster-name] v[7.1.0] [topology.yaml]```

**启动集群**

```tiup cluster start [cluster-name]```

**显示集群状态**

```tiup cluster display [cluster-name]```

**连接 TiDB**（MySQL 客户端）

```mysql -h [127.0.0.1] -P [4000] -u root```

**安装组件**

```tiup install tidb:v[7.1.0]```

# SYNOPSIS

**tiup** _component_ [_args_...]

**tiup** [_command_] [_options_]

# COMMANDS

**playground**
> 启动本地测试集群。

**cluster** deploy|start|stop|destroy|display|scale-out|scale-in
> 管理生产集群。

**install** _component_
> 安装 TiUP 组件。

**update** _component_
> 更新组件。

**list**
> 列出可用组件。

**status**
> 显示正在运行的组件。

**clean**
> 清理组件数据。

**uninstall** _component_
> 移除组件。

**--version**
> 显示 TiUP 版本。

# PLAYGROUND OPTIONS

**--db** _count_
> TiDB 实例数量。

**--pd** _count_
> PD 实例数量。

**--kv** _count_
> TiKV 实例数量。

**--tiflash** _count_
> TiFlash 实例数量。

**--host** _address_
> 绑定地址。

**--db.port** _port_
> TiDB 端口。默认：4000。

**--pd.port** _port_
> PD 端口。默认：2379。

# CLUSTER OPTIONS

**deploy** _name_ _version_ _topology_
> 从拓扑文件部署集群。

**start** _name_
> 启动集群。

**stop** _name_
> 停止集群。

**destroy** _name_
> 移除集群。

**scale-out** _name_ _topology_
> 添加节点。

**scale-in** _name_ --node _host:port_
> 移除节点。

**upgrade** _name_ _version_
> 升级集群。

# DESCRIPTION

**tiup** 是 TiDB 的组件管理器。TiDB 是一款 MySQL 兼容的分布式数据库，tiup 负责其集群的安装、部署和运维。

**tiup playground** 启动一个包含 TiDB、PD（placement driver）和 TiKV（存储）组件的本地开发集群。使用任意 MySQL 客户端连接 4000 端口即可。

生产部署使用 **tiup cluster** 配合 YAML 拓扑文件。拓扑文件定义主机、端口、目录和组件分布。**deploy** 创建集群；**start** 运行集群。

TiDB 与 MySQL 兼容，可以使用标准的 MySQL 客户端和驱动。TiFlash 为分析型负载提供列式存储。

TiUP 组件包括监控（Prometheus、Grafana）、诊断工具和各类实用程序。**tiup list** 可查看可用组件。

# CAVEATS

TiDB 大体兼容 MySQL，但部分特性有差异或不受支持。生产高可用至少需要 3 节点 PD。TiKV 需要 SSD 存储。资源需求随数据规模增长。

# HISTORY

TiDB 由 **PingCAP** 创建，首次发布于 **2015 年**。它受 Google Spanner 和 F1 启发，将 MySQL 兼容性与水平扩展能力结合在一起。其存储层 TiKV 加入 CNCF 并于 **2020 年**毕业。TiDB 广泛用于 HTAP（混合事务/分析处理）负载，尤其在亚洲地区。主要版本每年发布一次，并提供 LTS 支持。

# SEE ALSO

[mysql](/man/mysql)(1), [cockroach](/man/cockroach)(1)
