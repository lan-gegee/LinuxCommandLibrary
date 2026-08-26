# TAGLINE

用于选项解析的 POSIX shell 内建命令

# TLDR

脚本中的**基本选项解析**

```while getopts "ab:c" opt; do case $opt in a) echo "Option a";; b) echo "Option b with arg: $OPTARG";; c) echo "Option c";; esac; done```

**解析带参数的选项**（字母后跟冒号）

```getopts "f:o:v" opt```

**静默错误模式**（开头加冒号）

```getopts ":ab:c" opt```

解析后**移出已处理的参数**

```shift $((OPTIND - 1))```

**处理未知选项**

```case $opt in \?) echo "Invalid option: -$OPTARG";; esac```

# SYNOPSIS

**getopts** _OPTSTRING_ _NAME_ [_ARGS_]

# PARAMETERS

_OPTSTRING_
> 选项字符组成的字符串。字符后的冒号表示它需要一个参数；开头的冒号启用静默错误模式。

_NAME_
> 存放当前选项字符的变量名。

_ARGS_
> 用于替代位置参数的可选待解析参数。

# VARIABLES

**OPTIND**
> 下一个待处理参数的索引。初始值为 1。

**OPTARG**
> 包含需要参数的选项所对应的参数值；静默模式下则为无效的选项字符。

**OPTERR**
> 设为 0 可抑制错误消息。

# DESCRIPTION

**getopts** 是一个 POSIX shell 内建命令，用于在脚本中解析短命令行选项。它每次处理一个选项，通常与 while 循环和 case 语句搭配，逐一处理各个选项。

选项是前置横线的单字符（如 -a、-b），可以合并（-abc）。需要参数的选项既可以把参数紧跟其后（-ffile），也可以把参数放在下一个位置（-f file）。

所有选项处理完毕后，getopts 返回非零退出状态。解析完成后，用 **shift $((OPTIND - 1))** 移除已处理的选项，其余参数仍保留在 $@ 中。

# CAVEATS

getopts 只处理短选项（单字符）。对于长选项（--verbose），请改用外部的 **getopt** 命令。若要解析多组参数，必须将 OPTIND 重置为 1。遇到第一个非选项参数或 -- 时，选项处理停止。

# HISTORY

getopts 由 POSIX 标准定义，所有符合 POSIX 的 shell 都可用，包括 bash、dash、ksh 和 zsh。它的引入是为了替代在不同系统间表现各异的外部 getopt 工具，提供更好的可移植性。这一内建实现确保了不同类 Unix 平台上的一致行为。

# SEE ALSO

[getopt](/man/getopt)(1), [bash](/man/bash)(1)
