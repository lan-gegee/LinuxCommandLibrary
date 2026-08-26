# TAGLINE

Zsh 行编辑器内建命令

# TLDR

**通过 shell 函数定义新 widget**

```zle -N [widget_name] [function_name]```

**列出所有用户定义的 widget**

```zle -l```

**列出所有 widget（含内建）**

```zle -la```

**以可重建的 zle 命令形式列出 widget**

```zle -lL```

**删除用户定义的 widget**

```zle -D [widget_name]```

**创建 widget 别名**

```zle -A [old_widget] [new_widget]```

**在 shell 函数中调用 widget**

```zle [widget_name]```

**在命令行下方显示消息**

```zle -M "[message]"```

# SYNOPSIS

**zle** [_-lLaD_] [_widget ..._]
**zle** **-N** _widget_ [_function_]
**zle** **-C** _widget_ _completion-widget_ _function_
**zle** **-R** [**-c**] [_display-string_] [_string ..._]
**zle** **-M** _string_
**zle** **-U** _string_
**zle** **-K** _keymap_
**zle** **-F** [**-Lw**] [_fd_ [_handler_]]
**zle** _widget_ [**-n** _num_] [**-f** _flag_] [**-Nw**] [**-K** _keymap_] [**--** _args ..._]

# PARAMETERS

**-N** _widget_ [_function_]
> 定义一个由 shell 函数支撑的新用户自定义 widget。若省略 function，则默认使用 widget 名称

**-C** _widget_ _completion-widget_ _function_
> 创建一个继承既有内建补全 widget 行为的用户自定义补全 widget

**-l** [**-L** | **-a**]
> 列出用户自定义的 widget。**-L**：格式化为 zle 命令。**-a**：包含内建 widget

**-D** _widget ..._
> 删除指定的用户自定义 widget

**-A** _old-widget_ _new-widget_
> 创建别名；两个名称指向同一个 widget

**-R** [**-c**] [_display-string_] [_string ..._]
> 重新显示命令行。可选的 display-string 显示在状态行中。**-c** 清除补全列表

**-M** _string_
> 在命令行下方显示一条消息，且在 widget 返回后仍然保留

**-U** _string_
> 将字符推入 ZLE 的输入栈，在当前 widget 结束后进行处理

**-K** _keymap_
> 为后续按键选择指定的键映射

**-F** [**-Lw**] [_fd_ [_handler_]]
> 为文件描述符安装或移除处理器。**-w**：处理器是 widget。**-L**：列出处理器

**-I**
> 在外部输出之前使当前显示失效

**-f** _flag ..._
> 为当前 widget 设置标志：**yank**、**yankbefore**、**kill**、**vichange**、**nolast**

# DESCRIPTION

**zle** 是 **zsh** 的一个内建命令，用于控制 Zsh Line Editor（Zsh 行编辑器），即交互式命令行编辑子系统。它管理 widget（命名的编辑动作）、键映射、显示控制和编辑缓冲区。不带参数调用时，如果 ZLE 当前处于活动状态则返回零。完整文档见 **zshzle(1)** man page。

ZLE 在交互式 zsh 会话中自动启用。它工作于**多行模式**（默认）或**单行模式**（设置了 **SINGLE_LINE_ZLE** 选项时）。诸如 **BUFFER**、**CURSOR**、**LBUFFER** 和 **RBUFFER** 之类的特殊参数允许 widget 函数直接操作编辑缓冲区。

# KEYMAPS

ZLE 提供八个内建键映射：

**emacs** -- Emacs 风格编辑
**viins** -- Vi 插入模式
**vicmd** -- Vi 命令模式
**viopp** -- Vi 操作符等待模式
**visual** -- Vi 可视选择模式
**isearch** -- 增量搜索模式
**command** -- 命令名读取模式
**.safe** -- 不可变的后备键映射

**main** 键映射根据 **EDITOR** 环境变量链接到 **emacs** 或 **viins**，也可以通过 **bindkey -e**（emacs）或 **bindkey -v**（vi）设置。

# CONFIGURATION

ZLE 主要通过 **.zshrc** 中的 **bindkey** 命令和 **zle -N** widget 定义进行配置。**KEYTIMEOUT** 参数（默认 40，单位为百分之一秒）控制 ZLE 等待多字符按键序列的时长。诸如 **zle-line-init**、**zle-line-finish** 和 **zle-keymap-select** 这类钩子 widget 会在特定事件发生时自动运行。

在命令前添加 sudo 的自定义 widget 示例：

```
prepend-sudo() {
  BUFFER="sudo $BUFFER"
  CURSOR+=5
}
zle -N prepend-sudo
bindkey '^s' prepend-sudo
```

# SPECIAL PARAMETERS

当用户自定义的 widget 函数运行时，可以使用以下可读写参数：

**BUFFER** -- 整个编辑缓冲区的内容
**CURSOR** -- 光标位置（BUFFER 中的索引）
**LBUFFER** -- 光标左侧的缓冲区内容
**RBUFFER** -- 光标右侧的缓冲区内容
**WIDGET** -- 正在执行的 widget 名称
**LASTWIDGET** -- 上一次执行的 widget 名称
**KEYS** -- 触发此 widget 时按下的按键
**NUMERIC** -- 数字前缀参数（如有）
**KEYMAP** -- 当前选定的键映射

# CAVEATS

**zle** 仅在 **zsh** 中可用，既不是 POSIX 命令，bash 中也没有。widget 只有在交互模式下 ZLE 处于活动状态时才能被调用。widget 的 shell 函数运行时其 stdin 被重定向到 **/dev/null**。内建 widget 有带点前缀的变体（例如 **.end-of-line**），即使该 widget 被覆盖，这些变体仍可访问。

# HISTORY

ZLE 是 zsh（Z Shell）的基础组件。zsh 由 **Paul Falstad** 于 **1990 年**在普林斯顿大学编写。ZLE 为 zsh 提供了仿照 Emacs 和 vi 编辑模式的精细行编辑功能，但它是 zsh 自己的独立实现，采用基于 widget 的架构，与 bash 使用的 GNU Readline 不同。

# SEE ALSO

[zsh](/man/zsh)(1), [bindkey](/man/bindkey)(1)
