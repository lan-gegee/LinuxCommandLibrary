# TAGLINE

终端任务与笔记看板

# TLDR

**显示所有任务和笔记**

```tb```

**创建新任务**

```tb -t [Buy groceries]```

**在特定看板上创建任务**

```tb -t @[work] [Finish report]```

**创建笔记**

```tb -n [Remember to call John]```

**勾选/取消勾选**任务为完成状态

```tb -c [1] [2]```

**设置任务优先级**（1=普通，2=中，3=高）

```tb -p [1] [3]```

**删除条目**

```tb -d [1] [2]```

**搜索条目**

```tb -f [keyword]```

**显示时间线视图**

```tb -i```

# SYNOPSIS

**tb** [_options_] [_arguments_]

# PARAMETERS

**-t**, **--task** _description_
> 创建新任务；使用 @board 指派到看板

**-n**, **--note** _body_
> 创建新笔记

**-c**, **--check** _ids_
> 切换任务的完成状态

**-b**, **--begin** _ids_
> 开始或暂停任务

**-s**, **--star** _ids_
> 为条目加星或取消加星

**-p**, **--priority** _id_ _level_
> 设置任务优先级（1=普通，2=中，3=高）

**-m**, **--move** _id_ _@board_
> 将条目移动到其他看板

**-d**, **--delete** _ids_
> 删除条目（移入归档）

**-e**, **--edit** _id_ _description_
> 编辑条目描述

**-f**, **--find** _keywords_
> 按关键词搜索条目

**-l**, **--list** _attributes_
> 按属性过滤并列出条目

**-a**, **--archive**
> 显示已归档的条目

**-r**, **--restore** _ids_
> 从归档中恢复条目

**--clear**
> 删除所有已勾选（完成）的任务

**-y**, **--copy** _ids_
> 复制条目描述到剪贴板

**-i**, **--timeline**
> 按创建日期分组显示条目

**--taskbook-dir** _path_
> 使用自定义的 taskbook 存储目录

**-h**, **--help**
> 显示帮助信息

**-v**, **--version**
> 显示版本号

# DESCRIPTION

**tb**（Taskbook）是一个以看板为核心组织方式的命令行任务与笔记管理器。它提供一个极简界面，可直接在终端中创建、组织和追踪任务与笔记。

使用 **@boardname** 语法将条目组织到看板中。未指派看板的任务会进入默认的 "My Board"。一个条目可以同时指派到多个看板。界面会显示统计信息，包括待办、已完成和笔记的数量。

任务可以设置优先级（以不同颜色显示）、加星标强调，以及用 begin 命令标记为进行中。被删除的条目会进入归档，可以恢复。时间线视图按创建日期而非看板对条目分组。

数据以 JSON 格式存储在 **~/.taskbook/storage**。配置选项可在 **~/.taskbook.json** 中设置。

# CAVEATS

Taskbook 需要 Node.js 和 npm 才能安装。随着删除条目的累积，归档会不断增大，可能需要定期手动清理。看板名称区分大小写。

# HISTORY

**Taskbook** 由 **Klaus Sinani**（klaudiosinani）创建，于 **2018 年**发布在 **GitHub** 上。它使用 JavaScript 编写、基于 Node.js，旨在把任务管理直接带入终端工作流，强调简单易上手。

# SEE ALSO

[task](/man/task)(1), [todo.txt-cli](/man/todo.txt-cli)(1), [todoist](/man/todoist)(1)
