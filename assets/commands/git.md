# TAGLINE

用于跟踪代码变更的分布式版本控制系统

# TLDR

**克隆一个仓库**

```git clone [https://github.com/owner/repo.git]```

**暂存并提交更改**

```git add . && git commit -m "[message]"```

**推送到远程**

```git push origin [branch]```

**拉取更改**

```git pull```

**创建并切换分支**

```git checkout -b [branch-name]```

# SYNOPSIS

**git** [_options_] _command_ [_args_]

# PARAMETERS

**init**
> 创建空的 Git 仓库，或重新初始化已有仓库。

**clone** _URL_
> 将仓库克隆到新目录。

**add** _FILES_
> 暂存文件以便提交。

**commit**
> 将更改记录到仓库。

**status**
> 显示工作树状态。

**diff**
> 显示提交之间、工作树与索引之间的差异。

**push**
> 更新远程引用及相关对象。

**pull**
> 从远程获取并合并。

**fetch**
> 从另一个仓库下载对象和引用但不合并。

**checkout**
> 切换分支或恢复工作树文件。

**switch**
> 切换分支。

**branch**
> 列出、创建或删除分支。

**merge**
> 合并两个或以上的开发历史。

**rebase**
> 把提交重新应用到另一个基点之上。

**log**
> 显示提交历史。

**remote**
> 管理被跟踪的远程仓库集合。

**-v**, **--version**
> 打印 Git 套件版本。

**-C** _PATH_
> 如同 git 是在 _PATH_ 而非当前目录中启动一样运行。

**-c** _NAME_=_VALUE_
> 传递一条仅在本次命令期间生效的配置值。

**-p**, **--paginate**
> 将输出送入分页器（通常是 `less`）。

**--git-dir** _PATH_
> 设置仓库 `.git` 目录的路径。

**--work-tree** _PATH_
> 设置工作树的路径。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git** 是一个分布式版本控制系统，用于跟踪源代码的变更。它通过分支、合并和远程仓库支持协作开发，同时保留完整历史。

Git 的分布式特性意味着每个克隆都包含完整的历史记录。分支十分轻量，便于开展功能开发工作流程。暂存区提供了细粒度的提交控制。

# CONFIGURATION

**~/.gitconfig**
> 全局用户配置，包括身份、别名和默认行为。

**.git/config**
> 仓库级配置，涵盖远程、分支和本地设置。

**~/.gitignore_global**
> 应用于所有仓库的全局忽略模式。

# CAVEATS

高级功能有一定学习曲线。大型二进制文件需要 git-lfs。重写历史会影响协作者。

# HISTORY

Git 由 **Linus Torvalds** 于 **2005 年**为 Linux 内核开发而创建，起因是 BitKeeper 的授权问题。如今它已成为大多数软件项目采用的标准版本控制系统。

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

[gh](/man/gh)(1), [git-commit](/man/git-commit)(1), [git-push](/man/git-push)(1), [git-log](/man/git-log)(1), [git-branch](/man/git-branch)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git)```

<!-- verified: 2026-07-17 -->
