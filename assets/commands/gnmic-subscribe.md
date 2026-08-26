# TAGLINE

订阅 gNMI 流式遥测数据（完整形式）

# TLDR

**订阅一个路径**

```gnmic -a [host:port] subscribe --path [/state/port]```

**按采样间隔订阅**

```gnmic -a [host:port] subscribe --path [/state/port] --sample-interval [30s]```

**以 on-change 模式订阅**

```gnmic -a [host:port] subscribe --path [/state/port] --stream-mode on-change```

**带心跳间隔订阅**

```gnmic -a [host:port] subscribe --path [/path] --stream-mode on-change --heartbeat-interval [1m]```

**订阅多个路径**

```gnmic -a [host:port] subscribe --path [/path1] --path [/path2]```

**带身份验证订阅**

```gnmic -a [host:port] -u [user] -p [pass] subscribe --path [/path]```

# SYNOPSIS

**gnmic** **subscribe** [_options_]

# PARAMETERS

**--path** _path_
> 要订阅的 gNMI 路径。

**--mode** _mode_
> 订阅模式：STREAM、ONCE、POLL。

**--stream-mode** _mode_
> 流模式：SAMPLE、ON_CHANGE、TARGET_DEFINED。

**--sample-interval** _duration_
> SAMPLE 模式的采样间隔。

**--heartbeat-interval** _duration_
> ON_CHANGE 模式的心跳间隔。

**--suppress-redundant**
> 抑制冗余更新；只在值真正发生变化时才发送更新。

**--updates-only**
> 只发送更新，不发送初始状态快照。

**--quiet**
> 不输出到 stdout。

**--prefix** _PATH_
> 应用到所有 **--path** 值的公共前缀。

**--qos** _N_
> 用于数据包标记的 DSCP 值。默认为 20；设为 0 表示禁用。

**--output** _NAME_
> 来自配置文件的命名输出（如 Kafka 或 Prometheus 输出），订阅结果写入其中而非 stdout。

**--name** _NAME_
> 运行配置文件中预定义的一个或多个订阅，而不是在命令行上指定 **--path**。

# DESCRIPTION

**gnmic subscribe**（别名 **gnmic sub**）向网络设备发送 gNMI Subscribe RPC 以进行流式遥测采集。它支持三种订阅模式：STREAM（持续更新，默认）、ONCE（立即单次响应）和 POLL（按需请求）。流模式支持 SAMPLE（周期性，默认）和 ON_CHANGE（事件驱动）两种投递方式。

结果默认打印到 stdout，也可通过 **--output** 路由到已配置的输出目标（file、Kafka、NATS、Prometheus、InfluxDB 等）。

# INSTALL

```brew: brew install gnmic```

```nix: nix profile install nixpkgs#gnmic```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnmic](/man/gnmic)(1), [gnmic-get](/man/gnmic-get)(1), [gnmic-set](/man/gnmic-set)(1)

# RESOURCES

```[Documentation](https://gnmic.openconfig.net/cmd/subscribe/)```

```[Source code](https://github.com/openconfig/gnmic)```

<!-- verified: 2026-07-17 -->
