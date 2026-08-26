# TAGLINE

探索与发布 SQLite 数据库的工具

# TLDR

**伺服一个 SQLite 数据库**

```datasette [database.db]```

**伺服多个数据库**

```datasette [db1.db] [db2.db]```

**在指定端口伺服**

```datasette -p [8080] [database.db]```

**以只读模式伺服**（默认）

```datasette --immutable [database.db]```

**创建用于部署的数据库包**

```datasette package [database.db] -t [myapp:latest]```

**安装插件**

```datasette install [datasette-vega]```

**发布到云服务商**

```datasette publish [cloudrun] [database.db] --service=[myservice]```

# SYNOPSIS

**datasette** [_options_] _database.db_...

# PARAMETERS

**-p**, **--port** _port_
> 伺服端口（默认：8001）。

**-h**, **--host** _host_
> 要绑定的主机（默认：127.0.0.1）。

**--immutable** _db_
> 将数据库标记为不可变（启用缓存）。

**-m**, **--metadata** _file_
> YAML/JSON 元数据文件。

**--load-extension** _ext_
> 加载 SQLite 扩展。

**-o**, **--open**
> 启动时打开浏览器。

**--cors**
> 启用 CORS 头。

**--setting** _key_ _value_
> 设置配置项。

**--secret** _secret_
> 用于签名的密钥。

**serve**
> 伺服数据库（默认命令）。

**publish** _target_
> 部署到云端（cloudrun、vercel、heroku、fly）。

**package**
> 创建 Docker 镜像。

**install** _plugin_
> 安装 Datasette 插件。

# DESCRIPTION

**Datasette** 是一个将 SQLite 数据库作为交互式网站和 JSON API 进行探索与发布的工具。它可以为任何 SQLite 数据库即时创建可浏览的界面，提供分面搜索、SQL 查询和自动生成的 API 端点。

每张表都有分页的 HTML 视图、JSON API 和 CSV 导出。自定义 SQL 查询可通过 Web 界面执行。插件可扩展可视化、身份验证和数据转换等功能。

Datasette 特别擅长发布数据：政府数据集、研究数据、日志以及任何结构化数据。publish 命令一条指令即可部署到云平台。

# CAVEATS

默认为只读访问；写操作需要插件和配置。大型数据库可能需要优化才能获得良好性能。某些 SQLite 特性（全文搜索）需要在构建时包含扩展。公开部署需要考虑身份验证问题。

# HISTORY

Datasette 由 **Simon Willison**（Django 的联合创造者）创建并于 **2017 年**首次发布。它源于他对数据新闻的兴趣以及让数据库易于访问的想法。该项目开创了"小数据"发布的理念，已被用于新闻报道、政府透明化和数据探索。Datasette 于 **2021 年**获得 Mozilla 开源奖。

# INSTALL

```brew: brew install datasette```

```nix: nix profile install nixpkgs#datasette```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sqlite3](/man/sqlite3)(1), [sqlite-utils](/man/sqlite-utils)(1)
