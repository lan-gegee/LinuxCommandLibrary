# TAGLINE

为 AI 编程智能体的工具调用设置门禁的运行时防护栏

# TLDR

从 PyPI **安装** CLI（包名为 **doberman-core**）

```pip install doberman-core```

**接入** Claude Code 钩子（模式、防护规则、settings）

```doberman setup```

**检查**钩子、策略与决策数据库是否健康

```doberman doctor```

**设置**用于批准放宽策略操作的本地密码

```doberman password set```

**查看**最近的脱敏判定结果

```doberman log```

**代理**一个 MCP 工具服务器，让每次调用都先经过裁决

```doberman serve -- [npx -y @modelcontextprotocol/server-filesystem ~/project]```

通过真实引擎**回放**预置攻击（不会真正执行任何内容）

```doberman demo```

# SYNOPSIS

**doberman** [**-V**] _command_ [_options_]

# DESCRIPTION

**doberman** 是 Doberman 的命令行界面。Doberman 是一个面向编程智能体的自适应授权层。它位于执行路径上（作为宿主侧 **PreToolUse** 钩子或透明的 **MCP** 代理），在每个工具调用运行之前给出一个裁决：**PASS**（放行）、**AUTH**（暂停等待人工批准）或 **BLOCK**（永不执行）。不确定即拒绝。策略可以自动收紧；永久性的放宽则需要已登记的持有因子（possession factor，若设置了 TOTP 则用 TOTP，否则用本地 Doberman 密码）。

PyPI 上的发行包是 **doberman-core**。PyPI 上裸的 **doberman** 名称属于另一个不相关的废弃项目。安装之后，命令名和导入名仍然是 **doberman**。要求 Python **3.11+**。当前状态为 alpha（撰写本文时包版本为 **0.18.1**）。许可证为 Apache-2.0。

**doberman setup** 是 Claude Code 的接入路径：选择一种模式、保存偏好权重，并把钩子写入 **.claude/settings.json**（配合 **--global** 则写入 **~/.claude/settings.json**）。**doberman install-hooks --host codex** 则为 Codex CLI 接线。对于 Claude Desktop、Cursor 或任何 MCP 客户端，将 **doberman serve --** _downstream-server_ 注册为 MCP 命令即可；智能体客户端会自行启动该代理。OpenClaw 通过仓库内的适配器使用 **doberman hook openclaw**。

模式有 **light**、**balanced**（默认）、**strict** 和 **paranoid**。硬性拦截（机密外泄、破坏性命令、角色边界违规、确认过的先读后发）在所有模式下都一致。模式旋钮只决定模糊或高风险动作何时升级为 AUTH。与模式正交的是强制等级旋钮：**enforce**（默认）、**monitor**（记录酌情判定但不提示），或 **off**（跳过酌情层）。客观底线在任何状态下都始终生效。在没有对应账本条目的情况下手改 **policies.yaml** 中的 **enforcement: off** 会被钳制回 **enforce**。

判定结果在 **review**、**status**、**log**、TUI 和 **demo** 中按颜色标注（**BLOCK** 红色、**AUTH** 琥珀色、**PASS** 绿色）。输出被管道转发或设置了 **NO_COLOR** 时不使用颜色。诊断信息使用 **error:**、**warning:** 和 **note:** 前缀。

# COMMANDS

**setup** [**-y**] [**-m** _mode_] [**-g**] [**-p** _path_]

> Claude Code 的首次运行向导：选择模式、可选地调整偏好权重并写入钩子。**-y** 表示无提示接受 **balanced** 模式和项目级钩子。

**install-hooks** [**-g**] [**--local**] [**--host** _claude_|_codex_] [**-p** _path_] [**--dry-run**]

> 幂等的钩子安装。默认宿主为 Claude Code（**PreToolUse**、**PostToolUse**、**SessionStart**）。**--host codex** 会把 **doberman hook codex-pre** 写入 **hooks.json**。

**uninstall-hooks** [**-g**] [**--local**] [**--host** _claude_|_codex_] [**-p** _path_] [**--dry-run**]

