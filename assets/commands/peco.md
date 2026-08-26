# TAGLINE

简洁的交互式过滤工具

# TLDR

**交互式过滤**

```ls | peco```

**按查询词过滤**

```history | peco --query "[pattern]"```

**选择文件并用命令打开**

```find . -type f | peco | xargs [command]```

**使用自定义提示符**

```peco --prompt="Select> "```

# SYNOPSIS

**peco** [_options_]

# PARAMETERS

**--query** _STRING_
> 初始查询字符串。

**--prompt** _STRING_
> 自定义提示符字符串。

**--layout** _TYPE_
> 显示布局：自上而下或自下而上。默认为自上而下。

**--initial-index** _N_
> 从第 N 行开始选择。

**--rcfile** _PATH_
> 设置文件的路径。

**-b**, **--buffer-size** _N_
> 搜索缓冲区保留的行数。从无限流管道输入时很有用。

**--null**
> 以 NUL（\0）作为目标/输出的分隔符。

**--select-1**
> 若输入仅包含一项，立即选中并退出。

**--on-cancel** _ACTION_
> 用户取消时的动作：success 或 error。默认为 success。

**--initial-filter** _FILTER_
> 指定默认过滤器（如 Regexp、SmartCase）。

# DESCRIPTION

**peco** 是一个交互式过滤工具，可对 stdin 的内容做模糊匹配后进行选择。

该工具提供增量搜索。类似于 fzf 和 percol。

# CAVEATS

交互式使用需要终端。使用 Go 编写。可通过 JSON 配置文件（~/.config/peco/config.json）自定义配置。

# HISTORY

peco 受 percol 启发而诞生，是一个**交互式 grep** 工具。

# INSTALL

```apt: sudo apt install peco```

```pacman: sudo pacman -S peco```

```brew: brew install peco```

```nix: nix profile install nixpkgs#peco```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fzf](/man/fzf)(1), [percol](/man/percol)(1), [grep](/man/grep)(1)
