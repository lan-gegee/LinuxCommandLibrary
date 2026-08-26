# TAGLINE

Gradle 依赖树查看工具

# TLDR

**列出依赖**

```gradle dependencies```

**显示特定配置**

```gradle dependencies --configuration [compileClasspath]```

**模块依赖**

```gradle :module:dependencies```

**输出到文件**

```gradle dependencies > deps.txt```

# SYNOPSIS

**gradle dependencies** [_options_]

# PARAMETERS

**--configuration** _NAME_
> 要显示的特定配置。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gradle dependencies** 显示项目的依赖树。它会列出所有直接依赖和传递依赖及其版本和冲突解决结果。

输出展示不同配置（compile、runtime、test）下的依赖层次结构，有助于理解依赖链和版本冲突。

# CAVEATS

大型依赖树可能令人眼花缭乱。使用 --configuration 进行过滤。留意版本冲突。

# HISTORY

dependencies 任务是用于了解项目依赖关系的标准 **Gradle** 诊断任务。

# INSTALL

```pacman: sudo pacman -S gradle```

```apk: sudo apk add gradle```

```brew: brew install gradle```

```nix: nix profile install nixpkgs#gradle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gradle](/man/gradle)(1), [gradle-dependencyinsight](/man/gradle-dependencyinsight)(1)

# RESOURCES

```[Documentation](https://docs.gradle.org/current/userguide/viewing_debugging_dependencies.html)```

<!-- verified: 2026-07-17 -->
