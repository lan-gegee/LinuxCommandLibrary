# TAGLINE

Gradle 项目属性查看工具

# TLDR

**列出所有项目属性**

```gradle properties```

**通过 wrapper 列出**

```./gradlew properties```

**通过命令行设置属性**

```gradle build -PmyProp=value```

**设置多个属性**

```gradle build -Pprop1=val1 -Pprop2=val2```

# SYNOPSIS

**gradle** **properties**

**gradle** [**-P**_name_=_value_] _task_

# PARAMETERS

**-P**_name_=_value_
> 设置项目属性。

**-D**org.gradle.project._name_=_value_
> 通过系统属性设置属性。

# DESCRIPTION

**gradle properties** 显示 Gradle 项目中所有可用的属性，包括内置属性以及在 gradle.properties 文件中定义的属性。属性可以通过命令行 **-P** 设置，也可以通过环境变量（ORG_GRADLE_PROJECT_name）或项目级/用户级的 gradle.properties 文件设置。

# SEE ALSO

[gradle](/man/gradle)(1), [gradle-tasks](/man/gradle-tasks)(1)

# RESOURCES

```[Documentation](https://docs.gradle.org/current/userguide/build_environment.html)```

<!-- verified: 2026-07-17 -->
