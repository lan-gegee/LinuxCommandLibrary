# TAGLINE

在子代理长时间等待期间保持 Claude Code 提示词缓存的热度

# TLDR

通过预热器**运行 Claude Code**（交互式）

```uvx claude-thermos```

**传递一次性提示词**给 Claude

```uvx claude-thermos -p "[fix the bug]"```

在开始预热前**调整空闲阈值**（秒）

```uvx claude-thermos --idle [270]```

**更改预热周期之间的间隔**（秒）

```uvx claude-thermos --interval [270]```

限制每次空闲期间的**预热周期数上限**（或使用 auto 表示不限制）

```uvx claude-thermos --max-cycles [4]```

通过环境变量为单次运行**禁用预热**

```CLAUDE_WARMER_DISABLE=1 uvx claude-thermos```

# SYNOPSIS

**claude-thermos** [**--idle** _SECONDS_] [**--interval** _SECONDS_] [**-n** | **--max-cycles** _N_|**auto**] [**--subagent-window** _SECONDS_] [_claude_args_ ...]

# PARAMETERS

**--idle** _SECONDS_
> 主代理必须空闲多少秒后才运行一次预热周期。默认：**270**。环境变量：**CLAUDE_WARMER_IDLE_THRESHOLD_SEC**。

**--interval** _SECONDS_
> 预热周期之间的间隔秒数。默认：**270**。环境变量：**CLAUDE_WARMER_WARM_INTERVAL_SEC**。

**-n** _N_|**auto**, **--max-cycles** _N_|**auto**
> 每次空闲期间的最大预热请求数，或 **auto** 表示不限制。默认：**4**。环境变量：**CLAUDE_WARMER_WARM_MAX_CYCLES**。

**--subagent-window** _SECONDS_
> 子代理在其最后一次流量之后仍被视为活跃的时长。默认：**540**。环境变量：**CLAUDE_WARMER_SUBAGENT_ACTIVE_WINDOW_SEC**。

**-V**, **--version**
> 输出版本信息并退出。

**-h**, **--help**
> 显示帮助。

_claude_args_ ...
> 其余参数原样透传给 **claude** CLI。

# DESCRIPTION

**claude-thermos** 在 Anthropic 的 **Claude Code** CLI 前面启动一个小型本地反向代理，以便在子代理运行期间保持主代理的提示词缓存不过期。Claude Code 的提示词缓存 TTL 约为 **5 分钟**。当主代理等待某个子代理超过该时间时，主会话的前缀就会过期，下一轮对话将按更昂贵的缓存写入费率重新编码完整历史记录。预热会发送廉价的刷新请求（完全相同的可缓存前缀，**max_tokens: 1**），使恢复对话只需支付缓存读取费用，而不是完整重写。

该包装器将 **ANTHROPIC_BASE_URL** 指向一个观察 **/v1/messages** 流量的回环代理。谱系（缓存前缀）按模型、工具集和系统文本区分：第一个携带工具的谱系被视为主代理，其余视为子代理。当主谱系空闲而某个子代理仍然活跃时，预热器会在 TTL 之内按间隔发起请求。预热请求**直接**发送到 Anthropic API（不经过代理），因此不会干扰真实的会话流量。

会话遥测数据写入 **~/.claude-thermos/logs/**_session_id_**/`events.jsonl`** 和 **summary.json**，包含预热次数以及估计避免的重写 token 数。需要 **Python 3.11+** 以及位于 **PATH** 中的 **claude** 可执行文件。典型调用方式是通过 **uvx**，因此无需永久安装该软件包。

# CONFIGURATION

**CLAUDE_WARMER_DISABLE**
> 设为 **1** 即可在该进程中不带预热地运行 Claude。

**CLAUDE_WARMER_IDLE_THRESHOLD_SEC**, **CLAUDE_WARMER_WARM_INTERVAL_SEC**, **CLAUDE_WARMER_WARM_MAX_CYCLES**, **CLAUDE_WARMER_SUBAGENT_ACTIVE_WINDOW_SEC**
> 对应 CLI 选项的环境变量覆盖。

**~/.claude-thermos/logs/**_session_id_**/
> 每个会话的 **events.jsonl**（请求用量与预热决策）和 **summary.json**（节省量汇总估算）。

# CAVEATS

它并不取代 **claude**，而是包装它。预热仍会产生少量缓存读取成本和到 Anthropic 的网络流量。**summary.json** 中节省量的估算以基础输入 token 为单位而非美元——需乘以所用模型的输入价格。其行为取决于 Claude Code 的请求形态以及 Anthropic 缓存 TTL 保持约五分钟这一前提。需要一个可用的 Claude Code 安装和有效的 Anthropic 身份验证。

# HISTORY

由 **Iaroslav Zeigerman** 创建的 Python 软件包（PyPI 上的 **claude-thermos**），利用本地反向代理（基于 **mitmproxy**）在子代理长时间等待期间刷新 Claude Code 的提示词缓存前缀。以 MIT 许可证发布。

# SEE ALSO

[claude](/man/claude)(1), [uvx](/man/uvx)(1), [uv](/man/uv)(1)

# RESOURCES

```[Source code](https://github.com/izeigerman/claude-thermos)```

<!-- verified: 2026-07-23 -->
