# TAGLINE

使用 GitHub API 合并拉取请求

# TLDR

**合并当前 PR**

```gh pr merge```

**以 squash 方式合并**

```gh pr merge --squash```

**以 rebase 方式合并**

```gh pr merge --rebase```

**合并后删除分支**

```gh pr merge --delete-branch```

**条件满足时自动合并**

```gh pr merge --auto```

# SYNOPSIS

**gh pr merge** [_pr-number_] [_options_]

# PARAMETERS

_PR-NUMBER_
> 拉取请求编号（默认为当前分支）。

**--merge**
> 创建标准的合并提交。

**--squash**
> 将提交压缩为一个。

**--rebase**
> 将提交变基（rebase）到 base 分支上。

**--delete-branch**
> 合并后删除分支。

**--auto**
> 满足全部要求后自动合并。

**--admin**
> 以管理员权限合并。

**--body** _TEXT_
> 自定义合并提交信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gh pr merge** 通过 GitHub 的合并 API 来合并拉取请求。它支持所有合并策略：合并提交（merge commit）、squash 合并和变基合并。该命令可以先等待必需检查和批准完成后再执行合并。

自动合并（--auto）会将 PR 设置为在所有要求满足后自动合并，适合已获批准但仍在等待 CI 的 PR。--delete-branch 选项会在合并后清理功能分支。

# CAVEATS

分支保护规则可能阻止合并。自动合并需要在仓库中启用该功能。管理员标志可绕过保护规则。

# HISTORY

gh pr merge 是 **GitHub CLI** 的组成部分，实现了 GitHub 网页界面上可用的全部合并策略。

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

[gh-pr](/man/gh-pr)(1), [gh-pr-checks](/man/gh-pr-checks)(1), [git-merge](/man/git-merge)(1)

# RESOURCES

```[Documentation](https://cli.github.com/manual/gh_pr_merge)```

```[Source code](https://github.com/cli/cli)```

<!-- verified: 2026-07-15 -->
