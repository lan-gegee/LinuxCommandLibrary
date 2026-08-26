# TAGLINE

Maven 和 Ivy 依赖解析器

# TLDR

为构件**解析依赖**

```cs resolve [org.typelevel::cats-core:2.9.0]```

**显示依赖树**

```cs resolve -t [org.apache.spark::spark-sql:3.4.0]```

带排除规则解析

```cs resolve [app:version] --exclude [org.slf4j:*]```

从自定义仓库解析

```cs resolve -r [https://repo.example.com/maven] [org.example::app:1.0]```

**检查版本冲突**

```cs resolve --conflicts [app:version]```

以 JSON 输出

```cs resolve --json [app:version]```

# SYNOPSIS

**cs resolve** [_options_] _coordinates_...

# PARAMETERS

_COORDINATES_
> 要解析的 Maven 坐标（可指定多个）。

**-t**, **--tree**
> 以依赖树而不是扁平列表的形式显示。

**-r** _URL_, **--repository** _URL_
> 添加自定义 Maven 仓库。

**--exclude** _PATTERN_
> 排除匹配模式的构件（groupId:artifactId）。

**--conflicts**
> 显示依赖中的版本冲突。

**--json**
> 以 JSON 格式输出解析结果。

**--reverse**
> 显示反向依赖（什么依赖什么）。

**--what-depends-on** _COORDS_
> 显示哪些构件依赖某个特定构件。

**-q**, **--quiet**
> 抑制进度输出。

# DESCRIPTION

**cs resolve** 执行 Maven/Ivy 依赖解析，显示给定构件的全部传递依赖。它适合用来理解依赖树、发现版本冲突以及排查 classpath 问题。

该命令只做解析而不下载构件，因此浏览依赖时速度很快。树状视图展示依赖的层级关系，扁平视图则列出所有已解析的构件及其版本。

冲突检测有助于发现同一个库的不同版本被同时请求的情况。反向依赖功能有助于弄清某个库为何会被引入。

# CAVEATS

解析结果的准确性取决于 POM/ivy.xml 的完整程度。某些构件带有可选依赖，可能被遗漏。跨版本构件（Scala）需要使用正确的写法（::）。获取仓库元数据需要网络连接。

# HISTORY

cs resolve 是 Coursier 依赖管理能力的一部分。依赖解析是支撑应用启动和构件获取的核心操作，被抽取为独立命令以便分析和调试。

# INSTALL

```apt: sudo apt install csound```

```pacman: sudo pacman -S csound```

```zypper: sudo zypper install csound```

```brew: brew install csound```

```nix: nix profile install nixpkgs#csound```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cs](/man/cs)(1), [mvn](/man/mvn)(1), [gradle](/man/gradle)(1)
