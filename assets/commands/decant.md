# TAGLINE

面向 Claude Code 和 Codex 会话日志的本地优先分析工具

# TLDR

**启动**本地 Web UI（索引日志并监视变更）

```decant```

仅**索引**新增和变更的会话而不启动服务

```decant sync```

**列出**会话，然后**渲染**一份会话记录

```decant ls```

```decant show [1]```

**搜索**会话记录和工具调用

```decant search "[auth bug]"```

**按模型汇总**用量，再细分 token 和估算成本

```decant stats --by model```

```decant economics```

将会话**导出**为 Markdown

```decant export [1] > [session.md]```

使用**临时数据库**并跳过对默认源目录的摄取

```decant --db [/tmp/decant.db] --no-sync serve --no-open```

# SYNOPSIS

**decant** [_global-options_] [_command_] [_args_]

# PARAMETERS

**--db** _path_
> SQLite 归档路径（默认 **~/.decant/decant.db**，或环境变量 **DECANT_DB**）

**--json**
> 输出机器可读的 JSON

**--format** _table_|_json_|_md_
> 读取类命令的输出格式

**-q**, **--quiet**
> 抑制非必要的输出

**--no-color**
> 禁用 ANSI 颜色

**--no-sync**
> 跳过读取前同步。配合 **serve** 时还会禁用源目录监视器（仍可手动 **POST /api/sync**）

**--version**
> 打印 Decant 版本并退出

# COMMANDS

**serve** [**--host** _addr_] [**--port** _n_] [**--claude-dir** _dir_] [**--codex-dir** _dir_] [**--interval-ms** _ms_] [**--debounce-ms** _ms_] [**--no-fs-watch**] [**--trusted-peer** _ip_] [**--no-open**]
> 运行本地 UI 并保持索引最新。不带参数调用 **decant** 时这是默认行为。除非覆盖，否则绑定 **127.0.0.1:3000**。绑定到非回环地址时，**--trusted-peer**（可重复或逗号分隔）允许 API 客户端访问。

**sync** [**--claude-dir** _dir_] [**--codex-dir** _dir_] [**--path** _path_]
> 扫描会话目录，插入或更新新增及变更的会话。**--path** 可重复使用，用于摄取选定的文件或目录树。

**watch** [**--claude-dir** _dir_] [**--codex-dir** _dir_] [**--interval-ms** _ms_] [**--debounce-ms** _ms_] [**--no-fs-watch**]
> 监视源目录并刷新归档（文件系统事件加定期全量扫描）。

**ls** [**--tool** _name_] [**--model** _name_] [**--project** _path_] [**--include-subagents**] [**--limit** _n_]
> 列出会话（默认上限 50）。也可用 **session ls**。

**show** _id_
> 渲染完整的会话记录。也可用 **session show**。

**project ls**
> 列出项目及其会话数量和估算成本。

**search** _query_ [**--limit** _n_]
> 对消息、工具调用和会话记录进行全文搜索（默认上限 30）。

**stats** [**--by** _tool_|_model_|_project_|_day_]
> 用量和成本汇总。不带 **--by** 时打印总计。

**tokens**, **economics**
> 将 token、估算成本、代理耗时和用户等待时间细分为上下文、规划、编码和沟通四类。

**files** [**--group** _path_|_ext_] [**--op** _read_|_edit_|_write_|_delete_] [**--limit** _n_]
> 代理频繁操作的文件热点。

**tool stats**, **tool ls** [**--errors-only**] [**--limit** _n_]
> 工具调用用量统计。

**mcp stats**, **mcp ls** [**--limit** _n_]
> MCP 服务器用量统计。

**export** [_id_] [**--all**] [**--include-subagents**] [**--as** _md_|_json_|_trajectory_] [**--out** _dir_]
> 导出单个会话（或用 **--all** 导出到 **--out** 目录），格式为 Markdown、JSON 或 trajectory-v1 记录文件。

**distill script** [**--project** _name_] [**--work-type** _type_] [**--from-session** _id_] [**--as** _sh_|_just_|_make_] [**--min-frequency** _n_] [**-o** _path_] [**--force**]
> 从命令历史生成工作流脚本。

