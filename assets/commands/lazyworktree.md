# TAGLINE

面向终端的 Git worktree 管理 CLI 与 TUI

# TLDR

**启动 worktree TUI**

```lazyworktree```

**创建新的 worktree**

```lazyworktree create [branch_name]```

**列出所有 worktree**

```lazyworktree list```

**删除某个 worktree**

```lazyworktree delete [branch_name]```

**在 worktree 中运行命令**

```lazyworktree exec [branch_name] -- [command]```

**重命名当前 worktree**

```lazyworktree rename [new_name]```

# SYNOPSIS

**lazyworktree** [_command_] [_options_]

# SUBCOMMANDS

**create**
> 从分支、PR/MR 或 issue 创建新的 worktree。

**list**
> 列出所有 worktree。

**delete**
> 删除某个 worktree，无需启动 TUI。

**rename**
> 重命名 worktree（只给一个参数时重命名当前目录的 worktree）。

**exec**
> 在 worktree 中运行命令，或触发自定义命令的按键动作。

# DESCRIPTION

**lazyworktree** 是一个采用键盘优先工作流来管理 Git worktree 的终端 UI。它支持创建、重命名、移除、吸收（absorb）以及清理已合并的 worktree，还可以直接在 TUI 中完成暂存、提交、查看差异、推送、同步和 cherry-pick。

功能包括与 GitHub Actions 和 GitLab CI 的 CI/CD 集成（查看检查状态、读取日志、重启作业）、为每个 worktree 提供对应 tmux 和 zellij 会话的终端复用器支持、OCI 容器执行（docker/podman），以及基于 markdown 的任务笔记和交互式任务看板。

# CAVEATS

需要支持 worktree 的 Git。CI/CD 功能需要有 GitHub Actions 或 GitLab CI 配置。

# HISTORY

**lazyworktree** 由 **chmouel** 创建，使用 **Go** 基于 BubbleTea 框架编写。

# INSTALL

```zypper: sudo zypper install lazyworktree```

```nix: nix profile install nixpkgs#lazyworktree```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-worktree](/man/git-worktree)(1), [lazygit](/man/lazygit)(1)
