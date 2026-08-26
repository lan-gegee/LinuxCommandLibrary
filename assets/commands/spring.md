# TAGLINE

Spring Boot 应用框架 CLI

# TLDR

**创建新项目**（通过 start.spring.io）

```spring init --dependencies=[web,data-jpa,postgresql] [myapp]```

**以指定选项创建**

```spring init --build=[gradle] --java-version=[17] --packaging=[war] [myapp.zip]```

**列出可用依赖和选项**

```spring init --list```

**使用 bcrypt 编码密码**

```spring encodepassword [password]```

**配合 Maven wrapper 运行 Spring Boot 应用**

```./mvnw spring-boot:run```

**配合 Gradle wrapper 运行**

```./gradlew bootRun```

**打包为可执行 JAR**

```./mvnw package```

**显示 CLI 版本**

```spring --version```

# SYNOPSIS

**spring** _command_ [_options_] [_args_...]

**./mvnw** spring-boot:_goal_

**./gradlew** boot_Task_

# SPRING CLI COMMANDS

**init** [_options_] [_location_]
> 从 start.spring.io 创建新项目。

**encodepassword** [_options_] _password_
> 为 Spring Security 编码密码。

**shell**
> 启动交互式 Shell。

**version**
> 显示 CLI 版本。

**help** [_command_]
> 显示帮助。

# INIT OPTIONS

**-d**, **--dependencies** _list_
> 以逗号分隔的依赖标识符列表。

**-b**, **--build** _type_
> 构建系统：maven（默认）、gradle。

**-j**, **--java-version** _version_
> Java 版本：17、21。

**-l**, **--language** _lang_
> 语言：java、kotlin、groovy。

**-n**, **--name** _name_
> 项目名称。

**-g**, **--group-id** _group_
> Maven group ID。

**-a**, **--artifact-id** _artifact_
> Maven artifact ID。

**-p**, **--packaging** _type_
> 打包方式：jar（默认）、war。

**-v**, **--version** _version_
> 项目版本（例如 '0.0.1-SNAPSHOT'）。

**--boot-version** _version_
> Spring Boot 版本。

**-x**, **--extract**
> 解压项目归档。

**-f**, **--force**
> 强制覆盖已存在的文件。

**--list**
> 列出可用选项和依赖。

# MAVEN/GRADLE GOALS

**spring-boot:run** / **bootRun**
> 运行应用。

**spring-boot:build-image** / **bootBuildImage**
> 构建 OCI 容器镜像。

**package** / **bootJar**
> 创建可执行 JAR。

**spring-boot:start** / **bootStart**
> 在后台启动应用。

**spring-boot:stop** / **bootStop**
> 停止后台应用。

# DESCRIPTION

**spring** CLI 与 Spring Boot 的 Maven/Gradle 插件用于管理 Spring Boot 应用。CLI 负责搭建新项目骨架和编码密码；插件负责构建和运行。**run** 命令已在 Spring Boot 3.0 中移除。

**spring init** 从 start.spring.io 获取项目模板，并带上所选依赖。web、data-jpa、security 等依赖会添加自动配置相应功能的 starter。

开发期间运行应用使用 **bootRun**（Gradle）或 **spring-boot:run**（Maven）。若将 DevTools 加入依赖，即可启用热重载。

**bootJar** / **package** 创建内嵌服务器的可执行 JAR，用 **java -jar app.jar** 运行。**bootBuildImage** 无需 Dockerfile 即可创建 OCI 容器镜像。

借助 GraalVM 的原生镜像支持，可通过 **-Pnative** profile 将应用编译为原生可执行文件。该方式要求 GraalVM，并生成启动迅速的二进制文件。

# CAVEATS

**spring run** 命令已在 Spring Boot 3.0 中移除；请改用 Maven/Gradle 插件来运行应用。CLI 主要用于项目创建。自动配置可能与自定义配置冲突。原生镜像需要额外的元数据。DevTools 应从生产环境中排除。

# HISTORY

Spring Boot 由 **Phil Webb** 领导的 **Pivotal**（现为 VMware）团队创建，于 **2014 年**发布。它以"约定优于配置"的理念简化了 Spring Framework 开发。Spring Boot 2.0（2018 年）升级到 Spring Framework 5。3.0 版（2022 年）要求 Java 17，移除了 CLI 的 **run** 命令，并加入原生编译支持。Spring Boot 是使用最广泛的 Java 应用框架。

# INSTALL

```pacman: sudo pacman -S spring```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mvn](/man/mvn)(1), [gradle](/man/gradle)(1), [quarkus](/man/quarkus)(1)
