# TAGLINE

AI 代理技能测试运行器

# TLDR

针对技能目录**运行**评估器

```npx agent-skills-eval [./skills]```

使用目标模型和评审模型**比较**带技能与基线时的表现

```npx agent-skills-eval [./skills] --target [gpt-4o-mini] --judge [gpt-4o-mini] --baseline```

**使用** YAML 配置文件

```npx agent-skills-eval --config [agent-skills-eval.yaml]```

在运行产物之外**生成** HTML 报告

```npx agent-skills-eval [./skills] --baseline --report```

**限制**并行评估数并筛选参与运行的技能

```npx agent-skills-eval [./skills] --concurrency [2] --include "[skills/translate*]" --exclude "[**/draft-*]"```

流式输出机器可读 JSONL 日志并在验证失败时中止

```npx agent-skills-eval [./skills] --log-format [jsonl] --strict```

# SYNOPSIS

**agent-skills-eval** [_options_] [_skills_root_]

# PARAMETERS

**\-\-config**  _file_
> 从 _file_ 加载 YAML 配置。CLI 标志会覆盖配置文件中的取值。

**\-\-workspace**  _dir_
> 结果的输出目录（默认：**./agent-skills-workspace**）。

**\-\-baseline**
> 启用 **with_skill** 与 **without_skill** 对比。未开启时只执行带技能的运行。

**\-\-target**  _model_
> 被评估表现的目标模型。

**\-\-judge**  _model_
> 用于给目标模型输出打分的评审模型。

**\-\-base-url**  _url_
> API 基础 URL（默认为 OpenAI 端点）。

**\-\-api-key-env**  _VAR_
> 存放 API 密钥的环境变量（默认：**OPENAI_API_KEY**）。

**\-\-include**  _glob_
> 只运行路径匹配 _glob_ 的技能。

**\-\-exclude**  _glob_
> 跳过路径匹配 _glob_ 的技能。

**\-\-concurrency**  _N_
> 并行评估运行的数量（默认：**4**）。

**\-\-layout**  _mode_
> 工作区布局：**iteration**（默认，带编号的运行文件夹）或 **flat**。

**\-\-strict**
> 检测到 **SKILL.md** 验证错误即判为失败。

**\-\-log-format**  _mode_
> 输出格式：**pretty**、**jsonl** 或 **silent**。

**\-\-report**
> 在工作区下生成一份静态 HTML 报告。

**\-\-report-output**  _dir_
> 覆盖报告的写入目录。

# DESCRIPTION

**agent-skills-eval** 是面向 **agentskills.io** 规范的测试框架。每个技能存放在一个目录里，内有描述其用途的 **SKILL.md**，外加一个枚举提示词、附带文件和评审打分断言的 **evals/evals.json** 文件。运行器加载每个 eval，把提示词发给配置好的目标模型——可选择是否注入技能内容——然后请评审模型按照声明好的断言给结果打分。

设置 **\-\-baseline** 后，每个 eval 都会跑两次：一次把技能内容载入上下文，一次不载入。对比两组得分，可以衡量技能是否真正提升了模型输出，而不是仅仅证明模型自己就能完成任务。输出、耗时、token 计数、工具调用以及评分理由都会持久化到工作区之下，保证每次运行都可复现、可审计。

该 CLI 既适合本地临时迭代，也适合 CI 流水线。**iteration** 布局为每次运行编号，方便前后对比；**flat** 布局则会覆盖同一棵结果树。日志既可以渲染成人性化的彩色进度，也能以 JSONL 流式输出供程序消费，还可以生成无需服务器即可浏览的静态 HTML 报告以便分享。

# CONFIGURATION

YAML 配置能让冗长的调用变得可控。每个 CLI 标志都有等价的配置键。

```
root: ./skills
workspace: ./agent-skills-workspace
baseline: true
target: gpt-4o-mini
judge: gpt-4o-mini
baseUrl: https://api.openai.com/v1
apiKeyEnv: OPENAI_API_KEY
include: ["skills/**"]
exclude: ["**/draft-*"]
concurrency: 4
layout: iteration
strict: true
report:
  enabled: true
  title: Agent Skills Report
logging:
  format: pretty
  verbose: false
  color: auto
targetParams:
  temperature: 0
judgeParams:
  temperature: 0
```

# EVALS FILE

每个技能需提供 **evals/evals.json**：

```
{
  "skill_name": "my-skill",
  "evals": [
    {
      "id": "eval-id",
      "name": "Human-readable name",
      "prompt": "The test prompt",
      "files": ["path/to/file.csv"],
      "expected_output": "Expected behavior description",
      "assertions": ["Criterion the judge checks"]
    }
  ]
}
```

# OUTPUT LAYOUT

一次运行会在工作区下生成逐 eval 的产物：

> **meta.json**, **benchmark.json** — 运行元数据与通过/失败摘要  
> **eval-{id}/with_skill/** — 载入技能时的输出、耗时与评分  
> **eval-{id}/without_skill/** — 基线运行的相同产物  
> **report/index.html** — 可离线查看的静态报告（配合 **\-\-report**）

# CAVEATS

成本随 eval 数量增长：启用 **\-\-baseline** 会令目标模型调用翻倍，还要叠加额外的评审调用。请谨慎设置 **\-\-concurrency**，避免触发速率限制。评审本身也是一个 LLM，打分存在随机性——在 **judgeParams** 里固定 **temperature: 0** 可获得稳定的分数。技能必须符合 agentskills.io 的 frontmatter 规则；把 **\-\-strict** 与 CI 结合起来，可以尽早发现格式错误的 **SKILL.md**。

# HISTORY

**agent-skills-eval** 由 Rishabh（darkrishabh）于 **2025** 年作为开源 npm 包发布，旨在为新兴的 **agentskills.io** 生态——一组可跨模型携带的 AI 代理技能——提供可复现的基准测试。它实现了该规范采纳的官方 iteration-N 产物布局。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [gemini](/man/gemini)(1), [npx](/man/npx)(1), [node](/man/node)(1)
