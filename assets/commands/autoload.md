# TAGLINE

自动加载 shell 函数以实现惰性加载

# TLDR

按名称**自动加载函数**

```autoload [function_name]```

**自动加载并立即处理未定义函数**（zsh）

```autoload -U [function_name]```

以 zsh 风格初始化函数的方式**自动加载**（抑制别名展开）

```autoload -Uz [function_name]```

**自动加载目录中的所有函数**（该目录需已加入 fpath）

```autoload -Uz $fpath[1]/*(.:t)```

**自动加载补全系统**

```autoload -Uz compinit && compinit```

**自动加载提示符系统**

```autoload -Uz promptinit && promptinit```

# SYNOPSIS

**autoload** [_-UXmtz_] [_name ..._]

# PARAMETERS

**-U**
> 加载函数时抑制别名展开

**-z**
> 使用 zsh 风格的函数定义（zsh 中的默认值）

**-k**
> 使用 ksh 风格的函数定义

**-X**
> 立即加载并执行该函数（在函数自身内部使用）

**-t**
> 为自动加载的函数启用执行追踪

**-m**
> 将参数视为匹配函数名的模式

**+X**
> 强制立即加载函数但不执行它

# DESCRIPTION

**autoload** 将 shell 函数名标记为延迟加载。shell 启动时不把函数定义读入内存，只记录函数名。当该函数首次被调用时，shell 会在 **$fpath** 列出的目录中搜索与函数名同名的文件，读取其定义并执行。

当存在大量很少使用的函数时，这种机制能显著缩短 shell 启动时间。函数文件应直接包含函数体（采用 zsh 风格自动加载时，不要包裹在 `function name { }` 块中）。

**autoload** 对 zsh 的补全系统（**compinit**）、提示符主题（**promptinit**）以及随 zsh 分发的许多其他标准函数至关重要。

# CAVEATS

函数文件必须位于 **$fpath** 列出的目录中，且文件名必须与函数名完全一致。用 **-U** 自动加载的函数，其定义中的别名不会被展开——强烈建议使用此选项，以避免意外行为。仅在 zsh 和 ksh 中作为 shell 内建命令可用。

# HISTORY

**autoload** 源自 **ksh**（Korn Shell），由贝尔实验室的 **David Korn** 于 **20 世纪 80 年代**设计。Zsh 采用并扩展了这一概念，使其成为自身模块化函数系统的核心。**-U** 和 **-z** 标志是 zsh 特有的新增功能。

# SEE ALSO

[zsh](/man/zsh)(1)
