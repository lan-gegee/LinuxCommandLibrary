# TAGLINE

启动并跟踪 Copilot 编码智能体会话

# TLDR

从提示词**创建**新的智能体任务

```gh agent-task create "[refactor the auth module]"```

**创建**任务并实时跟踪会话日志

```gh agent-task create "[fix the failing tests]" --follow```

针对其他基础分支**创建**任务

```gh agent-task create "[add caching]" --base [develop]```

从文件或标准输入**读取**提示词

```gh agent-task create --from-file [prompt.md]```

**列出**你最近的智能体任务

```gh agent-task list```

**查看**某个任务并流式输出其日志

```gh agent-task view [123] --log --follow```

# SYNOPSIS

**gh** **agent-task** _subcommand_ [_options_]

# SUBCOMMANDS

**create** [_prompt_]
> 在当前仓库创建新的智能体任务。不带提示词时，会交互式地要求输入。

**list**
> 列出你最近的智能体任务。

**view** [_number_]
> 查看某个智能体任务的详情，或查看与某个 pull request 关联的任务详情。

# PARAMETERS

**-b**, **--base** _branch_
> create：pull request 的基础分支。默认为仓库的默认分支。

**-a**, **--custom-agent** _name_
> create：使用自定义智能体，例如 **my-agent** 对应 **my-agent.md** 智能体文件。

**-F**, **--from-file** _file_
> create：从文件读取任务描述；用 **-** 表示标准输入。

**--follow**
> create、view：实时跟踪智能体会话日志。

**--log**
> view：显示智能体会话日志。

**-R**, **--repo** _[HOST/]OWNER/REPO_
> 选择其他仓库而非当前仓库。

**-L**, **--limit** _int_
> list：获取智能体任务的最大数量（默认 **30**）。

**--json** _fields_
> list、view：以 JSON 输出指定字段。

**-q**, **--jq** _expression_
> list、view：用 jq 表达式过滤 JSON 输出。

**-t**, **--template** _string_
> list、view：用 Go 模板格式化 JSON 输出。

**-w**, **--web**
> list、view：在浏览器中打开智能体任务。

# DESCRIPTION

**gh agent-task** 从命令行把工作委派给 **GitHub Copilot coding agent**。该智能体是异步且自主的：创建任务后它会打开一个草稿 pull request，在后台完成更改，然后在完成后请求你审查。

**gh agent-task create** 针对当前仓库启动一个会话，你的提示词即为任务描述。由于智能体远程运行，命令会立即返回；除非指定 **--follow**，此时它会流式输出会话日志直到智能体完成。

**gh agent-task list** 显示正在运行和过去的会话，**gh agent-task view** 查看其中之一，可选地流式输出其日志。两者都支持用于脚本化的 **--json**；可用的 JSON 字段包括 **id**、**name**、**state**、**createdAt**、**completedAt**、**repository**、**pullRequestNumber**、**pullRequestState**、**pullRequestTitle** 和 **pullRequestUrl**。

该命令组也可以写作 **gh agent**、**gh agents** 或 **gh agent-tasks** 来调用。

# CAVEATS

需要 **GitHub CLI 2.80.0** 或更高版本以及具有 **Copilot coding agent** 访问权限的账户。这组命令处于**公开预览**阶段且可能变化，因此各版本之间的标志和输出可能有所调整。

任务会消耗 Copilot 高级请求配额，并且智能体会在草稿 pull request 中以你的名义推送提交。合并前请先审查其更改。

# HISTORY

**agent-task** 命令集于 **v2.80.0** 加入 GitHub CLI，并在 **2025 年 9 月**发布，将 Copilot 编码智能体会话带入终端。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [gh-copilot](/man/gh-copilot)(1), [gh-pr](/man/gh-pr)(1), [copilot](/man/copilot)(1)

# RESOURCES

```[Source code](https://github.com/cli/cli)```

```[Homepage](https://cli.github.com/)```

```[Documentation](https://cli.github.com/manual/gh_agent-task)```

<!-- verified: 2026-07-16 -->
