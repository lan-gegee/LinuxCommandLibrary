# TAGLINE

为站会展示最近的提交

# TLDR

**显示你最近的提交**

```git standup```

**显示指定天数内的提交**

```git standup -d [3]```

**显示所有作者的提交**

```git standup -a all```

**显示指定作者的提交**

```git standup -a "[author]"```

**按日期范围显示**

```git standup -D "[2024-01-01]" -U "[2024-01-07]"```

# SYNOPSIS

**git** **standup** [_options_]

# PARAMETERS

**-d** _DAYS_
> 显示过去 _DAYS_ 天内的提交（默认：_1_，若逢周一则回看 3 天）。

**-a** _AUTHOR_
> 只显示特定作者。传入 _all_ 表示所有作者。

**-D** _DATE_
> 日期范围的起点（覆盖 **-d**）。

**-U** _DATE_
> 日期范围的终点。

**-m** _DEPTH_
> 递归扫描目录至 _DEPTH_ 层深以寻找 git 仓库。

**-L**
> 切换是否为每个提交附带 git diff 统计信息。

**-B** _BRANCH_
> 仅限 _BRANCH_ 分支上的提交。

**-f**
> 扫描前先从远程拉取更新。

**-g**
> 显示每个提交的 GPG 签名信息。

# DESCRIPTION

**git standup** 展示你最近的提交，专为每日站会设计。它属于 git-extras，可以查看你最近做了什么，还能跨多个仓库进行扫描。

该命令默认显示你上一个工作日以来的提交，方便回顾自己完成了哪些工作。

# INSTALL

```brew: brew install git-standup```

```nix: nix profile install nixpkgs#git-standup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-log](/man/git-log)(1), [git-extras](/man/git-extras)(1)
