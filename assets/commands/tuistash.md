# TAGLINE

用于 Logstash 监控的终端用户界面

# TLDR

**连接本地 Logstash 实例**

```tuistash```

**连接指定的 Logstash API**

```tuistash --api [http://localhost:9600]```

以秒为单位**设置自定义刷新间隔**

```tuistash --refresh-interval [5]```

**使用 API 身份验证连接**

```tuistash --api [http://localhost:9600] --username [admin] --password [secret]```

# SYNOPSIS

**tuistash** [_options_]

# PARAMETERS

**--api** _URL_
> Logstash 监控 API 的 URL（默认：http://localhost:9600）。

**--refresh-interval** _SECONDS_
> 数据刷新间隔（秒）（默认：5）。

**--username** _USER_
> API 身份验证的用户名。

**--password** _PASS_
> API 身份验证的密码。

# DESCRIPTION

**tuistash** 提供一个 TUI，用于监控 Logstash 节点、管道、线程、数据流等。它连接到 Logstash 监控 API，并以图形方式实时显示 CPU 使用率、JVM 堆、吞吐量和队列数据等统计信息。

界面支持键盘导航：用 Tab 在面板间切换，用 q 退出。

# CAVEATS

需要一个已启用监控 API 的运行中 Logstash 实例（默认在端口 9600 启用）。运行 tuistash 的机器必须能够访问该 API。

# HISTORY

**tuistash** 由 **Edmo Vamerlatti Costa**（edmocosta）创建，用 **Rust** 编写。

# INSTALL

```nix: nix profile install nixpkgs#tuistash```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[logstash](/man/logstash)(1), [elasticsearch](/man/elasticsearch)(1)
