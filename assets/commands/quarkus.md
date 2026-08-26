# TAGLINE

Kubernetes 原生 Java 框架的 CLI

# TLDR

**创建新项目**

```quarkus create app [com.example:myapp]```

**启动开发模式**

```quarkus dev```

**构建原生可执行文件**

```quarkus build --native```

**添加扩展**

```quarkus extension add [resteasy-reactive]```

**列出扩展**

```quarkus extension list```

**搜索扩展**

```quarkus extension search [jdbc]```

**构建 JAR**

```quarkus build```

**运行测试**

```quarkus test```

# SYNOPSIS

**quarkus** [_create_] [_dev_] [_build_] [_extension_] [_options_] [_args_]

# PARAMETERS

**create app** _NAME_
> 创建新应用程序。

**create cli**
> 创建 CLI 应用程序。

**dev**
> 支持热重载的开发模式。

**build**
> 构建应用程序。

**build --native**
> 构建原生可执行文件。

**test**
> 运行测试。

**extension add** _EXT_
> 添加扩展。

**extension list**
> 列出项目的扩展。

**extension search** _QUERY_
> 搜索可用扩展。

**deploy**
> 部署应用程序。

**image build**
> 构建容器镜像。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**quarkus** 是 Quarkus（一个 Kubernetes 原生 Java 框架）的 CLI，用于创建、构建和运行 Quarkus 应用程序。

开发模式提供实时重载。代码更改会触发自动重启。Dev Services 会自动拉起数据库和其他依赖服务。

原生编译使用 GraalVM 生成独立的可执行文件，启动时间以毫秒计，内存占用也低于传统 Java。

扩展可增加功能：REST API、数据库访问、消息传递、安全性等。扩展目录覆盖了大多数企业需求。

容器镜像构建与 Docker、Podman 和 Kubernetes 集成。镜像可以使用 JVM 或原生模式。

该框架面向微服务和 Serverless 部署场景，这些场景对快速启动和低内存占用要求极高。

# CAVEATS

原生编译耗时且耗内存。部分 Java 库无法在原生模式下工作。原生构建需要 GraalVM。

# HISTORY

**Quarkus** 由 **Red Hat** 于 **2019 年**发布，是一款"超音速亚原子 Java"框架。它从零开始为容器和 Kubernetes 部署而设计，解决了 Java 在启动时间和内存方面的传统短板。

# INSTALL

```nix: nix profile install nixpkgs#quarkus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mvn](/man/mvn)(1), [gradle](/man/gradle)(1), [java](/man/java)(1), [docker](/man/docker)(1)
