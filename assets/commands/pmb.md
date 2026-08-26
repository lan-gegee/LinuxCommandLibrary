# TAGLINE

通过 MCP 为 AI 编码智能体提供本地优先的持久记忆

# TLDR

**检测你的智能体并接入 MCP 入口**

```pmb setup```

**显示存储了多少记忆以及存储在哪里**

```pmb stats```

**在已存储的记忆中搜索某个查询**

```pmb recall "[query]"```

**打开交互式终端界面**

```pmb tui```

**打开 Web 控制台（端口 8765）**

```pmb dashboard```

**将代码库索引进记忆**

```pmb index project [.]```

**接入特定智能体（Claude Code、Cursor、Codex）**

```pmb connect [claude]```

# SYNOPSIS

**pmb** _command_ [_arguments_] [_options_]

# DESCRIPTION

**pmb** 通过 **Model Context Protocol**（MCP）为 Claude Code、Cursor、Codex 等 AI 编码智能体提供本地优先的持久记忆。它将决策、经验教训和项目事实存入磁盘上的单个 SQLite 文件，并配套一个本地向量库，因此完全离线即可工作，无需 API 密钥、账户或遥测。

接入智能体之后，pmb 会在智能体行动前自动注入相关记忆，并通过生命周期钩子捕获新的上下文。检索采用混合方式，结合 BM25 关键词搜索、向量相似度和实体图，数十毫秒内即可返回结果。命令行接口负责驱动设置、摄取（代码库、PDF、ChatGPT/Claude 导出文件）、维护、配置以及检查已记住的内容。

pmb 从 PyPI 以 **pmb-ai** 的名称安装，该软件包提供 **pmb** 命令，也可以直接通过 **npx pmb-ai** 运行。每个工作区位于 **~/.pmb/<workspace_name>/** 下，是一个自包含的目录，可以被复制、纳入版本控制或在机器之间同步。

# COMMANDS

**setup**

> 检测当前使用的智能体并写入 MCP 服务器入口。

**connect** _agent_ [**--workspace** _name_]

> 接入特定智能体（Claude Code、Cursor、Codex 等），可选指向一个共享工作区。

**stats**

> 显示记忆数量和存储信息。

**recall** _"query"_

> 搜索已存储的记忆，并以调试输出形式打印结果。

**tui**

> 启动交互式终端用户界面。

**dashboard**

> 在端口 8765 上启动 Web 界面。

**index** _project|pdf_ _target_

> 扫描并向量化一个代码库、PDF 文件或 PDF 目录（配合 **--recurse**）。

**import chatgpt** _path_

> 导入 ChatGPT 或 Claude 的对话导出文件。

**hooks** _install|list|uninstall_ _agent_

> 管理用于自动捕获和恢复上下文的生命周期钩子。

**config** _list|get|set_ [_key_] [_value_]

> 查看或修改设置。

**forget** _ulid_ [**--hard**]

> 归档一条已存储的事实，或使用 **--hard** 永久删除它。

**doctor**

> 对安装执行健康检查。

# CONFIGURATION

**~/.pmb/<workspace_name>/**

> 每个工作区专属的目录，存放 SQLite 事件数据库、LanceDB 向量库和配置文件。复制或同步此目录即可在机器之间迁移记忆。

**pmb config set** _key_ _value_

> 修改一项文档中的设置；**pmb config list** 会列出常用键，加上 **--pro** 可查看全部设置项。

# CAVEAT

pmb 将所有内容存储在本地且默认离线运行，但由环境感知自动写入层产生的记忆会被自动捕获，因此在共享项目或敏感项目上请审查保留了哪些内容，并使用 **pmb forget** 或 **pmb forget-auto** 清理它们。钩子集成依赖宿主智能体对 MCP 生命周期钩子的支持；**pmb hooks capabilities** 可以显示各个智能体支持哪些能力。

# SEE ALSO

[claude](/man/claude)(1), [aider](/man/aider)(1), [cursor](/man/cursor)(1), [ollama](/man/ollama)(1)

# RESOURCES

```[Source code](https://github.com/oleksiijko/pmb)```

<!-- verified: 2026-06-23 -->
