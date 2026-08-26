# TAGLINE

Apache Maven 构建自动化与依赖管理工具

# TLDR

**构建项目**

```mvn package```

**清理并构建，安装到本地仓库**

```mvn clean install```

**运行测试**

```mvn test```

**构建期间跳过测试**

```mvn install -DskipTests```

**从原型生成新项目**

```mvn archetype:generate```

**将构件部署到远程仓库**

```mvn deploy```

**显示依赖树**

```mvn dependency:tree```

**检查依赖更新**

```mvn versions:display-dependency-updates```

**以指定 profile 运行**

```mvn clean install -P [profile-name]```

**离线构建，不下载依赖**

```mvn package -o```

# SYNOPSIS

**mvn** [_options_] [_phase(s)_] [_goal(s)_]

# PARAMETERS

_PHASES_
> 要执行的构建生命周期阶段。

**clean**
> 移除包含编译产物的 target 目录。

**validate**
> 验证项目正确且所有信息可用。

**compile**
> 编译项目源码。

**test**
> 运行单元测试。

**package**
> 打包编译后的代码（JAR、WAR 等）。

**verify**
> 运行集成测试和检查。

**install**
> 将软件包安装到本地仓库（~/.m2/repository）。

**deploy**
> 将软件包部署到远程仓库。

**-D** _PROPERTY=VALUE_
> 设置一个系统属性（例如 -DskipTests、-Dmaven.test.skip=true）。

**-P** _PROFILE_
> 激活 pom.xml 中定义的构建 profile。

**-pl** _MODULES_, **--projects** _MODULES_
> 构建多模块项目中的特定模块。

**-am**, **--also-make**
> 使用 -pl 时同时构建所需的依赖模块。

**-f** _FILE_, **--file** _FILE_
> 使用替代的 POM 文件。

**-o**, **--offline**
> 离线工作，不下载依赖。

**-U**, **--update-snapshots**
> 强制更新 SNAPSHOT 依赖。

**-T** _THREADS_
> 并行构建的线程数（例如 -T 4、每个 CPU 核心一个线程的 -T 1C）。

**-X**, **--debug**
> 产生调试输出。

**-q**, **--quiet**
> 安静输出，只显示错误。

**-e**, **--errors**
> 显示执行错误信息。

**-B**, **--batch-mode**
> 非交互式批处理模式（推荐在 CI 环境中使用）。

**-N**, **--non-recursive**
> 不递归进入子项目（仅构建 reactor 根项目）。

**-s** _FILE_, **--settings** _FILE_
> 使用替代的用户 settings 文件。

**-gs** _FILE_, **--global-settings** _FILE_
> 使用替代的全局 settings 文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mvn** 是 Apache Maven 的命令行界面。Maven 是一款主要用于 Java 项目的构建自动化和依赖管理工具。它使用项目对象模型（pom.xml）来描述项目及其依赖、插件和构建生命周期。

Maven 遵循约定优于配置的原则，采用标准项目结构（src/main/java、src/test/java 等）。构建生命周期由有序的阶段组成：validate、compile、test、package、verify、install、deploy。指定某个阶段会先执行其前面的所有阶段。

依赖从远程仓库解析（默认为 Maven Central）并缓存到 ~/.m2/repository 的本地仓库。Maven 支持多模块项目、面向不同环境的构建 profile，以及庞大的插件生态。

# CAVEATS

需要安装 JDK 和 pom.xml 文件。首次构建会下载大量依赖，可能耗时较长。**-DskipTests** 会跳过测试执行但仍编译测试代码；若要完全跳过测试的编译，请使用 **-Dmaven.test.skip=true**。本地仓库（~/.m2/repository）会随时间不断变大。

# HISTORY

Maven 由 Apache 软件基金会的 **Jason van Zyl** 创建。Maven 1.0 于 **2004 年**发布，Maven 2.0 在 **2005 年**随之推出，是一次完全重写。Maven 3.0 于 **2010 年**发布，性能和向后兼容性均有提升。它与 Gradle 并列，至今仍是最广泛使用的 Java 构建工具之一。

# INSTALL

```dnf: sudo dnf install maven```

```pacman: sudo pacman -S maven```

```apk: sudo apk add maven```

```zypper: sudo zypper install maven```

```brew: brew install maven```

```nix: nix profile install nixpkgs#maven```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gradle](/man/gradle)(1), [ant](/man/ant)(1), [java](/man/java)(1), [javac](/man/javac)(1)
