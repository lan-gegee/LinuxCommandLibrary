# TAGLINE

Cisco 网络测试自动化框架

# TLDR

**运行测试脚本**

```pyats run job [job.py]```

**解析设备输出**

```pyats parse "[show version]" --testbed [testbed.yaml]```

**学习设备特性**

```pyats learn [interface] --testbed [testbed.yaml]```

**比较状态**

```pyats diff [snapshot1] [snapshot2]```

**带 testbed 启动 Shell**

```pyats shell --testbed [testbed.yaml]```

**验证 testbed**

```pyats validate testbed [testbed.yaml]```

**创建 testbed**

```pyats create testbed interactive```

# SYNOPSIS

**pyats** _command_ [_options_] [_args_]

# PARAMETERS

**run**
> 执行测试作业。

**parse**
> 解析命令输出。

**learn**
> 学习设备状态。

**diff**
> 比较快照。

**shell**
> 交互式 Shell。

**validate**
> 验证配置。

**create**
> 创建配置。

**logs**
> 管理测试日志。

**--testbed** _FILE_
> Testbed YAML 文件。

**--device** _NAME_
> 指定设备。

**--output** _DIR_
> 结果输出目录。

# DESCRIPTION

**pyats**（Python Automated Test System）是 Cisco 开源的网络测试自动化框架，用于验证网络设备的配置与行为。它使用 YAML testbed 文件定义网络拓扑、设备连接和凭据，为自动化网络测试提供结构化的方法。

该框架内置强大的解析引擎（Genie），可将 show 命令的非结构化 CLI 输出转换为结构化的 Python 字典，覆盖数百种设备类型。**learn** 功能可捕获接口、路由表、VLAN 等特性的完整设备状态；**diff** 则比较不同时间点拍摄的快照，以发现配置漂移或维护窗口后的变更。

# CAVEATS

面向 Cisco 设备但也支持其他厂商。测试脚本编写有一定学习曲线。需要先完成 testbed 配置。

# HISTORY

**pyATS**（Python Automated Test System）由 **Cisco** 开发，最初用于内部网络测试。后开源发布，用于实现网络测试自动化。

# SEE ALSO

[ansible](/man/ansible)(1), [netmiko](/man/netmiko)(1), [napalm](/man/napalm)(1)
