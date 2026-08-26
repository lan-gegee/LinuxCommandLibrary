# TAGLINE

面向编码代理的持久化、可自动失效的发现记忆

# TLDR

**初始化**项目记忆和代理会话启动钩子

```capn init
capn init --git```

**询问**已记录（chart）的答案

```capn ask "[where are payment webhooks handled?]"```

将有价值的发现连同支撑文件一起**记录**

```capn chart "[question]" --files [src/a.ts,src/b.ts] --details "[notes]"```

**列出**已记录的条目或**清理**过期的条目

```capn list
capn prune```

**移除**单条记录或使某文件的所有记录失效

```capn unchart [id]
capn bust [path/to/file]```

输出**会话上下文**说明（供钩子使用）

```capn context```

# SYNOPSIS

**capn** _command_ [_options_] [_args_]

# DESCRIPTION

**capn**（包名 **capn-hook**）为编码代理提供一次性的本地代码库发现记忆。在完成一次高成本搜索后，代理会**chart** 一条简短的问题以及回答该问题的文件。只要 chart 仍然匹配，**capn ask** 就会返回这些文件（JSONL 格式）；一旦任何支撑文件发生变化，相应条目会在误导之前被自动删除。

**capn init** 会创建 **.capn/** 目录、一个 QMD 搜索索引，以及为 Claude Code 和 Codex 注入 **capn context** 的 SessionStart 钩子（先 ask，发现重要内容后 chart）。检索默认使用语义混合搜索（**--no-embedding** 则只用 BM25）。chart 数据被 gitignore，仅存在于工作副本本地。

# PARAMETERS

**init** [**--git**] [**--embedding**|**--no-embedding**]
> 创建 **.capn/**、索引和钩子；可选的 post-commit 清理钩子

**ask** _question_
> 先执行清理再返回相关的 chart 命中；未命中时以退出码 1 结束

**chart** _question_ **--files** _a,b_ [**--details** _text_]
> 保存一条发现，并记录支撑文件的内容哈希

**unchart** _id_ / **bust** _path_ / **prune** / **list**
> 分别用于：删除一条记录、删除某文件的全部记录、删除所有过期记录、列出所有 chart

**context**
> 输出供代理钩子使用的“先询问、再记录”契约说明

# CAVEATS

默认的嵌入路径在首次使用时会下载模型（几百 MB 到约 2GB）。chart 是本地且一次性的——绝不能代替阅读当前源码。未命中时有意以非零码退出。

# SEE ALSO

[rg](/man/rg)(1), [claude](/man/claude)(1)

# RESOURCES

```[Source code](https://github.com/CyrusNuevoDia/capn-hook)```

```[Documentation](https://github.com/CyrusNuevoDia/capn-hook/blob/main/INSTALL.md)```

<!-- verified: 2026-07-14 -->
