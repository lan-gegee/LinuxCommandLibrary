# TAGLINE

订阅 gNMI 流式遥测数据

# TLDR

**订阅一个路径**

```gnmic -a [host:port] sub --path [/state/port]```

**按采样间隔订阅**

```gnmic -a [host:port] sub --path [/state/port] --sample-interval [30s]```

**以 on-change 模式订阅**

```gnmic -a [host:port] sub --path [/state/port] --stream-mode on_change```

**带心跳间隔订阅**

```gnmic -a [host:port] sub --path [/path] --stream-mode on_change --heartbeat-interval [1m]```

**订阅多个路径**

```gnmic -a [host:port] sub --path [/path1] --path [/path2]```

**带身份验证订阅**

```gnmic -a [host:port] -u [user] -p [pass] sub --path [/path]```

# SYNOPSIS

**gnmic** **sub** | **subscribe** [_options_]

# PARAMETERS

**--path** _path_
> 要订阅的 gNMI 路径。

**--mode** _mode_
> 订阅模式：STREAM、ONCE、POLL（默认 STREAM）。

**--stream-mode** _mode_
> 流模式：sample、on_change、target_defined（默认 sample）。

**--prefix** _prefix_
> 为所有路径设置公共前缀。

**--target** _target_
> 在 SubscriptionList 的 prefix 字段中设置路径目标。

**--qos** _value_
> 订阅响应的 QoS 标记（默认 20，设为 0 表示禁用）。

**--sample-interval** _duration_
> 设备发送采样的间隔（如 1s、1m30s）。

**--heartbeat-interval** _duration_
> on_change 或 sample 模式的心跳间隔。

**--suppress-redundant**
> 抑制冗余更新，除非自上次更新后值发生了变化。

**--updates-only**
> 只发送更新，不发送初始状态。

**--quiet**
> 不将订阅响应输出到 stdout。

**--format** _format_
> 输出格式（json、protojson、prototext、event、flat）。

**--name** _name_
> 触发配置文件中预定义的订阅。

**--output** _output_
> 选择配置文件中定义的输出来源（如 Kafka 或 Prometheus 输出）。

**--depth** _depth_
> 设置 gNMI 扩展的深度值。

**--history-snapshot** _time_
> 设置历史快照值（纳秒或 RFC3339 格式）。

**--set-target**
> 将 SubscribeRequest Prefix 的 target 设置为已配置的目标名称。

# DESCRIPTION

**gnmic sub**（即 **subscribe**）向网络设备发送 gNMI Subscribe RPC 以进行流式遥测采集。它支持多种订阅模式：**once**（立即单次响应）、**poll**（按需请求）和 **stream**（持续更新）。流模式支持 **sample**（周期性）、**on_change**（事件驱动）和 **target_defined** 三种投递方式。

# INSTALL

```brew: brew install gnmic```

```nix: nix profile install nixpkgs#gnmic```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnmic](/man/gnmic)(1), [gnmic-get](/man/gnmic-get)(1), [gnmic-set](/man/gnmic-set)(1)
