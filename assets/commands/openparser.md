# TAGLINE

通过 OpenParser API 解析 PDF 和图像

# TLDR

**安装** CLI 并登录

```npm install -g @openparser/cli && openparser auth login```

以 JSON 格式同步**解析**文档

```openparser parse sync [path/to/file.pdf] --json```

用 JSON 模式**提取**结构化字段

```openparser extract sync [path/to/file.pdf] --schema [path/to/schema.json]```

**检查** API 连通性和当前 profile

```openparser status --json```

**列出**最近的作业

```openparser jobs list --status succeeded --limit 10```

**上传**文件以便跨作业复用

```openparser files upload [path/to/file.pdf]```

# SYNOPSIS

**openparser** _command_ [_subcommand_] [_options_] [_args_]

# DESCRIPTION

**openparser** 是 OpenParser 的终端客户端。OpenParser 是一个文档智能 API，可将 PDF 和图像转换为文本、版面信息以及受模式约束的结构化数据。该 CLI 面向交互式使用、CI 作业和智能体工具链。

stdout 承载数据载荷（JSON、表格、文件字节）；stderr 承载状态信息。编写脚本时建议使用 **--json**，并用 **--quiet** / **-q** 抑制 stderr 上的非错误状态行。

身份验证使用已保存的 profile（**openparser auth login**），或在无界面环境中使用 **OPENPARSER_API_KEY**（以及可选的 **OPENPARSER_BASE_URL**、**OPENPARSER_PROFILE**）。命令行选项优先于环境变量，环境变量又优先于当前激活的 profile。

# COMMANDS

**status**

> 验证 API 连通性和 profile 上下文。

**auth**

> profile 管理（**login**、**use**，以及用于预发布/生产环境的命名 profile）。

**models**

> 列出 OCR 和 LLM 模型目录。

**parse**

> 同步、异步和批量解析提交（**parse sync**、**parse batch** 等）。

**extract**

> 受模式约束的字段提取、批量提取和模式建议。

**jobs**

> 列出作业并获取状态、结果和源字节。

**files**

> 上传并复用池化文件。

**pipelines**

> 管理已保存的提取流水线。

# CAVEATS

需要能够访问 OpenParser API（默认 **https://api.openparser.dev**）以及有效的 API 密钥或登录状态。该 CLI 是云客户端，不是离线本地 OCR 引擎。

# SEE ALSO

[curl](/man/curl)(1), [jq](/man/jq)(1), [pdftotext](/man/pdftotext)(1)

# RESOURCES

```[Source code](https://github.com/eigenpal/openparser)```

```[Homepage](https://openparser.dev)```

```[Documentation](https://docs.openparser.dev)```

<!-- verified: 2026-07-30 -->
