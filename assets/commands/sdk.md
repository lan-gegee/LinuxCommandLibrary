# TAGLINE

管理 JVM 语言的并行 SDK 版本

# TLDR

**列出所有可用的 candidate**（Java、Scala、Kotlin 等）

```sdk list```

**列出**某个 candidate 的可用版本

```sdk list java```

**安装某个 candidate 的最新稳定版本**

```sdk install java```

**安装指定版本**

```sdk install java [21.0.4-tem]```

为当前 shell 会话**切换版本**

```sdk use java [17.0.12-tem]```

**将某个版本设为默认**，对所有 shell 生效

```sdk default java [21.0.4-tem]```

**显示当前激活的版本**

```sdk current```

**升级过期的 candidate**

```sdk upgrade```

# SYNOPSIS

**sdk** _command_ [_candidate_] [_version_]

# COMMANDS

**install** _candidate_ [_version_]
> 安装某个 candidate 的版本；省略 version 时安装最新稳定版

**uninstall** _candidate_ _version_
> 移除已安装的版本

**list** [_candidate_]
> 列出所有可用 candidate 或特定 candidate 的可用版本

**use** _candidate_ _version_
> 仅为当前终端会话切换版本

**default** _candidate_ _version_
> 将某版本设为默认，对所有后续 shell 生效

**current** [_candidate_]
> 显示某个或全部 candidate 当前激活的版本

**upgrade** [_candidate_]
> 升级过期版本

**version**
> 显示 SDKMAN 版本信息

**home** _candidate_ _version_
> 返回某个版本的绝对安装路径

**env** [**init**|**install**|**clear**]
> 管理项目专属的 .sdkmanrc 配置

**offline** [**enable**|**disable**]
> 切换离线模式

**selfupdate** [**force**]
> 更新 SDKMAN 自身

**update**
> 刷新 candidate 元数据缓存

**flush** [**tmp**|**broadcast**|**archives**|**version**]
> 清除本地缓存和状态

**config**
> 打开 SDKMAN 配置文件

# DESCRIPTION

**SDKMAN**（Software Development Kit Manager）是一款用于在基于 Unix 的系统上管理多个 SDK 并行版本的工具。它简化了 JVM 生态开发套件的安装、切换和移除。

支持的 candidate 包括 **Java**（Temurin、Zulu、GraalVM 等多个发行版）、**Scala**、**Kotlin**、**Groovy**、**Maven**、**Gradle**、**Ant**、**sbt**、**Spring Boot**、**Spark** 等。SDKMAN 会自动管理 **JAVA_HOME** 和 **PATH** 环境变量。

项目专属的版本可以通过 **.sdkmanrc** 文件配置。在配置中设置 **sdkman_auto_env=true** 后，SDKMAN 会在进入项目目录时自动切换版本。

# CONFIGURATION

**~/.sdkman/etc/config**
> SDKMAN 配置文件，控制自动应答、auto-env、颜色等设置。

**.sdkmanrc**
> 项目级文件，声明所需的 SDK 版本。若设置了 **sdkman_auto_env=true**，进入该目录时 SDKMAN 会自动切换版本。

**SDKMAN_DIR**
> 覆盖默认 SDKMAN 安装目录（~/.sdkman）的环境变量。

# CAVEATS

SDKMAN 需要已安装 **curl**、**zip** 和 **unzip**。安装过程中它会修改 shell 配置文件。**use** 命令只影响当前 shell；要在会话之间持久生效请使用 **default**。

# HISTORY

SDKMAN 最初由 **Marco Vermeulen** 于约 **2012 年**创建，名为 **GVM**（Groovy enVironment Manager）。后来更名为 SDKMAN，以体现其对 Groovy 之外多种 SDK candidate 的广泛支持。该工具的灵感来自 **RVM**（Ruby）、**nvm**（Node.js）和 **pyenv**（Python）等版本管理器。

# SEE ALSO

[java](/man/java)(1), [javac](/man/javac)(1), [gradle](/man/gradle)(1), [mvn](/man/mvn)(1), [sbt](/man/sbt)(1)
