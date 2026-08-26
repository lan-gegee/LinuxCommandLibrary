# TAGLINE

带费用凭证的多模型 AI 拉取请求评审 CLI

# TLDR

**针对基准分支评审当前分支**

```juror review --base [main]```

**评审拉取请求并打印发现的问题**

```juror review --pr [1234] --repo [owner/name]```

**评审 PR 并发布置顶评论**

```juror review --pr [1234] --repo [owner/name] --post```

**使用陪审团预设**

```juror review --preset [balanced] --base [main]```

**从语料文件运行影子基准测试**

```juror benchmark --file [benchmarks/case.json]```

# SYNOPSIS

**juror** **review** [_options_]

**juror** **benchmark** [**--file** _path_]

# PARAMETERS

**review**
> 对本地分支或 GitHub 拉取请求运行多模型评审

**--base** _REF_
> 本地工作分支评审时用来做 diff 对比的基准引用

**--pr** _NUMBER_
> 要评审的拉取请求编号

**--repo** _OWNER/NAME_
> **--pr** 评审所用的 GitHub 仓库

**--post**
> 在拉取请求上发布（或更新）置顶评审评论

**--preset**, **--mode** _NAME_
> 陪审团预设：fast（默认）、balanced、high 或 ultra

**--models** _A,B,..._
> 将选定的预设（或自定义陪审团）缩小到这些模型 ID，仅本次运行生效

**--config** _PATH_
> Juror 配置文件路径（默认：仓库根目录的 **.juror.yml**）

**--cost-target** _USD_
> 每个 PR 的规划成本目标（美元）

**--repo-dir** _PATH_
> 本地仓库目录（供 CI 和高级调用方式使用）

**--json** _PATH_
> 将结构化评审结果以 JSON 写入 _PATH_

**--dry-run**
> 不把本次运行视为正式发布（配合 Action 试运行使用）

**benchmark**
> 针对经过裁定的语料文件评估评审质量

**--file** _PATH_
> 基准测试语料 JSON 文件

# DESCRIPTION

**juror**（npm 包为 **juror-ai**）是一款多模型代码评审工具。它通过各模型的原生 agent harness（Claude Code、Codex、OpenCode、Grok Build、Kimi Code 以及通用的 OpenAI 兼容端点）并行运行多个前沿模型，然后合并并去重各项发现，产出一份带合并置信度分数和逐模型费用凭证的报告。

它面向 GitHub 拉取请求和本地分支 diff。典型的安装方式是 **npm i -g juror-ai**（二进制名为 **juror** 和 **juror-ai**）。同一套代码路径也驱动着 **juror-ai/juror** GitHub Action，后者会在 PR 上发布置顶总结评论和分批的内联评审评论。

各项发现会锚定到 diff 上，受文件/行窗口约束，经精确匹配和相似度/仲裁阶段折叠去重，还可以通过 **publish_mode: consensus** 进行更高精度的可选过滤。各家提供商的密钥按 harness 相互隔离；模型永远不会收到 **GITHUB_TOKEN**。

# CAVEATS

需要 Node.js 20+ 以及至少一个 LLM 提供商的 API 密钥（**JUROR_OPENAI_API_KEY**、**JUROR_ANTHROPIC_API_KEY**、**JUROR_XAI_API_KEY**、**JUROR_FIREWORKS_API_KEY**，或不带前缀的厂商回退变量）。实际评审质量和费用取决于已安装的 harness CLI 和可用密钥。部分 harness 的费用是根据 token 数 × 刊例价估算的，而非提供商上报的美元金额。GitHub Actions 中被隐藏 secrets 的 fork PR 会按设计跳过。这不是自动修复机器人，也不是 linter。

# CONFIGURATION

仓库根目录的 **.juror.yml**（可选）。配置键包括 **preset**、**models**、**consensus**、**review**（publish_mode、severity_floor、paths_ignore）、**budget** 和 **output**。显式的 **models:** 列表会完全取代预设。

提供商密钥存放在环境变量或本地 **.env** 文件中（会自动加载；未被跟踪的文件不会暴露给模型检出）。

# SEE ALSO

[gh](/man/gh)(1), [claude](/man/claude)(1), [codex](/man/codex)(1), [opencode](/man/opencode)(1), [grok](/man/grok)(1)

# RESOURCES

```[Source code](https://github.com/Juror-AI/juror)```

```[Documentation](https://github.com/Juror-AI/juror#readme)```

<!-- verified: 2026-08-10 -->
