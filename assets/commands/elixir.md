# TAGLINE

运行于 Erlang VM 的函数式语言运行时

# TLDR

**运行 Elixir 脚本**

```elixir [script.exs]```

**求值表达式**

```elixir -e "[IO.puts \"Hello\"]"```

**附带 Shell 启动**

```elixir -S iex```

**运行 Mix 项目**

```elixir -S mix run```

**启动命名节点**

```elixir --name [node@host] -S iex```

**设置环境**

```MIX_ENV=prod elixir -S mix phx.server```

# SYNOPSIS

**elixir** [_options_] [_script_] [_args_]

# PARAMETERS

_SCRIPT_
> 要运行的 Elixir 脚本文件。

**-e** _CODE_
> 求值代码字符串。

**-r** _FILE_
> 执行前加载文件。

**-S** _SCRIPT_
> 运行 Erlang/Elixir 脚本。

**--name** _NAME_
> 设置分布式节点名。

**--sname** _NAME_
> 设置短节点名。

**--cookie** _COOKIE_
> 设置 Erlang 分布式 cookie。

**--no-halt**
> 脚本结束后不退出；保持 VM 继续运行。

**--erl** _SWITCHES_
> 将开关参数传递给底层的 erl 命令。

**--rpc-eval** _NODE_ _CODE_
> 在远程运行中的节点上求值代码。

**-v**, **--version**
> 打印 Elixir 和 Erlang/OTP 版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**elixir** 运行 Elixir 代码和脚本。它是执行 Elixir 程序的主要命令，同时支持脚本文件（.exs）和编译后的模块。

该命令启动已加载 Elixir 的 Erlang VM。选项用于控制分布式计算设置、代码加载和执行模式。结合 `-S mix` 可以运行 Mix 任务。

Elixir 的交互式 Shell（IEx）可通过 `elixir -S iex` 启动，用于开发和调试。

# CAVEATS

需要安装 Erlang/OTP。启动时间包含 BEAM VM 引导。脚本按惯例使用 .exs 扩展名。分布式特性需要网络配置。

# HISTORY

Elixir 由 **José Valim** 创建并于 **2011 年**发布，运行于 Erlang BEAM VM 之上。它为 Erlang 生态带来了现代语法和工具链，同时保持了兼容性。

# INSTALL

```apt: sudo apt install elixir```

```dnf: sudo dnf install elixir```

```pacman: sudo pacman -S elixir```

```apk: sudo apk add elixir```

```zypper: sudo zypper install elixir```

```brew: brew install elixir```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iex](/man/iex)(1), [mix](/man/mix)(1), [erl](/man/erl)(1)

# RESOURCES

```[Source code](https://github.com/elixir-lang/elixir)```

```[Homepage](https://elixir-lang.org/)```

```[Documentation](https://hexdocs.pm/elixir/)```

<!-- verified: 2026-07-14 -->
