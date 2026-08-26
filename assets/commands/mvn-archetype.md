# TAGLINE

从模板（archetype）创建新的 Maven 项目

# TLDR

**以交互方式生成项目**（默认）

```mvn archetype:generate```

**使用特定的 archetype 生成**

```mvn archetype:generate -DarchetypeGroupId=[org.apache.maven.archetypes] -DarchetypeArtifactId=[maven-archetype-quickstart]```

**以非交互方式用完整坐标生成**

```mvn archetype:generate -DinteractiveMode=false -DgroupId=[com.example] -DartifactId=[myapp] -DarchetypeArtifactId=[maven-archetype-quickstart]```

**按关键字过滤可用的 archetype**

```mvn archetype:generate -Dfilter=[spring-boot]```

**从当前项目创建一个 archetype**

```mvn archetype:create-from-project```

**更新本地 archetype 目录**

```mvn archetype:update-local-catalog```

# SYNOPSIS

**mvn archetype:**_goal_ [_-Dproperty=value_ ...]

# PARAMETERS

**-DarchetypeGroupId=**_id_
> 要使用的 archetype 的 Group ID（如 `org.apache.maven.archetypes`）。

**-DarchetypeArtifactId=**_id_
> archetype 的 Artifact ID（如 `maven-archetype-quickstart`）。

**-DarchetypeVersion=**_version_
> archetype 的版本。

**-DarchetypeCatalog=**_catalog_
> 以逗号分隔的目录列表：`remote`、`local`、`internal`（默认：`remote,local`）。

**-DgroupId=**_id_
> 所生成项目的 Group ID。

**-DartifactId=**_id_
> 所生成项目的 Artifact ID。

**-Dversion=**_version_
> 所生成项目的版本（默认 `1.0-SNAPSHOT`）。

**-Dpackage=**_name_
> 基础 Java 包名（默认为 Group ID）。

**-DinteractiveMode=**_bool_
> 为 `true` 时对缺失的值进行交互提示（默认遵循 `settings.xml`）。

**-Dfilter=**_expr_
> 按 `groupId:artifactId` 子串过滤显示的 archetype。

**-DoutputDirectory=**_dir_
> 项目创建所在的目录（默认：当前目录）。

# GOALS

**archetype:generate**
> 从 archetype 创建新项目。

**archetype:create-from-project**
> 将当前项目转换为可复用的 archetype。

**archetype:crawl**
> 扫描本地 Maven 仓库并生成目录文件。

**archetype:integration-test**
> 运行该 archetype 的集成测试。

**archetype:jar**
> 将当前的 archetype 项目打包为 JAR。

**archetype:update-local-catalog**
> 刷新本地 archetype 目录。

**archetype:help**
> 显示插件帮助。使用 `-Ddetail=true -Dgoal=generate` 查看详情。

# DESCRIPTION

**mvn archetype:generate** 从称为 archetype 的模板创建新的 Maven 项目。一个 archetype 包含项目骨架、`pom.xml` 以及源码/资源模板，这些内容会通过 Velocity 和用户提供的属性展开生成。

常见的 archetype 包括 `maven-archetype-quickstart`（最小化的 Java 应用）、`maven-archetype-webapp`（servlet WAR），以及 Spring Boot 或 Quarkus starter 等第三方模板。archetype 可从远程目录、本地仓库和内置的后备目录中发现。

不带参数运行时，插件会进入交互模式，列出带编号的 archetype 并提示输入项目坐标。

# INSTALL

```dnf: sudo dnf install maven```

```pacman: sudo pacman -S maven```

```apk: sudo apk add maven```

```zypper: sudo zypper install maven```

```brew: brew install maven```

```nix: nix profile install nixpkgs#maven```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mvn](/man/mvn)(1), [maven](/man/maven)(1), [mvn-compile](/man/mvn-compile)(1), [mvn-package](/man/mvn-package)(1), [mvn-dependency](/man/mvn-dependency)(1)
