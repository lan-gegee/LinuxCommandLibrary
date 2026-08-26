# TAGLINE

HTTP 负载测试工具

# TLDR

**对端点发起压测**

```echo "GET http://localhost:8080/" | vegeta attack -rate=[50] | vegeta report```

**限定持续时间的压测**

```echo "GET http://localhost/" | vegeta attack -rate=[100] -duration=[30s] | vegeta report```

**绘制结果图表**

```vegeta attack ... | vegeta plot > [results.html]```

**编码为 JSON**

```vegeta attack ... | vegeta encode --to=json```

**从目标文件发起**

```vegeta attack -targets=[targets.txt] -rate=[10]```

**POST 请求**

```echo "POST http://localhost/api" | vegeta attack -body=[data.json]```

# SYNOPSIS

**vegeta** _command_ [_options_]

# PARAMETERS

**attack**
> 发送请求。

**report**
> 生成报告。

**plot**
> 生成 HTML 图表。

**encode**
> 转换格式。

**-rate** _N_
> 每秒请求数。

**-duration** _D_
> 压测持续时间。

**-targets** _FILE_
> 目标文件。

**-body** _FILE_
> 请求体文件。

**-header** _H_
> HTTP 头。

# DESCRIPTION

**vegeta** 是一款以恒定、可配置的速率发送请求的 HTTP 负载测试工具。**attack** 命令产生流量并将二进制结果流式输出到 stdout，可将其通过管道传给 **report** 进行统计分析，或传给 **plot** 进行 HTML 可视化。

这种管道式设计允许灵活组合负载测试工作流。目标定义支持多个端点、HTTP 方法、请求头和请求体。报告包含延迟百分位数、成功率和吞吐量指标，便于发现性能退化和容量上限。

# CAVEATS

高速率需要调优。可能受系统限制约束。目标服务器必须能够承受负载。

# HISTORY

**Vegeta** 由 **Tomás Senart** 创建，用于 HTTP 负载测试。其名称取自《龙珠》角色，强调力量与速度。

# INSTALL

```pacman: sudo pacman -S vegeta```

```zypper: sudo zypper install vegeta```

```brew: brew install vegeta```

```nix: nix profile install nixpkgs#vegeta```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ab](/man/ab)(1), [wrk](/man/wrk)(1), [hey](/man/hey)(1)
