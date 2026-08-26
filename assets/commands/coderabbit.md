# TAGLINE

终端里的 AI 驱动代码审查工具

# TLDR

以交互方式**审查**所有更改

```coderabbit```

以纯文本输出**审查**所有更改

```coderabbit --plain```

只**审查**未提交的更改

```coderabbit --type uncommitted```

将当前分支与基准分支进行**比较**

```coderabbit --base [develop]```

**提供**自定义审查指令

```coderabbit --config [./claude.md]```

向 CodeRabbit **认证**

```cr auth login```

将 CLI **更新**到最新版本

```coderabbit update```

# SYNOPSIS

**coderabbit** [_review_] [_options_]
**cr** [_review_] [_options_]

# PARAMETERS

**--plain**
> 以纯文本格式输出详细反馈。

**--prompt-only**
> 显示为 AI 智能体优化的最小输出。

**-t**, **--type** _type_
> 审查类型：all、committed、uncommitted（默认：all）。

**-c**, **--config** _files..._
> 提供给 AI 的额外指令文件。

**--base** _branch_
> 用于比较的基准分支。

**--base-commit** _commit_
> 当前分支上用于比较的基准 commit 哈希。

**--cwd** _path_
> 设置工作目录（必须包含一个 Git 仓库）。

**--api-key** _key_
> 用于按量计费访问的 API 密钥。

**--self-hosted**
> 启用自托管认证模式。

**--no-color**
> 禁用彩色终端输出。

# SUBCOMMANDS

**review**
> 运行 AI 驱动的代码审查（未给出子命令时的默认行为）。

**auth login**
> 使用 CodeRabbit 账户认证。

**auth logout**
> 退出 CodeRabbit 登录。

**auth status**
> 显示当前认证状态。

**auth org**
> 在多个组织之间切换。

**update**
> 检查并安装最新的 CLI 版本。

# DESCRIPTION

**CodeRabbit CLI** 将 AI 驱动的代码审查直接带入终端。它分析代码更改 -- 无论是未提交的、已暂存的、已提交的还是跨分支的 -- 并逐行给出审查意见，指出潜在问题，如安全漏洞、性能问题、代码坏味道、逻辑错误和缺失的单元测试。**cr** 是 **coderabbit** 的简短别名。

该工具有三种输出模式：交互模式（默认），提供可浏览的 TUI；纯文本模式（**--plain**），输出适合脚本处理的详细反馈；以及 prompt-only 模式（**--prompt-only**），用于与 AI 编程智能体集成。

# CAVEATS

需要工作目录中存在已初始化的 Git 仓库。建议进行认证以获得更强的分析能力，但也可以不认证使用（有速率限制）。免费层有速率限制；Pro 计划提供更高的额度。原生支持 macOS 和 Linux；Windows 可通过 WSL 使用。该 CLI 工具不开源。

# HISTORY

**CodeRabbit** 由 **Harjot Gill** 于 **2023 年**创立。公司最初以 GitHub/GitLab 机器人形式发布，用于审查 pull request。**CLI 工具于 2025 年 9 月 16 日发布**，将平台扩展到支持在终端中直接进行提交前审查。CodeRabbit 总部位于加利福尼亚州 El Dorado Hills。

# INSTALL

```aur: yay -S coderabbit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [git](/man/git)(1), [semgrep](/man/semgrep)(1)
