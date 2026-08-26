# TAGLINE

以标准化工作流创建和管理特性分支

# TLDR

**创建特性分支**

```git feature [feature_name]```

**创建带远程跟踪的特性分支**

```git feature [feature_name] -r [origin]```

**从指定起点创建特性分支**

```git feature [feature_name] --from [develop]```

**完成特性分支（合并并删除）**

```git feature finish [feature_name]```

**以 squash 合并方式完成**

```git feature finish --squash [feature_name]```

# SYNOPSIS

**git** **feature** [**-a** _prefix_] [**-s** _separator_] [**-r** [_remote_]] [**--from** _start_point_] _name_...

**git** **feature** **finish** [**--squash**] _name_...

# PARAMETERS

**-a** _PREFIX_, **--alias** _PREFIX_
> 使用自定义分支前缀，而不是 "feature"。

**-s** _SEPARATOR_, **--separator** _SEPARATOR_
> 使用自定义分隔符，而不是 "/"。

**-r** [_REMOTE_], **--remote** [_REMOTE_]
> 建立远程跟踪分支（默认为 origin）。

**--from** _START_POINT_
> 从指定的提交或分支创建特性分支。

**--squash**
> 完成时执行 squash 合并。

# SUBCOMMANDS

**finish**
> 将特性分支合并到当前分支并将其删除。

# DESCRIPTION

**git feature** 为遵循标准化命名约定的特性分支工作提供高层命令。作为 git-extras 套件的组成部分，它简化了在独立分支中创建、开发和完成特性工作的常见流程。

创建特性分支时，该命令会自动添加 "feature/" 前缀，以保持整个仓库的命名一致。finish 子命令负责将特性分支合并回主开发分支并进行后续清理，将多个手动 git 操作封装为一条命令。

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

[git-create-branch](/man/git-create-branch)(1), [git-extras](/man/git-extras)(1), [git-branch](/man/git-branch)(1), [git-flow](/man/git-flow)(1)
