# TAGLINE

使用简写表示法克隆 GitHub 仓库

# TLDR

**用简写方式克隆**

```hub clone [user/repo]```

**克隆到指定目录**

```hub clone [user/repo] [directory]```

**按深度克隆**

```hub clone --depth [1] [user/repo]```

**克隆自己的仓库**

```hub clone [repo-name]```

# SYNOPSIS

**hub clone** [_options_] _repository_ [_directory_]

# PARAMETERS

_[USER/]REPOSITORY_
> 要克隆的仓库。省略 _USER_ 时默认为你自己的 GitHub 用户名。

_DIRECTORY_
> 克隆到的目标目录（默认：仓库名）。

**-p**
> （已弃用）通过 SSH 克隆私有仓库。

**--depth** _N_
> 创建具有指定提交历史深度的浅克隆。直接透传给 git clone。

**-b**, **--branch** _BRANCH_
> 检出 _BRANCH_ 而不是远程的默认分支。直接透传给 git clone。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hub clone** 会把 GitHub 简写（`user/repo`，或对于你自己的仓库只写 `repo`）展开成完整的克隆 URL，然后交给普通的 **git clone** 处理，因此任何 git-clone 选项（**--depth**、**-b**、**--recurse-submodules** 等）都能照常使用。如果没有 `user/` 前缀，hub 会假定该仓库属于当前认证的 GitHub 用户。

默认情况下 hub 通过 HTTPS 克隆；运行 `git config --global hub.protocol ssh` 可让它在 **clone**、**fork** 及相关命令中改用 SSH URL。

# CAVEATS

Hub 已不再活跃维护，已被官方 GitHub CLI（**gh**，即 **gh repo clone**）取代。只有在处理私有仓库，或需要针对自己的账号解析 `repo`（不带用户前缀）这种简写时才需要 GitHub 认证；克隆公开的 `user/repo` 无需认证。

# HISTORY

hub clone 是 **hub** 的组成部分。hub 是 GitHub 最早的命令行工具，早于官方的 **gh** CLI。

# INSTALL

```apt: sudo apt install hub```

```pacman: sudo pacman -S hub```

```zypper: sudo zypper install hub```

```brew: brew install hub```

```nix: nix profile install nixpkgs#hub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hub](/man/hub)(1), [git-clone](/man/git-clone)(1), [gh](/man/gh)(1)

# RESOURCES

```[Source code](https://github.com/mislav/hub)```

<!-- verified: 2026-07-19 -->
