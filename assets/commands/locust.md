# TAGLINE

用 Python 编写的开源负载测试工具

# TLDR

**带 Web UI 运行负载测试**

```locust -f [locustfile.py]```

**无界面运行并指定用户数和生成速率**

```locust -f [locustfile.py] --headless -u [100] -r [10] -t [5m]```

**指定目标主机**

```locust -f [locustfile.py] --host [https://example.com]```

**作为分布式主节点运行**

```locust -f [locustfile.py] --master```

**作为分布式工作节点运行**

```locust -f [locustfile.py] --worker --master-host [master_ip]```

**将结果导出为 CSV**

```locust -f [locustfile.py] --headless --csv [results] -u [50] -r [5] -t [2m]```

**使用自定义 Web UI 端口运行**

```locust -f [locustfile.py] --web-port [8089]```

**运行指定的用户类**

```locust -f [locustfile.py] [UserClass1] [UserClass2]```

# SYNOPSIS

**locust** [_-f locustfile_] [_--headless_] [_-u users_] [_-r rate_] [_-t time_] [_--host url_] [_options_] [_UserClass ..._]

# PARAMETERS

**-f**, **--locustfile** _FILE_
> Python locustfile 的路径（默认：locustfile.py）。

**-H**, **--host** _URL_
> 要进行负载测试的主机。

**-u**, **--users** _NUM_
> 并发用户数的峰值。

**-r**, **--spawn-rate** _NUM_
> 每秒生成的用户数。

**-t**, **--run-time** _TIME_
> 在指定时间后停止（如 300s、5m、1h）。

**--headless**
> 无 Web UI 运行。

**--autostart**
> 立即开始测试而不等待。

**--autoquit** _SECONDS_
> 测试完成后退出（headless 模式）。

**--web-host** _HOST_
> Web 界面绑定的主机（默认：所有接口）。

**--web-port** _PORT_
> Web 界面的端口（默认：8089）。

**--master**
> 作为分布式主节点运行。

**--worker**
> 作为分布式工作节点运行。

**--master-host** _HOST_
> 主节点的主机名（供工作节点使用）。

**--master-port** _PORT_
> 主节点的端口（默认：5557）。

**--expect-workers** _NUM_
> 启动前等待工作节点就绪（仅限主节点）。

**--csv** _PREFIX_
> 将结果导出为带前缀的 CSV 文件。

**--html** _FILE_
> 生成 HTML 报告。

**--json**
> 以 JSON 格式输出结果。

**--loglevel** _LEVEL_
> 日志级别：DEBUG、INFO、WARNING、ERROR。

**--exit-code-on-error** _CODE_
> 发生错误时的退出码。

**-L**, **--list**
> 列出可用的用户类。

# DESCRIPTION

**Locust** 是一款用 Python 编写的开源负载测试工具。它允许你用 Python 代码定义用户行为，使测试灵活且可纳入版本控制。用户被模拟为 greenlet（轻量级线程），单台机器即可支撑数千并发用户。

测试在一个包含用户类的 locustfile 中定义。每个用户类定义若干任务（HTTP 请求或其他操作），并可设置权重表示概率。**@task** 装饰器将方法标记为任务，**between()** 设置请求之间的等待时间。

Web UI（默认端口 8089）提供实时统计、图表和控制功能。你可以启动/停止测试、调整用户数并下载结果。在 CI/CD 集成场景下，headless 模式可在没有 UI 的情况下运行。

分布式模式可以跨多台机器扩展。一个主节点协调各工作节点、汇总统计并控制测试；工作节点模拟用户并回报结果。这使得普通硬件也能产生每秒数百万的请求量。

Locust 通过自定义客户端支持 HTTP 以外的协议。事件系统提供钩子用于自定义日志记录、指标采集以及与监控系统集成。

# CAVEATS

基于 Python 的测试需要懂 Python。greenlet 并非真正的线程——CPU 密集型任务会阻塞其他用户。要获得最佳性能，请使用多个工作进程或多台机器。生产环境中应保护 Web UI。内存占用随用户数增长。

# HISTORY

**Locust** 由 **Jonatan Heyman** 于 **2011 年**前后发起，旨在替代 JMeter 等 Java 负载测试工具。其理念是"把负载测试当代码写"——用真正的编程语言而非 XML 配置。项目名称取自蝗虫群（locust swarm）的比喻，凭借简洁性以及在 Python 中定义复杂用户场景的能力而广受欢迎。该项目仍在积极维护并定期发布新版本。

# INSTALL

```brew: brew install locust```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ab](/man/ab)(1), [wrk](/man/wrk)(1), [hey](/man/hey)(1), [siege](/man/siege)(1), [vegeta](/man/vegeta)(1)
