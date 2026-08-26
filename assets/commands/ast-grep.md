# TAGLINE

基于 AST 模式的结构化代码搜索与重写工具

# TLDR

在当前目录中**搜索模式**

```ast-grep --pattern 'console.log($ARG)'```

用**指定语言**搜索

```ast-grep --pattern 'async function $NAME() {}' --lang typescript```

**搜索并重写**代码

```ast-grep --pattern '$OLD.forEach($FN)' --rewrite '$OLD.map($FN)'```

**交互式重写**并逐条确认

```ast-grep --pattern '$A == $B' --rewrite '$A === $B' --interactive```

**以 JSON 格式输出**匹配结果

```ast-grep --pattern 'var $X = $Y' --json```

使用规则配置文件进行**扫描**

```ast-grep scan```

**带上下文行**搜索

```ast-grep run --pattern '$FUNC()' --context 3```

用 glob 模式**过滤文件**

```ast-grep run --pattern '$X' --globs '*.ts'```

# SYNOPSIS

**ast-grep** [_command_] [_options_]

**sg** [_command_] [_options_]

# PARAMETERS

**run**
> 运行一次性的搜索或重写（默认命令）。

**scan**
> 使用 YAML 配置规则扫描并重写代码。

**test**
> 用测试用例验证 ast-grep 规则。

**new**
> 通过脚手架创建新的 ast-grep 项目、规则或测试。

**lsp**
> 启动语言服务器以集成到 IDE。

**-p** _pattern_, **--pattern** _pattern_
> 要搜索的 AST 模式。使用 $VAR 表示元变量。

**-r** _replacement_, **--rewrite** _replacement_
> 匹配项的替换模式。使用 $VAR 引用捕获到的元变量。

**-l** _lang_, **--lang** _lang_
> 目标语言（javascript、typescript、python、rust、go、c、cpp、java 等）。

**-i**, **--interactive**
> 交互模式，逐个确认重写操作。

**--json** [_style_]
> 以 JSON 格式输出（pretty、stream、compact）。

**-A** _num_, **--after** _num_
> 显示每个匹配之后的 num 行。

**-B** _num_, **--before** _num_
> 显示每个匹配之前的 num 行。

**-C** _num_, **--context** _num_
> 显示每个匹配前后的 num 行。

**--globs** _pattern_
> 包含或排除匹配给定 glob 的文件。可多次指定。

**--stdin**
> 从标准输入读取代码。

**--threads** _num_
> 线程数（0 表示自动检测）。

**-c** _file_, **--config** _file_
> 配置文件路径（默认：sgconfig.yml）。

# DESCRIPTION

**ast-grep**（也可通过 **sg** 调用）是一款结构化代码搜索与重写工具。与基于文本的 grep 不同，它将代码解析为抽象语法树（AST），并在语法层面匹配模式，确保匹配结果遵循代码结构。

模式采用类代码语法，其中 **$METAVARIABLES** 可匹配任意表达式。例如，**console.log($MSG)** 可以匹配任何 console.log 调用，而不论其参数是什么。这实现了基于文本的工具无法做到的精确重构。

该工具通过 tree-sitter 解析器支持多种语言，包括 JavaScript、TypeScript、Python、Rust、Go、C、C++、Java 等。**scan** 命令应用 YAML 配置文件中的规则，实现项目级的代码检查与代码模式强制约束。

配置文件（**sgconfig.yml**）定义规则目录和项目设置。每条规则指定模式、重写内容、严重级别和文件过滤器。

# CAVEATS

在某些系统上，**sg** 别名可能与其他命令冲突。由于 AST 差异，不同语言的模式语法略有区别。复杂模式可能需要了解 tree-sitter 节点类型。

# HISTORY

**ast-grep** 由 **Herrington Darkholme** 创建，于 **2022** 年发布。它使用 Rust 编写以保证性能，旨在将结构化代码搜索带到命令行，灵感来自 Semgrep 和 Comby 等工具。

# INSTALL

```pacman: sudo pacman -S ast-grep```

```apk: sudo apk add ast-grep```

```zypper: sudo zypper install ast-grep```

```brew: brew install ast-grep```

```nix: nix profile install nixpkgs#ast-grep```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[grep](/man/grep)(1), [ripgrep](/man/ripgrep)(1), [sed](/man/sed)(1), [semgrep](/man/semgrep)(1)
