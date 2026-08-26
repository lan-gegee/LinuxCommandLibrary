# TAGLINE

将代码库转化为供 LLM 使用的紧凑 XML 蓝图

# TLDR

**生成项目的结构蓝图**

```crespo [./myproject]```

**将蓝图写入指定的文件**

```crespo [./myproject] --output [blueprint.xml]```

**添加 AI 生成的一行式文件摘要**

```crespo [./myproject] --mode summary --groq [api_key]```

**包含已抹除机密信息的完整源码**

```crespo [./myproject] --mode concat```

**直接分析远程 GitHub 仓库**

```crespo --git [https://github.com/user/repo]```

# SYNOPSIS

**crespo** _PATH_ [**--mode** _structure|summary|concat_] [**--git** _URL_] [**--groq** _KEY_] [**--output** _FILENAME_]

# DESCRIPTION

**crespo** 将源码树转换为一种紧凑的 XML"蓝图"，用于喂给大语言模型。它不是简单拼接原始文件，而是借助 **Tree-sitter** AST 解析，仅提取每个文件中的结构性内容——导入、类、函数以及模块之间的关联。据该项目报告，与直接粘贴整个代码库相比，这能显著减少 token 消耗。

它有三种工作模式。默认的 **structure** 模式输出由导入、类和函数构成的 AST 骨架。**summary** 模式为每个文件添加一行 AI 生成的描述，需要 Groq API 密钥。**concat** 模式将每个文件的完整源码嵌入结构化 XML 中，同时抹除检测到的机密信息。

crespo 通过 **pip install crespo** 从 PyPI 安装，支持 Python、JavaScript、TypeScript、JSX、TSX、Rust、Go、Java、C 和 C++。它既可以分析本地目录，也可以通过 **--git** 就地克隆并分析 GitHub 仓库。

# PARAMETERS

**--mode** _structure|summary|concat_

> 输出模式。**structure**（默认）输出 AST 骨架；**summary** 为每个文件添加 AI 摘要；**concat** 包含已抹除机密的完整源码。

**--git** _URL_

> 直接克隆并分析 GitHub 仓库，而不是本地路径。

**--groq** _KEY_

> **summary** 模式所用的 Groq API 密钥。该密钥会被保存，供以后的运行使用。

**--output** _FILENAME_

> 将蓝图写入自定义的文件名。

# CAVEAT

**summary** 模式并非纯本地运行：它会把文件信息发送到 Groq API 并要求提供有效的 API 密钥，因此除非你能接受这一点，否则请不要对私有或敏感代码使用该模式。尽管 **concat** 模式会尝试抹除机密信息，但自动抹除只是尽力而为，在分享输出之前不应把它当作可靠保障。

# SEE ALSO

[repomix](/man/repomix)(1), [git](/man/git)(1), [pip](/man/pip)(1)

# RESOURCES

```[Source code](https://github.com/hrudulmmn/crespo)```

<!-- verified: 2026-06-23 -->
