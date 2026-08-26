# TAGLINE

在众多 GitHub 仓库中批量执行相同的修改

# TLDR

在匹配查询的仓库中**运行命令**并打开 PR

```git-xargs --branch-name [update] --github-org [org] --commit-message "[msg]" -- [make] [format]```

从文件中读取目标仓库

```git-xargs --repos [repos.txt] --branch-name [chore] --commit-message "[msg]" -- [./script.sh]```

**试运行**

```git-xargs --dry-run --github-org [org] -- [true]```

# SYNOPSIS

**git-xargs** [*options*] **--** *command* [*args*...]

# DESCRIPTION

**git-xargs**（Gruntwork 出品）会克隆选定的 GitHub 仓库，在其中运行任意命令，并可提交、推送以及根据结果打开 pull request。专为需要在整个组织内套用机械化重构或策略文件的平台团队而构建。

# PARAMETERS

**--github-org** *org* / **--repos** *file* / repo selectors

> 选择目标仓库。

**--branch-name** *name*

> 用于提交/PR 的分支。

**--commit-message** *msg*

> 存在变更时的提交信息。

**--pr-title** / **--pr-body**

> Pull request 的标题与正文字段。

**--dry-run**

> 只打印将执行的操作，不修改远程仓库。

**--** *command*

> 在每个克隆中执行的命令。

需要 GitHub 身份验证（具有 repo 权限范围的令牌）。

# CAVEATS

功能强大且可能造成破坏——先用 **--dry-run** 和单个仓库进行测试。注意遵守分支保护规则和 CODEOWNERS。组织规模下还需留意磁盘和 API 速率限制。

# INSTALL

```brew: brew install git-xargs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[multi-gitter](/man/multi-gitter)(1), [gh](/man/gh)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/gruntwork-io/git-xargs)```

<!-- verified: 2026-07-19 -->
