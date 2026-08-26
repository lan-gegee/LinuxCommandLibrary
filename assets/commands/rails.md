# TAGLINE

Ruby on Rails Web 应用框架命令行界面

# TLDR

**创建新的 Rails 应用**

```rails new [app_name]```

**创建使用 PostgreSQL 数据库的新应用**

```rails new [app_name] --database=postgresql```

**在端口 3000 上启动开发服务器**

```rails server```

**打开加载应用环境的交互式控制台**

```rails console```

**生成带属性的模型**

```rails generate model [ModelName] [field:type] [field:type]```

**生成带动作的控制器**

```rails generate controller [ControllerName] [action1] [action2]```

**运行数据库迁移**

```rails db:migrate```

**列出应用中的所有路由**

```rails routes```

# SYNOPSIS

**rails** _command_ [_options_] [_arguments_]

# PARAMETERS

**new** _app_name_
> 创建具有标准目录结构的新 Rails 应用

**server**, **s**
> 启动 Puma Web 服务器（默认端口 3000）

**console**, **c**
> 打开带有应用上下文的交互式 IRB 会话

**generate**, **g**
> 运行模型、控制器、迁移等的代码生成器

**destroy**, **d**
> 移除生成器创建的文件

**db:migrate**
> 运行待处理的数据库迁移

**db:create**
> 创建数据库

**db:seed**
> 从 db/seeds.rb 加载种子数据

**db:setup**
> 创建数据库、加载 schema 并填充种子数据

**routes**
> 显示所有已定义的路由

**test**
> 运行测试套件

**--help**, **-h**
> 显示任意命令的帮助信息

**--version**
> 显示 Rails 版本号

**-e**, **--environment** _ENV_
> 指定环境（development、test、production）

**-p**, **--port** _PORT_
> 设置服务器端口（默认 3000）

# DESCRIPTION

**rails** 是 Ruby on Rails Web 应用框架的命令行界面。它通过统一的接口提供创建、开发和管理 Rails 应用的工具。

该命令在两种场景下运行：在应用之外（主要是用 **rails new** 创建项目）和应用目录之内（其他所有命令）。在项目中，命令通常通过 **bin/rails** 调用，以确保使用正确的捆绑版本。

Rails 强调"约定优于配置"，其 CLI 也体现了这一点：提供的生成器会按照 Rails 约定创建样板代码。该框架将数据库管理、测试、资源编译和服务器运行整合为连贯的命令行工作流。

# CONFIGURATION

**config/database.yml**
> 各环境（development、test、production）的数据库连接设置，指定适配器、主机、凭据和连接池大小。

**config/routes.rb**
> 应用的 URL 路由定义，将 HTTP 方法和路径映射到控制器动作。

**config/application.rb**
> 主应用配置，包括框架默认值、中间件和自动加载路径。

**config/environments/**
> 各环境的设置文件（development.rb、test.rb、production.rb），控制缓存、日志和资源行为。

**RAILS_ENV**
> 选择当前激活环境的环境变量（默认为 development）。

# CAVEATS

大多数命令必须在 Rails 应用目录内运行。**rails new** 是例外，它负责创建这个目录结构。

生成的代码应先审查再使用。生成器创建的是标准模式，可能需要针对具体需求进行定制。

数据库命令需要在 **config/database.yml** 中有正确的数据库配置，并安装相应的数据库适配器 gem。

# HISTORY

Rails 由 **David Heinemeier Hansson** 创建，于 **2004 年**从 Basecamp 项目管理工具中提取出来。首个公开发布版本是 **2005 年 12 月**的 1.0 版。该框架推广了 Web 开发中的 MVC 模式，并引入了 RESTful 路由等约定，影响了众多后续框架。

# SEE ALSO

[ruby](/man/ruby)(1), [bundle](/man/bundle)(1), [rake](/man/rake)(1), [gem](/man/gem)(1)
