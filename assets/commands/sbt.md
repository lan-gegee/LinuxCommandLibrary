# TAGLINE

面向 JVM 项目的 Scala 构建工具

# TLDR

在当前项目中**启动交互式 sbt shell**

```sbt```

**编译项目**

```sbt compile```

**运行项目的主类**

```sbt run```

**运行所有测试**

```sbt test```

**运行指定的测试类**

```sbt "testOnly [com.example.MySpec]"```

**持续编译**文件变更

```sbt ~compile```

**清理并重新构建**项目

```sbt clean compile```

**将项目打包**为 JAR 文件

```sbt package```

# SYNOPSIS

**sbt** [_options_] [_command_...]

# PARAMETERS

**-h**, **--help**
> 显示帮助信息

**-v**, **--verbose**
> 启用详细日志输出

**--debug**
> 启用调试日志

**-no-colors**
> 禁用输出中的 ANSI 颜色码

**--batch**
> 禁用交互模式

**--sbt-version** _version_
> 使用指定版本的 sbt

**--java-home** _path_
> 指定其他 Java 安装目录

**-Dkey=val**
> 向 JVM 传递系统属性

**-J-Xfoo**
> 直接传递 JVM 选项（例如 -J-Xmx2048M）

**-mem** _MB_
> 设置内存分配（例如 -mem 2048）

# DESCRIPTION

**sbt**（Scala Build Tool）是 Scala 项目的标准构建工具。它负责编译、测试、依赖管理、打包和发布。sbt 使用 Scala 本身编写的构建定义，通常位于 **build.sbt** 中。

sbt 有两种运行模式：**批处理模式**将命令作为参数传入，执行完毕后 sbt 退出；**交互模式**则启动一个 shell 以便持续交互。由于 JVM 在命令之间保持运行，交互 shell 能提供更快的反馈。

主要特性包括**增量编译**（只重新编译发生变更的文件）、使用 **~** 前缀的**持续执行**（例如 ~test 会在每次保存文件时运行测试），以及使用 **+** 前缀针对多个 Scala 版本的**交叉构建**。

# COMMON COMMANDS

**compile**
> 编译主要源代码

**test**
> 运行所有测试

**run**
> 运行主类

**console**
> 启动带有项目 classpath 的 Scala REPL

**clean**
> 删除生成的文件（target 目录）

**reload**
> 重新加载构建定义

**update**
> 解析并下载依赖

**package**
> 用编译后的类创建 JAR 文件

**publish**
> 将构件发布到配置好的仓库

**publishLocal**
> 将构件发布到本地 Ivy 仓库

# CAVEATS

sbt 可能占用大量内存；大型项目可能需要通过 **SBT_OPTS** 或 **.jvmopts** 增大堆大小。首次运行需要下载依赖，可能较慢。构建定义涉及 settings、task 和 scope，有一定学习曲线。

# HISTORY

sbt 由 **Mark Harrah** 于 **2008 年**创建，现已成为 Scala 项目事实上的构建工具。它最初名为 "Simple Build Tool"，后来不再强调这个名称。1.0 版本于 **2017 年**发布，对构建语义和性能带来了显著改进。2023 年从 Lightbend 移交后，该项目现在由 **Scala Center** 和开源社区维护。

# INSTALL

```pacman: sudo pacman -S sbt```

```brew: brew install sbt```

```nix: nix profile install nixpkgs#sbt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scala](/man/scala)(1), [scalac](/man/scalac)(1), [gradle](/man/gradle)(1)
