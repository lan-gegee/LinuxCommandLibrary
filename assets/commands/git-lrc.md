# TAGLINE

在每次 git 提交时运行的 AI 驱动代码审查工具

# TLDR

**首次使用时完成安装与身份验证**

```lrc setup```

**对当前已暂存的更改运行 AI 审查**

```git add . && lrc review```

**提交更改**并触发自动审查

```git commit -m "[message]"```

**跳过 AI 审查**并为此次更改个人担责

```lrc review --vouch```

**完全绕过审查**

```lrc review --skip```

**管理 AI 连接器**或重新进行身份验证

```lrc ui```

**启用或禁用** git hook 集成

```lrc hooks enable```

# SYNOPSIS

**lrc** _command_ [_options_]

**git lrc** _command_ [_options_]

# DESCRIPTION

**git-lrc**（LiveReview Code）是一款 AI 驱动的代码审查工具，以 git pre-commit hook 的形式安装。在更改暂存后，执行 **git commit** 会在提交落库前自动触发对该 diff 的 AI 审查，尽早发现 bug、安全问题和技术债。它也可以作为 **lrc** 手动调用，或作为 git 子命令 **git lrc** 使用。

每次提交都会记录审查结果，例如 **ran (iter:3, coverage:85%)** 或 **vouched**，因此审查历史随仓库一同保存。该工具将实际审查委托给可配置的 AI 服务商，默认使用 Gemini 的免费额度，同时也支持 OpenAI、Claude、DeepSeek 和 OpenRouter 端点。

git-lrc 由 HexmosTech 用 Go 编写，以源码可用（source-available）许可证发布。

# PARAMETERS

**setup**

> 运行初始引导和身份验证流程。

**review**

> 对当前已暂存的更改运行 AI 审查。

**review --vouch**

> 跳过 AI 审查并为此次更改个人担责。该提交会被记录为 vouched。

**review --skip**

> 对本次提交完全绕过审查。

**ui**

> 打开连接器管理界面，用于配置 AI 服务商或重新进行身份验证。

**hooks enable** | **disable** | **status**

> 启用、禁用或报告 git pre-commit 集成的状态。

# CAVEATS

已暂存的 diff 会被发送到所配置的云端 AI 服务商，因此不适合包含不能离开你机器的代码。安装需要通过厂商的 **ipm** 包管理器，而非系统软件仓库。免费额度为每月 3 万行代码，超出后需付费计划。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-commit](/man/git-commit)(1), [claude](/man/claude)(1), [copilot](/man/copilot)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/HexmosTech/git-lrc)```

```[Homepage](https://hexmos.com)```

<!-- verified: 2026-06-17 -->
