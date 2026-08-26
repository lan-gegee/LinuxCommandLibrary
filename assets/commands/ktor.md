# TAGLINE

Ktor 的 CLI，Ktor 是用于构建异步服务器的 Kotlin 框架

# TLDR

**创建新项目**（交互式）

```ktor new```

**以指定插件创建**

```ktor new --plugins [routing,content-negotiation,ktor-serialization]```

**以自定义名称创建**

```ktor new --name [myapp]```

**以 Gradle Kotlin DSL 生成**

```ktor new --build-system gradle-kotlin```

**列出可用插件**

```ktor plugins list```

**搜索插件**

```ktor plugins search [auth]```

**显示版本号**

```ktor --version```

# SYNOPSIS

**ktor** _command_ [_options_]

# COMMANDS

**new**
> 创建新的 Ktor 项目。

**plugins** list|search
> 浏览可用插件。

**--version**
> 显示 CLI 版本。

**--help**
> 显示帮助信息。

# NEW OPTIONS

**--name** _name_
> 项目名称。

**--package** _package_
> 基础包名。

**--plugins** _list_
> 逗号分隔的插件列表。

**--build-system** _type_
> 构建系统：gradle-kotlin、gradle-groovy、maven。

**--engine** _engine_
> 服务器引擎：netty、jetty、tomcat、cio。

**--configuration** _type_
> 配置方式：hocon、yaml。

**--ktor-version** _version_
> Ktor 版本。

**--kotlin-version** _version_
> Kotlin 版本。

**--output** _path_
> 输出目录。

**--interactive**
> 交互模式。

# PLUGINS

**routing**
> HTTP 路由。

**content-negotiation**
> 内容类型协商。

**ktor-serialization-kotlinx-json**
> JSON 序列化。

**auth**, **auth-jwt**
> 身份验证支持。

**call-logging**
> 请求日志。

**websockets**
> WebSocket 支持。

**cors**
> 跨域资源共享。

**sessions**
> 会话管理。

**status-pages**
> 错误处理。

# DESCRIPTION

**ktor** 是 Ktor 的 CLI，Ktor 是一个用于构建异步服务器和客户端的 Kotlin 框架。它根据所选特性生成新项目骨架。

**ktor new** 会生成包含构建文件、应用配置和插件设置的项目。插件提供身份验证、序列化、WebSocket 等功能。

Ktor 应用在 Application.kt 中使用 DSL 配置特性。插件在模块中安装：**install(ContentNegotiation)**、**install(Authentication)** 等。

该框架可运行在多种引擎上：Netty、Jetty、Tomcat 或 CIO（Kotlin 协程）。按需选择——生产环境默认使用 Netty。

通过 HOCON (application.conf) 或 YAML 配置端口、主机和插件设置。环境变量会覆盖配置值。

# CAVEATS

需要 Kotlin 知识。插件兼容性可能因 Ktor 版本而异。CIO 引擎相比 Netty 功能有限。某些插件需要额外配置。

# HISTORY

Ktor 由 **JetBrains** 创建，于 **2017 年**首次发布。它被设计为利用协程进行异步编程的原生 Kotlin 框架。与 Spring 不同，Ktor 轻量且配置显式。2.0 版（2022 年）带来了重大的 API 变更。Ktor 在 Kotlin 项目的微服务和 API 开发中很受欢迎。

# INSTALL

```brew: brew install ktor```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gradle](/man/gradle)(1), [kotlin](/man/kotlin)(1)
