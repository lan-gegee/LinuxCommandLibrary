# TAGLINE

Erlang 运行时系统与交互式 Shell

# TLDR

**启动 Erlang shell**

```erl```

**运行指定模块**

```erl -s [module] [function]```

**运行后退出**

```erl -noshell -s [module] [function] -s init stop```

**启动命名节点**

```erl -name [node@host]```

为分布式通信**设置 cookie**

```erl -setcookie [secret]```

**添加代码加载路径**

```erl -pa [ebin/]```

**求值表达式**

```erl -eval "[io:format(\"Hello~n\")]"```

# SYNOPSIS

**erl** [_options_]

# PARAMETERS

**-s** _MOD_ [_FUNC_ [_ARGS_]]
> 启动模块函数。

**-noshell**
> 不带交互式 shell 运行。

**-name** _NAME_
> 长节点名。

**-sname** _NAME_
> 短节点名。

**-setcookie** _COOKIE_
> 分布式认证 cookie。

**-pa** _DIR_
> 添加到代码路径开头。

**-eval** _EXPR_
> 启动时求值表达式。

**-run** _MOD_ [_FUNC_ [_ARGS_]]
> 与 -s 类似，但以字符串列表的形式传递参数。

**-config** _FILE_
> 应用配置文件（sys.config）。

**-detached**
> 以脱离控制终端的方式启动 Erlang 运行时系统。

**-heart**
> 启动心跳监控进程。

**+P** _NUM_
> 设置最大并发进程数（默认 262144）。

**+K** _true|false_
> 启用或禁用内核轮询（epoll/kqueue）。

# CONFIGURATION

**sys.config**
> 应用配置文件，为 OTP 应用指定运行时参数。

**vm.args**
> VM 参数文件，用于分布式 Erlang 设置、内存限制和节点配置。

# DESCRIPTION

**erl** 启动 Erlang 运行时系统和交互式 shell。它是运行 Erlang 程序的主要方式，既可交互使用也可批处理运行。

shell 提供了求值 Erlang 表达式的交互环境。生产环境中可用 -noshell 不带 shell 运行，用 -s/-eval 执行特定代码。

Erlang 的分布式特性通过节点命名（-name/-sname）和身份验证（-setcookie）启用。

# CAVEATS

Shell 语法与模块语法不同。分布式要求各节点 cookie 一致。节点名必须唯一。内存占用随进程数增长。

# HISTORY

Erlang 由 **Joe Armstrong**、**Robert Virding** 和 **Mike Williams** 自 **1986 年**起在 **Ericsson** 开发，面向电信系统。自 **1998 年**开源以来，erl 命令一直是运行 Erlang 的标准方式。

# INSTALL

```apt: sudo apt install erlang-base```

```apk: sudo apk add erlang27```

```zypper: sudo zypper install erlang27```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[erlc](/man/erlc)(1), [elixir](/man/elixir)(1)
