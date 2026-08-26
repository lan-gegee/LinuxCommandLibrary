# TAGLINE

Scala 编程语言解释器与 REPL

# TLDR

**启动 REPL**

```scala```

**运行脚本**

```scala [script.scala]```

**带 classpath 运行**

```scala -cp [lib.jar] [script.scala]```

**求值表达式**

```scala -e "println(1 + 2)"```

**运行已编译的类**

```scala [ClassName]```

**指定 JVM 内存运行**

```scala -J-Xmx[2g] [script.scala]```

**以 explain 模式运行**

```scala -explain [script.scala]```

# SYNOPSIS

**scala** [_-cp classpath_] [_-e expr_] [_options_] [_script_] [_args_]

# PARAMETERS

**-cp**, **-classpath** _PATH_
> 为类文件和库设置 classpath。

**-e** _EXPR_
> 求值表达式并打印结果。

**-J** _FLAG_
> 向 JVM 传递标志（例如 -J-Xmx2g）。

**-deprecation**
> 显示弃用警告。

**-explain**
> 结合更多上下文详细解释错误。

**-feature**
> 对高级语言特性显示特性警告。

**-help**
> 显示帮助。

**-version**
> 显示版本。

**-X**
> 显示高级编译器选项。

**-Y**
> 显示私有编译器选项。

# DESCRIPTION

**scala** 用于运行 Scala 程序并提供交互式 REPL。Scala 在 JVM 上将面向对象与函数式编程相结合。

REPL 会对表达式求值并显示结果及其类型。Tab 补全有助于探索 API。:help 可查看 REPL 命令。

脚本无需编译即可直接运行。Scala 3 运行器可以将 .scala 文件作为带依赖的脚本执行。

Classpath 用于指定库和已编译的类。在 Scala 3 中可以使用 Maven 坐标声明依赖。

编译器解释有助于理解复杂的错误消息。explain 模式提供详细的推理说明。

该语言支持类型推断、模式匹配、隐式参数和高阶函数，并且与 Java 无缝互操作。

# CAVEATS

Scala 3 与 Scala 2 差异显著。JVM 启动会带来延迟。内存占用可能较高。某些特性有一定学习曲线。

# HISTORY

**Scala** 由瑞士 **EPFL** 的 **Martin Odersky** 设计，1.0 版本于 **2004 年**发布。**2021 年**发布的 Scala 3（Dotty）带来了显著的语言改进。

# INSTALL

```zypper: sudo zypper install scala```

```brew: brew install scala```

```nix: nix profile install nixpkgs#scala```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scalac](/man/scalac)(1), [sbt](/man/sbt)(1), [java](/man/java)(1), [kotlin](/man/kotlin)(1)
