# TAGLINE

面向编码智能体的代码库上下文图

# TLDR

**安装** CLI 并将其接入检测到的编码智能体

```npm install -g @nanonets/graft```

```graft init```

**预览** **init** 将写入哪些文件

```graft init --dry-run```

**构建** 结构图（tree-sitter，无需 API 密钥）

```graft build```

**添加** LLM 概念节点和逐符号摘要

```graft build --deep```

针对任务**查询**图

```graft ask "[how does authentication work]"```

**搜索**已索引的文件，按所属符号分组

```graft grep "[pattern]"```

**绘制**仓库地图（目录簇、枢纽、热点）

```graft map```

若图与代码产生偏差则让 CI **失败**

```graft check```

# SYNOPSIS

**graft** [_global-options_] _command_ [_args_] [_options_]

# DESCRIPTION

**graft**（npm 包 **@nanonets/graft**）为源码树构建本地上下文图，让编码智能体少花时间重新探索仓库。默认的 **graft build** 是一次确定性的 tree-sitter 处理：它在 **graft/** 下写入逐符号的连接关系图和逐文件卡片，且不需要 API 密钥。**graft build --deep** 会额外添加由 LLM 撰写的概念 markdown（**graft/*.md**）、逐符号摘要和关键片段摘录，使用你配置的服务商。

该图是一个可再生的缓存。**graft build** 会把 **graft/** 加入 **.gitignore**；队友在本地各自运行 **graft build**。你通常提交的是 **graft init** 写入的智能体接线配置（例如 **.claude/**）。查询命令会向上查找到最近一个已有 **graft/** 索引的祖先目录，因此从子目录中也能工作。

**graft init** 能检测编码智能体（Claude Code、Cursor、Gemini、Copilot、通过 **AGENTS.md** 的 Codex、Kiro、Windsurf、AdaL），并为每个宿主写入其原生的指令或技能文件。Claude Code 还会获得状态栏、编辑后钩子以及 **.mcp.json** 中的 MCP 服务器。在非 TTY 环境（CI、管道化的 shell）下，除非传入 **--agents**、**--yes** 或 **--all-agents**，否则 **init** 不会写入任何内容。

如果工作树发生了变化，**ask**、**skeleton**、**callers**、**grep** 和 **map** 会在回答前刷新结构图（不调用 LLM）。**graft check** 从不自动刷新，它是偏差报告（当图过期或缺失时以退出码 **1** 退出）。

完整保真度的解析器覆盖 TypeScript/JavaScript（JSX/TSX）、Python、Go 和 Java。更广泛的 tree-sitter 层级覆盖 Rust、C、C++、C#、Ruby、PHP、Kotlin、Scala、Swift、Elixir、Solidity、OCaml、Zig 和 Dart。不支持的文件会被跳过。当 **rust-analyzer**、**clangd**、**gopls**、**pyright** 或 **typescript-language-server** 位于 **PATH** 中时，**graft build --lsp** 可选地添加编译器级的调用边。

需要 **Node.js 20+**。采用 MIT 许可证。该软件包不含产品遥测；仅有的网络调用是你自行配置的 LLM 请求，以及用于打印升级提示的可选每日一次 npm 版本检查。

# COMMANDS

**init** [_dir_] [**--dry-run**] [**--agents** _ids..._] [**-y**] [**--all-agents**] [**--no-agents**] [**--no-build**] [**--no-mcp**] [**--no-hooks**] [**--no-global**] [**--list-agents**]

> 提示选择（或选择）智能体，写入指令/技能文件，可选地注册 MCP/钩子，并构建图（除非指定 **--no-build**）。智能体 id 包括 **claude**、**cursor**、**gemini**、**copilot**、**agents**、**kiro**、**windsurf**、**adal**。选择 **agents** 还可以在 **~/.codex/** 下写入用户级 Codex 文件（除非指定 **--no-global**）。

**build** [_dir_] [**--deep**] [**-e** _exts..._] [**--no-reuse**] [**--lsp**] [**-j** _n_] [**--include-dir** _name_]

> 构建 **graft/**。不带 **--deep** 时仅构建结构部分。在没有 **GRAFT_API_KEY** 的情况下使用 **--deep** 会回退到结构构建并打印警告。

**ask** _query_ [_dir_] [**-n** _limit_] [**--source**] [**--full**] [**--in** _scope_] [**--json**] [**--no-refresh**]

> 返回带 file:line 的排序节点。**--source** 内联摘录，使输出包可独立阅读。

**grep** _pattern_ [_dir_] [**-i**] [**--fixed**] [**--in** _path_] [**--json**] [**--no-refresh**]

> 对已索引文件进行穷举搜索，按所属符号分组并按耦合度排序。

**map** [_dir_] [**--max-dirs** _n_] [**--json**] [**--no-refresh**]

> 受 token 预算约束的定向概览：目录簇、枢纽和热点。

**callers** _symbol_ [_dir_] [**--direction** _in_|_out_] [**-d** _n_] [**--in** _path_] [**--json**] [**--no-refresh**]

> 入向引用（默认）或用 **--direction out** 查看出向引用。**-d** 进行传递式遍历（**all** 表示完整闭包）。

**skeleton** _file_ [_dir_] [**--json**] [**--no-refresh**]

> 仅输出单个文件的签名（仓库相对路径或唯一的基本文件名）。

**check** [_dir_] [**-e** _exts..._] [**--json**]

> 若 **graft/** 缺失或过期则以退出码 **1** 退出。不会重建。

**viz** [_dir_] [**-p** _port_] [**--no-open**]

> 启动内置的交互式查看器（默认端口 **4400**）。

**mcp** [_dir_]

> 基于 stdio 的 Model Context Protocol 服务器（**graft_find_code**、**graft_file_api**、**graft_trace_calls**、**graft_find_all**、**graft_repo_map**、**graft_check_freshness**）。

**version** / **upgrade**

> 打印已安装版本与最新 npm 版本的对比，或对最新版执行 **npm install -g**。

# PARAMETERS

**--dir** _path_

> 图目录（默认 **\<repo\>/graft**）。也可用 **GRAFT_DIR**。

**--provider** _openai_|_anthropic_

> **--deep** 所用的 LLM 接线格式（环境变量 **GRAFT_PROVIDER**）。**openai** 泛指任何 OpenAI 兼容端点。

**--model** _id_, **--api-key** _key_, **--base-url** _url_

> 模型、密钥和端点（环境变量 **GRAFT_MODEL**、**GRAFT_API_KEY**、**GRAFT_BASE_URL**）。

**-v**, **--version**

> 打印已安装的版本并退出。

**--no-refresh** / **GRAFT_NO_REFRESH=1**

> 对于查询命令，直接依据磁盘上的图作答，而不进行结构重建。**GRAFT_REFRESH=hash** 会对每个文件计算哈希，而不是信任大小加修改时间。

# CONFIGURATION

服务商设置可以放在环境变量或 **.env** 文件中（参见该软件包的 **.env.example**）：

**GRAFT_PROVIDER**
> **openai**（默认接线格式，包括 OpenRouter、Fireworks、Groq、LiteLLM、Ollama）或 **anthropic**（原生 API）。

**GRAFT_API_KEY**, **GRAFT_MODEL**, **GRAFT_BASE_URL**
> 运行 **graft build --deep** 所必需。仍兼容已被弃用的 **OPENROUTER_API_KEY** 作为回退。

**GRAFT_DIR**
> 覆盖图目录（与 **--dir** 相同）。

# CAVEATS

这是 NanoNets 的编码智能体 CLI，不是 Git 的提交嫁接（graft），也不是其他同名的旧 Unix 工具。在管道环境下不带 **--agents**/**--yes** 执行 **init** 是空操作。Codex 的 **agents** 接线可能改变机器上所有仓库共用的 **~/.codex/**。**--deep** 的质量取决于你选择的模型；结构图从不调用任何模型。语言覆盖范围仅限列出的 tree-sitter 集合。

# INSTALL

```aur: yay -S graft```

<!-- packages: 2026-08-14 -->

# SEE ALSO

[claude](/man/claude)(1), [cursor](/man/cursor)(1), [grep](/man/grep)(1), [npx](/man/npx)(1)

# RESOURCES

```[Source code](https://github.com/NanoNets/Graft)```

```[Homepage](https://graft.nanonets.ai)```

```[Documentation](https://github.com/NanoNets/Graft#readme)```

<!-- verified: 2026-08-14 -->
