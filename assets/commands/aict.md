# TAGLINE

面向 AI 代理、带结构化 XML/JSON 输出的 Unix 风格工具

# TLDR

以 **XML**（默认）**列出**目录

```aict ls [path]```

以 **JSON** **列出**目录

```aict ls [path] --json```

以经典的**纯文本** coreutils 风格**列出**

```aict ls [path] --plain```

递归**搜索**并返回结构化命中结果

```aict grep "[pattern]" [path] -r```

**查看**文件内容及元数据

```aict cat [file]```

**对比**两个文件并给出带类型的变更

```aict diff [old] [new]```

**运行**内置 **MCP** 服务器（stdio）

```aict mcp```

**显示所有工具的帮助**

```aict --help```

# SYNOPSIS

**aict** _tool_ [_args_] [_--xml_|_--json_|_--plain_]

# DESCRIPTION

**aict** 重新实现了一组常用 Unix 工具，使 AI 代理能够直接消费**带标签的结构化输出**，而不必解析面向人类的纯文本。默认情况下工具输出 XML；**--json** 和 **--plain** 可切换格式。字段遵循一致的约定：绝对路径、Unix 纪元时间戳（常附带 age 字段）、以字节为单位并附带人类可读形式的文件大小，以及结构化的错误元素（许多失败场景不再依赖自由格式的 stderr）。

这些工具涵盖文件检查（**cat**、**head**、**tail**、**file**、**stat**、**wc**）、搜索与比较（**ls**、**find**、**grep**、**diff**）、路径辅助（**realpath**、**basename**、**dirname**、**pwd**）、文本处理（**sort**、**uniq**、**cut**、**tr**、**sed**、**awk**）、数据/归档（**jq**、**tar**）、校验和，以及系统/环境查询（**env**、**system**、**ps**、**df**、**du**）。其他子命令包括 **git** 辅助工具、**completions**、**doctor**，以及通过 stdio 暴露 Model Context Protocol 的 **mcp**。

aict 刻意保持**只读**（除本地检测外不联网做 MIME/语言增强），并用 Go 编写。其结构化输出比简洁的 GNU 工具消耗更多 token，但旨在减少代理多步骤解析重试循环。当只需要原始内容时，**--plain** 会跳过增强处理。

# PARAMETERS

_tool_
> 内置工具之一（如 **ls**、**grep**、**cat**、**diff**、**find**、**stat**）。完整列表见 **aict --help**。

**--xml**
> 输出 XML（面向代理场景的默认值）。

**--json**
> 输出 JSON，结构与 XML 形式相同。

**--plain**
> 输出与原 Unix 工具类似的经典纯文本，不带结构化增强。

**-r**
> 递归（在支持的地方，例如 **grep**）。

**mcp**
> 通过 stdio 启动 MCP 服务器，使代理能够像调用原生函数一样调用工具。

**doctor**
> 对安装和环境进行自诊断。

**completions**
> Shell 补全辅助脚本（bash/zsh/fish）。

**--help**
> 列出工具和选项。

# ENVIRONMENT

**AICT_XML**
> 当设置为 **1** 时，对所有 aict 调用全局优先采用面向 XML 的行为（如项目针对代理环境所记载的那样）。

# CAVEATS

并不是 GNU coreutils 或 **ripgrep** 的性能级即插即用替代品：增强处理（语言/MIME 检测、绝对路径）会增加延迟，尤其是在大型目录树或大体积 **grep**/**cat** 任务上。部分工具受平台限制（**ps** 仅面向 Linux；**system** 支持 Linux/macOS）。人类交互场景下请优先使用真正的 **rg**/**eza**；当目标是让代理消费结构化数据时再使用 aict。

# SEE ALSO

[ls](/man/ls)(1), [grep](/man/grep)(1), [cat](/man/cat)(1), [find](/man/find)(1), [jq](/man/jq)(1), [diff](/man/diff)(1)

# RESOURCES

```[Source code](https://github.com/synseqack/aict)```

```[Homepage](https://synseqack.github.io/aict/)```

<!-- verified: 2026-07-15 -->
