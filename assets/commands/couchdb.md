# TAGLINE

面向文档的 NoSQL 数据库服务器

# TLDR

**启动 CouchDB** 服务器

```couchdb```

**在后台启动**

```couchdb -b```

**以指定配置文件启动**

```couchdb -c [/path/to/local.ini]```

**检查 CouchDB 是否在运行**

```curl http://127.0.0.1:5984/```

**优雅地停止 CouchDB**

```couchdb -d```

进程崩溃时**延迟后自动重启**

```couchdb -b -r [5]```

# SYNOPSIS

**couchdb** [_options_]

# PARAMETERS

**-b**
> 在后台启动（分离模式）。

**-d**
> 关闭正在运行的 CouchDB 实例。

**-c** _FILE_
> 使用额外的配置文件。

**-i**
> 启动交互式 Erlang shell。

**-o** _FILE_
> 将 stdout 重定向到指定文件。

**-e** _FILE_
> 将 stderr 重定向到指定文件。

**-p** _FILE_
> 在指定路径创建 PID 文件。

**-r** _SECONDS_
> 崩溃后延迟一段时间再重启 CouchDB。

**-s**
> 显示后台 CouchDB 进程的状态。

**-k**
> 杀死后台 CouchDB 进程（若设置了 -r 则会重新拉起）。

**-V**
> 显示版本信息并退出。

# DESCRIPTION

**Apache CouchDB** 是一个面向文档的 NoSQL 数据库：文档用 JSON 表示，MapReduce 查询用 JavaScript 编写，API 基于 HTTP。**couchdb** 命令用于启动数据库服务器。

CouchDB 以可靠性为目标进行设计，采用多版本并发控制（MVCC），无需加锁即可确保数据完整性。它内置面向分布式部署的复制功能，非常适合离线优先、在有网络时同步数据的应用。

该数据库为所有操作提供 RESTful HTTP API，涵盖从创建数据库和文档到执行查询的各个方面。内置的 Web 界面 Fauxton 允许你通过浏览器访问 http://localhost:5984/_utils/ 进行管理和查询。

# CONFIGURATION

**/etc/couchdb/local.ini**
> 本地配置覆盖项，用于网络绑定、身份验证、日志记录和性能调优。

**/etc/couchdb/default.ini**
> 系统默认配置（不应直接编辑；需要修改时请使用 local.ini 覆盖）。

# CAVEATS

默认安装只绑定到 localhost。若需远程访问，必须在 local.ini 中修改配置。admin party 模式（无身份验证）在生产环境中不安全。应定期执行 compaction 以回收磁盘空间。

# HISTORY

CouchDB 由 Damien Katz 创建，他于 **2005** 年用 C++ 启动该项目，随后在 **2008** 年用 Erlang 重写。它于 **2008** 年成为 Apache 项目，并在 **2010** 年晋升为顶级项目。其名字意指坐在"沙发"上放松。

# INSTALL

```pacman: sudo pacman -S couchdb```

```brew: brew install couchdb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [mongod](/man/mongod)(1), [redis-server](/man/redis-server)(1)
