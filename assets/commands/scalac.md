# TAGLINE

Scala 源代码编译器

# TLDR

**编译 Scala 源文件**

```scalac [Hello.scala]```

**将多个文件编译**到指定目录

```scalac -d [classes/] [*.scala]```

**带 classpath 依赖编译**

```scalac -classpath [lib/*] [Source.scala]```

**带详细输出编译**

```scalac -verbose [Source.scala]```

**带额外警告编译**

```scalac -Xlint [Source.scala]```

**将警告视为错误**

```scalac -Werror [Source.scala]```

**显示编译器版本**

```scalac -version```

# SYNOPSIS

**scalac** [_options_] [_source files_]

# PARAMETERS

**-d** _directory|jar_
> 指定生成的类文件的存放位置

**-classpath** _path_
> 指定用户类文件的查找位置（在 Unix 上以冒号分隔）

**-bootclasspath** _path_
> 覆盖引导类文件的位置

**-sourcepath** _path_
> 指定输入源文件的查找位置

**-verbose**
> 输出编译器正在执行的操作的消息

**-deprecation**
> 对弃用 API 的使用发出警告并指出位置

**-unchecked**
> 针对类型擦除启用额外的警告

**-Werror**
> 出现任何警告都使编译失败

**-Xlint**
> 启用推荐使用的额外警告

**-version**
> 打印产品版本并退出

**-help**
> 打印标准选项的概要

# DESCRIPTION

**scalac** 是 Scala 编程语言的编译器。它读取 Scala 源文件（.scala）并将其编译为可在 JVM 上运行的 Java 字节码类文件。

默认情况下，类文件与源文件放在同一目录。使用 **-d** 可以指定其他输出目录或 JAR 文件。编译器通过 classpath 机制与 Java 类集成。

选项按前缀分类：**-W** 表示警告相关，**-V** 表示详细输出，**-X** 表示扩展选项，**-Y** 表示私有/实验性选项。

# CONFIGURATION

**JAVA_HOME**
> Scala 编译器所使用 JDK 安装的路径。

**JAVA_OPTS**
> 传递给编译器进程的额外 JVM 选项（例如内存设置）。

# CAVEATS

JAVA_HOME 环境变量必须指向有效的 JDK 安装。JAVA_OPTS 可向底层 JVM 传递额外选项。Scala 3 使用不同的编译器，部分选项不兼容。

# HISTORY

Scala 由 **Martin Odersky** 自 **2001 年**起在 EPFL 设计，首个公开发布于 **2004 年**。其名字意为 "scalable language"（可扩展的语言）。**2021 年**发布的 Scala 3（Dotty）带来了显著的语言改进。

# SEE ALSO

[scala](/man/scala)(1), [javac](/man/javac)(1), [sbt](/man/sbt)(1), [java](/man/java)(1)
