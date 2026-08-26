# TAGLINE

基于快照的 API 负载测试工具

# TLDR

使用 ballast.json 配置从当前目录**运行负载测试**

```ballast```

不写入快照文件**运行负载测试**

```ballast --no-snapshot```

为快照附加描述并**运行负载测试**

```ballast --desc "[initial baseline]"```

# SYNOPSIS

**ballast** [**--no-snapshot**] [**--desc** _description_]

# PARAMETERS

**--no-snapshot**
> 运行负载测试时不写入快照文件。适用于无需基线对比的一次性测试。

**--desc** _description_
> 为快照附加描述，便于识别。

# DESCRIPTION

**ballast** 是一款针对 API 运行基于快照的性能测试的命令行工具。它将 UI 测试框架中常用的快照测试概念应用到 API 负载测试中：性能基线被捕获为快照，后续的每次测试运行都会与之对比以检测性能退化。

测试在 **ballast.json** 配置文件中定义，其中指定要测试的端点列表。对每个端点，ballast 在多个周期内发送可配置数量的并发请求并测量响应时间。然后计算平均、最小和最大响应时间，并与上一次快照比较。如果平均响应时间超出可配置的阈值（默认 250ms），测试将被标记为失败。

除响应时间外，ballast 还可以校验预期的 HTTP 状态码、响应体和响应头。在主测试周期开始前，会有一个对数递增的热身阶段来预热目标。结果以彩色编码输出显示在终端中：绿色表示通过的测试与性能提升，红色表示失败与性能退化，黄色表示警告。

快照存储在当前目录的 **.ballast_snapshot.json** 文件中，保留所有历史测试运行的带时间戳记录。

ballast 使用 Rust 编写，采用 tokio 执行异步请求，并使用 reqwest 作为 HTTP 客户端。

# CONFIGURATION

**ballast.json**
> 定义要测试端点的配置文件。必须位于工作目录中。包含一个 **endpoints** 数组，每个端点具有以下字段：

**name** _string_
> 必需。测试的标识符。

**url** _string_
> 必需。目标端点 URL。

**method** _string_
> 必需。HTTP 方法：GET、POST、PUT、DELETE、PATCH 或 OPTIONS。

**concurrent_requests** _number_
> 必需。每周期发送的并行请求数。

**cycles** _number_
> 必需。要运行的测试迭代次数。

**threshold** _number_
> 可接受的响应时间偏差（毫秒）（默认：250）。

**headers** _object_
> 自定义 HTTP 头，键值对形式。

**body** _json_
> POST、PUT 或 PATCH 请求的 JSON 请求负载。

**expected_status** _number_
> 用于校验的预期 HTTP 状态码。

**expected_body** _json_
> 用于校验的预期响应体。

**expected_headers** _object_
> 用于校验的预期响应头。

**ramp** _boolean_
> 是否在测试周期前启用对数热身（默认：true）。

# CAVEATS

Ballast 要求当前目录存在 **ballast.json** 文件；无法指定其他配置文件路径。该工具面向本地或开发环境的 API 测试，不适合大规模的生产级负载测试。每个周期之间会插入 100ms 的暂停，这限制了最大请求吞吐量。

# HISTORY

**ballast** 由 **Teo Nys** (synoet) 创建，是 MIT 许可证下的开源 Rust 项目。它发布于 crates.io，源代码托管在 GitHub 上。

# SEE ALSO

[ab](/man/ab)(1), [wrk](/man/wrk)(1), [curl](/man/curl)(1), [ali](/man/ali)(1), [hey](/man/hey)(1)
