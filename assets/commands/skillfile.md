# TAGLINE

Skillscript 智能体工作流运行时的 CLI

# TLDR

**安装**运行时、**初始化**项目、打开**仪表盘**

```npm install -g skillscript-runtime
skillfile init
skillfile dashboard```

对一个 skill 执行 **lint**、**compile** 和 **execute**

```skillfile lint [skill]
skillfile compile [skill]
skillfile execute [skill]```

**批准**一个草稿 skill（安全模式）

```skillfile approve [hello]```

查看 **health**、**diagram**，或 **replay** 一条 trace

```skillfile health
skillfile diagram [skill]
skillfile replay [trace_id]```

# SYNOPSIS

**skillfile** _command_ [_options_] [_args_]

# DESCRIPTION

**skillfile** 是 **Skillscript** 的命令行界面。Skillscript 是一种受限的声明式语言及运行时，面向由智能体编写、经人工批准的自动化任务。Skill 看起来类似受 Make 启发的工作流，包含变量、连接器和允许列表——没有不受限制的 shell，也不能随意安装软件包。

运行时（npm 上的 **skillscript-runtime**）通过配置好的连接器、文件系统和 shell 允许列表，以及带操作员签名的可选安全模式来执行 skill。智能体通常通过 MCP 编写 skill（仪表盘启动后为 **http://localhost:7878/rpc**）；操作员则使用 **skillfile** 审查、批准并运行它们。

# PARAMETERS

**init**
> 初始化本地 Skillscript 项目

**dashboard** [**--host**] [**--port**]
> 启动操作员 UI 和 MCP 端点（默认端口 **7878**）

**lint** / **compile** / **execute** _skill_
> 校验、编译或运行一个 skill

**approve** _skill_
> 批准一个草稿 skill 以供执行

**diagram** / **fires** / **replay** / **health**
> 可视化、检查触发器、重放 trace 或检查运行时健康状态

# CONFIGURATION

环境变量控制项包括 **SKILLSCRIPT_SHELL_ALLOWLIST**、**SKILLSCRIPT_FS_ALLOWLIST**（默认拒绝）、**SKILLSCRIPT_SECURED_MODE**，以及用于运行时持有密钥的 **SKILLSCRIPT_SECRET_***。项目配置示例以 **skillscript.config.json.example** 和 **connectors.json.example** 的形式提供。

# CAVEATS

尚处于 1.0 之前阶段；语言与连接器契约仍在稳定中。在加入允许列表之前，shell 和文件系统访问默认被拒绝。仅在具备相应网络防护的情况下才将仪表盘绑定到 **0.0.0.0**。

# SEE ALSO

[make](/man/make)(1)

# RESOURCES

```[Source code](https://github.com/sshwarts/skillscript)```

```[Homepage](https://skillscript.ai)```

```[Documentation](https://docs.skillscript.ai/docs)```

<!-- verified: 2026-07-14 -->
