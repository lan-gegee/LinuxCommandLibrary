# TAGLINE

高性能 L4/L7 代理与服务网格数据平面

# TLDR

**使用配置文件启动**

```envoy -c [/path/to/config.yaml]```

只**校验配置**而不运行

```envoy -c [config.yaml] --mode validate```

**带服务集群名称启动**

```envoy -c [config.yaml] --service-cluster [my-cluster]```

**以自定义节点 ID 启动**

```envoy -c [config.yaml] --service-node [node-1]```

为热重启**指定基础 ID 运行**

```envoy -c [config.yaml] --base-id [1]```

**以内联 YAML 配置启动**

```envoy --config-yaml "[yaml-string]"```

**启用调试日志**

```envoy -c [config.yaml] -l debug```

# SYNOPSIS

**envoy** [_options_]

# PARAMETERS

**-c**, **--config-path** _path_
> 引导配置文件的路径（.json、.yaml、.pb、.pb_text）。

**--config-yaml** _yaml_
> 内联 YAML 配置字符串。与 --config-path 合并。

**--mode** _mode_
> 运行模式：serve（默认）或 validate。

**--service-cluster** _name_
> 本地服务集群名称。

**--service-node** _id_
> 本地服务节点标识符。

**--service-zone** _zone_
> 用于区域感知的本地服务区域。

**--local-address-ip-version** _version_
> 本地地址的 IP 版本：v4 或 v6。

**-l**, **--log-level** _level_
> 日志级别：trace、debug、info、warning、error、critical、off。

**--log-path** _path_
> 日志文件路径。

**--log-format** _format_
> 日志消息格式字符串。

**--component-log-level** _config_
> 各组件的日志级别。

**--base-id** _id_
> 共享内存的基础 ID（热重启）。

**--use-dynamic-base-id**
> 自动选择未被占用的基础 ID。

**--restart-epoch** _epoch_
> 热重启纪元编号。

**--concurrency** _num_
> 工作线程数量。

**--file-flush-interval-msec** _ms_
> 文件缓冲区的刷新间隔（毫秒）。

**--drain-time-s** _seconds_
> 热重启期间排空连接的时间。

**--parent-shutdown-time-s** _seconds_
> 热重启期间父进程关闭前的等待时间。

**--disable-hot-restart**
> 完全禁用热重启功能。

**--enable-core-dump**
> 启用核心转储以便调试。

**--admin-address-path** _path_
> 绑定后将管理地址和端口写入给定路径。

**--version**, **-v**
> 显示版本信息。

**--help**, **-h**
> 显示帮助消息。

# CONFIGURATION

**/etc/envoy/envoy.yaml**
> Envoy 引导配置文件的常见位置。

**envoy.yaml**
> 定义监听器、集群、路由和过滤器的引导配置文件。

# DESCRIPTION

**envoy** 是一个高性能 L4/L7 代理与通信总线，为大型现代面向服务架构而设计。它负责负载均衡、服务发现和可观测性，并提供高级流量管理功能。

配置通过 **-c** 指定的 YAML、JSON 或 protobuf 文件提供。配置定义监听器（端口）、集群（上游）、路由和过滤器。动态配置可从 xDS API 获取。

热重置（hot restart）允许在不中断连接的情况下升级 Envoy。**--base-id** 标识父子进程之间共享的内存区域。使用 **--restart-epoch** 协调重启。

validate 模式在不启动代理的情况下检查配置的语法和语义，非常适合 CI/CD 流水线。

Envoy 通常作为 sidecar 代理部署在服务网格中（Istio、Consul Connect），或用作边缘/入口代理。它支持 HTTP/1.1、HTTP/2、gRPC、TCP 和 UDP 协议。

# CAVEATS

高级用例的配置复杂度可能很高。热重启需要正确协调 base-id。内存占用随连接数和集群数增长。部分功能需要特定的过滤器配置。

# HISTORY

Envoy 由 Matt Klein 在 **Lyft** 创建，于 **2016 年 9 月**开源。它的设计初衷是承载 Lyft 的微服务流量，重点关注可观测性与可调试性。Envoy 于 **2017 年**加入 CNCF，**2018 年**毕业。它成为 Istio 等服务网格的基础，并被广泛用作数据平面代理。

# INSTALL

```brew: brew install envoy```

```nix: nix profile install nixpkgs#envoy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nginx](/man/nginx)(1), [haproxy](/man/haproxy)(1), [istioctl](/man/istioctl)(1), [traefik](/man/traefik)(1), [kubectl](/man/kubectl)(1)
