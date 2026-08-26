# TAGLINE

基于 shell 的 todo.txt 任务管理

# TLDR

**添加新任务**

```todo.sh add "[Buy groceries +shopping @errands]"```

**列出所有任务**

```todo.sh list```

**列出匹配关键词的任务**

```todo.sh list "[search term]"```

**将任务标记为完成**

```todo.sh do [1]```

**为任务设置优先级**

```todo.sh pri [1] [A]```

**向任务追加文本**

```todo.sh append [1] "[additional text]"```

**归档已完成的任务**

```todo.sh archive```

**删除任务**

```todo.sh del [1]```

# SYNOPSIS

**todo.sh** [_options_] _action_ [_task_number_] [_task_description_]

# ACTIONS

**add** _text_: 添加新任务。

**list** _term_: 列出匹配关键词的任务。

**listall** _term_: 列出包括已完成在内的所有任务。

**do** _n_: 将任务 n 标记为完成。

**pri** _n_ _priority_: 为任务 n 设置优先级（A-Z）。

**depri** _n_: 移除任务 n 的优先级。

**append** _n_ _text_: 向任务 n 追加文本。

**prepend** _n_ _text_: 在任务 n 开头插入文本。

**replace** _n_ _text_: 用新文本替换任务 n。

**del** _n_: 删除任务 n。

**archive**: 将已完成的任务移动到 done.txt。

**report**: 将未完成/已完成数量追加到 report.txt。

**deduplicate**: 移除重复行。

# PARAMETERS

**-f**
> 强制执行操作而不确认。

**-h**
> 显示帮助。

**-p**
> 纯文本模式（无颜色）。

**-a**
> 不自动归档已完成的任务。

**-n**
> 不保留行号。

**-t**
> 添加时不自动加日期前缀。

**-v**
> 详细模式。

**-V**
> 显示版本。

**-d** _file_
> 使用替代的配置文件。

# DESCRIPTION

**todo.txt-cli**（todo.sh）是一个 shell 脚本，用于在纯文本文件中管理任务。它遵循 todo.txt 格式，用简单约定表示优先级、项目（+project）、上下文（@context）和日期。

任务存储在 todo.txt 中，每行一条。已完成的任务可以选择归档到 done.txt。纯文本格式确保了可移植性，并与任何文本编辑器、同步服务或脚本工具兼容。

该脚本支持优先级、上下文和项目的 Tab 补全。配置通过 .todo.cfg 文件完成，可自定义颜色、文件位置和默认行为。

通过包管理器或 Homebrew 安装：`brew install todo-txt`

# CAVEATS

需要 Bash。任务编号会随任务的添加或删除而变化。定期执行 archive 以保持编号一致。纯文本格式意味着没有内置提醒或依赖关系。

# HISTORY

**todo.txt** 由 Gina Trapani 创建，是一套简单、可移植的任务管理系统。其格式和 CLI 工具启发了各平台上众多应用和实现。该项目强调面向未来、人类可读的任务存储方式。

# SEE ALSO

[task](/man/task)(1), [taskwarrior](/man/taskwarrior)(1), [remind](/man/remind)(1)
