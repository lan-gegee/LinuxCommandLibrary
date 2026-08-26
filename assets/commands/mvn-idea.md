# TAGLINE

生成 IntelliJ IDEA 项目文件

# TLDR

**生成 IDEA 项目文件**

```mvn idea:idea```

**生成模块文件**

```mvn idea:module```

**生成工作区**

```mvn idea:workspace```

**清理 IDEA 文件**

```mvn idea:clean```

**下载源码**

```mvn idea:idea -DdownloadSources=true```

**下载 JavaDocs**

```mvn idea:idea -DdownloadJavadocs=true```

# SYNOPSIS

**mvn** **idea:**_goal_ [_options_]

# PARAMETERS

_GOAL_
> IDEA 插件的 goal。

**idea**
> 生成所有文件。

**module**
> 生成模块文件。

**workspace**
> 生成工作区。

**clean**
> 移除 IDEA 文件。

**-DdownloadSources**
> 包含源码 JAR 包。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mvn idea** 调用旧版的 Maven IDEA Plugin，它根据 Maven POM 生成 IntelliJ IDEA 项目文件（**.ipr**、**.iml** 和 **.iws**）。插件读取依赖、源码目录和资源，并将它们写入 IDEA 的 XML 项目元数据，使项目无需进一步配置即可打开。

现代 IntelliJ IDEA 通过内置的 Maven 集成直接导入 **pom.xml** 文件，因此该插件已基本过时。它仅在遗留构建环境或需要在不启动 IDE 的情况下生成 IDEA 项目文件的 CI 脚本中仍有用。

# CAVEATS

该插件不再积极开发，并已从官方 Maven 项目退役。生成的 **.iml** 文件可能使用较旧的 IDEA 模块格式，与新版 IDEA 不兼容。在现代 IDEA 中建议直接对 **pom.xml** 使用 File > Open。

# HISTORY

Maven IDEA Plugin（groupId 为 **org.apache.maven.plugins**，artifactId 为 **maven-idea-plugin**）创建于 IntelliJ IDEA 获得原生 Maven 导入支持之前。当 IDEA 的 Maven 集成成熟后，Apache Maven 正式将其退役。

# INSTALL

```dnf: sudo dnf install maven```

```pacman: sudo pacman -S maven```

```apk: sudo apk add maven```

```zypper: sudo zypper install maven```

```brew: brew install maven```

```nix: nix profile install nixpkgs#maven```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mvn](/man/mvn)(1), [mvn-compile](/man/mvn-compile)(1), [idea](/man/idea)(1)
