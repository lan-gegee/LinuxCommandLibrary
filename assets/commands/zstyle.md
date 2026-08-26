# TAGLINE

按上下文定义和查询 zsh 样式（style）

# TLDR

**为模式定义样式**（例如启用不区分大小写的补全匹配）

```zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'```

**以 zstyle 形式列出全部**样式定义

```zstyle -L```

**列出匹配元模式的样式**

```zstyle -L ':completion:*'```

**删除某模式下的样式**

```zstyle -d ':completion:*' menu```

**把样式值查询到标量变量**

```zstyle -s ':completion:*' completer REPLY```

**以数组形式查询样式**

```zstyle -a ':completion:*:descriptions' format DESCR```

**测试布尔样式**（设为 yes/true/on/1 时返回 0）

```zstyle -t ':completion:*' verbose```

用 `-e` **定义动态求值的**样式

```zstyle -e ':completion:*' max-errors 'reply=($((($#PREFIX+$#SUFFIX)/3))numeric)'```

# SYNOPSIS

**zstyle** [ **-L** [ _metapattern_ [ _style_ ] ] ]

**zstyle** [ **-** | **--** | **-e** ] _pattern_ _style_ _string_ ...

**zstyle** **-d** [ _pattern_ [ _style_ ... ] ]

**zstyle** **-g** _name_ [ _pattern_ [ _style_ ] ]

**zstyle** **-{a|b|s}** _context_ _style_ _name_ [ _sep_ ]

**zstyle** **-{T|t}** _context_ _style_ [ _string_ ... ]

**zstyle** **-m** _context_ _style_ _pattern_

# PARAMETERS

**-L** [_metapattern_ [_style_]]
> 以 **zstyle** 命令的形式列出样式定义。可选的 _metapattern_ 按模式过滤，_style_ 按样式名过滤。

**-e**
> 将值视为在查询样式时需求值的代码；参数 **reply** 必须被设置为结果字符串。

**-d** [_pattern_ [_style_ ...]]
> 删除样式。不带参数时删除全部定义。给定 _pattern_ 时删除该模式；再给定 _styles_ 时只删除这些样式。

**-g** _name_ [_pattern_ [_style_]]
> 把定义取入数组 _name_。可返回所有模式、某个模式的样式，或某个（模式, 样式）对的值。

**-s** _context_ _style_ _name_ [_sep_]
> 把样式作为标量读入 _name_，多个值之间用空格或 _sep_ 连接。已设置返回 0，否则返回 1。

**-b** _context_ _style_ _name_
> 把样式作为布尔值读取（当唯一值为 **yes**、**true**、**on** 或 **1** 时得到 `yes`，否则得到 `no`）。

**-a** _context_ _style_ _name_
> 把样式作为数组读取；若 _name_ 是关联数组，交替出现的字符串会分别成为键和值。

**-t** _context_ _style_ [_string_ ...]
> 测试样式。状态 0 = 匹配/为真，1 = 已定义但不匹配，2 = 未定义。

**-T** _context_ _style_ [_string_ ...]
> 与 **-t** 类似，但当样式对任何匹配模式都未定义时返回 0（而不是 2）。

**-m** _context_ _style_ _pattern_
> 对样式值做模式匹配。若 _pattern_ 至少匹配值中的一个字符串则返回 0。

# DESCRIPTION

**zstyle** 是 **zsh/zutil** 模块的一个内建命令，用于定义和查询样式。样式是以某个模式为键存储的名称/值对；查询时会提供一个以冒号分隔的 **context** 字符串，与这些模式进行匹配，其中最具体的匹配模式胜出。

模式的具体程度由冒号分隔组件的数量以及各组件的字面程度决定。字面字符串优先于模式，复杂模式优先于通配符 `*`，平局时先定义的模式获胜。`*` 可以匹配任意数量的字符，包括冒号。

样式最主要的应用是 zsh 基于 shell 函数的补全系统，其上下文形如 **:completion:_function_:_completer_:_command_:_argument_:_tag_**。提示符主题（如 **vcs_info**）、zsh 插件，以及任何调用 **zstyle -s/-a/-b/-t** 来读取用户偏好的自定义代码也都在使用样式。

# CAVEATS

使用 **-L** 有个常见的坑：元模式是与存储下来的模式做匹配的，所以 `zstyle -L ":completion:*"` 会匹配所有以 `:completion:` 开头的已存模式，而不只是字面上的 `:completion:*`。要按字面星号匹配，请写 `:completion:\*`。**-L** 选项不能与其他选项组合使用。

**-e** 形式会在每次查询时重新求值；如果求值后 **reply** 未被设置，该样式将被视为未定义。

# CONFIGURATION

样式通常在 **~/.zshrc** 中、紧跟 **autoload -U compinit && compinit** 之后设置。没有专门存放样式的磁盘配置文件；样式保存在 shell 内存中，直到 shell 退出。

常见上下文包括 **:completion:\***、**:vcs_info:\***、**:zle:\***，以及插件专属的命名空间，如 **:weather:** 或 **:zsh-autosuggest**。

# HISTORY

**zstyle** 内建命令作为 **zsh/zutil** 模块的一部分引入，用于支撑新的基于函数的补全系统——该系统在 **zsh 4.0**（2001 年）中取代了旧有的 **compctl** 方案。此后它成为配置补全行为、**vcs_info** 等提示符主题以及众多第三方 zsh 插件的标准机制。

# SEE ALSO

[zsh](/man/zsh)(1)
