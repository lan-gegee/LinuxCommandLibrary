# TAGLINE

管控 AI 代理流量的安全防火墙

# TLDR

使用 HCL 策略文件**运行网关**

```clawpatrol gateway [config.hcl]```

**包装单个进程**，使其流量受到过滤

```clawpatrol run [claude]```

通过隧道将一台主机**加入**正在运行的网关

```clawpatrol join [gateway-url]```

**安装** clawpatrol

```curl -fsSL https://clawpatrol.dev/install.sh | sh```

# SYNOPSIS

**clawpatrol** _subcommand_ [_options_]

# DESCRIPTION

**clawpatrol** 是一款面向 AI 代理的安全防火墙。它位于代理与其通信的系统之间，在线缆层面解析流量，并根据你用 HCL 编写的规则对每个操作进行评估，然后才放行。由于它检查的是协议事实而不仅仅是 URL，规则可以针对具体细节做出反应，例如破坏性的 SQL 语句或危险的 Kubernetes 调用，从而阻止它们或要求人工批准。

它有三种运行形态。**gateway** 加载策略文件并为所有指向它的流量提供代理；**join** 通过 WireGuard 隧道将主机连接到网关；**run** 包装单个进程，只过滤该程序的流量——在 Linux 上使用网络命名空间，在 macOS 上使用 Network Extension 框架。

# PARAMETERS

**gateway** _CONFIG_
> 运行代理，从指定的 HCL 文件加载策略。

**join** _GATEWAY-URL_
> 通过 WireGuard 隧道将本机连接到正在运行的网关。

**run** _COMMAND_
> 启动 _COMMAND_，并将其网络流量经由 clawpatrol 路由。

# CAVEATS

策略用 HCL 编写，强制执行线缆层面的协议事实，因此覆盖范围取决于 clawpatrol 是否理解所使用的协议。按进程包装依赖平台特定的网络机制（Linux 上的网络命名空间、macOS 上的 Network Extension）。

# SEE ALSO

[mitmproxy](/man/mitmproxy)(1), [iptables](/man/iptables)(8)

# RESOURCES

```[Source code](https://github.com/denoland/clawpatrol)```

```[Homepage](https://clawpatrol.dev)```

<!-- verified: 2026-06-10 -->
