# TAGLINE

在运行时直接从 OpenAPI 规范渲染 SaaS 风格的 UI

# TLDR

在当前目录**搭建新的 uigen 项目**

```npx @uigen-dev/cli init```

**从 OpenAPI 规范渲染 UI** 并在 http://localhost:4400 提供服务

```npx @uigen-dev/cli serve [openapi.yaml]```

将 API 调用路由到**本地运行的后端**

```npx @uigen-dev/cli serve [openapi.yaml] --proxy-base [http://localhost:8000]```

**打包用于生产环境**部署

```npx @uigen-dev/cli build --spec [openapi.yaml]```

使用**显式的 spec 标志**代替位置参数

```npx @uigen-dev/cli serve --spec [api/openapi.yaml]```

# SYNOPSIS

**uigen** _subcommand_ [_spec_] [_options_]

# DESCRIPTION

**uigen** 是一个 OpenAPI 到 UI 的编译器。它读取 OpenAPI 3.x 规范，将其解析为与框架无关的中间表示（Intermediate Representation），其中包含资源、操作、模式、身份验证流程和分页策略，并在运行时渲染出完整的 React 前端。它没有代码生成步骤——渲染的 UI 在每次服务器启动（或热重载）时重新计算，因此对规范的更改会立即反映出来。

开箱即用，uigen 可以生成支持排序、过滤和分页的表格视图；带有从 JSON 模式派生验证的创建和编辑表单；带跨资源链接的详情视图；图表；文件上传；以及适用于 OAuth 2.0、Bearer 令牌和 API 密钥的身份验证流程。主题定制和 AI 原生的"agent skills"允许下游工具（例如 Claude Code）在不触碰已生成源文件的情况下扩展生成的应用。

# PARAMETERS

**init**
> 搭建新项目，包括配置文件、agent skills 和示例 OpenAPI 规范。

**serve** [_spec_]
> 启动开发服务器，在运行时从 _spec_ 渲染 UI。默认为 **http://localhost:4400**。

**build** [_spec_]
> 生成渲染后 UI 的生产包，用于静态或服务器端托管。

**--spec** _file_
> 当子命令不接受位置参数时，用此标志指定 OpenAPI 文件的另一种方式。

**--proxy-base** _url_
> 将渲染后 UI 发出的 API 调用转发到 _url_ 处的后端（在本地开发时很有用）。

**--port** _n_
> 覆盖默认的开发服务器端口（4400）。

# CONFIGURATION

**uigen.config.json**
> 由 **init** 写入的项目级配置：主题覆盖、身份验证默认值和渲染器插件。

**.uigen/**
> 缓存目录，在多次运行之间保存解析后的中间表示。

# CAVEATS

目前只渲染 **React**；Svelte 和 Vue 渲染器已在路线图中但尚未发布。由于渲染是**仅在运行时进行**的，OpenAPI 规范必须在启动时可访问——不存在独立于规范的编译后 JS 包。复杂的多态模式（深度嵌套的 **oneOf**/**anyOf**）可能会以通用方式渲染，需要手动模板。

# HISTORY

**uigen** 由 **darula-hpp** 于 **2026 年**发布，是规范驱动、AI 原生 SaaS 前端这一更广泛趋势的一部分。它刻意避免了传统 **swagger-codegen** 生成的样板代码，将渲染保持在运行时完成，并通过 **npm** 以 **@uigen-dev/cli** 的形式分发。

# SEE ALSO

[swagger-codegen](/man/swagger-codegen)(1), [openapi-generator](/man/openapi-generator)(1), [npx](/man/npx)(1)
