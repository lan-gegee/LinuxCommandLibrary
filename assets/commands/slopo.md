# TAGLINE

基于嵌入模型的代码重复检测工具

# TLDR

**初始化配置文件**

```slopo init```

**索引源代码以供分析**

```slopo index```

**为已索引的代码计算嵌入**

```slopo embed```

**生成重复报告**

```slopo analyze```

**校验配置并显示参数**

```slopo show-config```

# SYNOPSIS

**slopo** _command_ [_options_]

# PARAMETERS

**init**
> 创建配置文件模板。

**index**
> 解析 **source_dir** 中的代码单元并建立索引。

**embed**
> 通过配置的提供商为已索引的代码计算嵌入。

**analyze**
> 查找相似代码簇，并将报告写入 **report_dir**。

**show-config**
> 校验配置并显示所有参数。

**--config** _PATH_
> 覆盖默认配置文件的位置。

# DESCRIPTION

**slopo** 是一个利用嵌入模型检测非精确代码重复的 CLI 工具。与复制粘贴扫描器不同，它能发现散布在不同模块之间、或大文件中相距很远位置的语义相似片段——这类重复最难被人或 AI 智能体察觉。

工作流是 **init** → **index** → **embed** → **analyze**。索引阶段将受支持的语言解析为基于 AST 的代码单元，存入本地 SQLite 数据库（**slopo.db**）。嵌入调用通过兼容 LiteLLM 的提供商完成（例如 Voyage AI）。分析阶段比较余弦相似度，将配对归入簇，并按代码库中的距离重新排序。

支持的语言包括 Python、TypeScript、JavaScript、Java、Kotlin、C#、Go 和 Rust。审查过的簇可以加入 **slopo.ignore.txt**，从而在后续报告中排除。

# CONFIGURATION

配置文件中的关键设置：

> **source_dir** — 要索引的目录（必需）
> **source_dir_exclude** — .gitignore 风格的排除模式
> **db_file** — SQLite 数据库路径（默认：slopo.db）
> **report_dir** — 分析报告的输出目录
> **ignore_file** — 列出要跳过的已审查簇哈希的文本文件
> **embedding_model** — LiteLLM 格式的模型名称
> **embedding_dimensions** — 该模型的向量维度
> **embedding_api_key** — 提供商密钥（或设置 **SLOPO_EMBEDDING_API_KEY**）
> **similarity_threshold** — 配对之间的最小余弦相似度
> **rerank_threshold** — 基于距离重排后的最低分数
> **body_node_count_threshold** — 代码单元的最小 AST 主体规模

首次索引之后，若不删除 **slopo.db** 并重建索引，则 **source_dir**、**embedding_model**、**embedding_dimensions** 和 **body_node_count_threshold** 无法更改。

# CAVEATS

embed 步骤需要外部嵌入 API 密钥和网络访问。完全相同的重复会被报告，但处理方式与仅仅相似的代码不同。

# SEE ALSO

[rg](/man/rg)(1), [ast-grep](/man/ast-grep)(1)

# RESOURCES

```[Source code](https://github.com/rafal-qa/slopo)```

```[Homepage](https://slopo.dev)```

<!-- verified: 2026-07-11 -->
