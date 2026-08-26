# TAGLINE

列出待处理的 systemd 任务

# TLDR

列出**所有**待处理和正在运行的任务

```systemctl list-jobs```

按**模式**匹配过滤任务

```systemctl list-jobs [pattern]```

按 ID **取消**特定任务

```systemctl cancel [job_id]```

# SYNOPSIS

**systemctl list-jobs** [_PATTERN_...]

# DESCRIPTION

**systemctl list-jobs** 显示 systemd 服务管理器中待处理和正在运行的任务队列。任务代表状态更改操作，例如启动、停止或重新加载单元。

输出内容包括任务 ID、单元名称、任务类型（start、stop、reload 等）和状态（waiting、running）。任务会在启动期间或触发多个单元状态更改时出现。

# JOB TYPES

**start** - 启动一个单元

**stop** - 停止一个单元

**reload** - 重新加载配置

**restart** - 重启一个单元

**try-restart** - 若单元处于活动状态则重启它

**reload-or-restart** - 重新加载或重启一个单元

**verify-active** - 检查是否处于活动状态

**nop** - 无操作（用于排序）

# CAVEATS

空闲系统的任务队列通常是空的。任务只在状态更改期间短暂存在，可能在命令输出显示之前就已完成。任务 ID 可配合 `systemctl cancel` 使用。

# HISTORY

**list-jobs** 子命令让 systemd 的内部任务队列可见，可用于排查卡住的启动过程或了解服务为何未能启动。它自 systemd 首个版本起就存在。

# SEE ALSO

[systemctl-cancel](/man/systemctl-cancel)(1), [systemctl](/man/systemctl)(1)
