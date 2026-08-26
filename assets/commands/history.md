# TAGLINE

用于显示或操作命令历史列表的 bash 内建命令

# TLDR

**显示带行号的命令历史**

```history```

**显示最近 N 条命令**

```history [20]```

**清空全部历史**

```history -c```

**按行号删除指定历史条目**

```history -d [42]```

**将当前会话的历史追加到历史文件**

```history -a```

**读取历史文件并追加到当前列表**

```history -r```

**将当前历史写入历史文件**

```history -w```

**按编号执行历史中的命令**

```![42]```

**执行上一条命令**

```!!```

# SYNOPSIS

**history** [_n_]

**history** -c

**history** -d _offset_

**history** [-anrw] [_filename_]

**history** -p _arg_ [_arg_ ...]

**history** -s _arg_ [_arg_ ...]

# PARAMETERS

**-c**
> 清空历史列表

**-d** _OFFSET_
> 删除位置 offset 处的历史条目

**-d** _START-END_
> 删除 start 和 end 之间的历史条目区间

**-a**
> 将新增的历史行追加到历史文件

**-n**
> 从文件读取尚未读取过的历史行并加入当前列表

**-r**
> 读取历史文件并将其内容追加到历史列表

**-w**
> 将当前历史写入历史文件

**-p**
> 对参数执行历史替换并显示结果，但不保存

**-s** _ARG_
> 将参数作为单个条目追加到历史列表末尾

# ENVIRONMENT

**HISTFILE**
> 保存历史的文件（默认：~/.bash_history）

**HISTSIZE**
> 当前会话在内存中保留的命令数量

**HISTFILESIZE**
> 历史文件中保留的命令数量

**HISTTIMEFORMAT**
> 时间戳的格式字符串（strftime 格式）

**HISTCONTROL**
> 控制哪些内容被保存（ignorespace、ignoredups、erasedups）

**HISTIGNORE**
> 以冒号分隔的要忽略的命令模式

# DESCRIPTION

**history** 是一个 bash 内建命令，用于显示或操作命令历史列表。shell 会记录会话期间输入的命令，方便快速调用之前的命令。

不带参数时，history 显示带编号的命令列表。给定整数参数 **n** 时，只显示最后 n 条。shell 启动时会从 **HISTFILE** 加载历史，可用 **-w** 写回，或在退出时自动写回。

历史扩展支持重复执行之前的命令：**!!** 重复上一条命令，**!n** 执行编号为 n 的命令，**!string** 执行最近一条以 string 开头的命令，**!?string** 匹配任何包含 string 的命令。可使用 **Ctrl+r** 进行交互式反向搜索。

# CAVEATS

若 **HISTCONTROL** 包含 ignorespace，则以空格开头的命令不会保存。历史是每个 shell 独立的，并发会话之间不共享，除非用 **-a** 和 **-r** 显式同步。历史文件可能包含不小心在命令行上输入的密码等敏感信息。请使用 **HISTIGNORE** 排除敏感命令。

# HISTORY

命令历史起源于 Bill Joy 于 20 世纪 70 年代末在伯克利开发的 **C shell**（csh）。bash 的实现基于提供历史操作和编辑能力的 **GNU Readline** 库。history 命令及其扩展语法已成为 Unix shell 的标准特性，让用户能够高效地复用和修改之前的命令。

# SEE ALSO

[bash](/man/bash)(1), [fc](/man/fc)(1), [readline](/man/readline)(3)
