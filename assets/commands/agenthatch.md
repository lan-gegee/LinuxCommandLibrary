# TAGLINE

把 markdown 技能编译为独立的 Python 代理

# TLDR

**初始化**配置和 LLM 提供方

```agenthatch init```

**注册**技能文件

```agenthatch skills add [./my-skill/SKILL.md]```

把技能**编译**为代理

```agenthatch hatch [my-skill]```

以交互方式**运行**孵化出的代理

```agenthatch run [my-skill]```

**列出**已注册的技能

```agenthatch skills list```

**诊断**环境

```agenthatch doctor```

# SYNOPSIS

**agenthatch** _command_ [_arguments_] [_options_]

# DESCRIPTION

**agenthatch** 是一个编译器，能把 markdown 格式的 **SKILL.md** 定义变成一个可独立运行的 Python AI 代理。它会解析技能文件，执行一轮 AI 推理来推断工具与结构，然后生成一个完整的 Python 软件包，带有自己的 CLI 入口点、带类型标注的工具定义以及 MCP 集成。

已注册的技能存放在本地索引（“skillhouse”）里。典型流程是：注册技能，用 **hatch** 孵化生成代码，再在交互式终端 UI 中**运行**生成的代理。

# COMMANDS

**init**
> 初始化配置并设置 LLM 提供方。

**skills add** _path_
> 在 skillhouse 索引中注册一个 SKILL.md 文件。

**skills list**
> 显示所有已注册的技能。

**skills delete** _name_
> 从 skillhouse 中移除一个技能。

**hatch** _name_
> 运行完整的编译流水线（解析、AI 推理、代码生成）。

**run** _name_
> 以交互式终端 UI 模式启动已孵化的代理。

**search** _query_
> 查询 skillhouse 索引。

**assemble**
> 重建已有的 skillhouse 代理。

**doctor**
> 诊断环境与依赖。

# PARAMETERS

**--no-generate**
> 跳过代码生成阶段，以便先审阅推断出的规格（配合 **hatch** 使用）。

**--force**
> 覆盖已存在的孵化代理。

**--dry-run**
> 预览输出而不写入文件。

# CAVEATS

需要 Python 3.11 或更高版本。编译过程会调用 LLM 提供方（OpenAI、DeepSeek、Anthropic 或任何 OpenAI 兼容端点），通过 TOML 文件配置，因此执行 **hatch** 步骤需要 API 密钥和网络连接。

# HISTORY

**agenthatch** 用 Python 编写，以 MIT 许可证发布。它于 2026 年推出，核心理念是把 markdown 技能文件当作源代码，编译成可部署的代理。

# SEE ALSO

[python](/man/python)(1), [pipx](/man/pipx)(1), [claude](/man/claude)(1)

# RESOURCES

```[Source code](https://github.com/agenthatch/agenthatch)```

<!-- verified: 2026-06-19 -->
