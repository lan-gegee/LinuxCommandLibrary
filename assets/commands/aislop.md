# TAGLINE

捕捉 AI 编程代理留下的 AI 生成的坏味道和低质量模式

# TLDR

扫描当前目录中的 AI slop

```aislop scan```

只扫描有改动的文件并以 JSON 输出供 CI 使用

```aislop scan --changes --json```

自动修复机械性问题

```aislop fix```

安装每次代理编辑后运行的钩子（Claude Code 示例）

```aislop hook install --claude```

以 CI 模式运行并在低于阈值时使构建失败

```aislop ci```

只扫描已暂存的文件

```aislop scan --staged```

以自定义配置运行 CI，分数低于 80 时失败

```aislop ci --fail-below 80```

打印一份可以交给代理处理剩余问题的提示词

```aislop fix --prompt```

# SYNOPSIS

**aislop** [_command_] [_options_] [_path_]

# DESCRIPTION

**aislop** 是一款快速、确定性的命令行工具，用于检测 AI 编程代理（Claude Code、Cursor、Codex 等）留下的特征性模式。它以 0–100 分为代码打分，并能自动修复许多机械性问题。

aislop 不依赖 LLM 实时判断，而是结合格式化工具、linter、AST 分析，以及大量手写规则，针对叙事性注释、无意义注释、`as any` 类型断言、幻觉导入、被吞掉的异常、死代码、超长函数等"能编译通过、能过测试但长期损害可维护性"的 slop 模式。

该工具支持 TypeScript/JavaScript、Python、Go、Rust、Ruby、PHP 和 Java。它被设计为可在编辑器、pre-commit 钩子、CI 管道中运行，作为接受代理生成变更前的质量关卡。

# PARAMETERS

**scan**  
> 分析代码并报告问题（未给出子命令时的默认命令）

**fix**  
> 自动修复可以通过机械手段解决的问题

**ci**  
> 以 CI 模式运行（JSON 输出，低于阈值时以非零值退出）

**hook**  
> 管理 Claude、Cursor 及其他代理的单次编辑钩子

**rules**  
> 列出所有生效的规则

**init**  
> 创建 .aislop/config.yml 文件

通用标志：

**--json**  
> 输出机器可读的 JSON

**--sarif**  
> 输出适用于 GitHub Code Scanning 的 SARIF 2.1.0

**-f**, **--force**（配合 fix）  
> 应用激进的修复（未使用的依赖、文件等）

# CONFIGURATION

创建 `.aislop/config.yml` 来调整行为：

```yaml
ci:
  failBelow: 75

rules:
  ai-slop/narrative-comment: warning
  security/hardcoded-secret: error

exclude:
  - "**/*.generated.ts"
```

# SEE ALSO

[ruff](/man/ruff), [clippy](/man/clippy), [biome](/man/biome)
