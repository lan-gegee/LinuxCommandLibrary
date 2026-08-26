# TAGLINE

JVM 构建自动化工具

# TLDR

**构建项目**

```gradle build```

**运行测试**

```gradle test```

**清理并重新构建**

```gradle clean build```

**列出可用任务**

```gradle tasks```

**并行执行构建**

```gradle build --parallel```

**运行并生成 build scan**以获得详细报告

```gradle build --scan```

**使用配置缓存**加速重复构建

```gradle build --configuration-cache```

**使用特定的构建文件**

```gradle -b [path/to/build.gradle] build```

# SYNOPSIS

**gradle** [_options_] [_tasks_...]

# PARAMETERS

_TASKS_
> 要执行的任务。

**--daemon**
> 使用 Gradle 守护进程（默认已启用）。

**--no-daemon**
> 不使用 Gradle 守护进程。

**-q**, **--quiet**
> 只记录错误日志。

**-i**, **--info**
> 将日志级别设为 info。

**-d**, **--debug**
> 将日志级别设为 debug。

**--parallel**
> 并行构建各项目。

**--configuration-cache**
> 启用配置缓存以加速重复构建。

**--scan**
> 在 scans.gradle.com 上创建构建扫描。

**-b**, **--build-file** _file_
> 指定构建文件。

**-c**, **--settings-file** _file_
> 指定 settings 文件。

**--refresh-dependencies**
> 刷新依赖的状态。

**-x**, **--exclude-task** _task_
> 将某个任务排除在执行之外。

**--continuous**
> 持续构建；在文件变更时重新执行。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gradle** 是一个面向 Java、Kotlin、Android 及其他 JVM 项目的构建自动化工具。它使用 Groovy 或 Kotlin DSL 编写构建脚本，提供依赖管理、增量构建和丰富的插件生态。

Gradle 是 Android 开发的标准构建系统，支持多项目构建。Gradle 守护进程会在后台持续运行以提升构建性能，且默认启用。在大多数项目中，推荐使用 **Gradle Wrapper**（`./gradlew`）而不是直接调用 `gradle`，以确保构建工具版本一致。

# CONFIGURATION

**build.gradle** / **build.gradle.kts**
> 项目构建脚本，定义任务、依赖和插件。

**gradle.properties**
> 用于构建配置的项目级和用户级属性。

**settings.gradle** / **settings.gradle.kts**
> 多项目构建设置及包含的模块。

**~/.gradle/gradle.properties**
> 应用于所有构建的用户级 Gradle 属性。

# CAVEATS

需要 JVM。首次运行会下载依赖和 Gradle 分发包。守护进程默认启用；使用 **--no-daemon** 可禁用。建议使用 Gradle Wrapper（**./gradlew**）以确保构建可复现。

# HISTORY

Gradle 由 **Hans Dockter** 创建，首次发布于 **2007 年**，并于 **2013 年**成为官方 Android 构建系统。Kotlin DSL 支持在 Gradle 5.0（2018 年）中加入。用于加速构建的配置缓存于 Gradle 8.1（2023 年）转为正式特性。

# INSTALL

```pacman: sudo pacman -S gradle```

```apk: sudo apk add gradle```

```brew: brew install gradle```

```nix: nix profile install nixpkgs#gradle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gradle-wrapper](/man/gradle-wrapper)(1), [mvn](/man/mvn)(1), [ant](/man/ant)(1)