> 只移除 Doberman 的钩子条目。不会删除 **.doberman/** 或设备级认证。请在 **pip uninstall doberman-core** **之前**运行本命令。

**uninstall** [**-p** _path_] [**-y**] [**--dry-run**]

> 移除项目级/本地的钩子**以及** **.doberman/**。需要持有因子；**-y** 会跳过输入目录名的确认步骤，但绝不会跳过持有因子校验。不动 **--global** 钩子和 **~/.doberman/**。

**doctor** [**-p** _path_] [**--json**]

> 只读健康检查（钩子、配置、决策数据库、2FA、强制等级、指纹密钥）。任一关键检查失败则以退出码 **1** 退出。

**status** [**-p** _path_] [**--json**]

> 角色、模式、偏好、策略摘要、钩子安装状态、污染标记、提权情况、最近决策。

**scan** [**-p** _path_] [**-q**] [**--json**] [**--mcp**]

> 只读的能力风险图（敏感文件仅显示名称）。**--mcp** 会静态收录仓库中的 MCP 配置；只报告模式类别，绝不输出原始 URL 或环境变量值。

**review** [**-p** _path_] [**-y**]

> 打印推荐的策略清单。**-y** 会写入 **.doberman/policies.yaml**。核心硬性拦截无法在此禁用。

**mode** [_light_|_balanced_|_strict_|_paranoid_] [**-p** _path_]

> 打印或设置安全模式。调低需要持有因子；调高立即生效。

**enforcement** [_enforce_|_monitor_|_off_] [**-p** _path_]

> 打印或设置强制等级旋钮。放松操作受门禁保护且需通过账本校验。

**prefs** [_dimension_ _value_] [**-p** _path_]

> 打印 SL5 权重（**confidentiality**、**reversibility**、**interruption_tolerance**、**blast_radius**，各自取值范围 **[0, 1]**）或设置其中一项。调低权重受门禁保护。客观底线永远不会移动。

**role enable-default** / **role disable-default** [**-p** _path_]

> 在不存在 **.doberman/role.yaml** 时，选择加入（或受控退出）内置的最小权限编程助手角色。

**policy-history** [**-n** _n_] [**-p** _path_] [**--json**]

> 仅追加的策略变更账本，包括被拒绝的放宽操作。

**log** [**-n** _n_] [**-p** _path_] [**--jsonl**]

> 最近的脱敏决策记录（路径类别、原因码、裁决、认证结果）。不含原始目标或机密。

**tui** [**-p** _path_]

> 交互式日志浏览器。需要 **pip install "doberman-core[tui]"**。

**dash** [**--port** _n_] [**-p** _path_]

> 仅限 localhost 的仪表板（默认 **127.0.0.1:8642**），带一次性 URL 令牌。需要 **pip install "doberman-core[dash]"**。

**demo** [**-p** _path_] [**--mode** _mode_] [**--fast**]

> 通过真实引擎播放脚本化的攻击片段。不会执行任何内容，也不会弹出提示。若预期裁决不符则返回退出码 **1**。

**session-summary**

> 从 **~/.doberman/metrics.db** 打印设备级累计统计后退出。总是返回退出码 **0**。隐藏别名：**dashboard**。

**serve** [**-p** _path_] **--** _server_ [_args_...]

> 位于 _server_ 之前的 MCP stdio 代理。日志走 stderr；stdout 即 MCP 通道。不要为了"启动"某个智能体而手动运行它 —— 该进程由 MCP 客户端负责拉起。

**hook pre** / **hook post** / **hook openclaw** / **hook codex-pre**

> 宿主钩子入口点（stdin 接收 JSON）。由 **install-hooks** 接线，并非供交互式输入使用。

**password set** [**--force**]

> 登记或轮换本地密码持有因子。

**2fa setup** [**--force**] / **2fa remove** / **2fa reset-lockout**

> 登记 TOTP（会打印一个配置 URI）、移除 TOTP（需证明当前的验证码），或清除锁定状态（需证明密码）。

**taint clear** [**-p** _path_]

> 受门禁保护的擦除操作，清除本仓库的机密读取污染标记以及读与发送的指纹。

**tools approve** _name_ [**-p** _path_]

> 在带外审查后，对已变更的 MCP 工具 schema 进行受门禁保护的重新固定。

**memory** [**-p** _path_] / **memory reset** [**--entity** _id_] / **memory prune --older-than-days** _n_

> 脱敏后的学习记忆摘要；受门禁保护的擦除；不受门禁限制的保留期修剪（不触及决策日志）。

**tune** [**-p** _path_] [**--json**] [**--last** _n_] [**--min-occurrences** _n_] [**--accept** _id_]

> 摩擦报告。**--accept** 通过同一个放宽门禁授予一段有时限的长期提权。可用 **revoke** 撤销。

**revoke** _elevation-id_ [**-p** _path_]

> 撤销一个处于活动状态的角色提权（见 **status**）。

**version**

> 打印已安装的版本（等同于 **-V**）。

# PARAMETERS

**-V**, **--version**

> 打印已安装的版本并退出（立即生效）。

**-p**, **--path** _dir_

> 以哪个仓库根目录的 **.doberman/** 策略来约束本命令（默认 **.**）。对于 **serve**，同一标志用于选择策略根目录。

**-y**, **--yes**

> 在 **setup**、**review** 和 **uninstall** 上接受默认值 / 跳过输入式确认。永远不会跳过持有因子校验。

**--json** / **--jsonl**

> 为 **doctor**、**status**、**scan**、**policy-history**、**tune**（**--json**）或 **log**（**--jsonl**）输出机器可读格式。

**--host** _claude_|_codex_

> **install-hooks** / **uninstall-hooks** 要编辑哪种宿主环境。

**--install-completion**

> Typer shell 补全安装器（需在 **pip install** 之后使用）。

# CONFIGURATION

**.doberman/**
> 每个仓库的控制平面（不提交入库）。**policies.yaml** 保存模式、强制等级、偏好权重和策略清单。**role.yaml** 是可选的显式角色定义（优先于 **role enable-default**）。决策数据库、污染标记和工具固定项也存放在这里。

**.doberman/audit_webhook.yaml**
> 可选的 HTTPS 接收端，用于接收脱敏后的决策记录。**auth_env** 指定一个环境变量，其值作为 **Authorization** 头发送。投递尽力而为，绝不阻塞裁决。

**.doberman/artifact_pins.yaml**
> 可选的取件后 sha256 固定项。未固定的工件不做校验。

**~/.doberman/**
> 设备级的密码 / TOTP 登记、指纹密钥和 **metrics.db**。在本机的所有项目之间共享。

**DOBERMAN_TURN_GATE**
> 设为 **off** 可禁用可选的推理前回合门禁（没有宿主推理前钩子的 MCP 代理部署本身就不含此机制）。

**DOBERMAN_EXPLAIN_LLM**
> 设为 **1**（并安装 **doberman-core[explain]** 且提供 **ANTHROPIC_API_KEY**）可让 TUI 用更通俗的语言改写某条裁决的理由。模型仅充当叙述者；任何失败都会回退到离线模板。

**NO_COLOR**
> 设置为非空值时，CLI 输出不使用颜色。

# CAVEATS

这是 fu351 的智能体防护栏 CLI，而不是 PyPI 上另一个恰好也叫 **doberman** 的无关项目。宿主钩子只运行确定性的客观底线（不含自适应/主观层）；该层目前需要通过 MCP 代理路径才能启用。静态出站分类可能漏掉运行时构造的主机、嵌套 shell、DNS 标签外泄和 **/dev/tcp**。未应答的 AUTH 会超时转为拒绝（桌面对话框 2 分钟，20 分钟为兜底上限）。坐在键盘前的人仍然可以禁用宿主钩子。卸载软件包之前必须先卸载钩子，否则每个受门禁保护的工具调用都会因 **doberman: command not found** 而失败。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [openclaw](/man/openclaw)(1), [cursor](/man/cursor)(1), [pip](/man/pip)(1), [npx](/man/npx)(1)

# RESOURCES

```[Source code](https://github.com/fu351/Doberman-Core)```

```[Documentation](https://github.com/fu351/Doberman-Core/blob/main/docs/SETUP.md)```

<!-- verified: 2026-08-18 -->
