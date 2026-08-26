# TAGLINE

管理项目中内嵌的外部仓库

# TLDR

**添加子模块**

```git submodule add [url] [path]```

**初始化子模块**

```git submodule init```

**更新子模块**

```git submodule update```

**连同子模块一起克隆**

```git submodule update --init --recursive```

**查看子模块状态**

```git submodule status```

**拉取子模块的更新**

```git submodule update --remote```

**移除子模块**

```git submodule deinit [path] && git rm [path]```

**在每个子模块中运行命令**

```git submodule foreach '[command]'```

**将子模块 URL 从 .gitmodules 同步到本地配置**

```git submodule sync --recursive```

# SYNOPSIS

**git** **submodule** _command_ [_options_]

# SUBCOMMANDS

**add** _URL_ [_path_]
> 在给定路径上将某个仓库添加为子模块。

**init** [_path_...]
> 初始化索引中记录的子模块。

**update** [_path_...]
> 更新已注册的子模块以与父项目保持一致。

**status** [_path_...]
> 显示子模块的状态。

**deinit** [_path_...]
> 注销子模块并删除其工作树。

**sync** [_path_...]
> 将子模块的远程 URL 从 .gitmodules 同步到本地配置。

**foreach** _command_
> 在每个已检出的子模块中执行一条 shell 命令。

**summary** [_commit_] [_path_...]
> 显示某提交与工作树/索引之间的提交摘要。

**set-branch** _path_
> 设置子模块默认跟踪的远程分支。

**set-url** _path_ _newurl_
> 设置子模块的 URL。

**absorbgitdirs**
> 将子模块的 .git 目录迁移到父项目的 .git/modules/ 中。

# PARAMETERS

**--init**
> 更新前先初始化尚未初始化的子模块。

**--recursive**
> 递归处理嵌套的子模块。

**--remote**
> 使用子模块的远程跟踪分支，而不是父项目记录的 SHA-1。

**-f**, **--force**
> 即使子模块已经一致也强制检出。

**-b** _branch_, **--branch** _branch_
> 要跟踪的仓库分支（用于 add、set-branch）。

**-j** _n_, **--jobs** _n_
> 以 n 个并行任务克隆新的子模块。

**-q**, **--quiet**
> 只输出错误信息。

**--depth** _depth_
> 创建历史被截断的浅克隆。

**-N**, **--no-fetch**
> 不从远程获取新对象（update 时）。

# DESCRIPTION

**git submodule** 管理子模块——即嵌入在父仓库特定路径上的外部 Git 仓库。每个子模块都跟踪外部仓库的某一个特定提交。

借助子模块，项目可以包含并跟踪依赖或共享组件，同时保持各自的历史相互独立。克隆之后使用 `update --init --recursive` 即可填充所有子模块的内容。

# CONFIGURATION

**.gitmodules**
> 配置文件，记录子模块名称与其仓库 URL 及本地路径的对应关系。

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

[git-clone](/man/git-clone)(1), [git-remote](/man/git-remote)(1), [git-fetch](/man/git-fetch)(1)
