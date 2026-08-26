# TAGLINE

交互式 Elixir Shell

# TLDR

**启动交互式 Elixir**

```iex```

**随项目一起启动**

```iex -S mix```

**求值表达式**

```iex -e "IO.puts(:hello)"```

**连接到节点**

```iex --remsh [node@host]```

**以短名称启动**

```iex --sname [mynode]```

**加载文件**

```iex [script.exs]```

# SYNOPSIS

**iex** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要加载的脚本文件。

**-S** _SCRIPT_
> 运行脚本（如 mix）。

**-e** _EXPR_
> 求值表达式。

**--remsh** _NODE_
> 连接到远程节点的 Shell。

**--sname** _NAME_
> 节点短名称。

**--name** _NAME_
> 节点完整名称。

**--help**
> 显示帮助信息。

# DESCRIPTION

**iex** 是交互式 Elixir Shell。它提供一个 REPL，用于求值 Elixir 表达式和探索代码。

该 Shell 支持 Tab 补全、历史记录和文档查询。它与 Mix 项目及远程节点集成。

# CAVEATS

需要 Elixir/Erlang。节点功能需要额外设置。常与 Mix 集成使用。

# HISTORY

iex 是 **Elixir** 的一部分，后者由 **José Valim** 创建，是运行在 Erlang 虚拟机上的函数式语言。

# INSTALL

```apt: sudo apt install elixir```

```dnf: sudo dnf install elixir```

```pacman: sudo pacman -S elixir```

```apk: sudo apk add elixir```

```zypper: sudo zypper install elixir```

```brew: brew install elixir```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[elixir](/man/elixir)(1), [mix](/man/mix)(1), [erl](/man/erl)(1)
