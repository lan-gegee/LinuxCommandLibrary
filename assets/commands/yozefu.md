# TAGLINE

用于浏览 Kafka 集群数据的 TUI 应用

# TLDR

**启动 Kafka 浏览器 TUI**

```yozefu```

**以无界面 CLI 模式运行**

```yozefu --headless --topic [my-topic]```

**连接到特定集群**

```yozefu --cluster [my-cluster]```

# SYNOPSIS

**yozefu** [_options_]

# DESCRIPTION

**yozefu** 是一个交互式终端应用，用于浏览和搜索 Kafka 集群中的数据。它具有类 SQL 的查询语言用于过滤记录、面向 Shell 脚本的无界面模式、基于 WebAssembly 的用户自定义过滤函数，以及存储最近 500 条记录的环形缓冲区。

# HISTORY

**yozefu** 由 **Yann Prono**（MAIF）创建，以 **Rust** 编写。

# INSTALL

```brew: brew install yozefu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kafkacat](/man/kafkacat)(1)
