# TAGLINE

启动 Java 应用程序

# TLDR

**运行 class 文件**

```java [ClassName]```

**运行 JAR 文件**

```java -jar [application.jar]```

**使用 classpath 运行**

```java -cp [path/to/classes] [ClassName]```

**设置堆大小**

```java -Xmx[512m] -jar [app.jar]```

**使用系统属性运行**

```java -D[property=value] [ClassName]```

**显示版本**

```java -version```

**运行单个源文件**

```java [Source.java]```

# SYNOPSIS

**java** [_options_] _class_ [_args_...]
**java** [_options_] **-jar** _jarfile_ [_args_...]

# PARAMETERS

_CLASS_
> 要执行的主类。

**-jar** _FILE_
> 执行 JAR 文件。

**-cp** _PATH_
> 依赖项的类路径。

**-Xmx** _SIZE_
> 最大堆大小。

**-Xms** _SIZE_
> 初始堆大小。

**-D** _PROP=VAL_
> 设置系统属性。

**-Xss** _SIZE_
> 线程栈大小。

**-ea**, **--enableassertions**
> 启用断言。

**--enable-preview**
> 启用预览语言特性。

**-verbose** _:class|:gc|:jni_
> 启用详细输出。

**-version**
> 显示版本信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**java** 通过在 Java 虚拟机（JVM）中加载并执行编译后的字节码来启动 Java 应用。它支持 class 文件、JAR 归档，以及从 Java 11 开始的单源文件程序。

JVM 负责内存管理（垃圾回收）、线程处理和平台抽象。内存通过 **-Xms**（初始堆）、**-Xmx**（最大堆）和 **-Xss**（栈大小）配置。系统属性（**-D**）用于在运行时配置应用行为。

# CAVEATS

需要 JRE/JDK。版本兼容性很重要。内存设置可能需要调优。

# HISTORY

Java 由 **James Gosling** 于 1995 年在 **Sun Microsystems** 创建。现在由 **Oracle** 和 OpenJDK 社区维护。

# INSTALL

```apk: sudo apk add java-common```

```brew: brew install java```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[javac](/man/javac)(1), [jar](/man/jar)(1), [jps](/man/jps)(1), [jstack](/man/jstack)(1)
