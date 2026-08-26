# TAGLINE

在命令行中管理 GitHub Actions 工作流

# TLDR

**列出工作流**

```gh workflow list```

**查看工作流详情**

```gh workflow view [workflow-name]```

**运行工作流**

```gh workflow run [workflow-name]```

**启用工作流**

```gh workflow enable [workflow-name]```

**禁用工作流**

```gh workflow disable [workflow-name]```

**带输入参数运行工作流**

```gh workflow run [workflow-name] -f [key]=[value]```

**在特定分支上运行工作流**

```gh workflow run [workflow-name] --ref [branch-name]```

**在网页浏览器中查看工作流运行**

```gh workflow view [workflow-name] --web```

# SYNOPSIS

**gh workflow** _command_ [_options_]

# PARAMETERS

**list**
> 列出工作流文件。

**view** _WORKFLOW_
> 查看工作流详情。

**run** _WORKFLOW_
> 触发一次工作流运行。

**enable** _WORKFLOW_
> 启用工作流。

**disable** _WORKFLOW_
> 禁用工作流。

**-r** _REF_, **--ref** _REF_
> 工作流运行使用的分支或标签。

**-f** _KEY=VALUE_
> 工作流运行的字符串输入参数。

**-F** _KEY=VALUE_
> 从文件或标准输入读取输入参数（@file 表示文件，- 表示标准输入）。

**-w**, **--web**
> 在网页浏览器中打开工作流。

**-a**, **--all**
> 列出时包含已禁用的工作流。

**-L**, **--limit** _N_
> 列出的条目数量上限（默认 50）。

**--json** _FIELDS_
> 以 JSON 格式输出指定字段的结果。

# DESCRIPTION

**gh workflow** 用于在命令行中管理 GitHub Actions 工作流。它可以对工作流定义进行控制，包括列出、查看、触发以及启用或禁用工作流。

run 命令会触发 workflow_dispatch 事件，按需执行工作流并可传入可选的输入参数。这样就能从终端进行手动 CI 运行和参数驱动的工作流。

# CAVEATS

工作流必须带有 workflow_dispatch 触发器才能手动运行。启用/禁用需要管理员权限。输入参数必须与工作流定义匹配。

# HISTORY

作为全面集成 GitHub Actions 的一部分，gh workflow 被加入 **GitHub CLI**，让完整的工作流管理可以在终端中完成。

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

[gh](/man/gh)(1), [gh-run](/man/gh-run)(1)
