# TAGLINE

Node.js 的 MVC Web 框架

# TLDR

**创建新应用**

```sails new [project-name]```

**启动开发服务器**

```sails lift```

**生成 API**

```sails generate api [user]```

**生成模型**

```sails generate model [user]```

**生成控制器**

```sails generate controller [user]```

**打开控制台**

```sails console```

**显示版本**

```sails --version```

# SYNOPSIS

**sails** _command_ [_options_] [_args_]

# PARAMETERS

**new** _NAME_
> 创建新应用。

**lift**
> 启动服务器。

**generate** _TYPE_ _NAME_
> 生成组件。

**console**
> 交互式 REPL。

**debug**
> 以调试模式启动应用。

**--version**
> 显示已安装的 Sails 版本。

**--port** _PORT_
> 设置服务器端口。

**--prod**
> 以生产模式启动。

# DESCRIPTION

**Sails.js** 是一个受 Ruby on Rails 启发的 Node.js MVC Web 框架。它提供约定和脚手架，以熟悉的模型-视图-控制器结构快速构建 REST API 和 Web 应用。

其突出特性是 Blueprints，可为模型自动生成具备完整 CRUD 操作的 RESTful API 端点。结合 Waterline ORM——它通过统一接口支持 MySQL、PostgreSQL、MongoDB 等数据库——应用只需极少的代码即可完成原型开发。

内置的 Socket.io 集成支持实时功能，让 Blueprint 路由同时工作在 HTTP 和 WebSocket 之上。策略（policies）提供类似中间件的访问控制，用于保护路由和实施身份验证。

# CAVEATS

框架有一定学习曲线。配置可能较为复杂。可能需要进行性能调优。

# HISTORY

**Sails.js** 由 **Mike McNeil** 创建，于 **2012 年**发布。它受 Rails 启发，将约定优于配置的理念带入 Node.js 开发。

# SEE ALSO

[node](/man/node)(1), [npm](/man/npm)(1), [express](/man/express)(1)
