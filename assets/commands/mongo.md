# TAGLINE

旧版 MongoDB shell

# TLDR

**连接本地数据库**

```mongo```

**连接远程数据库**

```mongo [mongodb://host:27017/dbname]```

**带认证连接**

```mongo -u [user] -p [password] [dbname]```

**执行 JavaScript 文件**

```mongo [dbname] [script.js]```

**求值表达式**

```mongo --eval "[db.collection.find()]"```

**通过 SSL 连接**

```mongo --ssl --host [host]```

# SYNOPSIS

**mongo** [_options_] [_db_address_] [_file_names_]

# PARAMETERS

_DB_ADDRESS_
> 数据库连接字符串。

**-u** _USER_
> 用于认证的用户名。

**-p** _PASSWORD_
> 用于认证的密码。

**--eval** _EXPR_
> 求值 JavaScript 表达式。

**--ssl**
> 使用 SSL 连接。

**--host** _HOST_
> 服务器主机名。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mongo** 是随 **MongoDB** 服务器发布直至 **4.4** 版的最初交互式 shell。它是一个 JavaScript REPL，通过 MongoDB wire protocol 连接到 **mongod** 或 **mongos** 进程，并把数据库暴露为一棵 JavaScript 对象树：**db**、**db.collection**，以及 **find()**、**insertOne()**、**aggregate()** 等辅助方法。

连接可接受 MongoDB URI（**mongodb://** 或 **mongodb+srv://**），也可使用单独的标志：认证可用 **--host**、**--port**、**-u** / **-p** / **--authenticationDatabase**，加密传输可用 **--tls** / **--ssl**。末尾附加 JavaScript 文件加上 **--eval** 可让 shell 用于脚本中，并把最后一个表达式的结果输出到 stdout。

除了作为 shell，**mongo** 还广泛用于管理任务：创建用户、配置副本集、分片，以及用 **db.serverStatus()** 检查服务器状态。

# CAVEATS

自 **MongoDB 6.0** 起已被弃用并从官方 MongoDB 发行版中移除；新安装只附带 **mongosh**，后者讲同样的协议，但以 Node.js 作为运行时，并支持高级文本格式化、代码片段和改进的自动补全等新特性。一些旧的管理脚本仍依赖 **mongo** 特定的 JavaScript 环境（SpiderMonkey），在 **mongosh** 下运行可能需要少量修改。

# HISTORY

**mongo** shell 出现于 **2009 年**最早的公开 MongoDB 版本中。当 **mongosh** 于 **MongoDB 5.0**（2021 年 7 月）正式可用后，它被官方弃用，并于 **2022 年**从 MongoDB Server **6.0** 软件包中被移除。

# SEE ALSO

[mongosh](/man/mongosh)(1), [mongod](/man/mongod)(1), [mongoimport](/man/mongoimport)(1)
