# TAGLINE

运行 Kotlin 脚本并提供 REPL

# TLDR

**运行 Kotlin 脚本**

```kotlin script.kts```

**带参数运行脚本**

```kotlin script.kts [arg1] [arg2]```

**启动交互式 REPL**

```kotlin```

**求值表达式**

```kotlin -e "println(\"Hello\")"```

**用额外的 classpath JAR 运行脚本**

```kotlin -cp [lib.jar] script.kts```

**传递 JVM 选项**（如增加内存）

```kotlin -J-Xmx512m script.kts```

# SYNOPSIS

**kotlin** [_options_] _script_ [_args_...]

# PARAMETERS

_SCRIPT_
> Kotlin 脚本文件（.kts）。

**-e** _EXPR_
> 求值表达式。

**-cp** _PATH_
> 类路径。

**-J** _ARG_
> 向 JVM 传递参数（如 -J-Xmx512m）。

**-nowarn**
> 抑制警告信息。

**-version**
> 显示 Kotlin 版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kotlin** 是 Kotlin 运行时命令，可以直接在 JVM 上执行 Kotlin 脚本（.kts 文件），无需单独的编译步骤。不带参数调用时，它会提供交互式读取-求值-打印循环（REPL），让你以交互方式试验 Kotlin 表达式和语句。

该工具可以使用 `-e` 选项从命令行求值单个表达式、带命令行参数运行脚本文件，以及把额外的 JAR 加入类路径以访问外部库。由于 Kotlin 脚本运行在 JVM 上，它们可以完整使用 Java 标准库以及加入类路径的任何 Java 或 Kotlin 库，因此适合自动化任务、快速原型开发和构建脚本等场景。

# CAVEATS

需要 JVM。脚本使用 .kts 扩展名。启动速度比编译后的代码慢。

# HISTORY

Kotlin 由 **JetBrains** 于 2011 年创建。kotlin 命令用于运行脚本并提供 REPL。

# INSTALL

```pacman: sudo pacman -S kotlin```

```brew: brew install kotlin```

```nix: nix profile install nixpkgs#kotlin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kotlinc](/man/kotlinc)(1), [java](/man/java)(1), [gradle](/man/gradle)(1)
