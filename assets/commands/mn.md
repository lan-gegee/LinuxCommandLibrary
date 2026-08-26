# TAGLINE

用于搭建应用骨架和生成代码的 Micronaut CLI

# TLDR

**创建新应用**

```mn create-app [com.example.myapp]```

**使用指定特性创建**

```mn create-app [com.example.myapp] --features [postgres,hibernate-jpa]```

**创建函数**

```mn create-function [com.example.myfunction]```

**创建 CLI 应用**

```mn create-cli-app [com.example.mycli]```

**生成控制器**

```mn create-controller [User]```

**生成服务 bean**

```mn create-bean [UserService]```

**列出可用特性**

```mn feature-diff --features```

**启动交互模式**

```mn```

# SYNOPSIS

**mn** _command_ [_options_] [_args_...]

# COMMANDS

**create-app** _name_
> 创建新的 Micronaut 应用。

**create-function** _name_
> 创建无服务器函数项目。

**create-cli-app** _name_
> 创建 CLI 应用。

**create-grpc-app** _name_
> 创建 gRPC 应用。

**create-messaging-app** _name_
> 创建消息传递应用。

**create-controller** _name_
> 生成控制器类。

**create-bean** _name_
> 生成服务 bean。

**create-client** _name_
> 生成 HTTP 客户端。

**create-job** _name_
> 生成定时任务。

**create-test** _name_
> 生成测试类。

**feature-diff**
> 比较特性差异。

# PARAMETERS

**--features** _list_
> 以逗号分隔的特性列表。

**--build** _tool_
> 构建工具：gradle（默认）、gradle-kotlin、maven。

**--lang** _language_
> 语言：java（默认）、kotlin、groovy。

**--jdk** _version_
> 目标 JDK 版本。

**--test** _framework_
> 测试框架：junit、spock、kotest。

**--inplace**
> 在当前目录中创建。

**-i**, **--interactive**
> 交互模式。

# FEATURES

**data-jdbc**, **data-jpa**, **hibernate-jpa**
> 数据库访问选项。

**postgres**, **mysql**, **h2**
> 数据库驱动。

**security-jwt**, **security-oauth2**
> 安全特性。

**kafka**, **rabbitmq**, **nats**
> 消息传递集成。

**graalvm**
> 原生镜像支持。

**openapi**
> OpenAPI/Swagger 文档。

**graphql**
> GraphQL 支持。

# DESCRIPTION

**mn** 是 Micronaut 的 CLI，用于搭建应用骨架和生成代码。Micronaut 是一个用于构建云原生微服务的 JVM 框架。

**create-app** 会生成一个包含构建文件、应用类和配置的项目。特性会自动添加依赖和配置。

Micronaut 采用编译期依赖注入——运行时不需要反射。这使得启动速度快、内存占用低，配合 GraalVM 原生镜像时尤为明显。

代码生成器（**create-controller**、**create-bean** 等）会按照 Micronaut 约定添加类。生成的代码带有用于注入、HTTP 路由和测试的注解。

交互模式为命令和特性提供 Tab 补全。使用 **feature-diff** 可以查看某个特性会给项目添加什么。

# CAVEATS

编译期依赖注入要求正确配置注解处理器。某些特性之间可能冲突。原生镜像需要 GraalVM 以及额外的配置。生成器会把文件创建在约定的位置。

# HISTORY

Micronaut 由 **Graeme Rocher**（Grails 的创造者）在 **Object Computing, Inc.** 开发，于 **2018 年**发布。它旨在解决 Spring 等传统框架的启动时间和内存问题。Micronaut 在 Java 生态中开创了编译期依赖注入。4.0 版本（2023 年）带来了模块化架构。该框架在无服务器和 Kubernetes 部署中很受欢迎。

# INSTALL

```apt: sudo apt install mininet```

```dnf: sudo dnf install mininet```

```zypper: sudo zypper install mininet```

```nix: nix profile install nixpkgs#mininet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gradle](/man/gradle)(1), [maven](/man/maven)(1), [quarkus](/man/quarkus)(1)
