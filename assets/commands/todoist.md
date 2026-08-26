# TAGLINE

命令行 Todoist 服务客户端

# TLDR

**添加任务**

```todoist add "[task description]"```

**列出任务**

```todoist list```

**完成任务**

```todoist close [task-id]```

**带截止日期添加**

```todoist add "[task]" --date "[tomorrow]"```

**添加到项目**

```todoist add "[task]" --project "[Project Name]"```

**同步**

```todoist sync```

# SYNOPSIS

**todoist** _command_ [_--date date_] [_--project name_] [_options_]

# PARAMETERS

**add**
> 创建任务。

**list**
> 显示任务。

**close**
> 完成任务。

**sync**
> 与服务器同步。

**--date** _DATE_
> 截止日期。

**--project** _NAME_
> 目标项目。

**--priority** _N_
> 优先级。

# DESCRIPTION

**todoist** 是 Todoist 任务管理服务的命令行客户端，让你可以在终端访问云同步的任务列表。任务可以用 "tomorrow" 或 "next week" 等自然语言截止日期创建，并可组织到项目中以及指定优先级。

该工具与 Todoist 云服务同步，因此在 CLI 中所做的更改会立即出现在所有其他设备上。身份验证需要 API token，通常在首次使用时配置。

# CAVEATS

需要 Todoist 账户。需要 API token。依赖网络。

# HISTORY

针对 **Todoist** 任务管理服务存在多种 **todoist** CLI 客户端，提供终端访问能力。

# INSTALL

```brew: brew install todoist```

```nix: nix profile install nixpkgs#todoist```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[task](/man/task)(1), [todo.sh](/man/todo.sh)(1), [todoman](/man/todoman)(1)
