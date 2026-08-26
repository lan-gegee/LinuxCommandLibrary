# TAGLINE

用多个 Git 仓库管理 dotfiles

# TLDR

**初始化仓库**

```vcsh init [reponame]```

**克隆仓库**

```vcsh clone [url] [reponame]```

**运行 git 命令**

```vcsh [reponame] [git-command]```

**列出仓库**

```vcsh list```

**进入仓库**

```vcsh enter [reponame]```

**查看全部状态**

```vcsh status```

**列出被跟踪的文件**

```vcsh list-tracked [reponame]```

**拉取所有仓库**

```vcsh pull```

在仓库中**添加并提交**文件

```vcsh [reponame] add [~/.bashrc] && vcsh [reponame] commit -m "[message]"```

**推送所有仓库**

```vcsh push```

**重命名仓库**

```vcsh rename [oldname] [newname]```

# SYNOPSIS

**vcsh** [_init|clone|list|enter|run|pull|push_] [_reponame_] [_args_]

# PARAMETERS

**init** _reponame_
> 初始化空仓库。

**clone** _url_ [_reponame_]
> 从 URL 克隆。

**list**
> 列出所有仓库。

**list-tracked** [_reponame_]
> 列出被跟踪的文件。

**list-untracked** [**-a**] [**-r**]
> 列出未跟踪的文件。-a 显示全部，-r 为递归。

**enter** _reponame_
> 生成设置了 $GIT_DIR 的子 Shell。

**run** _reponame_ _command_
> 在设置好 $GIT_DIR 和 $GIT_WORK_TREE 的情况下运行命令。

**pull**
> 从所有仓库拉取。

**push**
> 推送所有仓库。

**rename** _old_ _new_
> 重命名仓库。

**status** [_reponame_]
> 显示所有或某个仓库的状态。

**write-gitignore** _reponame_
> 通过 git ls-files 写入 .gitignore.d/reponame。

**delete** _reponame_
> 删除仓库。

# DESCRIPTION

**vcsh** 使用多个 Git 仓库管理配置文件（dotfiles），这些仓库全部共享同一个工作目录（$HOME）。每个仓库跟踪一组独立的文件，从而可以模块化地组织 shell 配置、编辑器设置和其他 dotfiles。

该工具使用裸（bare）Git 仓库，避免共存于同一目录中的各仓库之间发生冲突。**enter** 命令会打开一个作用于特定仓库的子 Shell，也支持直接对指定仓库运行 git 命令。

# ENVIRONMENT

**VCSH_REPO_D**
> 存放裸仓库的目录（默认：$XDG_CONFIG_HOME/vcsh/repo.d）。

# CAVEATS

需要具备基本的 Git 知识。裸仓库可能令人困惑——可用 `vcsh enter` 检查仓库状态。被多个仓库同时跟踪的文件会导致冲突。

# HISTORY

**vcsh**（version control system for $HOME）由 **Richard Hartmann** 创建，用于管理叠加在 $HOME 上的多个 Git 仓库。

# INSTALL

```dnf: sudo dnf install vcsh```

```pacman: sudo pacman -S vcsh```

```zypper: sudo zypper install vcsh```

```brew: brew install vcsh```

```nix: nix profile install nixpkgs#vcsh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [mr](/man/mr)(1), [stow](/man/stow)(1), [yadm](/man/yadm)(1), [chezmoi](/man/chezmoi)(1)