**distill replay** _id_ [**--include-errors**] [**-o** _path_] [**--force**]
> 将一个会话的命令和文件写入复现为脚本。

**distill skill** [**--project** _name_] [**--work-type** _type_] [**--kind** _skill_|_agents_|_command_] [**-o** _path_] [**--force**]
> 从历史生成 **SKILL.md**、AGENTS.md 片段或斜杠命令。

**db info**, **db migrate**, **db vacuum**
> 检查归档、应用 schema 迁移或回收空闲空间。

**recommendations ls** [**--status** _open_|_implemented_|_all_], **recommendations mark** _key_
> 列出或标记已持久化的建议。

**completion** _bash_|_zsh_|_fish_|_powershell_|_elvish_
> 打印 Shell 补全脚本。

# DESCRIPTION

**decant** 把机器上已有的 Claude Code 和 Codex 会话日志转化为可搜索的 SQLite 归档和本地分析 UI。它报告 token 消耗、估算成本、上下文窗口占用、代理耗时、涉及的文件与工具以及 MCP 活动。直接运行 **decant** 会启动 **serve**：索引数据源、监视变更并打开 **http://127.0.0.1:3000**。

默认数据源是 Claude Code 的 **~/.claude/projects** 和 Codex 的 **~/.codex**（包括已归档的 Codex 会话）。除非设置了 **--no-sync** 或 DECANT_NO_SYNC，读取类命令会先同步。**sync** 以事务方式插入新会话并替换变更的会话；未变化的文件会被跳过。删除或重建归档不会删除原始 JSONL 日志。

本地 HTTP API 没有凭据校验。除非你明确信任远端节点，否则请保持绑定地址在回环接口上。运行中的服务器在 **/api/openapi.json** 提供 OpenAPI 文档。

Decant 是本地优先的：运行时不发起任何出站网络调用，会话记录始终留在本机。发布的二进制覆盖 x64 和 arm64 架构的 Linux 和 macOS；没有原生 Windows 二进制。

# CONFIGURATION

**DECANT_DB**
> 归档路径（默认 **~/.decant/decant.db**）

**DECANT_CLAUDE_DIR**
> Claude Code 项目目录（默认 **~/.claude/projects**）

**DECANT_CODEX_DIR**
> Codex 主目录（默认 **~/.codex**）

**DECANT_NO_SYNC**
> 设置后等同于 **--no-sync**

**DECANT_NO_OPEN**
> **serve** 启动后不打开浏览器

**DECANT_TRUSTED_PEERS**
> 未绑定到回环地址时允许调用 API 的 IP 或 IPv4 CIDR，逗号分隔。空值表示不信任任何节点。

**DECANT_TRUST_DEFAULT_GATEWAY**
> 设为 **1** 时自动信任容器网桥网关（Docker 通过 **--publish** 发布到回环地址的场景）。默认关闭。

**DECANT_LOG_LEVEL**
> 结构化日志级别

Shell 安装脚本（**install.sh**）还支持 **DECANT_VERSION**、**DECANT_INSTALL_DIR**（默认 **~/.local/bin**）、**DECANT_NO_MODIFY_PATH** 和 **DECANT_BASE_URL**。

# CAVEATS

serve API 无身份验证。将端口发布到所有网络接口会暴露归档。绑定到非回环地址而未配置 **--trusted-peer** 或 DECANT_TRUSTED_PEERS 时，通常会返回 **403 forbidden remote**。

费用基于 Decant 的价格表估算。用更新版本的 Decant 重建归档时，即使源日志未变，历史数字也可能改变。

在 Decant 中归档或删除会话会隐藏或移除索引行，并可能对身份做墓碑标记以防后续同步将其复活。原始 JSONL 仍保留在原处；如果原始会话记录也必须删除，请通过 Claude Code 或 Codex 移除。

当源日志中存在无法解析的行（内容被丢弃）时，**sync** 以退出码 **3** 结束。其他摄取问题会报告错误码但不会导致命令失败。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [confessor](/man/confessor)(1)

# RESOURCES

```[Source code](https://github.com/dosu-ai/decant)```

```[Documentation](https://github.com/dosu-ai/decant#readme)```

<!-- verified: 2026-08-13 -->
