# TAGLINE

支持提前原生编译和多语言运行的高性能 JDK

# TLDR

**将 Java 编译为原生可执行文件**

```native-image -jar [app.jar]```

**以指定输出名称编译**

```native-image -jar [app.jar] -o [myapp]```

**运行 JavaScript 文件**

```js [script.js]```

**运行 Python 文件**

```graalpy [script.py]```

**安装额外的语言**

```gu install [python]```

**列出已安装的组件**

```gu list```

**显示 GraalVM 版本**

```java -version```

**编译并生成构建报告**

```native-image --diagnostics-mode -jar [app.jar]```

# SYNOPSIS

**native-image** [_options_] _class_|_-jar jarfile_

**gu** _command_ [_options_] [_component_]

**js** [_options_] [_file_]

**graalpy** [_options_] [_file_]

# NATIVE-IMAGE OPTIONS

**-o** _name_
> 输出文件名。

**-jar** _file_
> 输入 JAR 文件。

**--no-fallback**
> 构建纯原生镜像（无 JVM 回退）。

**--static**
> 构建完全静态的可执行文件。

**-H:Name=**_name_
> 原生镜像名称。

**-H:+ReportExceptionStackTraces**
> 启用堆栈跟踪。

**--initialize-at-build-time**
> 在构建时初始化类。

**--initialize-at-run-time=**_classes_
> 在运行时初始化类。

**-H:ReflectionConfigurationFiles=**_file_
> 反射配置。

**--diagnostics-mode**
> 生成诊断信息。

**--verbose**
> 详细输出。

# GU COMMANDS

**install** _component_
> 安装 GraalVM 组件。

**remove** _component_
> 移除组件。

**list**
> 列出已安装的组件。

**available**
> 列出可用组件。

**update**
> 更新已安装的组件。

**rebuild-images**
> 重建原生启动器。

# DESCRIPTION

**GraalVM** 是一个支持提前（AOT）原生编译和多语言运行的高性能 JDK。它可以运行 Java、JavaScript、Python、Ruby、R 以及基于 LLVM 的语言。

**native-image** 将 Java 应用程序编译为原生可执行文件。其优势包括即时启动、内存占用降低以及不依赖 JVM。它需要进行封闭世界分析——所有代码路径必须在构建时可知。

反射、动态代理和资源需要配置文件。可以使用追踪代理生成它们：**java -agentlib:native-image-agent=config-output-dir=conf -jar app.jar**。

**gu**（GraalVM Updater）管理可选组件。可安装 Python（**graalpy**）、Ruby（**truffleruby**）等语言运行时或 LLVM 工具链。

GraalVM 的 Truffle 框架支持高性能的语言实现。语言之间可以互操作——从 Java 调用 JavaScript，反之亦然。

# CAVEATS

原生镜像构建非常消耗资源。某些 Java 特性需要显式配置。并非所有库都支持原生编译。构建时间远长于 JVM 启动时间。

# HISTORY

GraalVM 由 **Oracle Labs** 开发，基于动态编译方面的研究。**2018 年**首次发布 1.0 版本。Graal 编译器源自 Maxine VM 项目。GraalVM CE（社区版）是开源的；企业版增加了额外优化。Native Image 在 GraalVM 21 中达到生产可用。该项目配合 Quarkus 和 Micronaut 等框架推动云原生 Java 发展。

# SEE ALSO

[java](/man/java)(1), [javac](/man/javac)(1), [quarkus](/man/quarkus)(1)
