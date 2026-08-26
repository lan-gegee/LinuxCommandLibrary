# TAGLINE

Java 的构建自动化与项目管理工具

# TLDR

**编译项目**

```mvn compile```

**运行测试**

```mvn test```

**打包（生成 JAR/WAR）**

```mvn package```

**安装到本地仓库**

```mvn install```

**清理构建产物**

```mvn clean```

**构建时跳过测试**

```mvn package -DskipTests```

**运行指定目标**

```mvn dependency:tree```

# SYNOPSIS

**mvn** [_options_] [_goal_...]

# PARAMETERS

**clean**
> 删除构建目录。

**compile**
> 编译源代码。

**test**
> 运行单元测试。

**package**
> 创建 JAR/WAR。

**install**
> 安装到本地仓库。

**deploy**
> 部署到远程仓库。

**-DskipTests**
> 跳过测试执行。

**-U**
> 强制更新快照依赖。

**-o**, **--offline**
> 离线模式。

**-P** _profile_
> 激活指定的 profile。

# DESCRIPTION

**Maven** 是 Java 的构建自动化与项目管理工具。它基于项目对象模型（pom.xml）管理依赖、编译代码、运行测试并打包应用。

Maven 遵循"约定优于配置"原则，使用标准的目录布局和构建生命周期。

# PROJECT STRUCTURE

```
project/
├── pom.xml
├── src/
│   ├── main/java/
│   └── test/java/
└── target/
```

# CAVEATS

需要 pom.xml。首次运行会下载依赖。本地仓库位于 ~/.m2。插件可以扩展功能。

# HISTORY

Maven 由 Jason van Zyl 于 **2002 年**在 **Apache 软件基金会** 创建，作为 Apache Ant 的继任者，强调约定优于配置。

# INSTALL

```dnf: sudo dnf install maven```

```pacman: sudo pacman -S maven```

```zypper: sudo zypper install maven```

```brew: brew install maven```

```nix: nix profile install nixpkgs#maven```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gradle](/man/gradle)(1), [ant](/man/ant)(1), [java](/man/java)(1)
