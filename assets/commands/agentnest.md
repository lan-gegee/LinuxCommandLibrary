# TAGLINE

面向 AI 代理沙箱的安全自托管运行时

# TLDR

**检查** Docker 与各后端是否可用

```agentnest doctor```

**运行演示**沙箱（需要 Docker）

```agentnest demo```

在一次性沙箱中**执行 Python**

```agentnest run [script.py] --image [python:3.12-slim] --timeout [60]```

在沙箱中**运行 Shell** 命令

```agentnest shell '[python -V]' --memory [256m] --cpus [0.5]```

**清理**崩溃后遗留的孤儿沙箱

```agentnest prune```

**启动远程 API**（需要 `agentnest[server]`）

```AGENTNEST_API_TOKEN=[secret] agentnest serve --host [127.0.0.1] --port [8765]```

**通过 MCP 暴露 AgentNest**（需要 `agentnest[mcp]`）

```agentnest mcp```

**列出**发现的运行时后端

```agentnest backends```

# SYNOPSIS

**agentnest** _command_ [_options_]

# DESCRIPTION

**agentnest** 是 AgentNest 的命令行接口。AgentNest 是一个自托管运行时，为 AI 代理提供一次性的、受策略控制的环境，可用于 Python、Shell 命令、文件、软件包、浏览器、GPU 和 Git 工作。

沙箱运行在你掌控的后端之上（默认 Docker；Kubernetes 等可通过插件支持）。默认设置偏重隔离：非 root 用户、只读根文件系统、不赋予 Linux capabilities、拒绝网络、资源限额，以及对过期资源的清理。可选的出站白名单能通过过滤代理只放行特定域名。

主要的编程入口是 Python 的 `Sandbox` API；CLI 则覆盖日常操作，例如一次性运行、健康检查、回收孤儿容器、对外提供远程 API，以及通过 Model Context Protocol（MCP）暴露工具。

# PARAMETERS

**run** _code_or_script_
> 在新沙箱中运行 Python 源码或 **.py** 文件。退出状态与沙箱内进程一致；stdout 和 stderr 原样保留。

**shell** _script_
> 在新沙箱中运行一段 Shell 脚本字符串。

**demo**
> 运行自包含的沙箱演示（无需额外参数）。需要一个可正常工作的 Docker 环境。

**doctor**
> 检查本地运行时环境。打印机器可读的 JSON；Docker 不可用时以非零状态退出。

**backends**
> 列出探测到的运行时后端名称。

**prune** [**--all**]
> 清除崩溃遗留的受管沙箱（已过期资源）。加上 **--all** 则清除所有受管沙箱，而不仅是过期的那些。

**serve** [**--host** _addr_] [**--port** _n_]
> 启动远程运行时 API（默认 **127.0.0.1:8765**）。需要 `pip install 'agentnest[server]'`。若未设置 **AGENTNEST_API_TOKEN**，则拒绝绑定非回环地址。

**mcp**
> 启动 AgentNest MCP 服务器，供 Claude Code 或 Cursor 之类的客户端使用。需要 `pip install 'agentnest[mcp]'`。

**--version**
> 打印 AgentNest 版本。

**run** 与 **shell** 的选项：

**--image** _name_
> 容器镜像（默认 **python:3.12-slim**）。

**--backend** _name_
> 运行时后端（默认 **docker**）。

**--timeout** _seconds_
> 沙箱超时时间，单位为秒（默认 **300**）。超时的命令会被终止；视具体用法而定，沙箱及其状态可能继续保留。

**--network**
> 启用网络（默认拒绝网络）。

**--memory** _limit_
> 内存上限（默认 **512m**）。

**--cpus** _n_
> CPU 上限，浮点数（默认 **1.0**）。

# CAVEATS

容器与主机共享内核；在运行多租户或不可信工作负载之前，请依据你的威胁模型选择恰当的隔离边界。默认后端必须有可用的 Docker。可选功能（**serve**、**mcp**、Kubernetes）需要安装对应的 pip extras。安装命令：`pip install agentnest`（或包含额外组件的 `pip install 'agentnest[all]'`）。

# HISTORY

**AgentNest** 是一个开源的 Apache-2.0 项目，专注于自托管 AI 代理沙箱。它以 **agentnest** 之名发布于 PyPI，并附带同名的控制台脚本入口。

# SEE ALSO

[docker](/man/docker)(1), [podman](/man/podman)(1), [firejail](/man/firejail)(1), [bubblewrap](/man/bubblewrap)(1), [pip](/man/pip)(1)

# RESOURCES

```[Source code](https://github.com/mihirahuja1/agentnestOSS)```

```[Documentation](https://mihirahuja1.github.io/agentnestOSS/)```

<!-- verified: 2026-07-23 -->
