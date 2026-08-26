# TAGLINE

通过 Coursier 管理 JDK 版本

# TLDR

**列出可用的 JDK** 发行版

```cs java --available```

**安装指定的 JDK** 版本

```cs java --jvm [adopt:11] --setup```

**设置默认 Java** 版本

```cs java --jvm [graalvm-java17] --setup```

**查看当前 Java** 配置

```cs java --env```

**列出已安装的 JDK**

```cs java --installed```

**安装并使用**指定发行版

```cs java --jvm [temurin:21]```

# SYNOPSIS

**cs java** [_options_]

# PARAMETERS

**--available**
> 列出所有可用的 JDK 发行版及版本。

**--jvm** _JVM_
> 指定 JDK 发行版与版本（如 adopt:11、temurin:21）。

**--setup**
> 将指定的 JDK 配置为默认版本。

**--env**
> 打印当前 Java 环境的环境变量。

**--installed**
> 列出本地已安装的 JDK 版本。

**--update**
> 更新到最新的补丁版本。

**--home**
> 打印指定 JVM 的 JAVA_HOME 路径。

# DESCRIPTION

**cs java** 是 Coursier 的 Java 版本管理器，可以轻松安装和切换不同的 JDK 发行版与版本。它支持众多发行版，包括 AdoptOpenJDK、Temurin、GraalVM、Corretto 和 Zulu。

该命令自动下载并管理 JDK 安装，配置环境变量以使用所选版本。可以同时安装多个版本，并方便地在它们之间切换。

这款工具简化了 Java 开发环境的搭建，特别适合在不同 Java 版本之间进行测试，或使用特定发行版的功能（例如 GraalVM 的原生编译）。

# CAVEATS

**--setup** 选项会修改 shell 配置文件。部分发行版可能在某些平台上不可用。大型 JDK 下载需要足够的磁盘空间和网络带宽。环境变更需要重启 shell 才能生效。

# HISTORY

cs java 被加入 Coursier 是为了提供全面的 JDK 管理能力，与其 Scala 工具链功能相辅相成。它遵循 sdkman 和 jabba 等版本管理器的模式，并集成到了 Coursier 生态系统中。

# INSTALL

```apt: sudo apt install csound```

```pacman: sudo pacman -S csound```

```zypper: sudo zypper install csound```

```brew: brew install csound```

```nix: nix profile install nixpkgs#csound```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cs](/man/cs)(1), [java](/man/java)(1), [sdk](/man/sdk)(1), [update-java-alternatives](/man/update-java-alternatives)(1)

# RESOURCES

```[Source code](https://github.com/coursier/coursier)```

```[Documentation](https://get-coursier.io/docs/cli-java)```

<!-- verified: 2026-06-26 -->
