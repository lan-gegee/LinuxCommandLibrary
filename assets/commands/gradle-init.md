# TAGLINE

Gradle 项目脚手架生成器

# TLDR

**以交互方式创建新项目**

```gradle init```

**创建 Java 应用**

```gradle init --type java-application```

**使用 Kotlin DSL 创建**

```gradle init --type java-application --dsl kotlin```

**创建带测试框架的库**

```gradle init --type java-library --test-framework junit-jupiter```

**创建 Kotlin 应用**

```gradle init --type kotlin-application```

**创建基础空项目**

```gradle init --type basic```

# SYNOPSIS

**gradle** **init** [**--type** _type_] [**--dsl** _dsl_] [_options_]

# PARAMETERS

**--type** _type_
> 项目类型：java-application、java-library、kotlin-application 等。

**--dsl** _dsl_
> 构建脚本 DSL：groovy 或 kotlin。

**--test-framework** _framework_
> 测试框架：junit、junit-jupiter、spock、testng。

**--project-name** _name_
> 项目名称。

**--package** _package_
> 源码包名。

# DESCRIPTION

**gradle init** 以标准目录结构创建新的 Gradle 项目。它可以交互式运行，提示选择项目类型、语言和构建脚本 DSL，也可以通过命令行选项非交互式运行。支持的类型包括 Java、Kotlin、Groovy、Scala、C++ 和 Swift 的应用程序与库。

# CAVEATS

在非空目录中运行时，如果检测到现有构建文件，可能会失败或跳过生成。用于搭建新项目类型的 **--incubating** API 可能随 Gradle 版本而变化。

# INSTALL

```pacman: sudo pacman -S gradle```

```apk: sudo apk add gradle```

```brew: brew install gradle```

```nix: nix profile install nixpkgs#gradle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gradle](/man/gradle)(1), [gradle-build](/man/gradle-build)(1)

# RESOURCES

```[Documentation](https://docs.gradle.org/current/userguide/build_init_plugin.html)```

<!-- verified: 2026-07-17 -->
