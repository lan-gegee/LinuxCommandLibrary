# TAGLINE

Scala 构件获取与应用启动器

# TLDR

**安装 Scala 应用**

```cs install [scala]```

按构件坐标**启动应用**

```cs launch [org.scalameta::metals:latest.stable]```

为构件**解析依赖**

```cs resolve [org.typelevel::cats-core:2.9.0]```

为依赖**获取 JAR 包**

```cs fetch [com.lihaoyi::ammonite:2.5.9]```

**更新已安装的应用**

```cs update```

**列出已安装的应用**

```cs list```

**初始化 Coursier**（安装默认应用）

```cs setup```

# SYNOPSIS

**cs** _command_ [_options_] [_arguments_]

# PARAMETERS

**install** _APP_
> 从默认渠道安装应用。

**launch** _COORDS_
> 按 Maven 坐标启动应用。

**resolve** _COORDS_
> 解析并显示依赖树。

**fetch** _COORDS_
> 下载依赖的构件。

**update**
> 更新所有已安装的应用。

**list**
> 列出已安装的应用。

**setup**
> 初始设置，安装常用的 Scala 工具。

**uninstall** _APP_
> 移除已安装的应用。

**java**
> 管理 Java 安装。

**--channel** _URL_
> 添加自定义应用渠道。

**-r** _REPO_
> 添加自定义 Maven 仓库。

# DESCRIPTION

**Coursier**（cs）是一个 Scala 构件获取器和应用启动器。它解析 Maven 和 Ivy 依赖、下载构件，并能直接按坐标启动 JVM 应用，无需手动安装。

该工具提供带缓存的快速并行下载。它可以安装和管理 sbt、scala、ammonite、scalafmt 等 Scala 生态工具。setup 命令可配置出完整的 Scala 开发环境。

Coursier 能处理复杂的依赖解析，包括版本冲突消解和排除规则。它是 Scala 官方推荐的工具安装方式，sbt 也用它进行依赖管理。

# CAVEATS

需要 Java 运行时环境。首次运行要下载依赖，耗时较长。各应用渠道的更新频率可能不同。庞大的依赖树会在缓存中占用大量磁盘空间。

# HISTORY

Coursier 由 Alexandre Archambault 创建，约 **2015** 年首次发布。它于 **2020** 年成为 Scala 工具的官方安装方式。该工具以快速可靠的构件解析，化解了 Java/Scala 依赖管理的复杂性。

# INSTALL

```apt: sudo apt install csound```

```pacman: sudo pacman -S csound```

```zypper: sudo zypper install csound```

```brew: brew install csound```

```nix: nix profile install nixpkgs#csound```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scala](/man/scala)(1), [sbt](/man/sbt)(1), [java](/man/java)(1), [mvn](/man/mvn)(1)

# RESOURCES

```[Source code](https://github.com/coursier/coursier)```

```[Documentation](https://get-coursier.io/docs/cli-overview)```

<!-- verified: 2026-06-26 -->
