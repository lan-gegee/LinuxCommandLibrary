# TAGLINE

用于跨智能体对抗性代码审查的本地 MCP 服务器

# TLDR

**从克隆的仓库安装**

```pip install -e .```

接入 **Claude Code**（审查由 Codex 执行）

```claude mcp add paranoia -- paranoia-local --engine codex```

接入 **Codex**（审查由 Claude Code 执行）

```codex mcp add paranoia -- paranoia-local --engine claude```

**以选定的审查引擎运行 MCP 服务器**

```paranoia-local --engine codex```

```paranoia-local --engine claude```

**自定义审计日志目录**

```paranoia-local --engine codex --log-dir [path]```

# SYNOPSIS

**paranoia-local** **--engine** {**codex**|**claude**} [**--log-dir** _DIR_]

# PARAMETERS

**--engine** **codex**|**claude**
> 必填。指定由哪个本地编码智能体 CLI **执行**审查——即调用方之外的*另一个*智能体。在 Claude Code 中使用 **codex**；在 Codex 中使用 **claude**。

**--log-dir** _DIR_
> 审计日志目录（默认为 **~/.paranoia/logs**）。类闭包谱系状态**不会**跟随这个路径；它存放在 **~/.paranoia/lineages** 下（或由 **PARANOIA_STATE_ROOT** 决定）。

# DESCRIPTION

**paranoia-local** 是一个本地模型上下文协议（MCP）服务器，它让*另一个*前沿编码智能体对代码、计划和决策进行一次不带先入之见的对抗性审查。安装在 Claude Code 中时，审查由 Codex 执行；安装在 Codex 中时，审查由 Claude Code 执行。该服务器负责构建提示词，以**只读**方式运行拥有完整仓库访问权限的审查者 CLI，并返回结构化的评审意见。

MCP 工具包括 **critique_branch**、**critique_plan**、**query**、**rebut** 和 **arbitrate**（最后一项需要两个厂商的 CLI）。多轮工作可以跨轮次跟踪缺陷**类别**（类闭包 / 谱系状态），使循环能够收敛，而不是重复同样的发现。可选的项目级默认值存放在仓库根目录的 **.paranoia.toml** 中。

审查者被限制在沙盒中：Codex 运行在其操作系统的**只读**沙盒之下；Claude 则受限于收紧后的工具白名单，没有任何写入工具。服务器不内嵌任何 API 密钥——它直接调用你已登录的 CLI。审查会消耗订阅的智能体用量配额。

# CONFIGURATION

**CLI 选项：** **--engine**（必填）、**--log-dir**。

**磁盘上的状态：**

- **~/.paranoia/logs/** — 每次调用的 JSON 审计记录
- **~/.paranoia/lineages/** — 类闭包状态（不随 **--log-dir** 改变）
- **PARANOIA_STATE_ROOT** — 重定位谱系（及相关）状态

**仓库文件：** **.paranoia.toml**（或 **[paranoia]** 表）用于存放 **base_ref**、**project_summary**、**stakes**、**isolate**、**converge**、**class_closure**、**model**、**effort**、**web_search** 等默认值。调用时的参数优先于文件。

**MCP 客户端超时：**长时间的审查要求在宿主配置中调高工具/启动超时（例如 Codex 的 **tool_timeout_sec** / **startup_timeout_sec**）。

# CAVEATS

需要 **Python 3.11+**、**PATH** 中可用的 **git**，并且至少安装并登录了 **codex**（建议 ≥ 0.144）或 **claude** 其中之一；**arbitrate** 则两者都需要。审查可能运行数分钟并消耗可观的订阅配额。宿主 MCP 超时若停留在较短的默认值上，会导致每次调用都被杀掉。在审查计划或非分支引用时，类闭包谱系键必须唯一。

# HISTORY

**paranoia-local** 由 **Andrew Hillel** 编写，采用 **MIT** 许可证，以 PyPI / 控制台脚本 **paranoia-local** 的形式发布。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [git](/man/git)(1), [pip](/man/pip)(1)

# RESOURCES

```[Source code](https://github.com/subvertnormality/paranoia-local)```

```[Homepage](https://github.com/subvertnormality/paranoia-local)```

```[Documentation](https://github.com/subvertnormality/paranoia-local/tree/main/docs)```

<!-- verified: 2026-08-05 -->
