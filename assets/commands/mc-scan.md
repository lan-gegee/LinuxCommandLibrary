# TAGLINE

面向 AI 智能体工具与能力的静态扫描器（MakerChecker 的一部分）

# TLDR

**扫描**目录或工具文件中的高风险智能体能力

```mc-scan .```

**输出**机器可读的 JSON

```mc-scan . --json```

**生成**可分享的 Markdown 报告

```mc-scan . --markdown```

**写入**默认拒绝的策略文件

```mc-scan init .```

配合 `--fix` **生成**治理脚手架代码

```mc-scan . --fix```

出现灾难级发现时使 CI **失败**

```mc-scan . --fail-on CATASTROPHIC```

**运行**可选的 LLM 深度扫描（通过 Ollama 可保持私有）

```mc-scan . --llm --llm-provider ollama```

# SYNOPSIS

**mc-scan** [_options_] _path_  
**mc-scan** init [_path_] [_options_]

# DESCRIPTION

`mc-scan`（也可以 `npx @makerchecker/scan` 方式使用）是一个零依赖、完全离线的静态分析工具，用于检查 AI 智能体的工具、函数 schema 和源代码，发现该智能体能够执行哪些操作。

它能解析 OpenAI 风格的工具定义、MCP `tools/list` 输出、LangChain 装饰器、Vercel AI SDK 工具以及 JavaScript、TypeScript 和 Python 中的类似声明，并根据真实 AI 智能体事件数据库对每项能力进行分类，报告风险等级：

- **CATASTROPHIC**：不可逆的危害（删除数据、执行代码、转移资金等）
- **HIGH / MEDIUM**：影响重大但有明确边界

它还能检测危险的**组合风险**（例如：读取不可信输入 + 执行 shell 命令 = RCE 通道）。

该工具可以输出 JSON 和 Markdown 报告、强制执行策略文件，并且配合 `--fix` 可以为 `@makerchecker/embedded` 运行时生成开箱即用的治理包装器（默认拒绝 + 职责分离）。

它是更大的 MakerChecker 安全网关项目的一部分，但扫描器可以在开发、审计和 CI 中独立使用。

# PARAMETERS

**_path_**  
> 包含智能体工具定义的目录或 JSON 文件（默认为当前目录）。

**--json**  
> 输出机器可读的 JSON 而不是终端报告。

**--markdown**, **--md**  
> 输出可分享的 Markdown 结果卡片。

**--policy** _file_, **-p** _file_  
> 加载现有的 `mc-policy.json` 作为评估依据。

**--fail-on** _SEVERITY_  
> 若任何发现的严重度达到或超过阈值（CATASTROPHIC、HIGH 等）则以非零值退出。适用于 CI。

**init** [_path_]  
> 生成默认拒绝的 `mc-policy.json`（或通过 `--policy` 自定义路径）。

**--fix**  
> 扫描后，使用嵌入式原语编写治理脚手架（`mc-governance.mjs` 或通过 `--out` 指定路径）。

**--out** _file_, **-o** _file_  
> `--fix` 所写文件的输出路径。

**--llm**  
> 启用可选的 LLM 深度扫描（对工具重新排序或扫描源代码以发现潜在能力）。绝不会降低静态严重度。

**--llm-provider** _id_  
> anthropic（默认）、openai、openrouter、together、groq、ollama 或 openai 兼容端点。

**--llm-model** _id_  
> 为所选提供方覆盖模型。

**--llm-base-url** _url_  
> 自定义端点（用于 Ollama 或网关）。

**--llm-key** _key_  
> API 密钥（优先使用提供方的环境变量）。

**--llm-no-key**  
> 在支持的情况下显式不使用密钥运行。

**-h**, **--help**  
> 显示用法。

**--version**, **-v**  
> 打印版本。

# CAVEATS

默认扫描完全本地且确定性强。`--llm` 模式需要主动启用且具有非确定性；它不影响 `--fail-on` 的退出码。

"scan" 和 "mc-scan" 二进制文件由 `@makerchecker/scan` 提供。通用名称 "scan" 可能与 PATH 上的其他工具冲突；建议使用 `mc-scan` 或 npx 形式。

使用云端提供方的 LLM 扫描会将工具名称/描述（以及可选的代码片段）发送给该提供方。若需完全私有的运行方式，请使用 `--llm-provider ollama`。

该工具只分析声明的接口和部分源代码；运行时行为或高度混淆的代码可能无法完全覆盖。

# HISTORY

MakerChecker 及其 `mc-scan` 组件的诞生，是在一系列备受关注的智能体失败事件之后，为智能体 AI 系统提供实用且可审计的防护栏。该扫描器强调离线运行，并与开发工作流及生产网关都能集成。

# SEE ALSO

[deptrust](/man/deptrust)(1), [semgrep](/man/semgrep)(1)

# RESOURCES

```[Source code](https://github.com/makerchecker/MakerChecker)```

```[Homepage](https://makerchecker.ai)```

```[Documentation](https://makerchecker.ai/docs)```

<!-- verified: 2026-07-11 -->
