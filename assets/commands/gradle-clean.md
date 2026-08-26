# TAGLINE

Gradle 构建产物清理任务

# TLDR

**清理构建目录**

```gradle clean```

**清理特定模块**

```gradle :module:clean```

**清理并构建**

```gradle clean build```

# SYNOPSIS

**gradle clean** [_options_]

# PARAMETERS

**clean**_TaskName_
> 任务规则：只删除指定任务的输出，例如 `cleanJar` 会删除 `jar` 任务生成的 JAR。

**--info**
> Info 级别日志。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gradle clean** 删除项目的构建目录（由 `layout.buildDirectory` 设置的路径，默认为 `build/`）及其中的所有内容。它会移除编译后的类文件、打包的构件和缓存的构建输出，确保构建环境干净如初。

该任务由 Gradle 的 base 插件提供，Java、Application 以及大多数其他语言插件都会应用该插件。当构建结果不一致或缓存损坏时，它非常有用，可强制下次调用时进行完整重建。

# CAVEATS

会移除所有构建输出。下次构建将是完整重建。不会清理依赖。

# HISTORY

clean 任务是用于移除构建产物的标准 **Gradle** 生命周期任务。

# INSTALL

```pacman: sudo pacman -S gradle```

```apk: sudo apk add gradle```

```brew: brew install gradle```

```nix: nix profile install nixpkgs#gradle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gradle](/man/gradle)(1), [gradle-build](/man/gradle-build)(1)
