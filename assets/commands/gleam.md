# TAGLINE

Gleam 编程语言的编译器与构建工具

# TLDR

**创建新项目**

```gleam new [project_name]```

**构建项目**

```gleam build```

**运行项目**

```gleam run```

**运行测试**

```gleam test```

**添加 Hex 依赖**

```gleam add [package_name]```

**移除依赖**

```gleam remove [package_name]```

**格式化源代码**

```gleam format```

**生成 HTML 文档**

```gleam docs build```

# SYNOPSIS

**gleam** _command_ [_options_]

# PARAMETERS

**new** _NAME_
> 以标准目录结构创建新项目。

**build**
> 编译项目及其依赖。

**run**
> 构建并运行项目。

**test**
> 构建并运行测试套件。

**add** _PACKAGE_
> 添加 Hex 软件包依赖。

**remove** _PACKAGE_
> 移除依赖。

**check**
> 对项目进行类型检查，但不产生构建产物。

**format**
> 格式化源代码文件。

**docs build**
> 生成 HTML 文档。

**docs publish**
> 将文档发布到 HexDocs。

**publish**
> 将软件包发布到 Hex。

**shell**
> 启动一个已加载项目的 Erlang shell。

**export erlang-shipment**
> 导出用于部署的独立 Erlang 发布包。

**--target** _TARGET_
> 编译目标：erlang 或 javascript。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gleam** 是 Gleam 编程语言的构建工具和编译器。Gleam 是一门类型安全的函数式语言，可编译为 Erlang 和 JavaScript。该工具负责管理项目、依赖、编译、测试和文档。

Gleam 与 Erlang/Elixir 生态的 Hex 软件包管理器集成，并可与 Erlang 和 Elixir 代码互操作。JavaScript 目标使 Gleam 能够在浏览器以及 Node.js/Deno/Bun 中运行。

# CONFIGURATION

**gleam.toml**
> 项目配置文件，定义名称、版本、目标平台、依赖和构建选项。

# CAVEATS

BEAM 目标需要 Erlang/OTP。JavaScript 目标需要 Node.js、Deno 或 Bun。Gleam 在设计上没有运行时异常——穷尽性模式匹配在编译期强制执行。

# HISTORY

Gleam 由 **Louis Pilfold** 自 **2018** 年起创建，目标是在保持与 Erlang 和 Elixir 库兼容的同时，为 BEAM 虚拟机生态带来静态类型安全。1.0 版本于 **2024 年 3 月**发布。

# INSTALL

```pacman: sudo pacman -S gleam```

```apk: sudo apk add gleam```

```zypper: sudo zypper install gleam```

```brew: brew install gleam```

```nix: nix profile install nixpkgs#gleam```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[elixir](/man/elixir)(1), [cargo](/man/cargo)(1), [mix](/man/mix)(1)
