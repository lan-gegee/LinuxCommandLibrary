# TAGLINE

面向可问责多智能体 AI 团队的 CLI，附带本地 Web 控制台

# TLDR

使用 pipx **安装**并初始化

```pipx install banksia```

```banksia init```

**启动**本地控制器并打开控制台

```banksia serve```

**显示**状态（无子命令时也是默认行为）

```banksia```

```banksia status```

**配置**一个 Task 提供方

```banksia setup```

```banksia providers list```

**可选的 PostgreSQL** 安装路径

```pipx install "banksia[postgres]"```

```banksia init --database-url [postgresql+asyncpg://…]```

# SYNOPSIS

**banksia** [**--debug**] [**-V**|**--version**] [_subcommand_] [_options_]

# DESCRIPTION

**banksia** 是一个命令行应用与本地运行时，用于在复杂工作上构建和运行**可问责的 AI 团队**。工作流定义的是一棵职责树（而非固定脚本）。管理者可以重新规划、并行化或迭代；进度和负责人的最终 Result 是持久的控制器状态，交付物则作为普通的工作区文件保存。

该包自带可视化**控制台**（浏览器 UI）。完成 **banksia init** 和 **banksia serve** 后，打开 **http://127.0.0.1:18125/**（默认地址）。初始化时可以配置一个 Task 提供方和一个可选的对话式 **Operator**，后者使用与 UI 相同的控制器操作。默认存储为 **SQLite**；通过 **banksia[postgres]** 可选配 PostgreSQL。

托管的提供方包括 Codex 和 Claude。需要 **Python 3.12+**；支持 Linux 和 macOS（不支持原生 Windows；WSL2 走 Linux 路径）。使用 **pipx install banksia** 安装。

# PARAMETERS

**(no subcommand)** / **status**
> 打印控制器状态（未给出子命令时的默认行为）。

**init** [**--data-dir** _dir_] [**--database-url** _url_] [**--workspace** _dir_] [**--host** _addr_] [**--port** _n_] [**--log-level** _level_] [**--force**] [**--skip-db-upgrade**] [**--non-interactive**] …
> 初始化本地控制器状态；可选配置 Task 提供方和 Operator。

**serve**
> 启动为控制台和运行时提供服务的本地 API/控制器进程。

**setup**
> 面向 Task 工作的引导式提供方配置。

**providers** **list**|**status**|**check**|**configure**|**identity**|**set-default** …
> 查看和配置 LLM/提供方。

**operator** **setup**|**status**|**disable** …
> 管理对话式 Operator 智能体。

**config** **show**|**path** …
> 显示配置或其路径。

**workflow** **import**|**export** …
> 导入或导出 Workflow 定义。

**task** **start** …
> 从 CLI 启动 Task/运行。

**--debug**
> 命令失败时附带回溯信息。

**-V**, **--version**
> 打印软件包版本。

# CONFIGURATION

**本地数据目录**（在 **init** 时通过 **--data-dir** 设置）
> 存放控制器状态、默认的 SQLite 数据库以及运行时文件。

**--database-url**
> PostgreSQL 的 SQLAlchemy URL（如 **postgresql+asyncpg://…**）。需要 **postgres** extra。

**--host** / **--port**
> 本地 API 的绑定地址（默认绑定环回地址，端口为项目默认值 **18125**）。

**默认工作区**
> 供 Task 成员进行文件操作和受管操作的目录。

# CAVEATS

设计用于可信的本地机器；控制器默认只绑定环回地址。一次运行中的 Task 成员共享同一个对提供方可见的工作区。**console/** 下的控制台资源采用 Sustainable Use License（并非纯 MIT）。它不是多租户托管服务。真实运行必须能访问提供方的 CLI/SDK 和 API 凭据。

# HISTORY

**Banksia** 是一个开源的可问责多智能体运行时（核心采用 MIT 许可证；控制台的衍生内容采用 Sustainable Use License）。上游仓库：**github.com/ringlochid/banksia**。以 **banksia** 为名发布于 PyPI。

# SEE ALSO

[pipx](/man/pipx)(1), [claude](/man/claude)(1), [codex](/man/codex)(1), [uvicorn](/man/uvicorn)(1)

# RESOURCES

```[Source code](https://github.com/ringlochid/banksia)```

```[Documentation](https://github.com/ringlochid/banksia/tree/main/docs)```

<!-- verified: 2026-08-02 -->
