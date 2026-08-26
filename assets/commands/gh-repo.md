# TAGLINE

在命令行中管理 GitHub 仓库

# TLDR

**克隆仓库**

```gh repo clone [owner]/[repo]```

**创建新仓库**

```gh repo create [name] --public```

**复刻（fork）仓库**

```gh repo fork [owner]/[repo]```

**查看仓库**

```gh repo view```

**列出你的仓库**

```gh repo list```

# SYNOPSIS

**gh repo** _command_ [_options_]

# PARAMETERS

**clone** _REPO_
> 在本地克隆仓库。

**create** _NAME_
> 创建新仓库。

**fork** _REPO_
> 复刻（fork）仓库。

**view** _REPO_
> 查看仓库详情。

**list**
> 列出可访问的仓库。

**delete** _REPO_
> 删除仓库。

**rename** _NEW-NAME_
> 重命名当前仓库。

**sync**
> 将 fork 与上游同步。

**--public**
> 将仓库设为公开。

**--private**
> 将仓库设为私有。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gh repo** 用于在命令行中管理 GitHub 仓库，无需访问 github.com 即可完成仓库创建、克隆、复刻（fork）和管理。

该命令可根据配置使用 HTTPS 或 SSH 方式克隆。创建仓库时可设置可见性、描述、许可证和 gitignore 模板等选项。复刻会创建相互关联的副本，便于开展贡献工作流。

# CAVEATS

删除操作需要确认。复刻操作需要网络访问。部分操作需要所有者权限。

# HISTORY

gh repo 是 **GitHub CLI** 的核心命令之一，承担了此前只能通过网页界面或 API 进行的仓库操作。

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

[gh](/man/gh)(1), [gh-pr](/man/gh-pr)(1), [git-clone](/man/git-clone)(1)

# RESOURCES

```[Documentation](https://cli.github.com/manual/gh_repo)```

```[Source code](https://github.com/cli/cli)```

<!-- verified: 2026-07-15 -->
