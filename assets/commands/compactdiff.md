# TAGLINE

版本化、回放和审计 AI 代理会话记录

# TLDR

**监视** Claude Code 与 Codex 会话并将变更快照到本地保管库

```compactdiff watch```

**立即将某个记录文件快照到保管库**

```compactdiff snapshot [~/.claude/projects/proj/session.jsonl]```

**列出**已入库的会话及其版本历史

```compactdiff list```

对两个快照 SHA 执行 **diff**，查看压缩过程删除了什么

```compactdiff diff [shaA] [shaB]```

**导出**某条记录或入库 SHA 的自包含 HTML 回放

```compactdiff export [file|sha] -o [replay.html]```

在第 N 条对话消息后**分支**某条记录，输出截断的 JSONL 文件

```compactdiff branch [file|sha] --at [12] -o [fork.jsonl]```

**使用自定义保管库目录**（默认 **~/.compactdiff**）

```compactdiff --vault [path/to/vault] list```

# SYNOPSIS

**compactdiff** [**--vault** _DIR_] [**--no-redact** **--i-understand-sensitive-data**] _command_ [_args_]

# PARAMETERS

**--vault** _DIR_
> 存储内容寻址快照的保管库目录（默认 **~/.compactdiff**）。

**--no-redact**
> 不做脱敏处理，原样存储和导出记录数据。不安全；必须与 **--i-understand-sensitive-data** 配合使用。这两个全局标志需放在子命令之前。

**--i-understand-sensitive-data**
> 设置 **--no-redact** 时必须作出的确认声明。未设置时 CLI 会报错退出。

**snapshot** _file_...
> 立即将一个或多个记录文件快照到保管库。为每个文件打印短 SHA、NEW/未变化状态、会话 ID 和行数。

**watch**
> 轮询默认的 Claude Code 与 Codex 会话匹配模式，自动将每次变化快照到保管库。**--pattern** _GLOB_ 用单个自定义模式替换默认的匹配规则。**--interval** _SECONDS_ 设置轮询周期（默认 **5** 秒）。按 Ctrl-C 停止。

**list**
> 列出每个已入库的会话及其版本链（短 SHA、时间戳、行数）。

**diff** _sha_old_ _sha_new_
> 比较两个入库的快照（完整 SHA 或唯一前缀）。输出判定结论（**append-only** 仅追加或 **history-rewritten** 历史被改写）、保留/新增/删除行的计数，以及被删行与新增行的预览。

**export** _source_ **-o** _file_
> 将记录文件路径或入库 SHA 导出为单个自包含的 HTML 回放时间线（用户 / 助手 / 思考 / 工具事件）。无需服务器或外部资源。

**branch** _source_ **--at** _N_ **-o** _file_
> 在前 _N_ 条对话消息之后写出一条可供检查的记录截断前缀（路径或入库 SHA）。Codex 的开发者引导记录会被保留，但不占用分支编号。不承诺可在 Claude/Codex 中直接恢复。

# DESCRIPTION

**compactdiff** 是一个本地优先的 CLI，用于对 AI 编码代理的会话记录进行版本管理、审计和回放。Claude Code 与 Codex 这类代理以 JSONL 形式持久化会话，并可能在压缩（compaction）过程中原地改写它们，导致历史丢失，而且没有内置的方式来分享可读的会话。compactdiff 将观察到的状态快照存入 **~/.compactdiff** 下按内容寻址的保管库，因此压缩操作无法销毁更早的版本。

**watch** 默认轮询 Claude Code 项目目录（**~/.claude/projects/**）和 Codex 会话目录（**~/.codex/sessions/**）；**snapshot** 按需记录指定文件。**list** 显示各会话的版本链。**diff** 通过感知出现次数的有序行计数（包括重复行和空行）来证明一次改写到底删除了什么，并在存在时以行的 uuid 作为键。**export** 写出深色主题的 HTML 时间线，可以离线打开或作为单个文件发送。**branch** 则切出一段截断前缀供检查或由调用方自行播种。

需要 **Python 3.9+**，运行时仅依赖标准库。从源码检出版本安装可用 **python3 -m pip install -e .**（或在正式发布后安装 **compactdiff** 软件包）。对于常见密钥字段、令牌、电子邮箱、电话号码和家庭目录用户名，**snapshot**、**watch**、**export** 和 **branch** 默认启用脱敏。

# CAVEATS

代理记录中可能包含凭据、私密提示词、源代码和个人数据。默认脱敏是纵深防御而非保证——分享前请逐条检查回放内容，并妥善保管保管库。原始模式（**--no-redact**）可能存储机密信息。经过模式脱敏后，会话 ID 和正文仍可能包含敏感内容。监视器采用轮询机制（默认 5 秒），而非文件系统事件。分支文件是供检查用的截断前缀；它们不会自动在 Claude Code 或 Codex 中恢复会话。Cursor 及其他非 JSONL 的代理存储不在 v1 支持范围内。

# HISTORY

**compactdiff** 是一款纯标准库实现的 Python 工具（MIT 许可证），提供本地代理会话保管库、审计 diff、HTML 回放和分支功能。版本 **0.1.0** 聚焦于 Claude Code JSONL、Codex 原生会话以及可选的 Nerve Codex 运行器日志，默认开启脱敏。

# SEE ALSO

[diff](/man/diff)(1), [claude](/man/claude)(1), [codex](/man/codex)(1), [claude-hibernate](/man/claude-hibernate)(1), [agent-vault](/man/agent-vault)(1)

# RESOURCES

```[Source code](https://github.com/mkmkkkkk/compactdiff)```

```[Documentation](https://github.com/mkmkkkkk/compactdiff#readme)```

<!-- verified: 2026-08-09 -->
