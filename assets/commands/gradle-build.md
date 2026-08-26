# TAGLINE

Gradle 完整构建生命周期任务

# TLDR

**构建项目**

```gradle build```

**跳过测试构建**

```gradle build -x test```

**构建特定模块**

```gradle :module:build```

**以 info 日志级别构建**

```gradle build --info```

**并行执行构建**

```gradle build --parallel```

**试运行**以查看将执行哪些任务

```gradle build --dry-run```

# SYNOPSIS

**gradle build** [_options_]

# PARAMETERS

**-x** _TASK_, **--exclude-task** _TASK_
> 将某个任务排除在执行之外。

**--info**
> 将日志级别设为 info。

**--debug**
> 将日志级别设为 debug。

**--stacktrace**
> 为异常打印完整的堆栈跟踪。

**--parallel**
> 并行构建各项目。

**--offline**
> 在不访问网络资源的情况下执行构建。

**--build-cache**
> 启用 Gradle 构建缓存。

**--no-daemon**
> 不使用 Gradle 守护进程运行构建。

**--continue**
> 在某个任务失败后继续执行其他任务。

**--dry-run**
> 显示将要执行的任务但不实际运行。

**-P** _PROP_, **--project-prop** _PROP_
> 设置项目属性。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gradle build** 编译源代码、运行测试并生成输出构件。它是组合了编译、测试和组装阶段的主构建生命周期任务。

该命令执行完整的构建过程，包括依赖解析、编译、测试和打包。可以通过构建脚本按项目进行定制。build 任务由 Java 插件提供，遵循 Gradle 的三阶段生命周期：初始化、配置和执行。

# CAVEATS

默认会运行测试。使用 **-x test** 可跳过。首次构建可能需要下载依赖，耗时较长。项目目录中需要有 **build.gradle** 或 **build.gradle.kts** 文件。

# HISTORY

build 任务是继承自 Java 插件约定的标准 **Gradle** 生命周期任务。

# INSTALL

```pacman: sudo pacman -S gradle```

```apk: sudo apk add gradle```

```brew: brew install gradle```

```nix: nix profile install nixpkgs#gradle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gradle](/man/gradle)(1), [gradle-clean](/man/gradle-clean)(1)
