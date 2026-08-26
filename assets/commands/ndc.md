# TAGLINE

BIND 名称守护进程控制器

# TLDR

**重新加载 BIND 配置**

```ndc reload```

**查看 BIND 状态**

```ndc status```

**停止 BIND 服务器**

```ndc stop```

**启动 BIND 服务器**

```ndc start```

**清空缓存**

```ndc flush```

**重启 BIND**

```ndc restart```

# SYNOPSIS

**ndc** [_command_]

# PARAMETERS

_COMMAND_
> 控制命令。

**reload**
> 重新加载配置。

**status**
> 显示服务器状态。

**stop**
> 停止服务器。

**start**
> 启动服务器。

**flush**
> 清空 DNS 缓存。

**restart**
> 重启服务器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ndc** 是 BIND 名称守护进程控制器。它用于管理 BIND DNS 服务器。

该工具向 named 发送命令。这是旧式工具，已被 rndc 取代。

# CAVEATS

旧式工具。请改用 rndc。需要 named 正在运行。

# HISTORY

ndc 是最初的 **BIND** 控制工具，现已被 rndc 取代而弃用。

# SEE ALSO

[rndc](/man/rndc)(1), [named](/man/named)(1), [bind](/man/bind)(1)
