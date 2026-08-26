# TAGLINE

用于 labgrid 硬件在环设备控制的 MCP 服务器

# TLDR

**运行演示实验室**（无需真实硬件；会打印 MCP 客户端配置）

```labgrid-mcp demo```

```uvx labgrid-mcp demo```

**针对 labgrid 协调器启动 MCP 服务器**（stdio）

```LG_COORDINATOR=[host:20408] labgrid-mcp```

通过 uvx **一次性运行**，无需永久安装

```uvx labgrid-mcp```

在自定义协调器端口上**运行演示**

```labgrid-mcp demo --port [20409]```

# SYNOPSIS

**labgrid-mcp** [_command_] [_options_]

# PARAMETERS

**(no subcommand)**
> 通过 **stdio** 提供 MCP 协议服务。这是所有 MCP 客户端启动时的运行形态。配置来自环境变量（参见 CONFIGURATION）。

**demo** [**--port** _n_]
> 启动一个无硬件的本地实验室：包含真实的 labgrid 协调器和导出器，外加一块模拟开发板（带电源开关和串口控制台）。会打印可直接粘贴使用的 MCP 客户端配置片段。默认端口即演示协调器端口；按 **Ctrl-C** 会将整套环境拆除。

# DESCRIPTION

**labgrid-mcp** 是一个模型上下文协议（MCP）服务器，它把 [labgrid](https://github.com/labgrid-project/labgrid) 的实验室操作暴露给 AI 智能体和其他 MCP 客户端。labgrid 是嵌入式团队用来共享开发板（"place"）的开源框架，提供可远程开关的电源、串口控制台、USB 复用器和烧录器。本软件包把 gRPC 时代的 labgrid 协调器接入 MCP，使智能体能够预约硬件、断电重启、打开控制台、SSH 登录，以及在明确允许的情况下烧录设备。

它会注册约 **47 个工具**（列出/获取 place、电源与 I/O、控制台的打开/读取/发送、SSH 与隧道、可选的烧录作业、place 元数据），外加可浏览的 **labgrid://** 资源。安全门控机制使不可逆的工具类别（**flash**、**place_delete**）默认关闭，除非在 **LABGRID_MCP_ALLOW** 中显式列出；设置 **LABGRID_MCP_READONLY=1** 则仅注册面向读取的工具。

身份与 **labgrid-client** 一致：使用 **LG_HOSTNAME** / **LG_USERNAME**，未设置时则采用真实的主机名和用户名。网络安全交由 VPN 或 SSH 隧道保障，这与 labgrid 自身的信任模型相同。

# CONFIGURATION

环境变量（原生 labgrid 的 **LG_*** 系列，加上 **LABGRID_MCP_*** 系列）：

- **LG_COORDINATOR** — 协调器的 **host:port**（默认 **127.0.0.1:20408**）
- **LG_HOSTNAME** / **LG_USERNAME** — labgrid 客户端身份
- **LABGRID_MCP_READONLY** — 设为 **1**/**true**/**yes** 即注册只读工具
- **LABGRID_MCP_ALLOW** — 以逗号分隔的工具类别；必须显式列出 **flash** 和 **place_delete** 才能启用
- **LABGRID_MCP_SSH_KEYFILE** — SSH 工具使用的私钥路径
- **LABGRID_MCP_ACQUIRE_TIMEOUT** — **acquire_place** 等待的最大秒数（默认 **120**）

# CAVEATS

需要有正在运行的 **labgrid ≥ 24** 协调器（gRPC 时代版本；已在 26.x 上测试）。要求 Python **3.12+**。旧的 crossbar 协调器无法连接。烧录和删除 place 默认被刻意关闭。不要在多个用户之间共用同一个运行中的服务器实例：每个实例只持有一个 labgrid 身份。SSH 工具等同于对已获取的开发板进行完整的远程命令执行。

# HISTORY

**labgrid-mcp** 由 **Onur Celep** 编写，采用 **Apache-2.0** 许可证，以 **labgrid-mcp** 之名发布在 PyPI 上。它以未经修改的库依赖形式使用 **labgrid**（LGPL-2.1-or-later）。

# SEE ALSO

[ssh](/man/ssh)(1), [pip](/man/pip)(1), [uv](/man/uv)(1)

# RESOURCES

```[Source code](https://github.com/onurcelep/labgrid-mcp)```

```[Homepage](https://pypi.org/project/labgrid-mcp/)```

```[Documentation](https://github.com/onurcelep/labgrid-mcp/blob/main/docs/DESIGN.md)```

<!-- verified: 2026-08-05 -->
