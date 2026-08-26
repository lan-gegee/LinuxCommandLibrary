# TAGLINE

管理仓库 issue 和错误报告

# TLDR

**列出 issues**

```gh issue list```

**创建 issue**

```gh issue create```

**查看 issue**

```gh issue view [number]```

**关闭 issue**

```gh issue close [number]```

**重新打开 issue**

```gh issue reopen [number]```

**编辑 issue**

```gh issue edit [number]```

**搜索 issues**

```gh issue list --search "[query]"```

**列出分配给你的 issues**

```gh issue list --assignee @me```

# SYNOPSIS

**gh** **issue** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出 issues。

**create**
> 创建 issue。

**view**
> 查看 issue。

**close**
> 关闭 issue。

**reopen**
> 重新打开 issue。

**edit**
> 编辑 issue。

**comment**
> 添加评论。

**delete**
> 删除 issue。

**status**
> 显示状态。

# PARAMETERS

**-R**, **--repo** _owner/repo_
> 仓库。

**-a**, **--assignee** _user_
> 按负责人过滤。

**-l**, **--label** _label_
> 按标签过滤。

**-s**, **--state** _state_
> 按状态过滤。

# DESCRIPTION

**gh issue** 管理 GitHub issue，用于跟踪缺陷、功能请求、任务和讨论。Issue 是 GitHub 项目管理的核心，支持标签、负责人、里程碑和项目。

该命令提供完整的 issue 生命周期管理，包括创建、编辑、评论、状态变更和删除。借助过滤功能，可以按负责人、标签、状态以及搜索查询查找 issue。Issue 还可以跨多个仓库进行管理。

通过与拉取请求集成，可以将 issue 关联到代码变更；提交信息中使用关键字时，PR 合并后会自动关闭对应的 issue。

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

[gh](/man/gh)(1), [gh-pr](/man/gh-pr)(1)

# RESOURCES

```[Documentation](https://cli.github.com/manual/gh_issue)```

```[Source code](https://github.com/cli/cli)```

<!-- verified: 2026-07-15 -->
