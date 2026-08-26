# TAGLINE

从远程仓库下载对象和引用

# TLDR

**从 origin 拉取**

```git fetch```

**从指定远程拉取**

```git fetch [remote]```

**拉取所有远程**

```git fetch --all```

**拉取并清理**

```git fetch -p```

**拉取指定分支**

```git fetch [remote] [branch]```

**连同标签一起拉取**

```git fetch --tags```

**试运行**

```git fetch --dry-run```

# SYNOPSIS

**git** **fetch** [_options_] [_remote_] [_refspec_...]

# PARAMETERS

**--all**
> 拉取所有远程。

**-p**, **--prune**
> 删除已在远程被删除的引用。

**--tags**
> 拉取所有标签。

**--depth** _depth_
> 浅克隆式拉取。

**--dry-run**
> 显示将要拉取的内容。

**-j**, **--jobs** _n_
> 并行拉取子模块。

**--unshallow**
> 将浅克隆转换为完整仓库。

**-f**, **--force**
> 允许对远程跟踪分支进行非快进更新。

**--no-tags**
> 不下载任何标签（覆盖 remote.<name>.tagOpt）。

**-t**, **--tags**
> 除其他本要拉取的内容外，还从远程拉取所有标签。

**--update-shallow**
> 接受更新 **.git/shallow** 的引用，加深浅克隆。

**--filter** _SPEC_
> 部分克隆过滤器，例如 `blob:none`（省略 blob）或 `tree:0`（仅提交）。

**--recurse-submodules** [_=on-demand_|_yes_|_no_]
> 控制子模块的拉取行为。

**-q**, **--quiet** / **-v**, **--verbose**
> 抑制 / 增加进度输出。

# DESCRIPTION

**git fetch** 从远程仓库获取提交、文件和引用，更新本地仓库对远程分支的认知，而不修改你的工作目录或当前分支。这使得它成为与远程改动保持同步的安全操作。

在 fetch 时，Git 会从远程下载所有新提交和对象，并更新远程跟踪分支（如 origin/main）。你的本地分支保持不变，让你可以在整合之前审查远程改动。这是它与 git pull 的关键区别——后者会在 fetch 之后自动合并。

prune 选项（-p）会删除指向服务器上已不存在分支的引用。配合 --depth 的浅拉取可以限制历史下载量，适用于 CI/CD 环境。--unshallow 选项则将浅克隆转换为完整仓库。

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

[git-pull](/man/git-pull)(1), [git-push](/man/git-push)(1)
