# TAGLINE

在 Cradle 框架中管理 Elasticsearch

# TLDR

通过 Cradle **启动 Elasticsearch**

```cradle elastic start```

**停止 Elasticsearch**

```cradle elastic stop```

**检查** Elasticsearch **的状态**

```cradle elastic status```

**刷新** Elasticsearch 索引

```cradle elastic flush```

**映射** Elasticsearch 的 schema

```cradle elastic map```

# SYNOPSIS

**cradle** **elastic** _command_ [_options_]

# PARAMETERS

**start**
> 为 Cradle 开发环境启动 Elasticsearch 服务。

**stop**
> 停止正在运行的 Elasticsearch 服务。

**status**
> 显示 Elasticsearch 服务的当前状态。

**flush**
> 刷新所有 Elasticsearch 索引，清除缓存数据。

**map**
> 向 Elasticsearch 索引应用 schema 映射。

# DESCRIPTION

**cradle elastic** 管理 Cradle PHP 框架中的 Elasticsearch 实例。它提供用于启动、停止和检查开发环境 Elasticsearch 服务状态的命令。

该工具通过 Cradle CLI 处理服务生命周期操作，简化了本地 Elasticsearch 管理。对于需要在本地运行 Elasticsearch 来测试搜索功能、又不想手动管理服务的开发者而言尤其有用。

它是 Cradle 框架集成服务管理工具的一部分，让开发者能够直接从框架 CLI 控制依赖服务。

# SEE ALSO

[cradle](/man/cradle)(1), [cradle-install](/man/cradle-install)(1), [cradle-sql](/man/cradle-sql)(1), [elasticsearch](/man/elasticsearch)(1)
