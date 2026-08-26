# TAGLINE

Gradle 依赖追踪工具

# TLDR

**追踪某个依赖**以查看它为何被引入

```gradle dependencyInsight --dependency [library-name]```

**在特定配置中追踪**依赖

```gradle dependencyInsight --configuration [compileClasspath] --dependency [guava]```

**只显示通向每个依赖的单一路径**（适用于大型依赖图）

```gradle dependencyInsight --dependency [library-name] --singlepath```

**在特定子项目中追踪**依赖

```gradle :[subproject]:dependencyInsight --dependency [library-name]```

# SYNOPSIS

**gradle dependencyInsight** [_options_]

# PARAMETERS

**--dependency** _NAME_
> 必需。要追踪的依赖。支持对 group、name 或 version 的部分匹配。

**--configuration** _NAME_
> 要检查的配置（例如 compileClasspath、runtimeClasspath）。Java 项目默认为 compileClasspath。

**--singlepath**
> 只显示通向每个依赖的一条路径而不是所有路径。适用于大型依赖图。

# DESCRIPTION

**gradle dependencyInsight** 追踪特定依赖为何出现在构建中。它会显示从直接依赖到传递引入的路径，揭示版本冲突是如何被解决的。

**--dependency** 的值会对依赖的 group、name 或 version 做部分匹配，因此查询 `guava` 可以匹配 `com.google.guava:guava:31.1-jre`。

该任务是调试依赖问题、理解解析过程中为何选中特定版本的关键工具。

# CAVEATS

必须提供 **--dependency** 标志。不指定 **--configuration** 时，该任务在 Java 项目中默认使用 compileClasspath。依赖值采用部分匹配，常见名称可能返回意料之外的结果。

# INSTALL

```pacman: sudo pacman -S gradle```

```apk: sudo apk add gradle```

```brew: brew install gradle```

```nix: nix profile install nixpkgs#gradle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gradle](/man/gradle)(1), [gradle-dependencies](/man/gradle-dependencies)(1)
