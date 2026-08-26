# TAGLINE

Rust 编写的命令行 Todoist 客户端

# TLDR

**导入**项目

```tod project import```

**快速添加**任务

```tod --quickadd [Buy more milk today]```

**创建**新任务

```tod task create```

在**项目**中创建任务

```tod task create --content "[Write more rust]" --project [code]```

获取**下一项**任务

```tod task next```

获取**已排期**的任务

```tod task list --scheduled --project [work]```

**列出**所有任务

```tod task list --project [work]```

# SYNOPSIS

**tod** [_OPTIONS_] _COMMAND_ [_ARGS_]

# COMMANDS

**project import**
> 导入你的 Todoist 项目

**task create**
> 创建新任务

**task next**
> 获取某个项目的下一项任务

**task list**
> 列出任务

# PARAMETERS

**--quickadd** _TEXT_
> 用自然语言快速创建任务

**--content** _TEXT_
> 任务内容/描述

**--project** _NAME_
> 指定项目名称

**--scheduled**
> 只显示已排期的任务

# DESCRIPTION

**tod** 是一个用 Rust 编写的轻量级 Todoist 客户端。它提供命令行界面来管理 Todoist 账户中的任务。该工具利用自然语言处理，从简单的文本输入中解析截止日期、标签和其他任务属性。

任务可以快速添加到收件箱或分配给特定项目。该工具支持查看已排期的任务并管理工作队列。

# CAVEATS

需要 Todoist 账户和 API token 配置。项目必须先导入才能引用。自然语言解析依赖 Todoist 自身的处理能力。

# HISTORY

**tod** 作为一款轻量快速的 Rust 命令行 Todoist 客户端而创建，专注于快速录入任务和简单的项目管理流程。

# SEE ALSO

[taskwarrior](/man/taskwarrior)(1)
