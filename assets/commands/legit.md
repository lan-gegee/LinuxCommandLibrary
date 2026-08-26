# TAGLINE

Git 的辅助命令行界面，简化常见工作流

# TLDR

**切换**分支并自动 stash

```git sw [branch]```

将当前分支与远程**同步**

```git sync```

将分支**发布**到远程

```git publish [branch]```

从远程**撤销发布**分支

```git unpublish [branch]```

列出**所有分支**及其状态

```git branches [pattern]```

**撤销**最近一次提交

```git undo --hard```

# SYNOPSIS

**git** _legit-command_ [_options_]

# DESCRIPTION

**legit** 是 Git 的辅助命令行界面，用于简化常见工作流。它新增了带自动 stash 的分支切换、同步以及分支发布等命令。

安装后，legit 命令可作为 Git 子命令使用（例如 `git sw`、`git sync`）。

# PARAMETERS

**sw BRANCH**
> 切换到指定分支，自动 stash 并恢复未暂存的更改

**sync**
> 将当前分支与远程同步（merge 或 rebase）

**publish BRANCH**
> 将分支推送到远程服务器

**unpublish BRANCH**
> 从远程服务器移除分支

**branches [PATTERN]**
> 列出分支及其发布状态

**undo [--hard]**
> 从历史中移除最近一次提交

# CAVEATS

Legit 命令是对标准 Git 操作的封装。`undo` 命令配合 `--hard` 会永久丢弃更改。

# INSTALL

```brew: brew install legit```

```nix: nix profile install nixpkgs#legit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [git-flow](/man/git-flow)(1)
