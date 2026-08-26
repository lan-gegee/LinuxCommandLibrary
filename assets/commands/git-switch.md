# TAGLINE

在分支之间切换

# TLDR

**切换到分支**

```git switch [branch]```

**创建并切换**

```git switch -c [new_branch]```

**切换回上一个分支**

```git switch -```

**从指定提交创建**

```git switch -c [branch] [commit]```

**分离 HEAD**

```git switch --detach [commit]```

**强制切换**

```git switch -f [branch]```

**创建孤立分支**

```git switch --orphan [branch]```

# SYNOPSIS

**git** **switch** [_options_] _branch_

# PARAMETERS

**-c**, **--create** _branch_
> 创建新分支。

**-C**
> 创建或重置分支。

**-d**, **--detach**
> 分离 HEAD。

**--orphan** _branch_
> 创建孤立分支。

**-f**, **--force**
> 强制切换。

**--guess**
> 猜测对应的远程分支。

**--no-guess**
> 不猜测远程分支。

**-t**, **--track**
> 建立跟踪关系。

# DESCRIPTION

**git switch** 用于切换当前分支。它于 Git 2.23 引入，为分支切换提供了专一命令，把这一职责从同时负责文件恢复的 `git checkout` 中分离出来。

用 `-c` 可以一步创建新分支并切换过去；用 `--detach` 可以移动到某个具体提交而不处于任何分支上。

# CAVEATS

引入后的几个版本中曾被标记为实验性；此后行为已趋于稳定，但在较旧的 Git 安装上请查阅 `git switch --help` 了解差异。

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

[git-checkout](/man/git-checkout)(1), [git-branch](/man/git-branch)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-switch)```

<!-- verified: 2026-07-17 -->
