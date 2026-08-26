# TAGLINE

Perplexity AI 的命令行界面，支持基于终端的使用方式

# TLDR

**向 Perplexity AI 提问**

```perplexity "What is quantum computing?"```

**用指定模型提问**

```perplexity -m [sonar-pro] "[question]"```

**在答案中显示引用来源**

```perplexity -c "[question]"```

**显示 token 用量**统计

```perplexity -u "[question]"```

**用 RAG 搜索笔记和聊天记录**

```perplexity rag "[query]"```

**设置 API 密钥**和配置

```perplexity setup```

# SYNOPSIS

**perplexity** [_options_] "_question_"

**perplexity** _command_ [_options_]

# PARAMETERS

**-m**, **--model** _model_
> 选择语言模型：sonar、sonar-pro、sonar-reasoning、sonar-reasoning-pro。

**-c**, **--citations**
> 在回答中显示来源引用。

**-u**, **--usage**
> 显示 token 消耗指标。

**-v**, **--verbose**
> 启用带详细输出的调试模式。

**-g**, **--glow**
> 应用与 Glow 兼容的 Markdown 格式。

**-a**, **--api-key** _key_
> 直接提供 API 密钥，而不通过环境变量。

# COMMANDS

**ask** _question_
> 查询 Perplexity AI，可选指定模型和主题参数。

**rag** _query_
> 使用 RAG 搜索笔记和聊天历史。支持 --mode（vector/keyword）和 --source（notes/chats）。

**rag-migrate**
> 把现有数据迁移到 RAG 知识库。

**rag-stats**
> 查看知识库统计信息。

**history**
> 显示聊天历史。

**note** --title _title_ --content _content_
> 创建新笔记，可选择附加标签。

**list-notes**
> 显示所有已保存的笔记。

**export-chat** _id_ --format _format_
> 将对话导出为 Markdown、JSON 或 Excel。

**setup**
> 以交互方式配置 API 密钥和相关设置。

# DESCRIPTION

**perplexity** 是 Perplexity AI 的命令行界面，让你能够在终端中使用其 AI 驱动的搜索与问答能力。它借助 Perplexity 的 Sonar 模型，将大语言模型与实时网络搜索结合在一起。

该 CLI 支持多个模型，从 **sonar**（最快）到 **sonar-reasoning-pro**（具备深度推理、能力最强）。回答可以附带引用，标明生成回复所依据的信息来源。

高级功能包括 RAG（检索增强生成），可以通过语义向量搜索或关键词匹配检索本地笔记和聊天历史。知识库使用 BGE 嵌入向量，实现极速的语义搜索。

聊天历史和笔记都存储在本地，可以导出为 Markdown、JSON 或 Excel 格式。本地操作可离线完成，而 AI 查询则需要联网。

# CAVEATS

需要设置含有有效 Perplexity API 密钥的 **PERPLEXITY_API_KEY** 环境变量。API 调用会产生费用，具体取决于所选模型和 token 消耗量。部分功能需要 Python 3.12 或更高版本。

# HISTORY

Perplexity AI 由曾任职于 Google 和 Meta 的工程师于 **2022 年**创立，以 AI 搜索引擎的形式问世。该公司在 **2024 年**推出 API，使开发者能以编程方式访问其 Sonar 模型。社区随后出现了多种 CLI 工具来提供终端访问，各种实现支持的功能各不相同，从简单问答到高级 RAG 能力都有覆盖。

# INSTALL

```aur: yay -S perplexity```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[anthropic](/man/anthropic)(1), [ollama](/man/ollama)(1), [llm](/man/llm)(1)
