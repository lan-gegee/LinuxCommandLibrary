# TAGLINE

现代 MongoDB shell

# TLDR

**连接本地数据库**

```mongosh```

**连接指定数据库**

```mongosh [mongodb://host:27017/dbname]```

**带认证连接**

```mongosh -u [user] -p [password] [dbname]```

**执行脚本文件**

```mongosh [dbname] [script.js]```

**求值表达式**

```mongosh --eval "[db.collection.find()]"```

**启动 shell 但不**连接数据库

```mongosh --nodb```

**通过 TLS 连接**远程主机

```mongosh --tls "mongodb://[host]:27017/[dbname]"```

**安静模式**（抑制启动消息）

```mongosh --quiet [script.js]```

# SYNOPSIS

**mongosh** [_options_] [_connection_string_] [_file_names_]

# PARAMETERS

_CONNECTION_STRING_
> MongoDB 连接 URI。

**-u** _USER_
> 用于认证的用户名。

**-p** _PASSWORD_
> 用于认证的密码。

**--eval** _EXPR_
> 求值 JavaScript 表达式。

**--nodb**
> 不连接数据库直接启动。

**--quiet**
> 抑制非必要的输出。

**--host** _HOST_
> 服务器主机名（默认：localhost）。

**--port** _PORT_
> 服务器端口（默认：27017）。

**--authenticationDatabase** _DB_
> 认证数据库（默认：admin）。

**--tls**
> 启用 TLS/SSL 连接。

**--shell**
> 运行完文件/eval 后强制进入交互式 shell。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mongosh** 是现代的 MongoDB shell，提供一个功能完备的 JavaScript 与 Node.js REPL 环境，用于操作 MongoDB 部署。

它取代了旧版 **mongo** shell，改进包括语法高亮、智能自动补全、内联帮助和可扩展的代码片段。它支持所有 CRUD 操作、聚合管道、数据库管理以及 Atlas 连接。

# CAVEATS

自 1.0 版起自带 Node.js 运行时。兼容 MongoDB 4.0+，但某些特性需要 MongoDB 5.0+。其驱动 API 与旧版 mongo shell 不同；脚本可能需要更新。

# HISTORY

mongosh 由 **MongoDB** 于 2020 年发布，是取代旧版 mongo shell 的下一代 shell。

# INSTALL

```brew: brew install mongosh```

```nix: nix profile install nixpkgs#mongosh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mongo](/man/mongo)(1), [mongod](/man/mongod)(1), [mongoimport](/man/mongoimport)(1), [mongoexport](/man/mongoexport)(1), [mongodump](/man/mongodump)(1)
