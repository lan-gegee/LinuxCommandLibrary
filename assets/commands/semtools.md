# TAGLINE

终端中的语义文档搜索、解析与问答工具

# TLDR

**将 PDF 解析**为文本/markdown 路径

```semtools parse [files...]```

在文本文件中进行**语义搜索**

```semtools search "[query]" [files...] --max-distance [0.3]```

针对文档**提问**

```semtools ask "[question]" [files...]```

**使用工作区**缓存嵌入向量

```semtools workspace use [name]```

导出后**结合工作区搜索**

```export SEMTOOLS_WORKSPACE=[name]; semtools search "[query]" [dir]/*.txt```

# SYNOPSIS

**semtools** *command* [*options*] [*args*]

# DESCRIPTION

**semtools** 是一款 Rust 编写的 CLI，专注于以文档为核心的工作流：**parse** 将 PDF 和办公文档转换为文本（默认后端：LlamaParse API），**search** 利用嵌入向量执行本地语义关键词搜索，**ask** 在语料库上运行带有搜索/读取工具的 LLM 智能体，**workspace** 则将大型集合的嵌入向量缓存到 **~/.semtools/workspaces/** 目录下。

通过 **npm i -g @llamaindex/semtools** 或 **cargo install semtools** 安装。专为 Unix 流水线设计（stdin/stdout 与 **xargs**）。

# PARAMETERS

**parse** [*OPTIONS*] *FILES*...

> 解析文档。**-b**, **--backend** 选择解析器（默认 **llama-parse**）。**-c** 配置文件路径。**-v** 详细输出。

**search** [*OPTIONS*] *QUERY* [*FILES*...]

> 语义搜索。**-n**, **--n-lines** 上下文行数（默认 3）。**--top-k** 结果数量。**-m**, **--max-distance** 距离阈值。**-i** 忽略大小写。**-j** JSON 输出。使用 stdin 时文件参数可选。

**ask** [*OPTIONS*] *QUERY* [*FILES*...]

> 针对文件或 stdin 的问答智能体。需要 LLM API 密钥（兼容 OpenAI；见配置）。

**workspace** **use**|**status**|**prune**

> 管理嵌入工作区。**use** 会打印设置 **SEMTOOLS_WORKSPACE** 所需的 shell export 指令。

# CAVEATS

**parse** 默认需要 LlamaIndex Cloud API 密钥。**ask** 需要 LLM 服务商的密钥。**search**/**workspace** 在本地运行但会使用嵌入模型（有下载和运行时开销）。未经审阅请勿将机密文档发送到第三方解析/LLM API。

# INSTALL

```nix: nix profile install nixpkgs#semtools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rg](/man/rg)(1), [pdftotext](/man/pdftotext)(1), [jq](/man/jq)(1)

# RESOURCES

```[Source code](https://github.com/run-llama/semtools)```

<!-- verified: 2026-07-19 -->
