# TAGLINE

具有函数式编程特性的可扩展 shell

# TLDR

**启动 es shell**

```es```

**运行命令**

```es -c "[echo hello]"```

**运行脚本**

```es [script.es]```

**不加载初始化配置启动**

```es -p```

# SYNOPSIS

**es** [_options_] [_script_] [_args_]

# PARAMETERS

**-c** _command_
> 执行命令字符串。

**-p**
> 不加载 profile 配置文件。

**-l**
> 作为登录 shell 运行。

**-v**
> 将输入打印到标准错误。

**-x**
> 执行前打印命令。

**-i**
> 强制交互模式。

**-n**
> 仅解析，不执行。

# CONFIGURATION

**~/.esrc**
> 启动时加载的用户初始化文件（使用 -p 标志时不加载）。

# DESCRIPTION

**es** 是从 rc（Plan 9 shell）衍生而来的可扩展 shell，支持一等函数、词法作用域和异常处理。它提供简洁、可编程并带函数式编程特性的 shell 体验。

与传统 shell 不同，es 将函数视为一等值，支持闭包，且语法比 bash 或 zsh 更简单、更一致。

# CAVEATS

不兼容 POSIX；脚本需要重写。社区规模和资源少于 bash。某些特性与 rc 不同。可能并非在所有系统上都可用。

# HISTORY

es 由 **Paul Haahr** 和 **Byron Rakitzis** 于 **20 世纪 90 年代初**创建，是 Plan 9 shell rc 的增强版本。它把一等函数、词法作用域等函数式编程概念引入了 shell 脚本。

# INSTALL

```apk: sudo apk add es-shell```

```nix: nix profile install nixpkgs#es```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rc](/man/rc)(1), [bash](/man/bash)(1), [zsh](/man/zsh)(1), [fish](/man/fish)(1)
