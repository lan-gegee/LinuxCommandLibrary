# TAGLINE

输出相关 issue、拉取请求和通知的信息

# TLDR

**显示**你在各订阅仓库中的状态仪表板

```gh status```

**将报告限定**到一个组织

```gh status --org [orgname]```

**从报告中排除**某些仓库

```gh status --exclude [owner/repo],[owner/other-repo]```

# SYNOPSIS

**gh** **status** [_flags_]

# PARAMETERS

**-o**, **--org** _string_
> 在某个组织范围内报告状态。

**-e**, **--exclude** _strings_
> 要排除的仓库列表，逗号分隔，格式为 **owner/name**。

# DESCRIPTION

**gh status** 会概览你在各个已订阅仓库中的 GitHub 工作。输出分为四个窗格：**Assigned Issues**、**Assigned Pull Requests**、**Review Requests** 和 **Mentions**，外加一个 **Repository Activity** 部分，列出新出现的 issue、拉取请求和评论。

它的意义在于回答"哪些事需要我关注"，而无需访问网页仪表板，也不必手动逐条运行 **gh issue list** 和 **gh pr list** 命令。由于报告基于你的订阅而非固定仓库构建，它可以在任意目录下运行，包括 git 仓库之外。

**--org** 会把每个窗格都限定到单个组织，这也是区分工作与个人活动的常用做法。**--exclude** 则可将嘈杂的仓库从结果中剔除。

# CAVEATS

报告只覆盖你通过 **notifications** 订阅的仓库，因此在那些仅有访问权限而未订阅的仓库里，活动不会出现。提及（mentions）来自你的通知流，并受其保留期限约束，较早的提及会被移除。

生成报告需要进行多次 API 调用；对订阅较多的账户而言，可能耗时数秒，并占用相当一部分速率配额。

# HISTORY

**gh status** 作为核心命令加入于 **GitHub CLI 2.7.0**（**2022 年 3 月**），由 **vilmibm** 贡献——他此前曾以 **gh** 扩展的形式探索过同一想法。

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

[gh](/man/gh)(1), [gh-issue](/man/gh-issue)(1), [gh-pr](/man/gh-pr)(1), [gh-search](/man/gh-search)(1)

# RESOURCES

```[Source code](https://github.com/cli/cli)```

```[Homepage](https://cli.github.com/)```

```[Documentation](https://cli.github.com/manual/gh_status)```

<!-- verified: 2026-07-16 -->
