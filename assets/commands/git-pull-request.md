# TAGLINE

从命令行创建拉取请求

# TLDR

**以交互方式创建拉取请求**

```git pull-request```

**带标题创建拉取请求**

```git pull-request -m "[title]"```

**创建指向特定 base 分支的拉取请求**

```git pull-request -b [base_branch]```

**带标题和正文创建拉取请求**

```git pull-request -m "[title]" -m "[body]"```

**从特定的 head 分支创建拉取请求**

```git pull-request -h [feature_branch] -b [main]```

# SYNOPSIS

**git** **pull-request** [_options_]

# PARAMETERS

**-m**, **--message** _text_
> PR 标题/信息。使用两次可分别设置标题和正文。

**-b**, **--base** _branch_
> 拉取请求的目标 base 分支。

**-h**, **--head** _branch_
> 源 head 分支（默认为当前分支）。

**-i**, **--issue** _number_
> 将现有 issue 转换为拉取请求。

# DESCRIPTION

**git pull-request** 从命令行创建 GitHub 拉取请求。它是 **hub** CLI 工具（GitHub 出品）的一部分，会在需要时推送当前分支，并向指定的 base 分支发起拉取请求。

该命令可以从提交信息中提取 PR 标题和正文，也可以交互式地询问。在不带 **-m** 调用时会打开编辑器撰写信息：第一行成为标题，后续行成为正文。

注意：**hub** 工具现已进入维护模式。官方替代品是 GitHub CLI 的 **gh pr create**，它提供更全面的 GitHub 集成。

# INSTALL

```dnf: sudo dnf install git-pull-request```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh-pr-create](/man/gh-pr-create)(1), [gh](/man/gh)(1), [hub](/man/hub)(1), [git-extras](/man/git-extras)(1), [git-request-pull](/man/git-request-pull)(1), [git-push](/man/git-push)(1)
