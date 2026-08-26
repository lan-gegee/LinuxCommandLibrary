# TAGLINE

函数式前端语言编译器与工具链

# TLDR

**初始化 Elm 项目**

```elm init```

**编译 Elm 文件**

```elm make [src/Main.elm]```

**编译为 JavaScript**

```elm make [src/Main.elm] --output=[main.js]```

**启动开发服务器**

```elm reactor```

**启动交互式 REPL**

```elm repl```

**安装软件包**

```elm install [elm/http]```

# SYNOPSIS

**elm** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作：init、make、reactor、repl、install 等。

**init**
> 初始化新的 Elm 项目。

**make** _FILE_
> 编译 Elm 源文件。

**--output** _FILE_
> 输出文件路径。

**--optimize**
> 启用优化。

**reactor**
> 启动开发服务器。

**repl**
> 启动交互式 Shell。

**install** _PACKAGE_
> 安装 Elm 软件包。

**diff** _PACKAGE_ _V1_ _V2_
> 显示软件包版本之间的 API 差异。

**bump**
> 根据 API 变更提升版本号。

**publish**
> 发布软件包到 Elm 软件包仓库。

# DESCRIPTION

**elm** 是 Elm 编程语言的命令行工具。Elm 是一种面向前端 Web 开发的函数式语言。它负责项目初始化、编译、软件包管理和开发工具。

Elm 通过强大的类型系统编译为没有运行时异常的 JavaScript。编译器提供友好的错误消息来帮助修复问题。

reactor 提供带热重载的开发服务器，而 repl 提供交互式的 Elm 求值环境。

# CAVEATS

大版本之间不兼容（0.19 与 0.18 不兼容）。与 JavaScript 的互操作有限。生态系统比主流语言小。严格的类型系统有学习曲线。

# HISTORY

Elm 由 **Evan Czaplicki** 于 **2012 年**作为其毕业论文项目创建。它开创了 "Elm Architecture" 模式，影响了 React/Redux 及其他前端框架。

# INSTALL

```apt: sudo apt install elm-compiler```

```brew: brew install elm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [npm](/man/npm)(1)
