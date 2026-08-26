# TAGLINE

用于查看 Claude 用量与速率限制的本地仪表盘

# TLDR

**启动仪表盘**（打开本地 Web 界面）

```claumon```

# SYNOPSIS

**claumon** [_options_]

# DESCRIPTION

**claumon** 是面向 Claude Pro 和 Max 用户的本地监控工具。它以单个零配置的 Go 二进制文件从终端启动，打开一个本地 Web 仪表盘（默认地址为 http://localhost:3131），实时显示 API 速率限制仪表、带可信区间的用量预测、按会话划分并附带多日趋势的 token 与费用明细，以及一个带健康度评分的 Claude 记忆文件浏览器。

它从 Claude OAuth API 读取速率限制信息，并呈现经过校准的用量预测，让重度用户能够了解自己距离上限还有多远，以及消耗随时间的变化趋势。

# CAVEATS

面向 Claude Pro 和 Max 账户，依赖 Claude 的 OAuth API，因此它显示的数据反映该服务的状态；如果上游 API 变更可能会失效。该仪表盘仅在本地提供服务，不是托管服务。

# HISTORY

**claumon** 使用 **Go** 编写，以单个自包含二进制文件分发，可通过 Homebrew 安装。名称是 "Claude monitor" 的缩写。

# SEE ALSO

[claude](/man/claude)(1), [top](/man/top)(1), [htop](/man/htop)(1)

# RESOURCES

```[Source code](https://github.com/fabioconcina/claumon)```

```[Homepage](https://claumon.fabioconcina.com)```

<!-- verified: 2026-06-14 -->
