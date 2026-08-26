# TAGLINE

高层分支模型工作流命令

# TLDR

**初始化 git flow**

```git flow init```

**使用默认分支名初始化**

```git flow init -d```

**开始特性分支**

```git flow feature start [feature-name]```

**完成特性**

```git flow feature finish [feature-name]```

**开始发布**

```git flow release start [version]```

**完成发布**

```git flow release finish [version]```

**将特性分支发布到远程**

```git flow feature publish [feature-name]```

**开始热修复**

```git flow hotfix start [version]```

**完成热修复**

```git flow hotfix finish [version]```

# SYNOPSIS

**git flow** _subcommand_ [_action_] [_name_]

# PARAMETERS

**init**
> 为仓库初始化 git-flow。

**feature** _ACTION_ _NAME_
> 管理特性分支。

**release** _ACTION_ _VERSION_
> 管理发布分支。

**hotfix** _ACTION_ _NAME_
> 管理热修复分支。

**support** _ACTION_ _NAME_
> 管理 support 分支。

**start**
> 开始一个新分支。

**finish**
> 完成并合并分支。

**publish**
> 将分支推送到远程仓库。

**track**
> 在本地跟踪远程分支。

**pull**
> 拉取远程分支（已被弃用，建议改用 track）。

**delete**
> 删除已完成的分支。

**list**
> 列出给定类型的现有分支。

**-d**
> 初始化时使用默认的分支命名约定。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git flow** 实现了 Vincent Driessen 的分支模型，提供高层命令以一致的命名和合并策略管理特性、发布和热修复分支。

该工作流使用 develop 作为集成分支，使用 main/master 进行发布。特性从 develop 分出，release 分支为上线做准备，热修复则直接进入 main。它以明确的约定规范了团队的分支工作流。

# CAVEATS

属于带有主观倾向的工作流。可能不适合所有项目。每个仓库都需要单独初始化。

# HISTORY

git flow 由 **Vincent Driessen** 于 **2010 年**基于其广受欢迎的 git 分支模型博客文章创建。

# INSTALL

```apk: sudo apk add git-flow```

```brew: brew install git-flow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-branch](/man/git-branch)(1), [git-merge](/man/git-merge)(1), [git-checkout](/man/git-checkout)(1), [git-tag](/man/git-tag)(1)
