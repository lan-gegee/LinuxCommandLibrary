# TAGLINE

带转录与视觉能力的 YouTube 视频知识引擎

# TLDR

**添加** YouTube 视频到库中

```mcptube add "[youtube_url]"```

以纯文本模式**添加**视频（不提取帧）

```mcptube add "[youtube_url]" --text-only```

**列出**库中的所有视频

```mcptube list```

**搜索**视频转录文本

```mcptube search "[query]"```

就视频内容**提问**

```mcptube ask "[question]"```

针对特定主题**生成报告**

```mcptube report [video_query] --focus "[topic]"```

**启动** MCP 服务器

```mcptube serve --stdio```

# SYNOPSIS

**mcptube** \<command\> [_options_]

# PARAMETERS

**add** _url_ [_--text-only_]
> 将 YouTube 视频添加到库；使用 --text-only 跳过帧提取

**remove** _query_
> 从库中移除视频

**list**
> 列出库中的所有视频

**info** _query_
> 显示视频的详细信息

**search** _query_
> 搜索视频转录文本

**ask** _question_
> 就视频内容提出自然语言问题

**frame** _query_ _timestamp_
> 提取特定时间戳的帧

**frame-query** _query_ _description_
> 查找与视觉描述匹配的帧

**classify** _query_
> 对视频内容进行分类

**report** _query_ [_--focus topic_] [_--format html_] [_-o file_]
> 生成关于某个视频的报告

**report-query** _topic_ [_--tag tag_]
> 按主题跨视频生成报告

**discover** _topic_
> 发现与主题相关的新视频

**wiki list** [_--type type_] [_--tag tag_]
> 列出 wiki 页面

**wiki show** _slug_
> 显示某个 wiki 页面

**wiki search** _query_
> 搜索 wiki 内容

**wiki toc**
> 显示 wiki 目录

**wiki export** [_--format html_] [_--page slug_]
> 导出 wiki 页面

**serve** [_--stdio_] [_--host host_] [_--port port_] [_--reload_]
> 启动 MCP 服务器

# DESCRIPTION

**mcptube** 是一个 YouTube 视频知识引擎，它从 YouTube 视频提取元数据、转录文本和帧，为它们建立语义搜索索引，并以 CLI 工具和 MCP (Model Context Protocol) 服务器的形式对外提供。

该工具构建一个持久的 wiki 知识库，随着每段视频的摄入不断丰富，而不是把视频当作孤立的、可搜索的碎片。它使用**场景切换检测**而非固定间隔采样来捕获高信息密度的帧。搜索将 FTS5 关键字匹配与 LLM 推理相结合，实现混合检索。

mcptube 有两种运行模式：**CLI 模式**使用你自己的 API 密钥（Anthropic、OpenAI 或 Google），结果确定；**MCP 透传模式**则由所连接的 AI 助手用其自身模型分析数据，避免重复计费。

# CAVEATS

需要 **Python 3.12 或 3.13**（ChromaDB 与 Python 3.14 不兼容），帧提取需要 **ffmpeg**。完整功能需要至少一家 LLM 提供方的 API 密钥（Anthropic、OpenAI 或 Google）。MCP 服务器目前仅限本地。不需要视觉功能时，可使用纯文本模式降低成本。

# HISTORY

mcptube 由 **0xchamin** 创建，用 **Python** 编写。它从简单的转录搜索工具发展为完整的视频知识引擎，具备 wiki 功能、基于视觉的帧分析以及与 AI 编程助手配合使用的 MCP 服务器集成。

# SEE ALSO

[yt-dlp](/man/yt-dlp)(1), [ffmpeg](/man/ffmpeg)(1), [youtube-dl](/man/youtube-dl)(1)
