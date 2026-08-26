# TAGLINE

面向 AI 开发团队的 Git 锚定意图账本

# TLDR

在当前 git 仓库中**初始化** rekal

```rekal init```

提交后**捕获**当前 AI 会话上下文

```rekal checkpoint```

**搜索**与查询相关的上下文

```rekal "[search query]"```

将**搜索**范围限定到特定文件或目录

```rekal --file [src/billing/] "[discount logic]"```

**查看**最近的检查点

```rekal log```

**深入查看**特定会话

```rekal query --session [session_id] --full```

将 rekal 数据**推送**到远程分支

```rekal push```

从远程分支**同步**团队上下文

```rekal sync```

# SYNOPSIS

**rekal** \<command\> [_options_] [_query_]

# PARAMETERS

**init**
> 在当前 git 仓库中初始化 rekal

**clean**
> 从仓库中移除 rekal 配置

**checkpoint**
> 在最新提交处捕获当前 AI 会话上下文

**push** [_--force_]
> 将 rekal 数据推送到远程分支

**sync** [_--self_]
> 从远程分支同步团队上下文

**index**
> 重建本地搜索索引数据库

**log** [_--limit n_]
> 显示最近的检查点

**query --session** _id_ [_--full_] [_--offset n_] [_--limit n_]
> 深入查看特定会话，可选分页参数

**query** _"SQL"_ [_--index_]
> 对数据或索引数据库执行原始 SQL 查询

**version**
> 打印 CLI 版本

**--file** _path_
> 将搜索范围限定为特定文件或目录

**--role** _human_
> 将搜索结果过滤为仅人类发言

# DESCRIPTION

**rekal** 在每次 git 提交时捕获 AI 会话上下文，创建一份永久的、只追加的开发推理与对话记录，与代码变更并存。它存储两个数据库：共享的 **data.db**（对话轮次、工具调用、检查点、涉及的文件——通过专用的 git 孤儿分支分发）和仅用于搜索的本地 **index.db**（全文索引、向量嵌入、文件共现图）。

该工具会安装 git 钩子，使检查点在每次提交时自动写入。检索结合了 BM25 词法搜索、LSA 和 Nomic 向量嵌入的混合方式，返回带评分的 JSON 以及最匹配的轮次索引，便于逐层下钻。2–10 MB 的原始会话记录可压缩至磁盘上约 300 字节。嵌入模型随二进制文件一起提供——无需 API 密钥、账户或外部服务。

# CAVEATS

目前仅支持 **Claude Code** 会话；对其他智能体的支持已在计划中。需要 **Git**，运行于 **macOS** 或 **Linux**。只追加设计意味着记录一经捕获便无法编辑或删除。数据绝不会离开你的本地机器或 git 仓库。

# HISTORY

rekal 由 **rekal-dev** 团队创建，使用 **Go** 编写。首次发布于 **2026 年**，是一款保存 AI 辅助开发背后推理上下文的工具，旨在解决 AI 编程智能体在团队工作流中使用时对话历史丢失的问题。

# SEE ALSO

[git](/man/git)(1), [claude](/man/claude)(1)
