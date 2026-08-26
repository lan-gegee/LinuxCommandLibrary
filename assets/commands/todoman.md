# TAGLINE

兼容 CalDAV 的待办事项管理器

# TLDR

**列出任务**

```todoman list```

**添加任务**

```todoman new "[task description]"```

**完成任务**

```todoman done [id]```

**编辑任务**

```todoman edit [id]```

**删除任务**

```todoman delete [id]```

**显示任务**

```todoman show [id]```

# SYNOPSIS

**todoman** _command_ [_options_] [_args_]

# PARAMETERS

**list**
> 列出任务。

**new**
> 创建任务。

**done**
> 完成任务。

**edit**
> 修改任务。

**delete**
> 移除任务。

**--list** _NAME_
> 指定列表。

# DESCRIPTION

**todoman** 是一个命令行待办事项管理器，以标准 iCalendar VTODO 格式存储任务。这使它与支持 iCalendar 标准的 CalDAV 服务器及其他日历应用兼容。

与 **vdirsyncer** 配合使用时，todoman 可以与 Nextcloud、Radicale 等 CalDAV 服务器或其他兼容服务同步任务。它支持多个列表、周期性任务、截止日期和优先级，全部存储在磁盘上的标准 .ics 文件中。

# CONFIGURATION

**~/.config/todoman/todoman.conf**
> 主配置文件，指定日历路径、日期格式、默认列表和显示设置。

# CAVEATS

需要已配置的日历。推荐配合 vdirsyncer 使用。基于 Python。

# HISTORY

**todoman** 为管理 iCalendar 格式的待办事项而创建，通过 vdirsyncer 支持 CalDAV 服务器。

# INSTALL

```pacman: sudo pacman -S todoman```

```brew: brew install todoman```

```nix: nix profile install nixpkgs#todoman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vdirsyncer](/man/vdirsyncer)(1), [khal](/man/khal)(1), [task](/man/task)(1)
