# TAGLINE

在结构化的目录层级中管理远程仓库的克隆

# TLDR

**克隆一个仓库**

```ghq get [https://github.com/owner/repo]```

**通过 SSH 克隆仓库**

```ghq get -p [owner/repo]```

**列出受管理的仓库**

```ghq list```

**列出完整路径**

```ghq list -p```

**获取仓库根目录**

```ghq root```

**创建新仓库**

```ghq create [owner]/[repo]```

**删除本地仓库**

```ghq rm [owner/repo]```

**更新已克隆的仓库**

```ghq get -u [owner/repo]```

# SYNOPSIS

**ghq** _command_ [_options_] [_arguments_]

# PARAMETERS

**get** _URL_
> 克隆一个仓库。别名：clone。

**list** [_query_]
> 列出本地仓库，可按查询条件过滤。

**root**
> 显示仓库根路径。

**create** _NAME_
> 在本地创建一个新仓库。

**rm** _NAME_
> 删除本地仓库克隆。

**-p**
> 通过 SSH 克隆（get）或显示完整路径（list）。

**-u**, **--update**
> 更新已有仓库（pull --ff-only）。

**--shallow**
> 浅克隆（深度为 1，仅 Git）。

**--branch** _BRANCH_
> 克隆指定分支。

**--bare**
> 执行裸克隆（bare clone，仅 Git）。

**--no-recursive**
> 不克隆 git 子模块。

**-e**, **--exact**
> 要求查询完全匹配（list）。

**--dry-run**
> 仅显示路径而不删除（rm）。

**--vcs** _VCS_
> 指定版本控制后端：git、svn、hg、darcs、fossil、bzr。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ghq** 在结构化的目录层级中管理远程仓库的克隆。它根据仓库 URL 将其克隆到有组织的路径中，从而实现跨项目一致的仓库组织方式。

该工具可与 Shell 工作流以及 **fzf** 等模糊查找器集成，实现快速导航仓库。它支持 GitHub、GitLab、Bitbucket 以及自定义 Git 主机。

# CONFIGURATION

**~/.gitconfig**
> 使用 `ghq.root` 设置配置仓库根路径，使用 `ghq.user` 设置默认用户，使用 `ghq.<url>.vcs` 为特定 URL 指定版本控制系统。

**GHQ_ROOT**
> 用于覆盖所有 ghq.root 设置的环境变量。

# CAVEATS

需要 git。默认根目录为 ~/ghq，可通过 gitconfig 中的 ghq.root 或环境变量 GHQ_ROOT 配置。目录结构由 URL 解析结果决定。支持 Git 以外的多种版本控制后端。

# HISTORY

ghq 由 **motemen** 创建，是一个用于组织 Git 仓库的工具，灵感来自 go get 的目录结构约定。

# INSTALL

```pacman: sudo pacman -S ghq```

```brew: brew install ghq```

```nix: nix profile install nixpkgs#ghq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [fzf](/man/fzf)(1), [gh](/man/gh)(1)
