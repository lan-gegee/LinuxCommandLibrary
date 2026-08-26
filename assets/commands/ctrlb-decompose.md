# TAGLINE

将日志行压缩为面向人类和 LLM 的结构化模式

# TLDR

通过 **stdin** 管道传入日志文件

```cat /var/log/syslog | ctrlb-decompose```

分析**日志文件**

```ctrlb-decompose [server.log]```

输出面向 **LLM 优化**的紧凑 markdown

```ctrlb-decompose --llm [app.log]```

输出 **JSON**

```ctrlb-decompose --json [app.log]```

显示出现最多的模式及示例行

```ctrlb-decompose --top 10 --context 3 [app.log]```

# SYNOPSIS

**ctrlb-decompose** [_OPTIONS_] [_FILE_]

# PARAMETERS

**FILE**
> 日志文件路径；省略或为 `-` 时读取 stdin

**--human**
> 适合人类阅读的彩色终端输出（默认）

**--llm**
> 为输入 LLM 而优化的紧凑 markdown

**--json**
> 结构化的 JSON 输出

**--top** _N_
> 显示前 N 个模式（默认：20）

**--context** _N_
> 每个模式的示例行数（默认：0）

**--no-color**
> 禁用 ANSI 颜色

**--no-banner**
> 不显示页眉/页脚

**-q**, **--quiet**
> 不显示进度消息

**-h**, **--help**
> 显示帮助

**-V**, **--version**
> 显示版本

# DESCRIPTION

**ctrlb-decompose** 将原始日志行压缩为带有统计信息、异常和关联关系的结构化模式。它采用 CLP 风格编码和 Drain3 聚类对日志进行单遍流式处理，对变量（IP、UUID、时长、枚举等）进行分类，并报告分位数、基数和异常信号。

典型的压缩幅度达数个数量级（数百万行压缩为数十个模式），使日志变得易于查阅或发送给 LLM，而不会撑爆上下文窗口。

# CAVEATS

最适合具有重复结构的文本型应用/系统日志；自由格式文本的聚类效果较差。内存占用随唯一模式数量增长（Drain3 有可配置的上限）。各输出格式在 token 密度和机器可读性上有所差异。

# HISTORY

由 ctrlb-hq 使用 **Rust** 编写；同时提供 WASM 库和 Claude Code 插件形式。

# SEE ALSO

[grep](/man/grep)(1), [jq](/man/jq)(1), [lnav](/man/lnav)(1)

# RESOURCES

```[Source code](https://github.com/ctrlb-hq/ctrlb-decompose)```

<!-- verified: 2026-07-28 -->
