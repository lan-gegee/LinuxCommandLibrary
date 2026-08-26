# TAGLINE

显示可用的 Gradle 项目任务

# TLDR

**列出主要任务**

```gradle tasks```

**列出所有任务（包括内部任务）**

```gradle tasks --all```

**通过 Gradle wrapper 列出**

```./gradlew tasks```

**列出子项目的任务**

```gradle :app:tasks```

**列出特定分组中的任务**

```gradle tasks --group [build]```

**获取特定任务的帮助**

```gradle help --task [taskName]```

# SYNOPSIS

**gradle** **tasks** [**--all**] [**--group** _name_]

# PARAMETERS

**--all**
> 显示所有任务，包括内部任务和未分组的生命周期任务。

**--group** _name_
> 只显示属于指定分组的任务。

**--no-report**
> 隐藏输出底部的任务规则报告。

# DESCRIPTION

**gradle tasks** 显示所选项目可用的任务。默认情况下，只显示已分配到任务组且带有描述的任务。使用 **--all** 可包含未分组、内部和生命周期任务。使用 **--group** 可按特定任务组过滤。使用 **gradle help --task** 可获取特定任务的详细信息，包括其类型、路径和选项。

任务按 build、verification、documentation、help 等分组组织。构建脚本中定义的自定义任务组也会出现在输出中。

# INSTALL

```pacman: sudo pacman -S gradle```

```apk: sudo apk add gradle```

```brew: brew install gradle```

```nix: nix profile install nixpkgs#gradle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gradle](/man/gradle)(1), [gradle-projects](/man/gradle-projects)(1), [ant](/man/ant)(1), [mvn](/man/mvn)(1)
