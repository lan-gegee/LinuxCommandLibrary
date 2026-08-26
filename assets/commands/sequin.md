# TAGLINE

通过变更数据捕获流式传输数据库变更

# TLDR

**启动消费者**

```sequin start```

**列出流**

```sequin streams```

**创建消费者**

```sequin consumers create [name]```

**查看状态**

```sequin status```

**查看日志**

```sequin logs```

# SYNOPSIS

**sequin** _command_ [_options_]

# PARAMETERS

**start**
> 启动消费者。

**streams**
> 列出流。

**consumers**
> 管理消费者。

**status**
> 显示状态。

**logs**
> 查看日志。

**--config** _FILE_
> 配置文件。

# DESCRIPTION

**sequin** 是一款变更数据捕获（CDC）工具，可将 PostgreSQL 的实时数据库变更以流的形式传出。它会在插入、更新和删除发生时将其捕获，并通过 HTTP webhook 或消息队列投递给消费者。

消费者订阅特定的变更流并按顺序处理。该工具负责管理消费者状态，跟踪哪些变更已被投递和确认。这使得构建事件驱动架构以及让下游系统与数据库状态保持同步成为可能。

# CAVEATS

专注于 Postgres。需要服务连接。需要配置。

# HISTORY

**Sequin** 是一款用于实时流式传输数据库变更的变更数据捕获工具。

# INSTALL

```apt: sudo apt install ncbi-tools-x11```

```brew: brew install sequin```

```nix: nix profile install nixpkgs#sequin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[debezium](/man/debezium)(1), [psql](/man/psql)(1), [kafka](/man/kafka)(1)
