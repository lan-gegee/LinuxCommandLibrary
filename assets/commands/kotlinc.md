# TAGLINE

Kotlin 编译器

# TLDR

**编译 Kotlin 文件**

```kotlinc [file.kt] -include-runtime -d [output.jar]```

**编译为 class 文件**

```kotlinc [file.kt] -d [output_dir]```

**编译多个文件**

```kotlinc [file1.kt] [file2.kt] -d [output.jar]```

**添加类路径**

```kotlinc -cp [lib.jar] [file.kt] -d [output.jar]```

**以指定 JVM 目标编译**

```kotlinc -jvm-target [17] [file.kt] -d [output.jar]```

# SYNOPSIS

**kotlinc** [_options_] _files_

# PARAMETERS

_FILES_
> Kotlin 源文件（.kt）。

**-d** _OUTPUT_
> 输出 JAR 或目录。

**-include-runtime**
> 打包 Kotlin 运行时。

**-cp** _PATH_
> 类路径。

**-jvm-target** _VERSION_
> 目标 JVM 版本。

**-no-stdlib**
> 不自动将 kotlin-stdlib.jar 和 kotlin-reflect.jar 加入类路径。

**-no-reflect**
> 不自动将 kotlin-reflect.jar 加入类路径。

**-jdk-home** _path_
> 使用自定义的 JDK 主目录而不是默认的 JAVA_HOME。

**-language-version** _version_
> 以指定的 Kotlin 语言版本编译（如 `2.0`）。

**-script**
> 求值 Kotlin 脚本文件（.kts）。

**-nowarn**
> 抑制所有编译器警告。

**-Werror**
> 将所有警告视为编译错误。

**-verbose**
> 启用包含编译细节的详细日志输出。

**-version**
> 显示编译器版本。

**-help**, **-h**
> 显示用法信息。

# DESCRIPTION

**kotlinc** 是 Kotlin 的命令行编译器，可将 Kotlin 源文件（.kt）翻译成 JVM 字节码。它既可以借助 `-include-runtime` 选项生成捆绑 Kotlin 运行时的独立 JAR 文件，也可以将 class 文件输出到目录中以便接入现有构建流水线。

该编译器与 Java 完全互操作，允许 Kotlin 代码调用 Java 库，反之亦然。它可以通过 `-jvm-target` 选项接受目标 JVM 版本，支持通过类路径添加外部依赖，并能同时编译多个源文件。对于较大的项目通常首选 Gradle 或 Maven 等构建工具，但 kotlinc 对快速编译任务、学习和脚本工作流很有用。

# CAVEATS

需要 JVM。启动慢。项目请考虑使用 Gradle。

# HISTORY

kotlinc 是 **Kotlin** 的官方编译器，Kotlin 由 **JetBrains** 创建，是一门现代 JVM 语言。

# SEE ALSO

[kotlin](/man/kotlin)(1), [javac](/man/javac)(1), [gradle](/man/gradle)(1)
