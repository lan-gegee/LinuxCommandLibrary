# TAGLINE

现代的 Scala 命令行运行器与构建工具

# TLDR

**运行 Scala 脚本**

```scala-cli [script.sc]```

**运行 Scala 文件**

```scala-cli run [Main.scala]```

**启动 REPL**

```scala-cli repl```

**编译为 JAR**

```scala-cli package [src/] -o [app.jar]```

**运行测试**

```scala-cli test [src/]```

**添加依赖并运行**

```scala-cli run --dep [com.lihaoyi::os-lib:0.9.1] [script.scala]```

**监视变更并重新运行**

```scala-cli run --watch [Main.scala]```

# SYNOPSIS

**scala-cli** [_command_] [_options_] [_inputs_...]

# PARAMETERS

**run**
> 运行 Scala 代码。

**repl**
> 启动交互式 REPL。

**compile**
> 编译源代码。

**package**
> 创建 JAR 或原生镜像。

**test**
> 运行测试。

**fmt**
> 格式化代码。

**-S** _version_, **--scala** _version_
> 设置 Scala 版本（例如 3.3、2.13）。

**--dep** _dependency_
> 添加依赖（例如 com.lihaoyi::os-lib:0.9.1）。

**-O** _option_
> Scala 编译器选项。

**-w**, **--watch**
> 监视源文件并在变更时重新运行。

**setup-ide**
> 生成 IDE 配置文件（BSP）。

**publish**
> 将库发布到 Maven 仓库。

**--native**
> 编译为 Scala Native 二进制文件。

**--js**
> 编译为 Scala.js JavaScript。

# DESCRIPTION

**scala-cli** 是现代化的 Scala 命令行工具，自 Scala 3.5 起被采用为官方 `scala` 命令。它可以运行脚本、编译项目、管理依赖并创建可执行文件。无论是学习 Scala 还是进行生产级开发都很适用。

Scala-CLI 支持在源文件内使用 directive（形如 `//> using dep` 的注释）来声明依赖、Scala 版本和编译器选项，无需单独的构建文件。这使它成为脚本和小型项目的理想选择。

# CAVEATS

对于大型多模块项目，sbt 或 Mill 等专用构建工具更为合适。源文件中的 using directive 是 Scala-CLI 的特性，并非标准 Scala 的一部分。

# INSTALL

```brew: brew install scala-cli```

```nix: nix profile install nixpkgs#scala-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sbt](/man/sbt)(1), [scala](/man/scala)(1), [gradle](/man/gradle)(1)
