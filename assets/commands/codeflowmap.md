# TAGLINE

绘制代码库的导入、调用和数据流图

# TLDR

**启动**交互式 Web UI 来探索图结构

```bunx codeflowmap serve```

**扫描**仓库并生成依赖图与 Obsidian vault

```bunx codeflowmap scan [./repo] -o [.codemap]```

通过 LLM **添加语义标注**（读、写、认证、数据流）

```bunx codeflowmap annotate -o [.codemap]```

# SYNOPSIS

**codeflowmap** _command_ [_options_]

command := **serve** | **scan** | **annotate**

# DESCRIPTION

**codeflowmap** 是一款静态分析工具，它使用 TypeScript Compiler API 构建确定性的依赖图来绘制代码库地图，随后可选择叠加由开放权重 LLM 生成的语义标注。它借助精确的模块解析（而非猜测）提取文件级导入图，提取符号到符号的函数级调用图，以及覆盖写、读、配置和认证路径的数据流标注。

结果写入 **.codemap** 目录，其中包含 **graph.json**（完整的依赖与调用图）、一个 Markdown vault（每个源码文件对应一个文件，并通过 **[[wikilinks]]** 相互链接，供 Obsidian 使用），以及以内容哈希为键的标注缓存。**serve** 命令会打开一个交互式 Web UI（默认 http://localhost:4321），用于浏览图结构。

codeflowmap 需要 **Bun** 运行时（1.0 或更新版本），最简单的运行方式是使用 **bunx**，它无需单独的安装步骤即可执行。

# COMMANDS

**serve**
> 启动用于探索图结构的交互式 Web UI。

**scan**  _path_
> 从仓库中提取导入图和调用图，并生成 Obsidian vault。

**annotate**
> 为已扫描的图添加 LLM 生成的语义层（写、读、认证、数据流）。

# PARAMETERS

**-o**  _dir_
> 生成产物的输出目录（例如 **.codemap**）。

# CAVEATS

该工具通过 TypeScript Compiler API 针对 TypeScript 和 JavaScript 项目，因此不分析其他语言。它是早期实验性软件；**annotate** 步骤依赖 LLM，其输出应经过审查而非盲目信任。

# SEE ALSO

[bunx](/man/bunx)(1), [bun](/man/bun)(1), [tsc](/man/tsc)(1)

# RESOURCES

```[Source code](https://github.com/man-consult/code-mapper)```

<!-- verified: 2026-06-22 -->
