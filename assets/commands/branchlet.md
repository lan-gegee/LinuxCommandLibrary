# TAGLINE

交互式 Git worktree 管理 TUI

# TLDR

**启动** worktree 管理器

```branchlet```

# SYNOPSIS

**branchlet** [_options_]

# DESCRIPTION

**branchlet** 是一个用于管理 **Git worktree** 的交互式终端用户界面。它通过可视化界面简化了创建、切换和删除 Git worktree 的工作流程，无需记忆 git worktree 子命令。

该 TUI 会显示现有的 worktree 及其关联的分支和路径。用户可以从分支创建新 worktree、删除 worktree，并使用键盘快捷键在它们之间切换。

# CAVEATS

必须在 Git 仓库内运行。需要支持 worktree 的 Git 版本（Git 2.5+）。通过 branchlet 删除 worktree 时也会一并清理 Git 的 worktree 元数据。

# SEE ALSO

[git](/man/git)(1), [git-worktree](/man/git-worktree)(1), [lazygit](/man/lazygit)(1)
