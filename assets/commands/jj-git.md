# TAGLINE

为 Jujutsu 提供 Git 互操作性

# TLDR

克隆 Git 仓库

```jj git clone [url]```

在现有 Git 仓库中初始化 jj（共存模式）

```jj git init --colocate```

从所有远程抓取

```jj git fetch```

将当前分支推送到远程

```jj git push```

将 Git 引用导入 jj

```jj git import```

将 jj 引用导出到 Git

```jj git export```

添加 Git 远程

```jj git remote add [name] [url]```

# SYNOPSIS

**jj git** _subcommand_ [_options_]

# PARAMETERS

**clone** _URL_ [_DESTINATION_]
> 克隆 Git 仓库并创建 jj 仓库。

**init** [_DESTINATION_]
> 创建新的 Git 后端 jj 仓库。

**fetch**
> 从 Git 远程抓取。

**push**
> 推送到 Git 远程。

**import**
> 将 Git 引用（分支、标签）导入 jj 的内部状态。

**export**
> 将 jj 引用导出为 Git 引用。

**remote** _subcommand_
> 管理 Git 远程（add、remove、list、rename）。

**--remote** _NAME_
> 指定远程名称。

**--branch** _BRANCH_
> 指定分支（用于 push/fetch）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jj git** 为现代版本控制系统 Jujutsu（jj）提供 Git 互操作能力。它支持在 Git 服务器上克隆、抓取、推送和管理远程。

Jujutsu 使用 Git 作为存储后端，因此所有显式的 Git 互操作命令都位于 **git** 子命令之下。**init --colocate** 选项允许 jj 与现有 .git 目录并存并保持两者同步。

# CAVEATS

jj 的子命令。需要 Git 后端。某些 Git 工作流（如暂存区）在 jj 中以不同方式处理。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-git-push](/man/jj-git-push)(1), [jj-git-clone](/man/jj-git-clone)(1), [git](/man/git)(1)
