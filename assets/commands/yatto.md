# TAGLINE

终端中基于 Git 的交互式待办清单

# TLDR

**启动交互式 TUI**

```yatto```

**添加任务**

```yatto add "[Fix login bug]" --project [myapp] --priority high```

**列出未完成任务**

```yatto list --status open```

# SYNOPSIS

**yatto** [_command_] [_options_]

# DESCRIPTION

**yatto** 是一个终端任务管理器，它将每个任务存储为一个 JSON 文件，并把任务目录作为 Git 或 Jujutsu 仓库来管理。每次更改都会被版本化记录，从而可以通过共享仓库实现同步和协作。支持截止日期、优先级、状态和 markdown 描述。

# HISTORY

**yatto** 由 **handlebargh** 创建，使用 **Go** 编写。

# INSTALL

```nix: nix profile install nixpkgs#yatto```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[taskwarrior](/man/taskwarrior)(1), [todoman](/man/todoman)(1)
